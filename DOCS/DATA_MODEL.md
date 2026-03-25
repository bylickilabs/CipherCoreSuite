# DATA_MODEL

### Deutsch
• [Datenmodell](#datenmodell)  
• [Zielsetzung](#zielsetzung)  
• [Lokale Speicherorte](#lokale-speicherorte)  
• [Vault-Datenbank](#vault-datenbank)  
• [App-State](#app-state)  
• [Aktivitätslog](#aktivitätslog)  
• [Verschlüsselte Datei-Artefakte](#verschlüsselte-datei-artefakte)  
• [Datenklassifikation](#datenklassifikation)  
• [Integritäts- und Konsistenzaspekte](#integritäts--und-konsistenzaspekte)  
• [Bekannte Grenzen](#bekannte-grenzen)  

### English
• [English](#english)  
• [Data Model](#data-model)  
• [Objective](#objective)  
• [Local Storage Locations](#local-storage-locations)  
• [Vault Database](#vault-database)  
• [App State](#app-state-1)  
• [Activity Log](#activity-log)  
• [Encrypted File Artifacts](#encrypted-file-artifacts)  
• [Data Classification](#data-classification)  
• [Integrity and Consistency Aspects](#integrity-and-consistency-aspects)  
• [Known Boundaries](#known-boundaries)  

<br>

---

<br>

## Deutsch

## Datenmodell

CipherCore Suite speichert Anwendungsdaten lokal in einer Kombination aus SQLite-Datenbank, Zustandsdateien, Log-Dateien und vom Benutzer erzeugten verschlüsselten Datei-Artefakten. Das Datenmodell ist bewusst lokal, einfach nachvollziehbar und auf Desktop-Nutzung ausgerichtet.

## Zielsetzung

Das Datenmodell soll:

• sensible Vault-Inhalte lokal speichern  
• minimale notwendige Zustände der Anwendung verwalten  
• Protokollierung betrieblicher Ereignisse erlauben  
• verschlüsselte Datei-Artefakte konsistent handhaben  
• spätere Erweiterungen wie Backup, Export und Migration ermöglichen  

## Lokale Speicherorte

Die Anwendung legt ihre Daten in einem versteckten App-Verzeichnis im Benutzerprofil ab:

```text
~/.ciphercore_suite/
```

Typische Unterbereiche:

• `data/`  
• `logs/`  

Typische Dateien:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

## Vault-Datenbank

Die Vault-Datenhaltung basiert auf SQLite. Sie stellt den zentralen lokalen Speicher für Secure-Vault-Einträge dar.

### Zentrale Tabelle
Nach der dokumentierten Projektstruktur werden Einträge in `vault_entries` verwaltet.

### Typische Felder
• `title`  
• `category`  
• `username`  
• `secret`  
• `notes`  
• Erstellungszeitpunkt  
• Aktualisierungszeitpunkt  

### Schutzstatus
Nach aktuellem Stand:

• `secret` ist verschlüsselt  
• `notes` ist verschlüsselt  
• `title` ist Klartext  
• `category` ist Klartext  
• `username` ist Klartext  

### Bedeutung
Das Datenmodell trennt damit zwischen semantisch stark sensiblen Geheimdaten und organisatorischen Beschreibungsfeldern. Für höhere Vertraulichkeit wäre eine weitergehende Feldverschlüsselung sinnvoll.

## App-State

Die Anwendung verwaltet einen lokalen Status für nichtdatenbankbasierte Zustände.

Mögliche Inhalte:

• Spracheinstellung  
• UI-bezogene Zustände  
• Initialisierungsstatus  
• nichtkritische Bedienparameter  

### Aktueller Hinweis
Die Sprache wird persistent gespeichert. Das Theme-Verhalten ist nach dokumentiertem Stand nicht in gleicher Weise persistent umgesetzt.

## Aktivitätslog

Das Aktivitätslog dient der lokalen Nachvollziehbarkeit betrieblicher Vorgänge.

Mögliche protokollierte Bereiche:

• Start und Laufzeitereignisse  
• Bedienaktionen  
• Statuswechsel  
• Fehlerereignisse  
• technische Rückmeldungen  

### Sicherheitsanforderung
Logs dürfen keine sensiblen Geheimwerte im Klartext enthalten. Besonders kritisch wären:

• Master-Passwörter  
• entschlüsselte Vault-Geheimnisse  
• vollständige Dateiinhalte  
• Schlüsselmaterial  

## Verschlüsselte Datei-Artefakte

Neben internen Zuständen kann CipherCore Suite benutzerinitiierte verschlüsselte Datei-Artefakte erzeugen.

### Kennzeichen
Verschlüsselte Artefakte verwenden die Dateiendung:

```text
.ccore
```

### Erwartete inhaltliche Struktur
Ein robustes Datenmodell für solche Artefakte umfasst typischerweise:

• Formatkennung  
• Versionsinformation  
• Ableitungsparameter oder Salt  
• verschlüsselte Nutzdaten  
• optionale Metadaten  

## Datenklassifikation

Für den Betrieb ist eine klare Datenklassifikation sinnvoll:

### Hochsensitiv
• Master-Passwort  
• abgeleitete Schlüsselkontexte  
• `secret`  
• `notes`  
• entschlüsselte Klartextinhalte  

### Sensitiv
• `username`  
• Dateipfade  
• Hashwerte in bestimmten Kontexten  
• Log-Einträge mit semantischem Bezug  

### Mittel
• `title`  
• `category`  
• Spracheinstellung  
• allgemeine Bedienzustände  

### Niedrig
• Theme-Präferenz  
• generische Informationsinhalte  
• statische UI-Labels  

## Integritäts- und Konsistenzaspekte

Das Datenmodell muss folgende Eigenschaften möglichst sicherstellen:

• konsistente Schreibvorgänge in SQLite  
• keine beschädigten Zustandsdateien nach Abbruch  
• nachvollziehbare Trennung von Daten und Logs  
• kontrollierte Fehlerbehandlung bei Dateioperationen  
• Lesbarkeit verschlüsselter Artefakte nur bei korrektem Kontext  

Empfohlene Weiterentwicklungen:

• Backup- und Restore-Mechanismen  
• Export mit Integritätsprüfung  
• Schema-Versionierung  
• Migrationspfade für Vault und App-State  
• Validierung vor dem Schreiben struktureller Daten  

## Bekannte Grenzen

• keine vollständige Verschlüsselung aller Vault-Spalten  
• keine dokumentierte Schema-Migration für Passwortwechsel  
• keine explizit dokumentierte Backup-Strategie  
• mögliches Risiko inkonsistenter Zustände bei abruptem Abbruch ohne zusätzliche Schutzlogik  
• Platzhalter-Links oder generische Konfigurationen können semantische Unschärfen erzeugen  

<br>

---

<br>

## English

## Data Model

CipherCore Suite stores application data locally through a combination of SQLite, state files, log files and user-generated encrypted file artifacts. The model is intentionally local, understandable and aligned with desktop usage.

## Objective

The data model is intended to:

• store sensitive vault content locally  
• manage the minimum necessary application state  
• support logging of operational events  
• handle encrypted file artifacts consistently  
• enable future backup, export and migration features  

## Local Storage Locations

The application stores data in a hidden application folder inside the user profile:

```text
~/.ciphercore_suite/
```

Typical subareas:

• `data/`  
• `logs/`  

Typical files:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

## Vault Database

Vault persistence is based on SQLite. It acts as the central local store for Secure Vault entries.

### Core Table
According to the documented project structure, entries are managed in `vault_entries`.

### Typical Fields
• `title`  
• `category`  
• `username`  
• `secret`  
• `notes`  
• created timestamp  
• updated timestamp  

### Protection Status
At the current implementation state:

• `secret` is encrypted  
• `notes` is encrypted  
• `title` is plaintext  
• `category` is plaintext  
• `username` is plaintext  

### Meaning
The model therefore distinguishes strongly sensitive secret content from organizational descriptor fields. For higher confidentiality, broader field encryption would be appropriate.

## App State

The application maintains local state for non-database settings.

Potential contents:

• language preference  
• UI-related states  
• initialization state  
• noncritical operating parameters  

### Current Note
Language is persisted. Theme behavior is, according to the documented state, not persisted in the same way.

## Activity Log

The activity log supports local traceability of operational events.

Potential logged areas:

• startup and runtime events  
• interaction events  
• state transitions  
• error events  
• technical feedback  

### Security Requirement
Logs must not expose sensitive secrets in plaintext. Particularly critical examples would be:

• master passwords  
• decrypted vault secrets  
• full file contents  
• key material  

## Encrypted File Artifacts

In addition to internal state, CipherCore Suite can create user-driven encrypted file artifacts.

### Marker
Encrypted artifacts use the suffix:

```text
.ccore
```

### Expected Internal Structure
A robust model for these artifacts typically includes:

• format marker  
• version information  
• derivation parameters or salt  
• encrypted payload  
• optional metadata  

## Data Classification

A clear data classification is useful for operations:

### Highly Sensitive
• master password  
• derived key contexts  
• `secret`  
• `notes`  
• decrypted plaintext content  

### Sensitive
• `username`  
• file paths  
• hashes in certain contexts  
• logs with semantic linkage  

### Medium
• `title`  
• `category`  
• language preference  
• general interaction state  

### Low
• theme preference  
• generic information content  
• static UI labels  

## Integrity and Consistency Aspects

The data model should aim to ensure:

• consistent SQLite writes  
• no corrupted state files after interruption  
• traceable separation of data and logs  
• controlled error handling for file operations  
• encrypted artifact readability only under the correct context  

Recommended future work:

• backup and restore mechanisms  
• export with integrity validation  
• schema versioning  
• migration paths for vault and app state  
• validation before writing structural data  

## Known Boundaries

• no full encryption of all vault columns  
• no documented schema migration for password changes  
• no explicit backup strategy documented  
• possible risk of inconsistent state after abrupt interruption without additional safeguards  
• placeholder links or generic configuration values can create semantic ambiguity  
