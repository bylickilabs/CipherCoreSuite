# CipherCore Suite

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![MIT License](https://img.shields.io/github/license/bylickilabs/CipherCoreSuite?label=MIT%20License)
![Windows](https://img.shields.io/badge/Desktop-Windows-0078D6?logo=windows&logoColor=white)
![Security](https://img.shields.io/badge/Security-Cryptography-darkred)
![Analytics](https://img.shields.io/badge/Analytics-NumPy%20%26%20SciPy-013243?logo=numpy&logoColor=white)
![State](https://img.shields.io/badge/State-Enterprise%20Analytics-purple)
![Last Commit](https://img.shields.io/github/last-commit/bylickilabs/CipherCoreSuite?label=Last%20Commit)

### Deutsch
• [CipherCore Suite](#ciphercore-suite)  
• [Deutsch](#deutsch)  
• [Funktionsumfang](#funktionsumfang)  
  • [Kernmodule](#kernmodule)  
  • [Desktop-Bereiche](#desktop-bereiche)  
• [Technologie-Stack](#technologie-stack)  
• [Projektstruktur](#projektstruktur)  
• [Architekturüberblick](#architekturüberblick)  
  • [`run.py`](#runpy)  
  • [`ciphercore/ui/main_window.py`](#ciphercoreuimain_windowpy)  
  • [`ciphercore/crypto.py`](#ciphercorecryptopy)  
  • [`ciphercore/storage.py`](#ciphercorestoragepy)  
  • [`ciphercore/analytics.py`](#ciphercoreanalyticspy)  
  • [`ciphercore/shredding.py`](#ciphercoreshreddingpy)  
  • [`ciphercore/i18n.py`](#ciphercorei18npy)  
  • [`ciphercore/info_text.py`](#ciphercoreinfo_textpy)  
  • [`ciphercore/app_config.py`](#ciphercoreapp_configpy)  
• [Installation](#installation)  
  • [Voraussetzungen](#voraussetzungen)  
  • [Abhängigkeiten installieren](#abhängigkeiten-installieren)  
  • [Anwendung starten](#anwendung-starten)  
• [Windows-Build](#windows-build)  
• [Lokale Datenhaltung](#lokale-datenhaltung)  
• [Sicherheitsworkflow](#sicherheitsworkflow)  
• [Hinweise zur tatsächlichen Implementierung](#hinweise-zur-tatsächlichen-implementierung)  
  • [1. Vault-Verschlüsselung](#1-vault-verschlüsselung)  
  • [2. Session-Modell](#2-session-modell)  
  • [3. Master-Passwort-Rotation](#3-master-passwort-rotation)  
  • [4. Theme-Verhalten](#4-theme-verhalten)  
  • [5. Social-Links](#5-social-links)  
  • [6. Dateiendung](#6-dateiendung)  
• [Analysefunktionen](#analysefunktionen)  
  • [Textanalyse](#textanalyse)  
  • [Passwortanalyse](#passwortanalyse)  
  • [Dateianalyse](#dateianalyse)  
  • [Dateivergleich](#dateivergleich)  
  • [Randomness Lab](#randomness-lab)  
• [Risiken und Betriebshinweise](#risiken-und-betriebshinweise)  
• [Geeignete Einsatzbereiche](#geeignete-einsatzbereiche)  
• [Roadmap-Empfehlungen](#roadmap-empfehlungen)  
• [Copyright](#copyright)  

### English
• [English](#english)  
• [Feature Set](#feature-set)  
  • [Core Modules](#core-modules)  
  • [Desktop Areas](#desktop-areas)  
• [Technology Stack](#technology-stack)  
• [Project Structure](#project-structure)  
• [Architecture Overview](#architecture-overview)  
  • [`run.py`](#runpy-1)  
  • [`ciphercore/ui/main_window.py`](#ciphercoreuimain_windowpy-1)  
  • [`ciphercore/crypto.py`](#ciphercorecryptopy-1)  
  • [`ciphercore/storage.py`](#ciphercorestoragepy-1)  
  • [`ciphercore/analytics.py`](#ciphercoreanalyticspy-1)  
  • [`ciphercore/shredding.py`](#ciphercoreshreddingpy-1)  
  • [`ciphercore/i18n.py`](#ciphercorei18npy-1)  
  • [`ciphercore/info_text.py`](#ciphercoreinfo_textpy-1)  
  • [`ciphercore/app_config.py`](#ciphercoreapp_configpy-1)  
• [Installation](#installation-1)  
  • [Requirements](#requirements)  
  • [Install dependencies](#install-dependencies)  
  • [Start the application](#start-the-application)  
• [Windows Build](#windows-build-1)  
• [Local Data Storage](#local-data-storage)  
• [Security Workflow](#security-workflow)  
• [Notes About the Actual Implementation](#notes-about-the-actual-implementation)  
  • [1. Vault Encryption](#1-vault-encryption)  
  • [2. Session Model](#2-session-model)  
  • [3. Master Password Rotation](#3-master-password-rotation)  
  • [4. Theme Behavior](#4-theme-behavior)  
  • [5. Social Links](#5-social-links-1)  
  • [6. File Extension](#6-file-extension)  
• [Analytics Functions](#analytics-functions)  
  • [Text Analysis](#text-analysis)  
  • [Password Analysis](#password-analysis)  
  • [File Analysis](#file-analysis)  
  • [File Comparison](#file-comparison)  
  • [Randomness Lab](#randomness-lab-1)  
• [Risks and Operational Guidance](#risks-and-operational-guidance)  
• [Suitable Use Cases](#suitable-use-cases)  
• [Roadmap Recommendations](#roadmap-recommendations)  
• [Copyright](#copyright-1)

## Deutsch

**CipherCore Suite** ist eine modulare Desktop-Anwendung für Verschlüsselung, geschützte lokale Datenhaltung, kontrollierte Dateivernichtung und technische Sicherheitsanalyse. Das Projekt kombiniert klassische Kryptografie mit einer strukturierten Analytics-Ebene und stellt mehrere sicherheitsrelevante Workflows in einer zentralen PySide6-Oberfläche bereit.

Die Anwendung ist auf lokale Nutzung ausgelegt und bündelt Text- und Dateiverschlüsselung, einen Secure Vault, Passwortfunktionen, File Shredding sowie statistische Analysefunktionen in einer zusammenhängenden Desktop-Workbench.

## Funktionsumfang

### Kernmodule
• Textverschlüsselung und Textentschlüsselung  
• Dateiverschlüsselung und Dateientschlüsselung  
• Secure Vault mit lokaler SQLite-Datenbank  
• Master-Passwort und Session-Lock  
• Passwortgenerator und Passwortbewertung  
• File Shredder mit mehrfacher Überschreibung  
• Security Analytics für Texte, Passwörter, Dateien und Dateivergleiche  
• Randomness Lab zur Bewertung zufallsbasierter Daten  
• Deutsche und englische Benutzeroberfläche  
• Aktivitätsprotokoll und Informationszentrum  
• Drag-and-drop für Datei-Queues  
• Windows-Build per PyInstaller inklusive EXE-Metadaten  

### Desktop-Bereiche
Die Oberfläche ist in folgende operative Bereiche gegliedert:

• Dashboard  
• Text Cryptography  
• File Cryptography  
• Security Analytics  
• Secure Vault  
• Password Center  
• File Shredder  
• Settings  
• Information  

## Technologie-Stack

• Python 3.11+  
• PySide6  
• cryptography  
• NumPy  
• SciPy  
• SQLite3  

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

### `run.py`
Startpunkt der Anwendung. Initialisiert `QApplication`, setzt das Fenster-Icon und öffnet das Hauptfenster.

### `ciphercore/ui/main_window.py`
Zentrale Desktop-Oberfläche. Hier werden Navigation, Seitenlogik, Sprache, Session-Steuerung, Vault-Handling, Analytics-Ausgabe und UI-Styling zusammengeführt.

### `ciphercore/crypto.py`
Implementiert die kryptografischen Kernfunktionen.

Enthalten sind unter anderem:
• Schlüsselableitung über PBKDF2-HMAC-SHA256  
• Fernet-basierte Nutzdatenverschlüsselung  
• Portable JSON-Payloads für Text- und Dateioperationen  
• Passwort-Hashing und Verifikation für das Master-Passwort  
• Session-Schlüsselaufbau für den Vault-Zugriff  

### `ciphercore/storage.py`
Verwaltet den Secure Vault auf Basis von SQLite. Datensätze werden in `vault_entries` gespeichert.

Gespeicherte Felder:
• `title`  
• `category`  
• `username`  
• `secret`  
• `notes`  
• Zeitstempel für Erstellung und Aktualisierung  

### `ciphercore/analytics.py`
Stellt Analysefunktionen für unterschiedliche Datentypen bereit.

Berechnete Kennzahlen umfassen unter anderem:
• Entropie  
• SHA-256  
• Zeichensatzgröße  
• Unique Ratio  
• Chi-Quadrat-Uniformität  
• serielle Korrelation  
• Byte-Verteilungen  
• Blockmittelwert-Streuung  
• Passwort-Score  

### `ciphercore/shredding.py`
Verantwortlich für kontrollierte, überschreibende Dateilöschung.

### `ciphercore/i18n.py`
Enthält die Laufzeitübersetzungen für Deutsch und Englisch.

### `ciphercore/info_text.py`
Liefert die Inhalte für das integrierte Informationszentrum.

### `ciphercore/app_config.py`
Definiert zentrale Pfade, Konstanten und Konfigurationen.

Wesentliche Punkte:
• versteckter App-Ordner im Benutzerverzeichnis  
• Daten- und Log-Verzeichnisse  
• SQLite-Datenbankpfad  
• Statusdatei  
• Log-Datei  
• PBKDF2-Iterationsanzahl  
• Social-Links  

## Installation

### Voraussetzungen
• Python 3.11 oder neuer  
• pip  
• Windows empfohlen für den vorhandenen Build-Workflow  

### Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### Anwendung starten

```bash
python run.py
```

## Windows-Build

Für Windows ist ein vorbereiteter Build-Prozess enthalten:

```bat
build_windows_pyinstaller.bat
```

Der Build-Skript übernimmt unter anderem:
• Bereinigung alter Build-Artefakte  
• Installation bzw. Aktualisierung der Abhängigkeiten  
• Installation von PyInstaller  
• Onefile-Build mit Fensteranwendung  
• Einbettung des Icons  
• Einbettung der Metadaten aus `version_info.txt`  

Erwartete Ausgabe:

```text
dist/CipherCoreSuite.exe
```

## Lokale Datenhaltung

CipherCore Suite legt lokale Dateien in einem versteckten Ordner im Home-Verzeichnis des Benutzers an:

```text
~/.ciphercore_suite/
```

Darin enthalten:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

## Sicherheitsworkflow

1. Master-Passwort festlegen  
2. Mit dem Master-Passwort anmelden  
3. Entsperrte Sitzung aufbauen  
4. Vault-Einträge verschlüsselt speichern oder lesen  
5. Texte und Dateien verschlüsseln bzw. entschlüsseln  
6. Analysefunktionen für technische Bewertung verwenden  
7. Nicht mehr benötigte Dateien bei Bedarf sicher vernichten  

## Hinweise zur tatsächlichen Implementierung

Auf Basis der vorhandenen Quelldateien sind folgende Punkte wichtig:

### 1. Vault-Verschlüsselung
Im Secure Vault werden aktuell **`secret`** und **`notes`** mit dem Session-Schlüssel verschlüsselt gespeichert.  
Die Felder **`title`**, **`category`** und **`username`** werden in der Datenbank im Klartext gespeichert.

### 2. Session-Modell
Der Zugriff auf verschlüsselte Vault-Inhalte setzt eine erfolgreiche Master-Anmeldung voraus. Ohne gültige Sitzung können Einträge nicht sinnvoll entschlüsselt werden.

### 3. Master-Passwort-Rotation
Das Master-Passwort wird lokal gehasht gespeichert. Der Session-Schlüssel für Vault-Inhalte wird aus dem eingegebenen Passwort und dem gespeicherten Salt abgeleitet.  
Daraus ergibt sich operativ: Ein späteres Ändern des Master-Passworts kann bestehende Vault-Daten unzugänglich machen, wenn keine Migrationslogik implementiert ist.

### 4. Theme-Verhalten
Die Oberfläche unterstützt Dark- und Light-Theme. In der aktuellen Implementierung wird die Theme-Auswahl jedoch nicht persistent in der Statusdatei gespeichert, während die Sprache persistent abgelegt wird.

### 5. Social-Links
Einige Social-Links in `app_config.py` sind noch Platzhalter oder generisch gesetzt, zum Beispiel LinkedIn.

### 6. Dateiendung
Verschlüsselte Dateipayloads arbeiten mit der konfigurierten Endung:

```text
.ccore
```

## Analysefunktionen

### Textanalyse
Bewertet unter anderem:
• Länge in Zeichen und Bytes  
• eindeutige Zeichen  
• Verhältnis eindeutiger Zeichen  
• Entropie pro Symbol  
• Verteilung von Buchstaben, Ziffern, Sonderzeichen und Leerzeichen  
• SHA-256 des Eingabetexts  

### Passwortanalyse
Erweitert die Textanalyse um:
• theoretische Entropie  
• geschätzte Zeichensatzgröße  
• Wiederholungsmuster  
• Stärke-Score  

### Dateianalyse
Bewertet unter anderem:
• Dateigröße  
• SHA-256  
• Byte-Entropie  
• Chi-Quadrat-Wert und p-Wert  
• serielle Korrelation  
• häufigste Bytes  
• Streuung blockweiser Mittelwerte  

### Dateivergleich
Vergleicht zwei Dateien technisch und strukturell.

### Randomness Lab
Erzeugt und bewertet Zufallsdaten zur technischen Einordnung statistischer Eigenschaften.

## Risiken und Betriebshinweise

• File Shredding ist destruktiv und irreversibel  
• Lokale Sicherheit hängt auch von Systemhärtung, Zugriffsrechten und Backup-Strategie ab  
• Analysewerte sind technische Indikatoren und kein Ersatz für forensische Gutachten oder Compliance-Prüfungen  
• Platzhalter-Links sollten vor produktiver Veröffentlichung ersetzt werden  
• Für Passwortwechsel im Produktivbetrieb sollte eine sichere Vault-Migration ergänzt werden  

## Geeignete Einsatzbereiche

• lokale Verschlüsselungs- und Entschlüsselungsprozesse  
• Verwaltung sensibler Notizen oder Zugangsdaten  
• technische Passwort- und Dateibewertung  
• kontrollierte Dateivernichtung  
• Desktop-basierte Sicherheits- und Analyseworkflows  

## Roadmap-Empfehlungen

Für den nächsten Reifegrad wären geschäftlich sinnvoll:

• vollständige Verschlüsselung zusätzlicher Vault-Felder  
• sichere Re-Key- oder Migrationsfunktion für Master-Passwort-Wechsel  
• persistente Theme-Speicherung  
• bereinigte produktive Social- und Kontaktlinks  
• Export- und Backup-Funktionen für Vault-Daten  
• Signierung und Hardening der Release-Artefakte  

## Copyright

© Thorsten Bylicki · BYLICKILABS. Alle Rechte vorbehalten.

<br>

---

<br>

## English

**CipherCore Suite** is a modular desktop application for encryption, protected local data storage, controlled file destruction and technical security analysis. The project combines classical cryptography with a structured analytics layer and brings multiple security-relevant workflows into one central PySide6 interface.

The application is designed for local usage and unifies text and file encryption, a Secure Vault, password utilities, file shredding and statistical analysis functions inside one cohesive desktop workbench.

## Feature Set

### Core Modules
• Text encryption and text decryption  
• File encryption and file decryption  
• Secure Vault backed by a local SQLite database  
• Master password and session lock  
• Password generator and password evaluation  
• File shredder with repeated overwrite  
• Security analytics for text, passwords, files and file comparison  
• Randomness Lab for evaluating random-based data  
• German and English user interface  
• Activity log and information center  
• Drag and drop for file queues  
• Windows build pipeline via PyInstaller including EXE metadata  

### Desktop Areas
The interface is organized into the following operational areas:

• Dashboard  
• Text Cryptography  
• File Cryptography  
• Security Analytics  
• Secure Vault  
• Password Center  
• File Shredder  
• Settings  
• Information  

## Technology Stack

• Python 3.11+  
• PySide6  
• cryptography  
• NumPy  
• SciPy  
• SQLite3  

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

### `run.py`
Application entry point. Initializes `QApplication`, sets the window icon and opens the main window.

### `ciphercore/ui/main_window.py`
Central desktop UI. This is where navigation, page logic, language handling, session management, vault handling, analytics output and UI styling are combined.

### `ciphercore/crypto.py`
Implements the cryptographic core functions.

Included capabilities:
• key derivation through PBKDF2-HMAC-SHA256  
• Fernet-based payload encryption  
• portable JSON payloads for text and file operations  
• password hashing and verification for the master password  
• session key creation for vault access  

### `ciphercore/storage.py`
Manages the Secure Vault using SQLite. Records are stored in `vault_entries`.

Stored fields:
• `title`  
• `category`  
• `username`  
• `secret`  
• `notes`  
• creation and update timestamps  

### `ciphercore/analytics.py`
Provides analytics functions for different data types.

Calculated indicators include:
• entropy  
• SHA-256  
• character set size  
• unique ratio  
• chi-square uniformity  
• serial correlation  
• byte distributions  
• block mean dispersion  
• password score  

### `ciphercore/shredding.py`
Responsible for controlled overwrite-based file deletion.

### `ciphercore/i18n.py`
Contains runtime translations for German and English.

### `ciphercore/info_text.py`
Provides the content for the integrated information center.

### `ciphercore/app_config.py`
Defines central paths, constants and configuration values.

Key points:
• hidden app folder in the user home directory  
• data and log directories  
• SQLite database path  
• state file  
• log file  
• PBKDF2 iteration count  
• social links  

## Installation

### Requirements
• Python 3.11 or newer  
• pip  
• Windows recommended for the included build workflow  

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the application

```bash
python run.py
```

## Windows Build

A prepared Windows build process is included:

```bat
build_windows_pyinstaller.bat
```

The build script handles, among other things:
• cleanup of previous build artifacts  
• installation or update of dependencies  
• installation of PyInstaller  
• onefile windowed build  
• icon embedding  
• metadata embedding from `version_info.txt`  

Expected output:

```text
dist/CipherCoreSuite.exe
```

## Local Data Storage

CipherCore Suite creates local files inside a hidden folder in the user's home directory:

```text
~/.ciphercore_suite/
```

Contents include:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

## Security Workflow

1. Set the master password  
2. Authenticate using the master password  
3. Establish an unlocked session  
4. Store or read encrypted vault entries  
5. Encrypt or decrypt text and files  
6. Use analytics functions for technical evaluation  
7. Securely destroy files when needed  

## Notes About the Actual Implementation

Based on the available source files, the following points matter:

### 1. Vault Encryption
Inside the Secure Vault, **`secret`** and **`notes`** are currently stored encrypted with the session key.  
The fields **`title`**, **`category`** and **`username`** are stored in plaintext in the database.

### 2. Session Model
Access to encrypted vault content requires a successful master login. Without a valid session, entries cannot be meaningfully decrypted.

### 3. Master Password Rotation
The master password is stored locally in hashed form. The session key for vault content is derived from the entered password and the stored salt.  
Operationally, this means a later password change can make existing vault data inaccessible unless a migration flow is implemented.

### 4. Theme Behavior
The interface supports dark and light themes. In the current implementation, however, the theme selection is not persistently stored in the state file, while the language setting is persisted.

### 5. Social Links
Some social links in `app_config.py` are still placeholders or generic defaults, including LinkedIn.

### 6. File Extension
Encrypted file payloads use the configured suffix:

```text
.ccore
```

## Analytics Functions

### Text Analysis
Evaluates, among other things:
• length in characters and bytes  
• unique characters  
• unique ratio  
• entropy per symbol  
• distribution of letters, digits, special characters and whitespace  
• SHA-256 of the input text  

### Password Analysis
Extends text analysis with:
• theoretical entropy  
• estimated character set size  
• repetition patterns  
• strength score  

### File Analysis
Evaluates, among other things:
• file size  
• SHA-256  
• byte entropy  
• chi-square value and p-value  
• serial correlation  
• top byte frequencies  
• block mean deviation  

### File Comparison
Compares two files on a technical and structural basis.

### Randomness Lab
Generates and evaluates random data to classify its statistical properties.

## Risks and Operational Guidance

• File shredding is destructive and irreversible  
• Local security also depends on system hardening, access controls and backup strategy  
• Analytics values are technical indicators and not a substitute for forensic reports or compliance assessments  
• Placeholder links should be replaced before production release  
• A secure vault migration should be added before supporting password rotation in production  

## Suitable Use Cases

• local encryption and decryption workflows  
• management of sensitive notes or credentials  
• technical password and file evaluation  
• controlled file destruction  
• desktop-based security and analytics workflows  

## Roadmap Recommendations

For the next maturity level, the following would add clear value:

• full encryption of additional vault fields  
• secure re-key or migration flow for master password changes  
• persistent theme storage  
• cleaned production-ready social and contact links  
• export and backup features for vault data  
• signing and hardening of release artifacts  

## Copyright

© Thorsten Bylicki · BYLICKILABS. All rights reserved.
