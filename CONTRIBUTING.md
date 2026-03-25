# CONTRIBUTING

## Inhaltsverzeichnis

### Deutsch
• [Beitragen zu CipherCore Suite](#beitragen-zu-ciphercore-suite)  
• [Ziel dieses Dokuments](#ziel-dieses-dokuments)  
• [Grundsätze für Beiträge](#grundsätze-für-beiträge)  
• [Geeignete Arten von Beiträgen](#geeignete-arten-von-beiträgen)  
• [Nicht geeignete Beiträge](#nicht-geeignete-beiträge)  
• [Entwicklungsumgebung](#entwicklungsumgebung)  
• [Projektstruktur und Zuständigkeiten](#projektstruktur-und-zuständigkeiten)  
• [Branching und Arbeitsweise](#branching-und-arbeitsweise)  
• [Commit-Richtlinien](#commit-richtlinien)  
• [Code-Standards](#code-standards)  
• [Dokumentationsstandards](#dokumentationsstandards)  
• [Security-Anforderungen](#security-anforderungen)  
• [Test- und Validierungsanforderungen](#test--und-validierungsanforderungen)  
• [Pull-Request-Anforderungen](#pull-request-anforderungen)  
• [Review-Kriterien](#review-kriterien)  
• [Lizenz- und Rechtehinweise](#lizenz--und-rechtehinweise)  
• [Kommunikation](#kommunikation)  

### English
• [English](#english)  
• [Contributing to CipherCore Suite](#contributing-to-ciphercore-suite)  
• [Purpose of This Document](#purpose-of-this-document)  
• [Contribution Principles](#contribution-principles)  
• [Suitable Contribution Types](#suitable-contribution-types)  
• [Unsuitable Contributions](#unsuitable-contributions)  
• [Development Environment](#development-environment)  
• [Project Structure and Ownership](#project-structure-and-ownership)  
• [Branching and Workflow](#branching-and-workflow)  
• [Commit Guidelines](#commit-guidelines)  
• [Code Standards](#code-standards-1)  
• [Documentation Standards](#documentation-standards)  
• [Security Requirements](#security-requirements)  
• [Testing and Validation Requirements](#testing-and-validation-requirements)  
• [Pull Request Requirements](#pull-request-requirements)  
• [Review Criteria](#review-criteria)  
• [License and Rights Notes](#license-and-rights-notes)  
• [Communication](#communication-1)  

<br>

---

<br>

## Deutsch

## Beitragen zu CipherCore Suite

Vielen Dank für dein Interesse an Beiträgen zu CipherCore Suite. Dieses Dokument definiert die qualitativen, technischen und organisatorischen Rahmenbedingungen für Beiträge am Projekt.

## Ziel dieses Dokuments

Dieses Dokument soll sicherstellen, dass Beiträge:

• technisch nachvollziehbar bleiben  
• architektonisch konsistent umgesetzt werden  
• keine Sicherheitsrisiken oder Qualitätsverluste einführen  
• sauber dokumentiert und reviewfähig sind  
• zum Produkt- und Reifegrad von CipherCore Suite passen  

## Grundsätze für Beiträge

Beiträge sollen sich an folgenden Leitlinien orientieren:

• Qualität vor Geschwindigkeit  
• Sicherheit vor Komfort  
• Klarheit vor unnötiger Komplexität  
• lokale Nachvollziehbarkeit vor verstecktem Verhalten  
• konsistente Terminologie in Code und Dokumentation  
• keine Änderungen ohne erkennbaren fachlichen Mehrwert  

## Geeignete Arten von Beiträgen

Geeignet sind insbesondere:

• Bugfixes  
• Stabilitätsverbesserungen  
• sicherheitsrelevante Härtungen  
• bessere Fehlerbehandlung  
• Erweiterungen der Dokumentation  
• UX-Verbesserungen ohne Bruch der Architektur  
• Verbesserungen an Build- und Release-Prozessen  
• Tests und Validierungslogik  
• Internationalisierung und sprachliche Korrekturen  
• Performance-Optimierungen mit nachvollziehbarer Wirkung  

## Nicht geeignete Beiträge

Nicht geeignet oder nur nach expliziter Abstimmung geeignet sind:

• unkommentierte große Architekturumbauten  
• Änderungen mit verstecktem Netzwerkverhalten  
• Einbau externer Telemetrie ohne klare Dokumentation  
• ungeprüfte Kryptografie-Änderungen  
• schwer nachvollziehbare Obfuskation  
• Debug-Code, Platzhalter, Testdaten oder Secrets im Beitrag  
• Änderungen, die bestehende Daten unkontrolliert migrieren oder gefährden  

## Entwicklungsumgebung

Empfohlene lokale Basis:

• Python 3.11 oder neuer  
• virtuelle Umgebung  
• aktuelle Abhängigkeiten aus `requirements.txt`  
• Windows für den vorhandenen Build-Workflow empfohlen  

Typische Initialisierung:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Projektstruktur und Zuständigkeiten

Wichtige Projektbereiche:

• `ciphercore/crypto.py` für kryptografische Kernlogik  
• `ciphercore/storage.py` für Vault-Persistenz  
• `ciphercore/analytics.py` für technische Analysefunktionen  
• `ciphercore/shredding.py` für überschreibende Dateivernichtung  
• `ciphercore/i18n.py` für Sprachlogik  
• `ciphercore/ui/main_window.py` für zentrale UI- und Orchestrierungslogik  
• `ciphercore/app_config.py` für Pfade, Konstanten und Konfiguration  
• Markdown-Dokumente für Projekt-, Security- und Betriebsdokumentation  

Beiträge sollen sich funktional möglichst auf den betroffenen Bereich beschränken.

## Branching und Arbeitsweise

Empfohlene Branch-Namenskonventionen:

• `feature/...` für neue Funktionen  
• `fix/...` für Fehlerbehebungen  
• `docs/...` für Dokumentation  
• `security/...` für Sicherheitsverbesserungen  
• `refactor/...` für interne Strukturverbesserungen  

Beispiele:

• `feature/vault-export`  
• `fix/theme-persistence`  
• `docs/user-guide-update`  
• `security/password-rotation-guard`  

## Commit-Richtlinien

Commits sollen klar, fachlich präzise und möglichst klein gehalten werden.

Empfohlene Präfixe:

• `feat:` neue Funktion  
• `fix:` Fehlerbehebung  
• `docs:` Dokumentation  
• `refactor:` interne Umstrukturierung  
• `test:` Tests  
• `security:` Sicherheitsrelevante Änderung  
• `build:` Build- oder Packaging-Änderung  

Beispiele:

• `feat: add backup export preparation for vault data`  
• `fix: prevent invalid session access in vault operations`  
• `docs: extend user guide for file cryptography`  
• `security: harden local handling of sensitive values`  

## Code-Standards

Erwartete Standards:

• gut lesbarer, wartbarer Python-Code  
• klare Funktions- und Variablennamen  
• keine unnötige Komplexität  
• keine stillen Seiteneffekte ohne Dokumentation  
• saubere Fehlerbehandlung  
• nachvollziehbare Trennung von UI, Fachlogik und Persistenz  
• keine sensiblen Klartextwerte im Code  
• Änderungen an Kryptografie nur mit besonderer Sorgfalt und Dokumentation  

Zusätzlich gilt:

• bestehende Architektur respektieren  
• neue Konfigurationen zentral und nachvollziehbar definieren  
• UI-Änderungen sollen funktional konsistent bleiben  
• Dateipfade und Speicherorte dürfen nicht unsauber hartkodiert werden  

## Dokumentationsstandards

Jeder relevante Beitrag soll die Dokumentation mitdenken.

Insbesondere dann, wenn Änderungen betreffen:

• Architektur  
• Kryptografie  
• Datenmodell  
• Bedienung  
• Security-Verhalten  
• Build- oder Release-Prozesse  

Mögliche zu aktualisierende Dokumente:

• `README.md`  
• `OVERVIEW.md`  
• `ARCHITECTURE.md`  
• `CRYPTOGRAPHY.md`  
• `DATA_MODEL.md`  
• `USER_GUIDE.md`  
• `CHANGELOG.md`  
• Security-Dokumente und Checklisten  

## Security-Anforderungen

Sicherheitsrelevante Beiträge müssen besonders sauber umgesetzt werden.

Pflichtanforderungen:

• keine Secrets im Repository  
• keine sensiblen Testdaten in Commits  
• keine Protokollierung von Master-Passwörtern, Schlüsselmaterial oder entschlüsselten Geheimnissen  
• keine unkontrollierten Änderungen an Vault-Verschlüsselung  
• keine Änderungen am Passwortmodell ohne Bewertung der Migrationsfolgen  
• neue Risiken transparent dokumentieren  

Besonders kritische Bereiche:

• `crypto.py`  
• `storage.py`  
• Session-Handling in `main_window.py`  
• Logging  
• Build- und Release-Artefakte  

## Test- und Validierungsanforderungen

Vor einem Pull Request sollte mindestens geprüft werden:

• Anwendung startet lokal  
• geänderte Funktion arbeitet reproduzierbar  
• keine offensichtlichen Regressionen im betroffenen Bereich  
• relevante UI-Abläufe funktionieren weiter  
• bei Security-Änderungen sind Risiken und Grenzen dokumentiert  
• bei Datenänderungen wurde auf Konsistenz geachtet  

Wo sinnvoll, sollten Tests oder reproduzierbare Prüfschritte beschrieben werden.

## Pull-Request-Anforderungen

Ein guter Pull Request enthält:

• klare Zusammenfassung der Änderung  
• fachliche Motivation  
• betroffene Module oder Dokumente  
• Risiken oder bekannte Grenzen  
• Hinweise zu manuellen Testschritten  
• bei UI-Änderungen optional Screenshots oder Beschreibung  
• bei Security-Änderungen klare Einordnung der Auswirkungen  

Empfohlene Struktur:

1. Ziel der Änderung  
2. betroffene Bereiche  
3. Validierung  
4. Risiken oder offene Punkte  

## Review-Kriterien

Ein Beitrag wird insbesondere danach bewertet, ob er:

• fachlich sinnvoll ist  
• architektonisch passt  
• die Lesbarkeit verbessert oder mindestens erhält  
• keine unnötigen Risiken einführt  
• Dokumentation und Verhalten konsistent hält  
• produktionsreif genug für das Projektziel ist  

## Lizenz- und Rechtehinweise

Mit einem Beitrag bestätigst du, dass:

• du über die nötigen Rechte an deinem Beitrag verfügst  
• der Beitrag keine fremden Rechte verletzt  
• keine unzulässigen oder geheimen Inhalte eingebracht werden  
• der Beitrag unter den Projektbedingungen weiterverwendet werden darf  

Die verbindliche Lizenz wird durch die Lizenzdatei des Projekts geregelt.

## Kommunikation

Beiträge sollten sachlich, klar und technisch nachvollziehbar kommuniziert werden. Bei Unsicherheiten gilt:

• Annahmen offen benennen  
• Risiken klar formulieren  
• sicherheitsrelevante Fragen nicht bagatellisieren  
• lieber präzise als ausschweifend argumentieren  

<br>

---

<br>

## English

## Contributing to CipherCore Suite

Thank you for your interest in contributing to CipherCore Suite. This document defines the qualitative, technical and organizational framework for contributions to the project.

## Purpose of This Document

This document is intended to ensure that contributions:

• remain technically understandable  
• stay architecturally consistent  
• do not introduce security risks or quality regressions  
• are properly documented and reviewable  
• fit the product and maturity level of CipherCore Suite  

## Contribution Principles

Contributions should follow these principles:

• quality before speed  
• security before convenience  
• clarity before unnecessary complexity  
• local traceability before hidden behavior  
• consistent terminology across code and documentation  
• no changes without a clear functional benefit  

## Suitable Contribution Types

The following are especially suitable:

• bug fixes  
• stability improvements  
• security hardening  
• improved error handling  
• documentation enhancements  
• UX improvements without breaking architecture  
• build and release process improvements  
• tests and validation logic  
• internationalization and language corrections  
• performance optimizations with traceable value  

## Unsuitable Contributions

The following are unsuitable or should only be proposed after explicit alignment:

• undocumented large-scale architectural rewrites  
• changes with hidden network behavior  
• external telemetry without clear documentation  
• unreviewed cryptographic changes  
• hard-to-understand obfuscation  
• debug code, placeholders, test data or secrets in contributions  
• changes that migrate or endanger existing data without control  

## Development Environment

Recommended local baseline:

• Python 3.11 or newer  
• virtual environment  
• current dependencies from `requirements.txt`  
• Windows recommended for the existing build workflow  

Typical setup:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

## Project Structure and Ownership

Relevant project areas:

• `ciphercore/crypto.py` for cryptographic core logic  
• `ciphercore/storage.py` for vault persistence  
• `ciphercore/analytics.py` for technical analytics  
• `ciphercore/shredding.py` for overwrite-based file destruction  
• `ciphercore/i18n.py` for language handling  
• `ciphercore/ui/main_window.py` for central UI and orchestration logic  
• `ciphercore/app_config.py` for paths, constants and configuration  
• Markdown documents for project, security and operations documentation  

Contributions should stay as scoped as possible to the affected area.

## Branching and Workflow

Recommended branch naming conventions:

• `feature/...` for new features  
• `fix/...` for bug fixes  
• `docs/...` for documentation  
• `security/...` for security improvements  
• `refactor/...` for internal restructuring  

Examples:

• `feature/vault-export`  
• `fix/theme-persistence`  
• `docs/user-guide-update`  
• `security/password-rotation-guard`  

## Commit Guidelines

Commits should be clear, technically precise and reasonably small.

Recommended prefixes:

• `feat:` new feature  
• `fix:` bug fix  
• `docs:` documentation  
• `refactor:` internal restructuring  
• `test:` tests  
• `security:` security-related change  
• `build:` build or packaging change  

Examples:

• `feat: add backup export preparation for vault data`  
• `fix: prevent invalid session access in vault operations`  
• `docs: extend user guide for file cryptography`  
• `security: harden local handling of sensitive values`  

## Code Standards

Expected standards:

• readable, maintainable Python code  
• clear function and variable names  
• no unnecessary complexity  
• no silent side effects without documentation  
• proper error handling  
• traceable separation of UI, business logic and persistence  
• no sensitive plaintext values in code  
• cryptographic changes require extra care and documentation  

Additionally:

• respect the existing architecture  
• define new configuration values centrally and transparently  
• UI changes should remain functionally consistent  
• file paths and storage locations must not be unsafely hardcoded  

## Documentation Standards

Every relevant contribution should consider documentation impact.

Especially when changes affect:

• architecture  
• cryptography  
• data model  
• user operation  
• security behavior  
• build or release processes  

Potential documents to update:

• `README.md`  
• `OVERVIEW.md`  
• `ARCHITECTURE.md`  
• `CRYPTOGRAPHY.md`  
• `DATA_MODEL.md`  
• `USER_GUIDE.md`  
• `CHANGELOG.md`  
• security documents and checklists  

## Security Requirements

Security-relevant contributions must be implemented with particular care.

Mandatory requirements:

• no secrets in the repository  
• no sensitive test data in commits  
• no logging of master passwords, key material or decrypted secrets  
• no uncontrolled changes to vault encryption  
• no password model changes without assessing migration consequences  
• document new risks transparently  

Particularly critical areas:

• `crypto.py`  
• `storage.py`  
• session handling in `main_window.py`  
• logging  
• build and release artifacts  

## Testing and Validation Requirements

Before opening a pull request, contributors should at least verify:

• the application starts locally  
• the changed feature works reproducibly  
• no obvious regressions exist in the affected area  
• relevant UI flows still work  
• for security changes, risks and boundaries are documented  
• for data-related changes, consistency has been considered  

Where appropriate, tests or reproducible validation steps should be described.

## Pull Request Requirements

A good pull request includes:

• a clear summary of the change  
• technical motivation  
• affected modules or documents  
• risks or known boundaries  
• notes about manual validation steps  
• optional screenshots or behavior notes for UI changes  
• clear impact statement for security changes  

Recommended structure:

1. objective of the change  
2. affected areas  
3. validation  
4. risks or open points  

## Review Criteria

A contribution is primarily evaluated by whether it:

• is functionally meaningful  
• fits the architecture  
• improves readability or at least preserves it  
• does not introduce unnecessary risks  
• keeps documentation and behavior consistent  
• is production-appropriate for the project goal  

## License and Rights Notes

By contributing, you confirm that:

• you have the necessary rights to your contribution  
• the contribution does not infringe third-party rights  
• no prohibited or confidential content is introduced  
• the contribution may be reused under the project conditions  

The binding license terms are defined by the project license file.

## Communication

Contributions should be communicated factually, clearly and in technically traceable form. In case of uncertainty:

• state assumptions openly  
• formulate risks clearly  
• do not downplay security-relevant questions  
• prefer precision over unnecessary length  
