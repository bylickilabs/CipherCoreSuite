# ARCHITECTURE

### Deutsch
• [Architektur](#architektur)  
• [Systemziel](#systemziel)  
• [Architekturprinzipien](#architekturprinzipien)  
• [Logische Systembereiche](#logische-systembereiche)  
• [Modulübersicht](#modulübersicht)  
• [Datenfluss](#datenfluss)  
• [Sicherheitsrelevante Architekturentscheidungen](#sicherheitsrelevante-architekturentscheidungen)  
• [Persistenzmodell](#persistenzmodell)  
• [Session-Modell](#session-modell)  
• [Build- und Release-Architektur](#build--und-release-architektur)  
• [Architekturelle Grenzen](#architekturelle-grenzen)  

### English
• [English](#english)  
• [Architecture](#architecture)  
• [System Goal](#system-goal)  
• [Architectural Principles](#architectural-principles)  
• [Logical System Areas](#logical-system-areas)  
• [Module Overview](#module-overview)  
• [Data Flow](#data-flow)  
• [Security-Relevant Architectural Decisions](#security-relevant-architectural-decisions)  
• [Persistence Model](#persistence-model)  
• [Session Model](#session-model)  
• [Build and Release Architecture](#build-and-release-architecture)  
• [Architectural Boundaries](#architectural-boundaries)  

<br>

---

<br>

## Deutsch

## Architektur

CipherCore Suite ist als modulare lokale Desktop-Anwendung aufgebaut. Die Lösung bündelt kryptografische Funktionen, lokale Datenhaltung, technische Analysefunktionen, UI-Steuerung und Build-Logik in einer zusammenhängenden PySide6-basierten Anwendungsarchitektur.

Das System verfolgt kein verteiltes Client-Server-Modell. Es ist bewusst als lokal ausgeführte Workbench konzipiert, bei der Sicherheitslogik, Bedienoberfläche, Datenhaltung und Analyseprozesse auf einem Endgerät zusammengeführt werden.

## Systemziel

Die Architektur dient dazu, mehrere sicherheitsrelevante Workflows in einer einheitlichen Desktop-Oberfläche bereitzustellen:

• textbasierte Verschlüsselung und Entschlüsselung  
• dateibasierte Verschlüsselung und Entschlüsselung  
• sichere lokale Ablage ausgewählter sensibler Vault-Inhalte  
• technische Sicherheits- und Qualitätsanalyse von Texten, Passwörtern und Dateien  
• kontrollierte und überschreibende Dateivernichtung  
• lokale Konfiguration, Aktivitätsprotokollierung und Bedienlogik  

## Architekturprinzipien

Die Architektur folgt den folgenden Grundprinzipien:

• lokale Ausführung statt externer Serviceabhängigkeit  
• modulare Trennung von UI, Kryptografie, Persistenz und Analyse  
• nachvollziehbare Datenpfade und deterministische lokale Speicherung  
• klare Session-Abgrenzung für Vault-Entschlüsselung  
• funktionale Trennung zwischen produktiver Bedienung und Build-Prozess  
• Erweiterbarkeit für spätere Hardening-, Migrations- und Exportfunktionen  

## Logische Systembereiche

CipherCore Suite kann in fünf logische Ebenen unterteilt werden:

### 1. Präsentationsschicht
Die Präsentationsschicht umfasst die gesamte Desktop-Oberfläche inklusive Navigation, Buttons, Eingaben, Statusanzeige, Dialogen und Theme-Logik.

### 2. Orchestrierungsschicht
Diese Schicht verbindet UI-Ereignisse mit den jeweiligen Fachfunktionen. Hier werden Nutzeraktionen in kryptografische, analytische oder speicherbezogene Operationen übersetzt.

### 3. Kryptografie- und Sicherheitslogik
Diese Schicht umfasst Schlüsselableitung, Payload-Erzeugung, Verifikation, Entschlüsselung und Passwortbehandlung.

### 4. Persistenz- und Dateischicht
Diese Schicht verwaltet SQLite-Daten, Statusdateien, Aktivitätslogs und dateibezogene Operationen.

### 5. Analyse- und Bewertungslogik
Hier werden statistische Kennzahlen, Entropie, Hashes, Byte-Verteilungen und weitere technische Indikatoren berechnet.

## Modulübersicht

### `run.py`
Startpunkt der Anwendung. Initialisiert `QApplication`, setzt das Fenster-Icon und startet das Hauptfenster.

### `ciphercore/ui/main_window.py`
Zentrale Orchestrierungs- und UI-Datei. Sie verbindet Navigation, Benutzerinteraktion, Session-Zustände, Vault-Operationen, Analysefunktionen und Sprachumschaltung.

### `ciphercore/crypto.py`
Kryptografische Kernlogik. Verantwortlich für Schlüsselableitung, Passwort-Hashing, Payload-Verschlüsselung und Entschlüsselung.

### `ciphercore/storage.py`
Persistenzmodul für den Secure Vault auf Basis von SQLite. Verwaltet die gespeicherten Einträge und deren Lebenszyklus.

### `ciphercore/analytics.py`
Stellt technische Bewertungsfunktionen für Texte, Passwörter, Dateien, Randomness und Vergleiche bereit.

### `ciphercore/shredding.py`
Implementiert die überschreibende und irreversibel gedachte Dateivernichtung.

### `ciphercore/i18n.py`
Stellt die Übersetzungsstruktur für Deutsch und Englisch bereit.

### `ciphercore/info_text.py`
Liefert Inhalte für das integrierte Informationszentrum innerhalb der Oberfläche.

### `ciphercore/app_config.py`
Definiert Pfade, Konstanten, Zustandsdateien, Iterationen, Dateiendungen und weitere Basiskonfigurationen.

### `ciphercore/social.py`
Ergänzt projektbezogene Verlinkungen und Kontaktpunkte, soweit konfiguriert.

### `ciphercore/utils.py`
Hilfsfunktionen für wiederkehrende technische Abläufe.

## Datenfluss

Ein typischer Ablauf lässt sich architektonisch wie folgt beschreiben:

1. Die UI nimmt Eingaben des Benutzers entgegen.  
2. Die Orchestrierung validiert Kontext und Eingabedaten.  
3. Je nach Aktion wird das zuständige Modul aufgerufen.  
4. Kryptografische oder analytische Ergebnisse werden erzeugt.  
5. Ergebnisse werden entweder lokal gespeichert, angezeigt oder als Datei geschrieben.  
6. Relevante Zustände oder Aktivitäten können in Statusdatei oder Log abgelegt werden.  

Beispiele:

### Textverschlüsselung
UI → Eingabetext → `crypto.py` → verschlüsselte JSON-Payload → Ausgabe in UI oder Datei

### Vault-Speicherung
UI → Session-Prüfung → `storage.py` + `crypto.py` → SQLite-Speicherung

### Dateianalyse
UI → Dateiauswahl → `analytics.py` → Kennzahlenberechnung → Anzeige im UI

### File Shredding
UI → Dateipfad → `shredding.py` → Überschreibung → Löschung → Rückmeldung im UI

## Sicherheitsrelevante Architekturentscheidungen

### Lokale First-Party-Ausführung
Die Anwendung ist lokal orientiert. Das reduziert externe Angriffsflächen, verschiebt die Verantwortung jedoch stärker auf Gerätesicherheit, Betriebssystemhärtung und lokale Zugriffskontrolle.

### Trennung von Vault und Kryptomodul
Die Vault-Datenhaltung und die Kryptologik sind funktional getrennt. Das verbessert Wartbarkeit und erlaubt spätere Re-Key- oder Migrationspfade.

### Session-gebundene Entschlüsselung
Verschlüsselte Vault-Inhalte werden nicht ohne aktive Sitzung sinnvoll verarbeitet. Das begrenzt unbeabsichtigte Klartextzugriffe innerhalb der Anwendung.

### Datei- und Textpayloads als logische Artefakte
Text- und Dateioperationen werden über portable Payload-Strukturen organisiert. Das vereinfacht Wiederherstellung und spätere Formatversionierung.

### Bewusste Nichtpersistenz bestimmter Zustände
Einige Zustände, etwa Theme-Änderungen, sind in der aktuellen Implementierung nicht persistent. Das reduziert Konfigurationsumfang, ist aber funktional ausbaufähig.

## Persistenzmodell

Die Anwendung verwendet mehrere lokale Speicherorte:

• SQLite-Datenbank für Vault-Inhalte  
• JSON- oder Statusdatei für App-Zustände  
• Aktivitätslog für operative Ereignisse  
• verschlüsselte Datei-Artefakte für Nutzeroperationen  

Zentrale Merkmale:

• Daten liegen in einem versteckten Anwendungsordner im Benutzerverzeichnis  
• Vault-Daten werden tabellenbasiert verwaltet  
• nicht alle Vault-Felder sind aktuell verschlüsselt  
• Zustände werden teilweise persistiert, teilweise nur zur Laufzeit gehalten  

## Session-Modell

Das Session-Modell dient dem kontrollierten Zugriff auf den Secure Vault.

### Ablauf
• Master-Passwort wird gesetzt oder geprüft  
• aus Passwort und Salt wird ein Schlüsselkontext abgeleitet  
• Sitzung wird entsperrt  
• verschlüsselte Inhalte können gelesen oder geschrieben werden  
• bei Sperrung oder Neustart muss die Sitzung erneut aufgebaut werden  

### Relevanz
Dieses Modell ist zentral, weil verschlüsselte Inhalte nicht unabhängig vom gültigen Passwortkontext gelesen werden können.

## Build- und Release-Architektur

Der Anwendungsbetrieb und der Packaging-Prozess sind architektonisch getrennt.

### Entwicklungsmodus
• Start über `python run.py`  
• direkte Nutzung der Python-Module  
• schnelle Validierung und Debugging  

### Windows-Build
• Build über `build_windows_pyinstaller.bat`  
• Onefile-Paketierung  
• Fensteranwendung  
• Einbettung von Icon und EXE-Metadaten  
• Ausgabe nach `dist/CipherCoreSuite.exe`  

## Architekturelle Grenzen

Die vorhandene Architektur ist funktional konsistent, hat aber produktiv relevante Grenzen:

• keine vollständige Feldverschlüsselung aller Vault-Attribute  
• keine dokumentierte Vault-Migration für Passwortwechsel  
• keine separate Schlüsselverwaltung außerhalb des Passwortmodells  
• keine signierten Release-Artefakte als garantierter Standard  
• keine zentrale Richtlinie für Telemetrie oder erweiterte Auditierbarkeit  
• keine isolierte Sandbox für riskante Dateioperationen  

<br>

---

<br>

## English

## Architecture

CipherCore Suite is designed as a modular local desktop application. The solution consolidates cryptographic functions, local persistence, technical analytics, UI control and build logic into one cohesive PySide6-based architecture.

The system does not follow a distributed client-server model. It is intentionally built as a locally executed workbench where security logic, interface, storage and analysis are combined on a single endpoint.

## System Goal

The architecture is intended to support multiple security-relevant workflows inside one unified desktop experience:

• text encryption and decryption  
• file encryption and decryption  
• secure local storage for selected sensitive vault content  
• technical security and quality analysis of text, passwords and files  
• controlled overwrite-based file destruction  
• local configuration, activity logging and interaction logic  

## Architectural Principles

The architecture follows these principles:

• local execution instead of dependence on external services  
• modular separation of UI, cryptography, persistence and analytics  
• traceable data paths and deterministic local storage  
• clear session boundaries for vault decryption  
• functional separation between runtime usage and build process  
• extensibility for future hardening, migration and export capabilities  

## Logical System Areas

CipherCore Suite can be divided into five logical layers:

### 1. Presentation Layer
This layer includes the desktop interface, navigation, buttons, inputs, dialogs, status indicators and theme handling.

### 2. Orchestration Layer
This layer connects UI events to the underlying business functions. User actions are translated into cryptographic, analytic or storage operations here.

### 3. Cryptography and Security Logic
This layer covers key derivation, payload creation, verification, decryption and password handling.

### 4. Persistence and File Layer
This layer manages SQLite data, state files, activity logs and file-related operations.

### 5. Analytics and Evaluation Logic
This layer computes statistical indicators, entropy, hashes, byte distributions and related technical metrics.

## Module Overview

### `run.py`
Application entry point. Initializes `QApplication`, sets the window icon and launches the main window.

### `ciphercore/ui/main_window.py`
Central UI and orchestration file. It connects navigation, user interaction, session state, vault operations, analytics and language switching.

### `ciphercore/crypto.py`
Cryptographic core logic. Responsible for key derivation, password hashing, payload encryption and decryption.

### `ciphercore/storage.py`
Persistence module for the SQLite-backed Secure Vault. Manages stored entries and their lifecycle.

### `ciphercore/analytics.py`
Provides technical evaluation functions for text, passwords, files, randomness and comparisons.

### `ciphercore/shredding.py`
Implements overwrite-based and intended irreversible file destruction.

### `ciphercore/i18n.py`
Provides the runtime translation structure for German and English.

### `ciphercore/info_text.py`
Supplies content for the integrated information center inside the interface.

### `ciphercore/app_config.py`
Defines paths, constants, state files, iteration counts, suffixes and other base configuration values.

### `ciphercore/social.py`
Provides project-related links and contact references where configured.

### `ciphercore/utils.py`
Provides helper functions for recurring technical tasks.

## Data Flow

A typical operational flow can be described as follows:

1. The UI collects user input.  
2. The orchestration layer validates context and input.  
3. The appropriate module is invoked.  
4. Cryptographic or analytic results are generated.  
5. Results are stored locally, shown in the UI or written to files.  
6. Relevant states or actions may be written to state files or logs.  

Examples:

### Text Encryption
UI → input text → `crypto.py` → encrypted JSON payload → UI or file output

### Vault Storage
UI → session validation → `storage.py` + `crypto.py` → SQLite storage

### File Analysis
UI → file selection → `analytics.py` → metric calculation → UI rendering

### File Shredding
UI → file path → `shredding.py` → overwrite → deletion → UI feedback

## Security-Relevant Architectural Decisions

### Local First-Party Execution
The application is local by design. This reduces external attack surface, but shifts more responsibility to device security, OS hardening and local access control.

### Separation of Vault and Cryptography
Vault persistence and cryptographic logic are functionally separated. This improves maintainability and supports future re-key or migration flows.

### Session-Bound Decryption
Encrypted vault content is not meaningfully processed without an active session. This reduces unintended plaintext access within the application.

### File and Text Payloads as Logical Artifacts
Text and file operations are organized through portable payload structures. This simplifies recovery and future file format versioning.

### Deliberate Non-Persistence of Some States
Some states, such as theme selection, are not currently persisted. This keeps configuration simple, while remaining expandable.

## Persistence Model

The application uses several local storage locations:

• SQLite database for vault content  
• JSON or state file for application state  
• activity log for operational events  
• encrypted file artifacts for user operations  

Core properties:

• data is stored in a hidden application folder in the user home directory  
• vault data is managed in a table-based structure  
• not all vault fields are currently encrypted  
• some states are persisted while others only exist at runtime  

## Session Model

The session model provides controlled access to the Secure Vault.

### Flow
• master password is set or verified  
• a key context is derived from password and salt  
• session is unlocked  
• encrypted content can be read or written  
• when locked or restarted, the session must be rebuilt  

### Relevance
This model is central because encrypted content cannot be read independently of the valid password context.

## Build and Release Architecture

Runtime operation and packaging are architecturally separated.

### Development Mode
• start via `python run.py`  
• direct use of Python modules  
• fast validation and debugging  

### Windows Build
• build via `build_windows_pyinstaller.bat`  
• onefile packaging  
• windowed application  
• icon and EXE metadata embedding  
• output to `dist/CipherCoreSuite.exe`  

## Architectural Boundaries

The current architecture is functionally coherent, but still has production-relevant boundaries:

• no full encryption of all vault attributes  
• no documented vault migration for password changes  
• no separate key management beyond the password model  
• no signed release artifacts as a guaranteed standard  
• no centralized telemetry policy or advanced audit model  
• no isolated sandbox for risky file operations  
