from __future__ import annotations
import sys
from pathlib import Path
from typing import Callable

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices, QIcon
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QFileDialog, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QMainWindow, QMessageBox, QPushButton, QPlainTextEdit, QProgressBar,
    QSpinBox, QStackedWidget, QTextBrowser, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget, QHeaderView
)

from ciphercore import APP_NAME, APP_TITLE
from ciphercore.analytics import analyze_file, analyze_password, analyze_random_sample, analyze_text, compare_files
from ciphercore.app_config import LOG_PATH, SOCIAL_LINKS
from ciphercore.crypto import create_password_hash, decrypt_file, decrypt_text, encrypt_file, encrypt_text, make_session_fernet, verify_password
from ciphercore.i18n import I18N
from ciphercore.info_text import INFO_TEXT
from ciphercore.shredding import shred_file
from ciphercore.social import open_social
from ciphercore.storage import VaultRecord, VaultStorage
from ciphercore.utils import append_log, human_size, load_state, save_state


class DropListWidget(QListWidget):
    def __init__(self, on_files_dropped: Callable[[list[str]], None], parent=None) -> None:
        super().__init__(parent)
        self.on_files_dropped = on_files_dropped
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            paths = [u.toLocalFile() for u in event.mimeData().urls() if u.toLocalFile()]
            if paths:
                self.on_files_dropped(paths)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.state = load_state()
        self.i18n = I18N(self.state.get('language', 'de'))
        self.vault = VaultStorage()
        self.session_fernet = None
        self.session_unlocked = False
        self.selected_vault_id = None
        self.file_queue: list[Path] = []
        self.shred_queue: list[Path] = []
        self.analysis_file_a: Path | None = None
        self.analysis_file_b: Path | None = None
        self._build_ui()
        self.apply_translations()
        self.refresh_dashboard()
        self.refresh_vault_table()
        self.load_log_excerpt()
        self.apply_stylesheet()

    def t(self, key: str) -> str:
        return self.i18n.t(key)

    def _build_ui(self) -> None:
        self.setWindowTitle(APP_TITLE)
        self.resize(1650, 980)
        central = QWidget()
        root = QHBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.sidebar = QFrame()
        self.sidebar.setObjectName('Sidebar')
        sl = QVBoxLayout(self.sidebar)
        sl.setContentsMargins(18, 18, 18, 18)
        sl.setSpacing(10)
        brand = QLabel(APP_NAME)
        brand.setObjectName('BrandLabel')
        sl.addWidget(brand)
        self.nav_buttons: dict[str, QPushButton] = {}
        for idx, key in enumerate(['dashboard', 'text', 'files', 'analytics', 'vault', 'passwords', 'shredder', 'settings', 'info']):
            btn = QPushButton()
            btn.setCheckable(True)
            btn.clicked.connect(lambda _=False, i=idx: self.pages.setCurrentIndex(i))
            btn.clicked.connect(self._update_nav_state)
            self.nav_buttons[key] = btn
            sl.addWidget(btn)
        sl.addStretch(1)
        social_box = QGroupBox('Social')
        social_layout = QVBoxLayout(social_box)
        for name in SOCIAL_LINKS:
            btn = QPushButton(name)
            btn.clicked.connect(lambda _=False, n=name: open_social(n))
            social_layout.addWidget(btn)
        sl.addWidget(social_box)
        self.status_badge = QLabel()
        self.status_badge.setObjectName('StatusBadge')
        sl.addWidget(self.status_badge)
        root.addWidget(self.sidebar, 0)

        main = QWidget()
        ml = QVBoxLayout(main)
        ml.setContentsMargins(18, 18, 18, 18)
        ml.setSpacing(12)
        top = QHBoxLayout()
        self.window_title = QLabel()
        self.window_title.setObjectName('WindowTitle')
        top.addWidget(self.window_title)
        top.addStretch(1)
        self.language_box = QComboBox()
        self.language_box.addItems(['de', 'en'])
        self.language_box.setCurrentText(self.i18n.language)
        self.language_box.currentTextChanged.connect(self.change_language)
        top.addWidget(self.language_box)
        self.lock_button = QPushButton()
        self.lock_button.clicked.connect(self.lock_session)
        top.addWidget(self.lock_button)
        ml.addLayout(top)

        self.pages = QStackedWidget()
        ml.addWidget(self.pages, 1)
        root.addWidget(main, 1)
        self.setCentralWidget(central)

        self.pages.addWidget(self._build_dashboard_page())
        self.pages.addWidget(self._build_text_page())
        self.pages.addWidget(self._build_files_page())
        self.pages.addWidget(self._build_analytics_page())
        self.pages.addWidget(self._build_vault_page())
        self.pages.addWidget(self._build_password_page())
        self.pages.addWidget(self._build_shredder_page())
        self.pages.addWidget(self._build_settings_page())
        self.pages.addWidget(self._build_info_page())
        self.pages.currentChanged.connect(self._update_nav_state)
        self._update_nav_state()

    def _page_shell(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setSpacing(12)
        title = QLabel()
        title.setObjectName('PageTitle')
        subtitle = QLabel()
        subtitle.setWordWrap(True)
        subtitle.setObjectName('PageSubtitle')
        layout.addWidget(title)
        layout.addWidget(subtitle)
        return page, layout, title, subtitle

    def _metric_card(self):
        box = QFrame()
        box.setObjectName('MetricCard')
        layout = QVBoxLayout(box)
        title = QLabel()
        title.setObjectName('MetricTitle')
        value = QLabel('0')
        value.setObjectName('MetricValue')
        layout.addWidget(title)
        layout.addWidget(value)
        box.title_label = title
        box.value_label = value
        return box

    def _build_dashboard_page(self):
        page, layout, self.dashboard_title, self.dashboard_subtitle = self._page_shell()
        cards = QGridLayout()
        self.card_files = self._metric_card()
        self.card_entries = self._metric_card()
        self.card_logs = self._metric_card()
        self.card_language = self._metric_card()
        self.card_analytics = self._metric_card()
        cards.addWidget(self.card_files, 0, 0)
        cards.addWidget(self.card_entries, 0, 1)
        cards.addWidget(self.card_logs, 0, 2)
        cards.addWidget(self.card_language, 1, 0)
        cards.addWidget(self.card_analytics, 1, 1)
        layout.addLayout(cards)
        qg = QGroupBox()
        ql = QHBoxLayout(qg)
        self.quick_text_btn = QPushButton()
        self.quick_text_btn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.quick_files_btn = QPushButton()
        self.quick_files_btn.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        self.quick_analytics_btn = QPushButton()
        self.quick_analytics_btn.clicked.connect(lambda: self.pages.setCurrentIndex(3))
        self.quick_vault_btn = QPushButton()
        self.quick_vault_btn.clicked.connect(lambda: self.pages.setCurrentIndex(4))
        for btn in [self.quick_text_btn, self.quick_files_btn, self.quick_analytics_btn, self.quick_vault_btn]:
            ql.addWidget(btn)
        layout.addWidget(qg)
        lg = QGroupBox()
        ll = QVBoxLayout(lg)
        self.log_excerpt_title = QLabel()
        self.log_excerpt = QPlainTextEdit()
        self.log_excerpt.setReadOnly(True)
        self.open_log_btn = QPushButton()
        self.open_log_btn.clicked.connect(self.open_log_file)
        ll.addWidget(self.log_excerpt_title)
        ll.addWidget(self.log_excerpt)
        ll.addWidget(self.open_log_btn)
        layout.addWidget(lg, 1)
        return page

    def _build_text_page(self):
        page, layout, self.text_title, self.text_subtitle = self._page_shell()
        self.text_password = QLineEdit(); self.text_password.setEchoMode(QLineEdit.Password)
        self.text_input = QPlainTextEdit(); self.text_output = QPlainTextEdit()
        layout.addWidget(self.text_password)
        layout.addWidget(self.text_input)
        layout.addWidget(self.text_output)
        row = QHBoxLayout()
        self.text_encrypt_btn = QPushButton(); self.text_encrypt_btn.clicked.connect(self.encrypt_text_action)
        self.text_decrypt_btn = QPushButton(); self.text_decrypt_btn.clicked.connect(self.decrypt_text_action)
        self.text_copy_btn = QPushButton(); self.text_copy_btn.clicked.connect(lambda: self.copy_text(self.text_output.toPlainText()))
        self.text_clear_btn = QPushButton(); self.text_clear_btn.clicked.connect(lambda: [self.text_password.clear(), self.text_input.clear(), self.text_output.clear()])
        for btn in [self.text_encrypt_btn, self.text_decrypt_btn, self.text_copy_btn, self.text_clear_btn]:
            row.addWidget(btn)
        layout.addLayout(row)
        return page

    def _build_files_page(self):
        page, layout, self.files_title, self.files_subtitle = self._page_shell()
        controls = QHBoxLayout()
        self.file_password = QLineEdit(); self.file_password.setEchoMode(QLineEdit.Password)
        self.file_output = QLineEdit()
        self.file_choose_output_btn = QPushButton(); self.file_choose_output_btn.clicked.connect(self.choose_output_folder)
        controls.addWidget(self.file_password, 2); controls.addWidget(self.file_output, 3); controls.addWidget(self.file_choose_output_btn)
        layout.addLayout(controls)
        options = QHBoxLayout()
        self.keep_original_check = QCheckBox(); self.keep_original_check.setChecked(True)
        self.shred_original_check = QCheckBox()
        options.addWidget(self.keep_original_check); options.addWidget(self.shred_original_check); options.addStretch(1)
        layout.addLayout(options)
        self.file_list = DropListWidget(self.add_files_to_queue)
        layout.addWidget(self.file_list, 1)
        actions = QHBoxLayout()
        self.add_files_btn = QPushButton(); self.add_files_btn.clicked.connect(self.pick_files)
        self.remove_files_btn = QPushButton(); self.remove_files_btn.clicked.connect(self.remove_selected_files)
        self.encrypt_files_btn = QPushButton(); self.encrypt_files_btn.clicked.connect(lambda: self.process_file_queue('encrypt'))
        self.decrypt_files_btn = QPushButton(); self.decrypt_files_btn.clicked.connect(lambda: self.process_file_queue('decrypt'))
        for btn in [self.add_files_btn, self.remove_files_btn, self.encrypt_files_btn, self.decrypt_files_btn]:
            actions.addWidget(btn)
        layout.addLayout(actions)
        self.file_progress = QProgressBar(); layout.addWidget(self.file_progress)
        return page

    def _build_analytics_page(self):
        page, layout, self.analytics_title, self.analytics_subtitle = self._page_shell()
        grid = QGridLayout()

        text_box = QGroupBox(); text_layout = QVBoxLayout(text_box)
        self.analytics_text_label = QLabel(); self.analytics_text_input = QPlainTextEdit(); self.analytics_text_btn = QPushButton(); self.analytics_text_btn.clicked.connect(self.run_text_analysis)
        text_layout.addWidget(self.analytics_text_label); text_layout.addWidget(self.analytics_text_input); text_layout.addWidget(self.analytics_text_btn)
        grid.addWidget(text_box, 0, 0)

        pw_box = QGroupBox(); pw_layout = QVBoxLayout(pw_box)
        self.analytics_password_label = QLabel(); self.analytics_password_input = QLineEdit(); self.analytics_password_input.setEchoMode(QLineEdit.Password)
        self.analytics_password_btn = QPushButton(); self.analytics_password_btn.clicked.connect(self.run_password_analysis)
        pw_layout.addWidget(self.analytics_password_label); pw_layout.addWidget(self.analytics_password_input); pw_layout.addWidget(self.analytics_password_btn)
        grid.addWidget(pw_box, 0, 1)

        file_box = QGroupBox(); file_layout = QVBoxLayout(file_box)
        self.analytics_file_label = QLabel(); self.analytics_file_path = QLineEdit(); self.analytics_file_pick = QPushButton(); self.analytics_file_pick.clicked.connect(self.pick_analysis_file)
        self.analytics_file_btn = QPushButton(); self.analytics_file_btn.clicked.connect(self.run_file_analysis)
        file_layout.addWidget(self.analytics_file_label); file_layout.addWidget(self.analytics_file_path); file_layout.addWidget(self.analytics_file_pick); file_layout.addWidget(self.analytics_file_btn)
        grid.addWidget(file_box, 1, 0)

        cmp_box = QGroupBox(); cmp_layout = QFormLayout(cmp_box)
        self.compare_a_path = QLineEdit(); self.compare_b_path = QLineEdit()
        self.compare_a_pick = QPushButton(); self.compare_a_pick.clicked.connect(lambda: self.pick_compare_file('a'))
        self.compare_b_pick = QPushButton(); self.compare_b_pick.clicked.connect(lambda: self.pick_compare_file('b'))
        self.compare_btn = QPushButton(); self.compare_btn.clicked.connect(self.run_file_comparison)
        cmp_row_a = QWidget(); ra = QHBoxLayout(cmp_row_a); ra.setContentsMargins(0,0,0,0); ra.addWidget(self.compare_a_path); ra.addWidget(self.compare_a_pick)
        cmp_row_b = QWidget(); rb = QHBoxLayout(cmp_row_b); rb.setContentsMargins(0,0,0,0); rb.addWidget(self.compare_b_path); rb.addWidget(self.compare_b_pick)
        self.compare_label_a = QLabel(); self.compare_label_b = QLabel()
        cmp_layout.addRow(self.compare_label_a, cmp_row_a); cmp_layout.addRow(self.compare_label_b, cmp_row_b); cmp_layout.addRow(self.compare_btn)
        grid.addWidget(cmp_box, 1, 1)

        random_box = QGroupBox(); random_layout = QFormLayout(random_box)
        self.random_length_label = QLabel(); self.random_length = QSpinBox(); self.random_length.setRange(256, 1048576); self.random_length.setValue(4096)
        self.random_btn = QPushButton(); self.random_btn.clicked.connect(self.run_random_lab)
        random_layout.addRow(self.random_length_label, self.random_length); random_layout.addRow(self.random_btn)
        grid.addWidget(random_box, 2, 0, 1, 2)

        layout.addLayout(grid)
        self.analytics_output_label = QLabel()
        self.analytics_output = QPlainTextEdit(); self.analytics_output.setReadOnly(True)
        layout.addWidget(self.analytics_output_label); layout.addWidget(self.analytics_output, 1)
        return page

    def _build_vault_page(self):
        page, layout, self.vault_title, self.vault_subtitle = self._page_shell()
        self.vault_search = QLineEdit(); self.vault_search.textChanged.connect(self.refresh_vault_table)
        layout.addWidget(self.vault_search)
        split = QHBoxLayout()
        self.vault_table = QTableWidget(0, 4)
        self.vault_table.setSelectionBehavior(QTableWidget.SelectRows); self.vault_table.setSelectionMode(QTableWidget.SingleSelection)
        self.vault_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.vault_table.itemSelectionChanged.connect(self.load_selected_vault)
        split.addWidget(self.vault_table, 3)
        editor = QGroupBox(); form = QFormLayout(editor)
        self.vault_entry_title = QLineEdit(); self.vault_entry_category = QLineEdit(); self.vault_entry_username = QLineEdit(); self.vault_entry_secret = QPlainTextEdit(); self.vault_entry_notes = QPlainTextEdit()
        self.vault_title_label = QLabel(); self.vault_category_label = QLabel(); self.vault_user_label = QLabel(); self.vault_secret_label = QLabel(); self.vault_notes_label = QLabel()
        form.addRow(self.vault_title_label, self.vault_entry_title); form.addRow(self.vault_category_label, self.vault_entry_category); form.addRow(self.vault_user_label, self.vault_entry_username)
        form.addRow(self.vault_secret_label, self.vault_entry_secret); form.addRow(self.vault_notes_label, self.vault_entry_notes)
        self.vault_save_btn = QPushButton(); self.vault_save_btn.clicked.connect(self.save_vault_entry)
        self.vault_delete_btn = QPushButton(); self.vault_delete_btn.clicked.connect(self.delete_vault_entry)
        form.addRow(self.vault_save_btn, self.vault_delete_btn)
        split.addWidget(editor, 2)
        layout.addLayout(split, 1)
        return page

    def _build_password_page(self):
        page, layout, self.passwords_title, self.passwords_subtitle = self._page_shell()
        group = QGroupBox(); form = QFormLayout(group)
        self.master_password_input = QLineEdit(); self.master_password_input.setEchoMode(QLineEdit.Password)
        self.master_password_confirm = QLineEdit(); self.master_password_confirm.setEchoMode(QLineEdit.Password)
        self.master_login_input = QLineEdit(); self.master_login_input.setEchoMode(QLineEdit.Password)
        self.password_strength_label = QLabel('-')
        self.password_generator_output = QLineEdit()
        self.label_mp = QLabel(); self.label_mp_confirm = QLabel(); self.label_mp_login = QLabel(); self.label_strength = QLabel(); self.label_generated = QLabel('Generated')
        form.addRow(self.label_mp, self.master_password_input); form.addRow(self.label_mp_confirm, self.master_password_confirm); form.addRow(self.label_mp_login, self.master_login_input)
        form.addRow(self.label_strength, self.password_strength_label); form.addRow(self.label_generated, self.password_generator_output)
        layout.addWidget(group)
        row = QHBoxLayout()
        self.set_master_btn = QPushButton(); self.set_master_btn.clicked.connect(self.set_master_password)
        self.login_btn = QPushButton(); self.login_btn.clicked.connect(self.login_master_password)
        self.generate_password_btn = QPushButton(); self.generate_password_btn.clicked.connect(self.generate_password)
        for btn in [self.set_master_btn, self.login_btn, self.generate_password_btn]: row.addWidget(btn)
        layout.addLayout(row)
        self.master_password_input.textChanged.connect(self.update_password_strength)
        return page

    def _build_shredder_page(self):
        page, layout, self.shredder_title, self.shredder_subtitle = self._page_shell()
        row = QHBoxLayout(); self.shred_passes_label = QLabel(); self.shred_passes = QSpinBox(); self.shred_passes.setRange(1, 10); self.shred_passes.setValue(3); row.addWidget(self.shred_passes_label); row.addWidget(self.shred_passes); row.addStretch(1); layout.addLayout(row)
        self.shred_list = DropListWidget(self.add_files_to_shred_queue); layout.addWidget(self.shred_list, 1)
        actions = QHBoxLayout(); self.shred_add_btn = QPushButton(); self.shred_add_btn.clicked.connect(self.pick_shred_files); self.shred_remove_btn = QPushButton(); self.shred_remove_btn.clicked.connect(self.remove_selected_shred_files); self.shred_execute_btn = QPushButton(); self.shred_execute_btn.clicked.connect(self.execute_shred)
        for btn in [self.shred_add_btn, self.shred_remove_btn, self.shred_execute_btn]: actions.addWidget(btn)
        layout.addLayout(actions)
        return page

    def _build_settings_page(self):
        page, layout, self.settings_title, self.settings_subtitle = self._page_shell()
        group = QGroupBox(); form = QFormLayout(group)
        self.settings_language = QComboBox(); self.settings_language.addItems(['de', 'en']); self.settings_language.setCurrentText(self.i18n.language); self.settings_language.currentTextChanged.connect(self.change_language)
        self.theme_box = QComboBox(); self.theme_box.addItems(['dark', 'light']); self.theme_box.currentTextChanged.connect(lambda *_: self.apply_stylesheet())
        self.settings_language_label = QLabel(); self.theme_label = QLabel()
        form.addRow(self.settings_language_label, self.settings_language); form.addRow(self.theme_label, self.theme_box)
        layout.addWidget(group); layout.addStretch(1)
        return page

    def _build_info_page(self):
        page, layout, self.info_title, self.info_subtitle = self._page_shell(); self.info_browser = QTextBrowser(); self.info_browser.setOpenExternalLinks(True); layout.addWidget(self.info_browser, 1); return page

    def apply_stylesheet(self):
        light = hasattr(self, 'theme_box') and self.theme_box.currentText() == 'light'
        if light:
            stylesheet = """
            QWidget { background: #f5f7fb; color: #122033; font-size: 13px; }
            #Sidebar { background: #e9eef8; }
            #BrandLabel { font-size: 24px; font-weight: 700; color: #203a70; }
            #WindowTitle { font-size: 20px; font-weight: 700; }
            #PageTitle { font-size: 22px; font-weight: 700; }
            #PageSubtitle { color: #425069; }
            #MetricCard { background: white; border-radius: 12px; border: 1px solid #d8dfef; }
            #MetricTitle { color: #55657d; }
            #MetricValue { font-size: 24px; font-weight: 700; }
            #StatusBadge { padding: 10px; border-radius: 10px; background: #dce7ff; }
            QPushButton { background: white; border: 1px solid #ccd7ed; border-radius: 10px; padding: 10px 12px; }
            QPushButton:checked { background: #dce7ff; border-color: #7da0f6; }
            QLineEdit, QPlainTextEdit, QListWidget, QTableWidget, QTextBrowser, QComboBox, QSpinBox { background: white; border: 1px solid #ccd7ed; border-radius: 10px; padding: 8px; }
            QGroupBox { border: 1px solid #d8dfef; border-radius: 12px; margin-top: 10px; padding: 12px; }
            """
        else:
            stylesheet = """
            QWidget { background: #0d1118; color: #eef2fb; font-size: 13px; }
            #Sidebar { background: #111826; }
            #BrandLabel { font-size: 24px; font-weight: 700; color: #8ab4ff; }
            #WindowTitle { font-size: 20px; font-weight: 700; }
            #PageTitle { font-size: 22px; font-weight: 700; }
            #PageSubtitle { color: #9db0cf; }
            #MetricCard { background: #131b2b; border-radius: 12px; border: 1px solid #273551; }
            #MetricTitle { color: #8fa4c6; }
            #MetricValue { font-size: 24px; font-weight: 700; }
            #StatusBadge { padding: 10px; border-radius: 10px; background: #162339; }
            QPushButton { background: #182233; border: 1px solid #2b3d5d; border-radius: 10px; padding: 10px 12px; }
            QPushButton:checked { background: #23406f; border-color: #5e8ef8; }
            QLineEdit, QPlainTextEdit, QListWidget, QTableWidget, QTextBrowser, QComboBox, QSpinBox { background: #101827; border: 1px solid #2b3d5d; border-radius: 10px; padding: 8px; }
            QGroupBox { border: 1px solid #273551; border-radius: 12px; margin-top: 10px; padding: 12px; }
            """
        self.setStyleSheet(stylesheet)

    def apply_translations(self):
        self.setWindowTitle(self.t('app.title')); self.window_title.setText(self.t('app.title')); self.lock_button.setText(self.t('action.lock'))
        self.status_badge.setText(f"{self.t('label.status')}: {self.t('status.unlocked') if self.session_unlocked else self.t('status.locked')}")
        for key in self.nav_buttons: self.nav_buttons[key].setText(self.t(f'sidebar.{key}'))
        self.dashboard_title.setText(self.t('dashboard.welcome')); self.dashboard_subtitle.setText(self.t('dashboard.subtitle')); self.card_files.title_label.setText(self.t('dashboard.cards.files')); self.card_entries.title_label.setText(self.t('dashboard.cards.entries')); self.card_logs.title_label.setText(self.t('dashboard.cards.logs')); self.card_language.title_label.setText(self.t('dashboard.cards.language')); self.card_analytics.title_label.setText(self.t('dashboard.cards.analytics')); self.quick_text_btn.setText(self.t('dashboard.quick_text')); self.quick_files_btn.setText(self.t('dashboard.quick_files')); self.quick_analytics_btn.setText(self.t('dashboard.quick_analytics')); self.quick_vault_btn.setText(self.t('dashboard.quick_vault')); self.log_excerpt_title.setText(self.t('label.logs')); self.open_log_btn.setText(self.t('action.open_log'))
        self.text_title.setText(self.t('text.title')); self.text_subtitle.setText(self.t('text.subtitle')); self.text_password.setPlaceholderText(self.t('label.password')); self.text_input.setPlaceholderText(self.t('text.placeholder')); self.text_output.setPlaceholderText(self.t('text.result_placeholder')); self.text_encrypt_btn.setText(self.t('action.encrypt')); self.text_decrypt_btn.setText(self.t('action.decrypt')); self.text_copy_btn.setText(self.t('action.copy')); self.text_clear_btn.setText(self.t('action.clear'))
        self.files_title.setText(self.t('files.title')); self.files_subtitle.setText(self.t('files.subtitle')); self.file_password.setPlaceholderText(self.t('label.password')); self.file_output.setPlaceholderText(self.t('label.output_folder')); self.file_choose_output_btn.setText(self.t('action.add_output_dir')); self.keep_original_check.setText(self.t('label.keep_original')); self.shred_original_check.setText(self.t('label.shred_original')); self.add_files_btn.setText(self.t('action.add_files')); self.remove_files_btn.setText(self.t('action.remove_selected')); self.encrypt_files_btn.setText(self.t('action.encrypt')); self.decrypt_files_btn.setText(self.t('action.decrypt'))
        self.analytics_title.setText(self.t('analytics.title')); self.analytics_subtitle.setText(self.t('analytics.subtitle')); self.analytics_text_label.setText(self.t('analytics.text_group')); self.analytics_text_btn.setText(self.t('action.analyze_text')); self.analytics_password_label.setText(self.t('analytics.password_group')); self.analytics_password_btn.setText(self.t('action.analyze_password')); self.analytics_file_label.setText(self.t('analytics.file_group')); self.analytics_file_pick.setText(self.t('action.add_files')); self.analytics_file_btn.setText(self.t('action.analyze_file')); self.compare_label_a.setText(self.t('label.compare_a')); self.compare_label_b.setText(self.t('label.compare_b')); self.compare_a_pick.setText(self.t('action.add_files')); self.compare_b_pick.setText(self.t('action.add_files')); self.compare_btn.setText(self.t('action.compare_files')); self.random_length_label.setText(self.t('label.random_length')); self.random_btn.setText(self.t('action.random_lab')); self.analytics_output_label.setText(self.t('label.analysis_output'))
        self.vault_title.setText(self.t('vault.title')); self.vault_subtitle.setText(self.t('vault.subtitle')); self.vault_search.setPlaceholderText(self.t('label.search')); self.vault_title_label.setText(self.t('label.title')); self.vault_category_label.setText(self.t('label.category')); self.vault_user_label.setText(self.t('label.username')); self.vault_secret_label.setText(self.t('label.secret')); self.vault_notes_label.setText(self.t('label.notes')); self.vault_save_btn.setText(self.t('action.save_entry')); self.vault_delete_btn.setText(self.t('action.delete_entry')); self.vault_table.setHorizontalHeaderLabels(['ID', self.t('label.title'), self.t('label.category'), 'Updated'])
        self.passwords_title.setText(self.t('passwords.title')); self.passwords_subtitle.setText(self.t('passwords.subtitle')); self.label_mp.setText(self.t('label.master_password')); self.label_mp_confirm.setText(self.t('label.confirm_master_password')); self.label_mp_login.setText(self.t('label.master_password')); self.label_strength.setText(self.t('label.password_strength')); self.set_master_btn.setText(self.t('action.set_master_password')); self.login_btn.setText(self.t('action.login')); self.generate_password_btn.setText(self.t('action.generate'))
        self.shredder_title.setText(self.t('shredder.title')); self.shredder_subtitle.setText(self.t('shredder.subtitle')); self.shred_passes_label.setText(self.t('label.shred_passes')); self.shred_add_btn.setText(self.t('action.add_files')); self.shred_remove_btn.setText(self.t('action.remove_selected')); self.shred_execute_btn.setText(self.t('action.shred_selected'))
        self.settings_title.setText(self.t('settings.title')); self.settings_subtitle.setText(self.t('settings.subtitle')); self.settings_language_label.setText(self.t('label.language')); self.theme_label.setText(self.t('label.theme'))
        self.info_title.setText(self.t('info.title')); self.info_subtitle.setText(self.t('info.subtitle')); self.info_browser.setHtml(INFO_TEXT[self.i18n.language])
        self.refresh_dashboard(); self.refresh_file_lists(); self.load_log_excerpt()

    def change_language(self, language: str):
        self.i18n.set_language(language)

        if hasattr(self, "language_box"):
            self.language_box.blockSignals(True)
            self.language_box.setCurrentText(language)
            self.language_box.blockSignals(False)

        if hasattr(self, "settings_language"):
            self.settings_language.blockSignals(True)
            self.settings_language.setCurrentText(language)
            self.settings_language.blockSignals(False)

        self.state["language"] = language
        save_state(self.state)
        self.apply_translations()

    def _update_nav_state(self):
        current = self.pages.currentIndex() if hasattr(self, 'pages') else 0
        for idx, key in enumerate(self.nav_buttons): self.nav_buttons[key].setChecked(idx == current)

    def notify(self, level: str, message: str):
        if level == 'error': QMessageBox.critical(self, self.t('msg.error'), message)
        elif level == 'warning': QMessageBox.warning(self, self.t('msg.warning'), message)
        else: QMessageBox.information(self, self.t('msg.success'), message)

    def refresh_dashboard(self):
        self.card_files.value_label.setText(str(len(self.file_queue)))
        self.card_entries.value_label.setText(str(self.vault.count()))
        count = len(LOG_PATH.read_text(encoding='utf-8').splitlines()) if LOG_PATH.exists() else 0
        self.card_logs.value_label.setText(str(count)); self.card_language.value_label.setText(self.i18n.language.upper()); self.card_analytics.value_label.setText('5')

    def load_log_excerpt(self):
        self.log_excerpt.setPlainText('\n'.join(LOG_PATH.read_text(encoding='utf-8').splitlines()[-20:]) if LOG_PATH.exists() else '')

    def open_log_file(self):
        if not LOG_PATH.exists(): LOG_PATH.write_text('', encoding='utf-8')
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(LOG_PATH)))

    def copy_text(self, text: str):
        QApplication.clipboard().setText(text); self.notify('success', self.t('text.copy_success'))

    def encrypt_text_action(self):
        password = self.text_password.text().strip()
        if not password: return self.notify('warning', self.t('msg.password_required'))
        try:
            self.text_output.setPlainText(encrypt_text(self.text_input.toPlainText(), password)); append_log('Text encrypted through text module.'); self.load_log_excerpt(); self.notify('success', self.t('text.success_encrypt'))
        except Exception as exc:
            self.notify('error', str(exc))

    def decrypt_text_action(self):
        password = self.text_password.text().strip()
        if not password: return self.notify('warning', self.t('msg.password_required'))
        try:
            self.text_output.setPlainText(decrypt_text(self.text_input.toPlainText(), password)); append_log('Text decrypted through text module.'); self.load_log_excerpt(); self.notify('success', self.t('text.success_decrypt'))
        except Exception as exc:
            self.notify('error', str(exc))

    def choose_output_folder(self):
        folder = QFileDialog.getExistingDirectory(self, self.t('action.add_output_dir'))
        if folder: self.file_output.setText(folder)

    def pick_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, self.t('action.add_files'))
        if files: self.add_files_to_queue(files)

    def add_files_to_queue(self, files: list[str]):
        for f in files:
            p = Path(f)
            if p.exists() and p not in self.file_queue: self.file_queue.append(p)
        self.refresh_file_lists(); self.refresh_dashboard()

    def remove_selected_files(self):
        rows = {self.file_list.row(item) for item in self.file_list.selectedItems()}
        self.file_queue = [p for idx, p in enumerate(self.file_queue) if idx not in rows]
        self.refresh_file_lists(); self.refresh_dashboard()

    def refresh_file_lists(self):
        if hasattr(self, 'file_list'):
            self.file_list.clear()
            for p in self.file_queue:
                size = human_size(p.stat().st_size) if p.exists() else 'missing'
                self.file_list.addItem(f'{p}  •  {size}')
        if hasattr(self, 'shred_list'):
            self.shred_list.clear()
            for p in self.shred_queue:
                size = human_size(p.stat().st_size) if p.exists() else 'missing'
                self.shred_list.addItem(f'{p}  •  {size}')

    def process_file_queue(self, mode: str):
        password = self.file_password.text().strip(); out = self.file_output.text().strip()
        if not self.file_queue: return self.notify('warning', self.t('msg.queue_required'))
        if not password: return self.notify('warning', self.t('msg.password_required'))
        if not out: return self.notify('warning', self.t('msg.output_required'))
        output_dir = Path(out); output_dir.mkdir(parents=True, exist_ok=True); self.file_progress.setMaximum(len(self.file_queue)); self.file_progress.setValue(0)
        for idx, path in enumerate(list(self.file_queue), start=1):
            try:
                if mode == 'encrypt':
                    target = encrypt_file(path, output_dir, password); append_log(f'Encrypted file: {path} -> {target}')
                    if self.shred_original_check.isChecked() and path.exists(): shred_file(path, 3)
                    elif not self.keep_original_check.isChecked() and path.exists(): path.unlink(missing_ok=True)
                else:
                    target = decrypt_file(path, output_dir, password); append_log(f'Decrypted file: {path} -> {target}')
                self.file_progress.setValue(idx)
            except Exception as exc:
                self.notify('error', f'{path}\n{exc}')
        self.load_log_excerpt(); self.refresh_dashboard(); self.notify('success', self.t('status.done'))

    def _format_result(self, title: str, result):
        lines = [title, '=' * len(title), '']
        for key, value in result.metrics.items():
            lines.append(f'{key}: {value}')
        lines.append(''); lines.append(result.summary)
        self.analytics_output.setPlainText('\n'.join(lines))

    def run_text_analysis(self):
        result = analyze_text(self.analytics_text_input.toPlainText()); self._format_result(self.t('analytics.text_group'), result); append_log('Text analytics executed.'); self.load_log_excerpt()

    def run_password_analysis(self):
        pw = self.analytics_password_input.text()
        if not pw: return self.notify('warning', self.t('msg.password_required'))
        result = analyze_password(pw); self._format_result(self.t('analytics.password_group'), result); append_log('Password analytics executed.'); self.load_log_excerpt()

    def pick_analysis_file(self):
        files, _ = QFileDialog.getOpenFileNames(self, self.t('action.add_files'))
        if files:
            self.analysis_file_a = Path(files[0]); self.analytics_file_path.setText(files[0])

    def run_file_analysis(self):
        path = self.analysis_file_a or (Path(self.analytics_file_path.text()) if self.analytics_file_path.text() else None)
        if not path or not path.exists(): return self.notify('warning', self.t('msg.file_required'))
        result = analyze_file(path); self._format_result(self.t('analytics.file_group'), result); append_log(f'File analytics executed for {path}.'); self.load_log_excerpt()

    def pick_compare_file(self, slot: str):
        files, _ = QFileDialog.getOpenFileNames(self, self.t('action.add_files'))
        if not files: return
        if slot == 'a': self.analysis_file_a = Path(files[0]); self.compare_a_path.setText(files[0])
        else: self.analysis_file_b = Path(files[0]); self.compare_b_path.setText(files[0])

    def run_file_comparison(self):
        path_a = self.analysis_file_a or (Path(self.compare_a_path.text()) if self.compare_a_path.text() else None)
        path_b = self.analysis_file_b or (Path(self.compare_b_path.text()) if self.compare_b_path.text() else None)
        if not path_a or not path_b or not path_a.exists() or not path_b.exists(): return self.notify('warning', self.t('msg.compare_required'))
        result = compare_files(path_a, path_b); self._format_result(self.t('analytics.compare_group'), result); append_log(f'File comparison executed for {path_a} and {path_b}.'); self.load_log_excerpt()

    def run_random_lab(self):
        result = analyze_random_sample(self.random_length.value()); self._format_result(self.t('analytics.random_group'), result); append_log('Randomness lab executed.'); self.load_log_excerpt()

    def update_password_strength(self):
        pw = self.master_password_input.text(); result = analyze_password(pw) if pw else None
        if not pw: self.password_strength_label.setText('-'); return
        score = result.metrics['strength_score']
        key = 'strength.very_weak' if score < 20 else 'strength.weak' if score < 40 else 'strength.medium' if score < 60 else 'strength.strong' if score < 80 else 'strength.very_strong'
        self.password_strength_label.setText(f"{self.t(key)}  •  {score}/100")

    def set_master_password(self):
        pw = self.master_password_input.text(); confirm = self.master_password_confirm.text()
        if not pw: return self.notify('warning', self.t('msg.master_required'))
        if pw != confirm: return self.notify('warning', self.t('msg.password_mismatch'))
        state = load_state(); state['master_password'] = create_password_hash(pw); save_state(state); append_log('Master password created or updated.'); self.load_log_excerpt(); self.notify('success', self.t('passwords.set_success'))

    def login_master_password(self):
        pw = self.master_login_input.text(); state = load_state(); master = state.get('master_password')
        if not master: return self.notify('warning', self.t('passwords.no_master'))
        if verify_password(pw, master['salt'], master['verifier']):
            self.session_fernet = make_session_fernet(pw, master['salt']); self.session_unlocked = True; self.apply_translations(); append_log('Master password authentication successful.'); self.load_log_excerpt(); self.notify('success', self.t('passwords.login_success'))
        else:
            self.notify('error', self.t('msg.error'))

    def lock_session(self):
        self.session_unlocked = False; self.session_fernet = None; self.apply_translations(); append_log('Session locked.'); self.load_log_excerpt(); self.notify('success', self.t('passwords.lock_success'))

    def generate_password(self):
        import secrets, string
        alphabet = string.ascii_letters + string.digits + '!@#$%^&*()_+-=[]{}:;,.?/'
        generated = ''.join(secrets.choice(alphabet) for _ in range(24)); self.password_generator_output.setText(generated); self.analytics_password_input.setText(generated); self.notify('success', self.t('passwords.generate_success'))

    def require_session(self):
        if not self.session_unlocked or self.session_fernet is None: self.notify('warning', self.t('vault.locked')); return False
        return True

    def save_vault_entry(self):
        if not self.require_session(): return
        secret_enc = self.session_fernet.encrypt(self.vault_entry_secret.toPlainText().encode('utf-8')).decode('ascii')
        notes_enc = self.session_fernet.encrypt(self.vault_entry_notes.toPlainText().encode('utf-8')).decode('ascii')
        record = VaultRecord(id=self.selected_vault_id, title=self.vault_entry_title.text().strip(), category=self.vault_entry_category.text().strip(), username=self.vault_entry_username.text().strip(), secret=secret_enc, notes=notes_enc)
        self.selected_vault_id = self.vault.upsert(record); append_log(f'Vault entry saved: {record.title}'); self.refresh_vault_table(); self.load_log_excerpt(); self.notify('success', self.t('vault.saved'))

    def refresh_vault_table(self):
        if not hasattr(self, 'vault_table'): return
        records = self.vault.list_records(self.vault_search.text().strip() if hasattr(self, 'vault_search') else '')
        self.vault_table.setRowCount(len(records))
        for row_idx, row in enumerate(records):
            self.vault_table.setItem(row_idx, 0, QTableWidgetItem(str(row['id']))); self.vault_table.setItem(row_idx, 1, QTableWidgetItem(row['title'])); self.vault_table.setItem(row_idx, 2, QTableWidgetItem(row['category'])); self.vault_table.setItem(row_idx, 3, QTableWidgetItem(row['updated_at']))
        self.refresh_dashboard()

    def load_selected_vault(self):
        selected = self.vault_table.selectedItems()
        if not selected or not self.require_session(): return
        record_id = int(self.vault_table.item(selected[0].row(), 0).text()); record = self.vault.get(record_id)
        if not record: return
        self.selected_vault_id = record_id; self.vault_entry_title.setText(record['title']); self.vault_entry_category.setText(record['category']); self.vault_entry_username.setText(record['username'])
        try:
            self.vault_entry_secret.setPlainText(self.session_fernet.decrypt(record['secret'].encode('ascii')).decode('utf-8')); self.vault_entry_notes.setPlainText(self.session_fernet.decrypt(record['notes'].encode('ascii')).decode('utf-8'))
        except Exception:
            self.vault_entry_secret.setPlainText('[Locked / invalid session key]'); self.vault_entry_notes.setPlainText('[Locked / invalid session key]')

    def delete_vault_entry(self):
        if self.selected_vault_id is None: return self.notify('warning', self.t('vault.no_selection'))
        if QMessageBox.question(self, self.t('msg.warning'), self.t('msg.confirm_delete')) != QMessageBox.Yes: return
        self.vault.delete(self.selected_vault_id); append_log(f'Vault entry deleted: {self.selected_vault_id}'); self.selected_vault_id = None; self.vault_entry_title.clear(); self.vault_entry_category.clear(); self.vault_entry_username.clear(); self.vault_entry_secret.clear(); self.vault_entry_notes.clear(); self.refresh_vault_table(); self.load_log_excerpt(); self.notify('success', self.t('vault.deleted'))

    def pick_shred_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, self.t('action.add_files'))
        if files: self.add_files_to_shred_queue(files)

    def add_files_to_shred_queue(self, files: list[str]):
        for f in files:
            p = Path(f)
            if p.exists() and p not in self.shred_queue: self.shred_queue.append(p)
        self.refresh_file_lists()

    def remove_selected_shred_files(self):
        rows = {self.shred_list.row(item) for item in self.shred_list.selectedItems()}
        self.shred_queue = [p for idx, p in enumerate(self.shred_queue) if idx not in rows]
        self.refresh_file_lists()

    def execute_shred(self):
        if not self.shred_queue: return self.notify('warning', self.t('msg.queue_required'))
        if QMessageBox.question(self, self.t('msg.warning'), self.t('msg.confirm_shred')) != QMessageBox.Yes: return
        for path in list(self.shred_queue):
            try: shred_file(path, self.shred_passes.value()); append_log(f'Shredded file: {path}')
            except Exception as exc: self.notify('error', f'{path}\n{exc}')
        self.shred_queue.clear(); self.refresh_file_lists(); self.load_log_excerpt(); self.notify('success', self.t('status.done'))


def main() -> None:
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/ciphercore.ico"))

    window = MainWindow()
    window.setWindowIcon(QIcon("assets/ciphercore.ico"))
    window.show()

    sys.exit(app.exec())