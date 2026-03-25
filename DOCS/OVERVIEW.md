# CipherCore Suite Project Overview

### Deutsch
• [Projektüberblick](#projektüberblick)  
• [Kernmodule](#kernmodule)  
• [Operative Desktop-Bereiche](#operative-desktop-bereiche)  
• [Sicherheitsworkflow](#sicherheitsworkflow)  
• [Datenablage](#datenablage)  
• [Projektstruktur](#projektstruktur)  
• [Architekturüberblick](#architekturüberblick)  
• [Technologie-Stack](#technologie-stack)  
• [Build- und Release-Kontext](#build--und-release-kontext)  
• [Wesentliche Implementierungshinweise](#wesentliche-implementierungshinweise)  
• [Operative Einsatzbereiche](#operative-einsatzbereiche)  
• [Zusammenfassung](#zusammenfassung)  

### English
• [Project Overview](#project-overview)  
• [Core Modules](#core-modules)  
• [Operational Desktop Areas](#operational-desktop-areas)  
• [Security Workflow](#security-workflow)  
• [Data Locations](#data-locations)  
• [Project Structure](#project-structure)  
• [Architecture Overview](#architecture-overview)  
• [Technology Stack](#technology-stack-1)  
• [Build and Release Context](#build-and-release-context)  
• [Key Implementation Notes](#key-implementation-notes)  
• [Operational Use Cases](#operational-use-cases)  
• [Summary](#summary)  

<br>

---

<br>

## Projektüberblick

**CipherCore Suite** ist eine modulare Desktop-Anwendung für Verschlüsselung, geschützte lokale Datenhaltung, kontrollierte Dateivernichtung und technische Sicherheitsanalyse. Das Projekt bündelt mehrere sicherheitsrelevante Workflows in einer zentralen PySide6-Oberfläche und ist auf lokale Nutzung mit klarer Desktop-Orientierung ausgelegt.

Die Anwendung kombiniert klassische kryptografische Prozesse mit unterstützenden Analyse- und Verwaltungsfunktionen. Dazu zählen Text- und Dateiverschlüsselung, ein Secure Vault, Passwortfunktionen, File Shredding, Aktivitätsprotokollierung, ein Informationszentrum und technische Bewertungsfunktionen für Texte, Passwörter und Dateien.

## Kernmodule

• `ciphercore/crypto.py` übernimmt passwortbasierte Payload-Erzeugung und Wiederherstellung für Texte und Dateien.  
• `ciphercore/storage.py` verwaltet den SQLite-basierten Secure Vault und die Tabelle `vault_entries`.  
• `ciphercore/shredding.py` führt überschreibende, destruktive Dateilöschung aus.  
• `ciphercore/i18n.py` enthält die Laufzeitübersetzungen für Deutsch und Englisch.  
• `ciphercore/info_text.py` stellt die Inhalte für das integrierte Informationszentrum bereit.  
• `ciphercore/analytics.py` berechnet technische Metriken für Texte, Passwörter, Dateien und Dateivergleiche.  
• `ciphercore/app_config.py` definiert zentrale Pfade, Konstanten und Konfigurationswerte.  
• `ciphercore/social.py` kapselt projektbezogene Social- oder Link-Funktionen.  
• `ciphercore/utils.py` enthält unterstützende Hilfslogik für die Anwendung.  
• `ciphercore/ui/main_window.py` enthält die zentrale Business-Desktop-Oberfläche und die Verdrahtung der Module.  
• `run.py` startet die Anwendung, initialisiert `QApplication`, setzt das Fenster-Icon und öffnet das Hauptfenster.  

## Operative Desktop-Bereiche

Die Oberfläche ist in mehrere Funktionsbereiche gegliedert:

• Dashboard  
• Text Cryptography  
• File Cryptography  
• Security Analytics  
• Secure Vault  
• Password Center  
• File Shredder  
• Settings  
• Information  

Diese Struktur schafft eine klar segmentierte Workbench für kryptografische, analytische und administrative Arbeitsabläufe.

## Sicherheitsworkflow

1. Master-Passwort festlegen.  
2. Sitzung entsperren.  
3. Sensible Vault-Einträge über den Secure Vault speichern oder lesen.  
4. Texte und Dateien über die vorgesehenen Kryptografie-Workflows verschlüsseln oder entschlüsseln.  
5. Analysefunktionen zur technischen Bewertung verwenden.  
6. Dateien bei Bedarf irreversibel über den Shredder vernichten.  

## Datenablage

Die Anwendung speichert lokalen Zustand, Vault-Daten und Logs in einem versteckten Anwendungsordner im Home-Verzeichnis des Benutzers.

Typische Inhalte:

• `~/.ciphercore_suite/data/vault.db`  
• `~/.ciphercore_suite/data/app_state.json`  
• `~/.ciphercore_suite/logs/activity.log`  

## Projektstruktur

```text
ciphercore_suite/
├── assets/
│   └── ciphercore.ico
├── ciphercore/
│   ├── analytics.py
│   ├── app_config.py
│   ├── crypto.py
│   ├── i18n.py
│   ├── info_text.py
│   ├── shredding.py
│   ├── social.py
│   ├── storage.py
│   ├── utils.py
│   └── ui/
│       └── main_window.py
├── build_windows_pyinstaller.bat
├── PROJECT_OVERVIEW.md
├── README.md
├── requirements.txt
├── run.py
├── start_windows.bat
└── version_info.txt
```

## Architekturüberblick

### UI und Orchestrierung

Die zentrale Benutzerführung liegt in `ciphercore/ui/main_window.py`. Dort werden Navigation, Seitenwechsel, UI-Interaktion, Sprachumschaltung, Sitzungsverwaltung, Vault-Funktionen, Analytics-Ausgabe und Theme-Logik zusammengeführt.

### Kryptografie

`ciphercore/crypto.py` implementiert die kryptografischen Kernfunktionen, darunter Schlüsselableitung, Payload-Verschlüsselung, Passwort-Hashing und die Grundlagen für geschützte Text- und Dateioperationen.

### Persistenz

`ciphercore/storage.py` verwaltet die lokale SQLite-Datenbank. Der Secure Vault speichert Einträge in `vault_entries`. Nach der tatsächlich dokumentierten Implementierung sind insbesondere `secret` und `notes` verschlüsselt, während bestimmte Metadatenfelder derzeit im Klartext gespeichert werden.

### Analytics

`ciphercore/analytics.py` stellt technische Analysefunktionen bereit, beispielsweise Entropie, SHA-256, Unique-Ratio, Zeichenklassenverteilung, Chi-Quadrat-Uniformität, serielle Korrelation, Passwort-Score und dateibasierte Bewertungskennzahlen.

### Shredding

`ciphercore/shredding.py` ist für kontrollierte, überschreibende Dateilöschung zuständig. Dieser Bereich ist operativ hochsensibel, da er destruktiv und irreversibel arbeitet.

### Konfiguration und Hilfsschichten

`ciphercore/app_config.py`, `ciphercore/i18n.py`, `ciphercore/info_text.py`, `ciphercore/social.py` und `ciphercore/utils.py` bilden die projektweiten Konfigurations-, Übersetzungs-, Informations- und Hilfsschichten.

## Technologie-Stack

• Python 3.11+  
• PySide6  
• cryptography  
• NumPy  
• SciPy  
• SQLite3  

## Build- und Release-Kontext

Für Windows ist ein Build-Prozess über `build_windows_pyinstaller.bat` vorbereitet. Der Workflow deckt Bereinigung alter Artefakte, Installation von Abhängigkeiten, PyInstaller-Build, Icon-Einbettung und Metadaten über `version_info.txt` ab.

Typisches Zielartefakt:

```text
dist/CipherCoreSuite.exe
```

## Wesentliche Implementierungshinweise

Aus den bereits dokumentierten Projektmerkmalen ergeben sich folgende operative Punkte:

• Der Secure Vault verschlüsselt derzeit vor allem `secret` und `notes`.  
• `title`, `category` und `username` sind aktuell nicht vollständig geschützt und bleiben ein relevantes Metadatenrisiko.  
• Das Master-Passwort-Modell ist zentral für den Zugriff auf verschlüsselte Vault-Inhalte.  
• Ein Passwortwechsel benötigt perspektivisch eine sichere Re-Key- oder Migrationslogik.  
• Die Oberfläche unterstützt Dark- und Light-Theme, jedoch ist die Theme-Auswahl aktuell nicht persistiert wie die Spracheinstellung.  
• Einige Social- oder Kontaktlinks können noch Platzhalterwerte enthalten.  
• Verschlüsselte Dateipayloads verwenden die Endung `.ccore`.  

## Operative Einsatzbereiche

CipherCore Suite eignet sich besonders für:

• lokale Verschlüsselungs- und Entschlüsselungsprozesse  
• geschützte Ablage sensibler Informationen  
• technische Passwort- und Dateibewertung  
• kontrollierte Dateivernichtung  
• Desktop-basierte Sicherheits- und Analyseabläufe  

## Zusammenfassung

CipherCore Suite ist als integrierte lokale Security-Workbench konzipiert. Das Projekt vereint Kryptografie, Datenhaltung, Analyse und Dateivernichtung in einer modularen Desktop-Struktur. Der aktuelle Stand bietet bereits eine belastbare funktionale Basis, zeigt aber zugleich klare Weiterentwicklungspunkte im Bereich vollständiger Vault-Verschlüsselung, Passwortrotation, Build-Hardening und produktiver Release-Reife.

<br>

---

<br>

## Project Overview

**CipherCore Suite** is a modular desktop application for encryption, protected local data storage, controlled file destruction and technical security analysis. The project combines multiple security-relevant workflows inside one central PySide6 interface and is designed for local usage with a clear desktop-first orientation.

The application combines classical cryptographic operations with supporting analysis and management capabilities. These include text and file encryption, a Secure Vault, password-related utilities, file shredding, activity logging, an information center and technical evaluation functions for text, passwords and files.

## Core Modules

• `ciphercore/crypto.py` handles password-based payload creation and recovery for text and files.  
• `ciphercore/storage.py` manages the SQLite-backed secure vault and the `vault_entries` table.  
• `ciphercore/shredding.py` performs overwrite-based destructive deletion.  
• `ciphercore/i18n.py` contains the runtime translation map for German and English.  
• `ciphercore/info_text.py` provides the detailed information center content.  
• `ciphercore/analytics.py` calculates technical metrics for text, passwords, files and file comparison.  
• `ciphercore/app_config.py` defines central paths, constants and configuration values.  
• `ciphercore/social.py` encapsulates project-related social or link functions.  
• `ciphercore/utils.py` contains supporting helper logic for the application.  
• `ciphercore/ui/main_window.py` contains the main business desktop interface and module wiring.  
• `run.py` starts the application, initializes `QApplication`, sets the window icon and opens the main window.  

## Operational Desktop Areas

The interface is organized into several functional areas:

• Dashboard  
• Text Cryptography  
• File Cryptography  
• Security Analytics  
• Secure Vault  
• Password Center  
• File Shredder  
• Settings  
• Information  

This structure creates a clearly segmented workbench for cryptographic, analytical and administrative workflows.

## Security Workflow

1. Set a master password.  
2. Unlock the session.  
3. Store or read sensitive vault entries through the secure vault.  
4. Encrypt or decrypt text and files through the intended cryptography workflows.  
5. Use analytics functions for technical evaluation.  
6. Destroy files irreversibly through the shredder where required.  

## Data Locations

The application writes local state, vault data and logs into a hidden application folder inside the user's home directory.

Typical contents:

• `~/.ciphercore_suite/data/vault.db`  
• `~/.ciphercore_suite/data/app_state.json`  
• `~/.ciphercore_suite/logs/activity.log`  

## Project Structure

```text
ciphercore_suite/
├── assets/
│   └── ciphercore.ico
├── ciphercore/
│   ├── analytics.py
│   ├── app_config.py
│   ├── crypto.py
│   ├── i18n.py
│   ├── info_text.py
│   ├── shredding.py
│   ├── social.py
│   ├── storage.py
│   ├── utils.py
│   └── ui/
│       └── main_window.py
├── build_windows_pyinstaller.bat
├── PROJECT_OVERVIEW.md
├── README.md
├── requirements.txt
├── run.py
├── start_windows.bat
└── version_info.txt
```

## Architecture Overview

### UI and orchestration

The main user flow is centered in `ciphercore/ui/main_window.py`. This file combines navigation, page handling, UI interaction, language switching, session management, vault functions, analytics output and theme logic.

### Cryptography

`ciphercore/crypto.py` implements the cryptographic core, including key derivation, payload encryption, password hashing and the basis for protected text and file operations.

### Persistence

`ciphercore/storage.py` manages the local SQLite database. The Secure Vault stores records in `vault_entries`. Based on the documented implementation state, `secret` and `notes` are encrypted, while certain metadata fields are still stored in plaintext.

### Analytics

`ciphercore/analytics.py` provides technical analysis functions such as entropy, SHA-256, unique ratio, character class distribution, chi-square uniformity, serial correlation, password scoring and file-oriented metrics.

### Shredding

`ciphercore/shredding.py` is responsible for controlled overwrite-based file destruction. This area is operationally sensitive because it is destructive and irreversible.

### Configuration and support layers

`ciphercore/app_config.py`, `ciphercore/i18n.py`, `ciphercore/info_text.py`, `ciphercore/social.py` and `ciphercore/utils.py` form the shared configuration, translation, information and support layers of the project.

## Technology Stack

• Python 3.11+  
• PySide6  
• cryptography  
• NumPy  
• SciPy  
• SQLite3  

## Build and Release Context

A Windows build workflow is prepared through `build_windows_pyinstaller.bat`. The process covers cleanup of old artifacts, dependency installation, PyInstaller packaging, icon embedding and metadata integration through `version_info.txt`.

Typical target artifact:

```text
dist/CipherCoreSuite.exe
```

## Key Implementation Notes

Based on the already documented project characteristics, the following points matter operationally:

• The Secure Vault currently encrypts mainly `secret` and `notes`.  
• `title`, `category` and `username` are not yet fully protected and remain a relevant metadata exposure risk.  
• The master password model is central for access to encrypted vault content.  
• Password rotation should eventually be backed by a secure re-key or migration flow.  
• The interface supports dark and light themes, but theme selection is not currently persisted the same way as language settings.  
• Some social or contact links may still contain placeholder values.  
• Encrypted file payloads use the `.ccore` suffix.  

## Operational Use Cases

CipherCore Suite is particularly suited for:

• local encryption and decryption workflows  
• protected storage of sensitive information  
• technical password and file evaluation  
• controlled file destruction  
• desktop-based security and analysis workflows  

## Summary

CipherCore Suite is designed as an integrated local security workbench. The project combines cryptography, storage, analytics and file destruction in a modular desktop structure. The current state already provides a solid functional basis, while also showing clear next-step priorities around full vault encryption, password rotation, build hardening and production-grade release maturity.
