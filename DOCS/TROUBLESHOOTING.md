# TROUBLESHOOTING

### Deutsch
• [Fehlerbehebung](#fehlerbehebung)  
• [Startprobleme](#startprobleme)  
• [Installationsprobleme](#installationsprobleme)  
• [Vault-Probleme](#vault-probleme)  
• [Verschlüsselungsprobleme](#verschlüsselungsprobleme)  
• [Analyseprobleme](#analyseprobleme)  
• [Shredder-Probleme](#shredder-probleme)  
• [Build-Probleme](#build-probleme)  
• [Daten- und Pfadprobleme](#daten--und-pfadprobleme)  
• [Empfohlene Erstdiagnose](#empfohlene-erstdiagnose)  

### English
• [English](#english)  
• [Troubleshooting](#troubleshooting)  
• [Startup Problems](#startup-problems)  
• [Installation Problems](#installation-problems)  
• [Vault Problems](#vault-problems)  
• [Encryption Problems](#encryption-problems)  
• [Analytics Problems](#analytics-problems)  
• [Shredder Problems](#shredder-problems)  
• [Build Problems](#build-problems)  
• [Data and Path Problems](#data-and-path-problems)  
• [Recommended First Diagnosis](#recommended-first-diagnosis)  

<br>

---

<br>

## Deutsch

## Fehlerbehebung

Dieses Dokument unterstützt bei typischen Betriebs-, Installations-, Build- und Datenproblemen innerhalb von CipherCore Suite.

## Startprobleme

### Anwendung startet nicht
Mögliche Ursachen:

• Python-Version ist zu alt  
• Abhängigkeiten fehlen  
• Start wird aus falschem Verzeichnis ausgeführt  
• PySide6 ist nicht korrekt installiert  
• Datei- oder Berechtigungsproblem verhindert Initialisierung  

Empfohlene Prüfung:

```bash
python --version
pip install -r requirements.txt
python run.py
```

### Oberfläche öffnet sich nicht korrekt
Mögliche Ursachen:

• beschädigte lokale Zustandsdatei  
• fehlende Assets  
• fehlerhafte Initialisierung des UI-Kontexts  
• Paketierungsproblem bei einer EXE-Ausgabe  

## Installationsprobleme

### `pip install -r requirements.txt` schlägt fehl
Mögliche Ursachen:

• keine passende Python-Version  
• Netzwerk- oder Indexproblem  
• konfliktbehaftete lokale Umgebung  
• fehlende Build-Tools einzelner Pakete  

Empfohlene Maßnahmen:

• virtuelle Umgebung verwenden  
• `pip` aktualisieren  
• Installation in sauberer Umgebung wiederholen  

## Vault-Probleme

### Vault-Einträge können nicht gelesen werden
Mögliche Ursachen:

• keine aktive Sitzung  
• falsches Master-Passwort  
• geänderter Passwortkontext ohne Migration  
• beschädigte SQLite-Datenbank  
• inkonsistente verschlüsselte Nutzdaten  

Wichtiger Hinweis:
Wenn das Master-Passwort geändert wurde, ohne bestehende Vault-Daten kontrolliert zu migrieren, können Altbestände unlesbar werden.

### Vault zeigt nur teilweise geschützte Daten
Das ist nach dokumentiertem Stand erwartbar. Derzeit werden nur `secret` und `notes` verschlüsselt gespeichert. `title`, `category` und `username` bleiben im Klartext.

## Verschlüsselungsprobleme

### Text lässt sich nicht entschlüsseln
Mögliche Ursachen:

• falsches Passwort  
• beschädigte Payload  
• unvollständig kopierte oder manipulierte Daten  
• Versions- oder Strukturabweichung  

### Datei lässt sich nicht wiederherstellen
Mögliche Ursachen:

• falscher Entschlüsselungskontext  
• defekte `.ccore`-Datei  
• abgebrochener Schreibvorgang  
• Dateisystem- oder Zugriffsproblem  

## Analyseprobleme

### Analyse liefert unerwartete Werte
Mögliche Ursachen:

• Eingabe ist sehr kurz  
• Binärdaten werden anders interpretiert als erwartet  
• Vergleichsdateien unterscheiden sich strukturell stärker als angenommen  
• Kennzahlen werden semantisch überinterpretiert  

Wichtiger Hinweis:
Analytische Kennzahlen sind technische Indikatoren. Sie ersetzen keine forensische Bewertung und keine inhaltliche Sicherheitsfreigabe.

## Shredder-Probleme

### Datei kann nicht gelöscht werden
Mögliche Ursachen:

• Datei ist noch geöffnet  
• fehlende Schreibrechte  
• Antivirus oder anderes Programm blockiert den Zugriff  
• Pfad ist ungültig oder bereits verändert  

### Löschung wurde gestartet, Datei existiert aber noch
Mögliche Ursachen:

• Prozess wurde unterbrochen  
• Dateisystem verhält sich anders als erwartet  
• Datei wurde in anderer Form gespiegelt oder gesichert  
• Dateiname wurde verwechselt  

## Build-Probleme

### PyInstaller-Build schlägt fehl
Mögliche Ursachen:

• PyInstaller fehlt  
• Abhängigkeiten sind unvollständig  
• Icon-Datei fehlt  
• Metadatendatei enthält Fehler  
• Build-Skript wird aus falschem Verzeichnis ausgeführt  

### EXE startet, aber Verhalten weicht vom Python-Start ab
Mögliche Ursachen:

• Pfadauflösung im Paketkontext  
• fehlende eingebettete Ressourcen  
• Umgebungsunterschied zwischen Entwicklungsmodus und Onefile-Build  
• Fehler bei Dateizugriff oder Arbeitsverzeichnis  

## Daten- und Pfadprobleme

### Anwendungsdaten werden nicht gefunden
Prüfen, ob der versteckte Ordner existiert:

```text
~/.ciphercore_suite/
```

Wichtige Dateien:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

### Theme oder Einstellungen bleiben nicht erhalten
Nach dokumentiertem Stand ist die Sprache persistent. Das Theme ist aktuell nicht in gleicher Weise persistent implementiert. Dieses Verhalten ist daher erwartbar.

## Empfohlene Erstdiagnose

1. Python-Version prüfen  
2. Abhängigkeiten erneut installieren  
3. Start im Terminal ausführen und Fehlermeldung lesen  
4. Pfade zu `vault.db`, `app_state.json` und `activity.log` prüfen  
5. Master-Passwort-Kontext hinterfragen, falls Vault-Daten nicht lesbar sind  
6. Test mit neuer Datei oder neuem Vault-Eintrag durchführen  
7. Build und Entwicklungsstart getrennt validieren  

<br>

---

<br>

## English

## Troubleshooting

This document supports typical runtime, installation, build and data-related issues in CipherCore Suite.

## Startup Problems

### Application does not start
Possible causes:

• Python version is too old  
• dependencies are missing  
• application is started from the wrong directory  
• PySide6 is not installed correctly  
• file or permission issues prevent initialization  

Recommended check:

```bash
python --version
pip install -r requirements.txt
python run.py
```

### Interface does not open correctly
Possible causes:

• corrupted local state file  
• missing assets  
• broken UI context initialization  
• packaging issue in an EXE build  

## Installation Problems

### `pip install -r requirements.txt` fails
Possible causes:

• incompatible Python version  
• network or package index issue  
• conflicting local environment  
• missing build tools for certain packages  

Recommended actions:

• use a virtual environment  
• update `pip`  
• retry installation in a clean environment  

## Vault Problems

### Vault entries cannot be read
Possible causes:

• no active session  
• wrong master password  
• changed password context without migration  
• corrupted SQLite database  
• inconsistent encrypted payloads  

Important note:
If the master password was changed without controlled migration of existing vault content, older records may become unreadable.

### Vault displays only partially protected data
This is expected according to the documented implementation state. At the moment, only `secret` and `notes` are stored encrypted. `title`, `category` and `username` remain plaintext.

## Encryption Problems

### Text cannot be decrypted
Possible causes:

• wrong password  
• corrupted payload  
• incompletely copied or manipulated data  
• version or structure mismatch  

### File cannot be restored
Possible causes:

• wrong decryption context  
• damaged `.ccore` file  
• interrupted write operation  
• filesystem or access issue  

## Analytics Problems

### Analysis returns unexpected values
Possible causes:

• input is very short  
• binary content is interpreted differently than expected  
• compared files differ structurally more than assumed  
• metrics are semantically overinterpreted  

Important note:
Analytic metrics are technical indicators. They do not replace forensic assessment or content-level security approval.

## Shredder Problems

### File cannot be deleted
Possible causes:

• file is still open  
• missing write permissions  
• antivirus or another program blocks access  
• path is invalid or has changed already  

### Deletion started, but the file still exists
Possible causes:

• process was interrupted  
• filesystem behaves differently than expected  
• file was mirrored or backed up elsewhere  
• wrong file name was selected  

## Build Problems

### PyInstaller build fails
Possible causes:

• PyInstaller is missing  
• dependencies are incomplete  
• icon file is missing  
• metadata file contains errors  
• build script is executed from the wrong directory  

### EXE starts, but behaves differently than Python runtime
Possible causes:

• path resolution differences inside packaged mode  
• missing embedded resources  
• environment differences between development mode and onefile build  
• file access or working directory issues  

## Data and Path Problems

### Application data cannot be found
Check whether the hidden folder exists:

```text
~/.ciphercore_suite/
```

Relevant files:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

### Theme or settings do not persist
According to the documented implementation state, language persists. Theme selection is currently not implemented with the same level of persistence. This behavior is therefore expected.

## Recommended First Diagnosis

1. Verify Python version  
2. Reinstall dependencies  
3. Start from a terminal and read the error output  
4. Check the paths to `vault.db`, `app_state.json` and `activity.log`  
5. Reevaluate the master password context if vault content cannot be read  
6. Test with a new file or a new vault entry  
7. Validate development mode and packaged build separately  
