# CipherCore Suite Threat Model

### Deutsch
• [Ziel und Zweck](#ziel-und-zweck)  
• [Systemkontext](#systemkontext)  
• [Schutzobjekte](#schutzobjekte)  
• [Vertrauensgrenzen](#vertrauensgrenzen)  
• [Annahmen](#annahmen)  
• [Nicht-Ziele](#nicht-ziele)  
• [Akteure und Bedrohungsquellen](#akteure-und-bedrohungsquellen)  
• [Angriffsflächen](#angriffsflächen)  
• [Datenflüsse](#datenflüsse)  
• [Bedrohungskategorien](#bedrohungskategorien)  
• [Detaillierte Bedrohungen nach Bereich](#detaillierte-bedrohungen-nach-bereich)  
• [Risikobewertung](#risikobewertung)  
• [Priorisierte Top-Risiken](#priorisierte-top-risiken)  
• [Bestehende Schutzmaßnahmen](#bestehende-schutzmaßnahmen)  
• [Empfohlene Gegenmaßnahmen](#empfohlene-gegenmaßnahmen)  
• [Residualrisiken](#residualrisiken)  
• [Test- und Validierungsstrategie](#test--und-validierungsstrategie)  
• [Bezug zu Security Policy und Roadmap](#bezug-zu-security-policy-und-roadmap)  

### English
• [Purpose](#purpose)  
• [System Context](#system-context)  
• [Assets](#assets)  
• [Trust Boundaries](#trust-boundaries)  
• [Assumptions](#assumptions)  
• [Non Goals](#non-goals)  
• [Actors and Threat Sources](#actors-and-threat-sources)  
• [Attack Surfaces](#attack-surfaces)  
• [Data Flows](#data-flows)  
• [Threat Categories](#threat-categories)  
• [Detailed Threats by Domain](#detailed-threats-by-domain)  
• [Risk Evaluation](#risk-evaluation)  
• [Top Priority Risks](#top-priority-risks)  
• [Existing Safeguards](#existing-safeguards)  
• [Recommended Mitigations](#recommended-mitigations)  
• [Residual Risks](#residual-risks)  
• [Testing and Validation Strategy](#testing-and-validation-strategy)  
• [Alignment with Security Policy and Roadmap](#alignment-with-security-policy-and-roadmap)  

<br>

---

<br>

## Ziel und Zweck

Dieses Dokument beschreibt das Bedrohungsmodell für **CipherCore Suite**. Es dient dazu, sicherheitsrelevante Angriffswege, Vertrauensgrenzen, Schutzobjekte und operative Restrisiken systematisch sichtbar zu machen. Ziel ist nicht nur die Beschreibung einzelner Schwachstellen, sondern die strukturierte Einordnung des gesamten Sicherheitsraums der Anwendung.

## Systemkontext

CipherCore Suite ist eine lokal ausgeführte Desktop-Anwendung mit folgenden funktionalen Schwerpunkten:

• Textverschlüsselung und Textentschlüsselung  
• Dateiverschlüsselung und Dateientschlüsselung  
• Secure Vault auf SQLite-Basis  
• Master-Passwort und Sitzungssperre  
• Passwortgenerator und Passwortbewertung  
• File Shredder  
• statistische und technische Analysefunktionen  
• zweisprachige Desktop-Oberfläche mit PySide6  

Die Anwendung speichert Statusdaten, Logs und Vault-Daten lokal im Benutzerkontext. Sie ist primär als Offline- oder Local-First-Produkt konzipiert.

## Schutzobjekte

Aus Sicht des Bedrohungsmodells sind insbesondere folgende Assets kritisch:

• Master-Passwort  
• abgeleitete Schlüssel und Session-Schlüssel  
• verschlüsselte Text- und Dateipayloads  
• Vault-Inhalte und Vault-Metadaten  
• lokale Datenbankdatei  
• Statusdatei und Aktivitätslog  
• Build-Artefakte und ausführbare Binärdateien  
• Abhängigkeiten und Build-Skripte  

## Vertrauensgrenzen

Die wichtigsten Vertrauensgrenzen verlaufen zwischen:

• Benutzer und Anwendung  
• Anwendung und lokalem Dateisystem  
• entsperrter Sitzung und gesperrtem Zustand  
• verschlüsselten und unverschlüsselten Datenzuständen  
• Quellcode und kompiliertem Release-Artefakt  
• vertrauenswürdigen Bibliotheken und potenziell manipulierten Abhängigkeiten  

## Annahmen

Das Bedrohungsmodell basiert auf folgenden Annahmen:

• die Anwendung läuft auf einem grundsätzlich funktionsfähigen Betriebssystem  
• die Benutzeroberfläche wird lokal bedient  
• das Master-Passwort wird vom Nutzer selbst gewählt und verwaltet  
• Endpunktsicherheit, Benutzerkontentrennung und Datenträgerverschlüsselung liegen außerhalb der direkten Kontrolle der Anwendung  
• keine Cloud-Komponente ist erforderlich, um Kernfunktionen auszuführen  

## Nicht-Ziele

Dieses Bedrohungsmodell deckt nicht vollständig ab:

• physische Laborangriffe auf Datenträger unter Spezialbedingungen  
• vollständige Abwehr eines bereits kompromittierten Systems  
• regulatorische Detailanalysen für alle Jurisdiktionen  
• soziale Engineering-Angriffe außerhalb des Produktkontexts  

## Akteure und Bedrohungsquellen

Relevante Bedrohungsakteure sind unter anderem:

• neugierige lokale Dritte mit Benutzer- oder Gerätezugriff  
• Schadsoftware auf dem Endpunkt  
• Angreifer mit Zugriff auf lokale Dateien oder Backups  
• Entwicklerfehler oder fehlerhafte Releases  
• böswillig manipulierte Abhängigkeiten oder Build-Umgebungen  
• gutmeinende, aber fehlerhafte Benutzerinteraktionen  

## Angriffsflächen

Die wesentlichen Angriffsflächen umfassen:

• Master-Passwort-Eingabe und Sitzungsfreigabe  
• lokale SQLite-Vault-Datenbank  
• verschlüsselte Dateipayloads und deren Import  
• Text-Payloads und Entschlüsselungsvorgänge  
• Log-Dateien und Statusdateien  
• Build- und Packaging-Prozess  
• Bibliotheksabhängigkeiten  
• Datei-Shredding-Workflows mit destruktiver Wirkung  
• unverschlüsselte Vault-Metadatenfelder  

## Datenflüsse

Zentrale Datenflüsse im Sicherheitskontext:

1. Benutzer setzt oder validiert Master-Passwort.  
2. Anwendung leitet daraus Hash- und Sitzungsmaterial ab.  
3. Sitzung wird entsperrt und erlaubt Zugriff auf geschützte Vault-Inhalte.  
4. Texte oder Dateien werden in verschlüsselte Payloads transformiert.  
5. Vault-Einträge werden in SQLite gespeichert, teils verschlüsselt, teils im Klartext.  
6. Logs und Statusdateien werden lokal geschrieben.  
7. Datei-Shredding überschreibt und entfernt lokale Dateien.  

## Bedrohungskategorien

Zur Strukturierung werden die Risiken in folgende Kategorien gegliedert:

• **Vertraulichkeit**  
• **Integrität**  
• **Verfügbarkeit**  
• **Authentifizierung und Autorisierung**  
• **Supply Chain und Release**  
• **Fehlbedienung und UX-Risiken**  

## Detaillierte Bedrohungen nach Bereich

### 1. Master-Passwort und Session-Modell

Mögliche Bedrohungen:

• schwaches oder wiederverwendetes Master-Passwort  
• Offline-Angriffe auf lokal gespeicherte Passwort- oder Salt-bezogene Daten  
• zu lange im Speicher verbleibende Session-Schlüssel  
• inkonsistente Sperr- oder Logout-Logik  
• fehlende Migrationslogik bei Passwortänderungen  

Auswirkungen:

• Verlust der Vertraulichkeit von Vault-Daten  
• dauerhafte Unzugänglichkeit bestehender Daten  
• ungewollte Entsperrung oder inkonsistenter Sitzungszustand  

### 2. Secure Vault

Mögliche Bedrohungen:

• Klartextoffenlegung von `title`, `category` und `username`  
• Manipulation der SQLite-Datenbank  
• ungesicherte Backups oder Kopien der Vault-Datei  
• Datenverlust durch fehlerhafte lokale Eingriffe  

Auswirkungen:

• Metadaten-Leakage  
• Integritätsverlust von Einträgen  
• Vertraulichkeitsverlust außerhalb verschlüsselter Felder  

### 3. Text- und Dateiverschlüsselung

Mögliche Bedrohungen:

• manipulierte oder korrupt übergebene Payloads  
• Dateiverwechslung bei Ein- und Ausgabe  
• unsichere Behandlung temporärer Dateien  
• Fehlinterpretation des Payload-Formats durch Nutzer oder Prozesse  

Auswirkungen:

• fehlgeschlagene Entschlüsselung  
• Datenverlust oder Verwechslung  
• potenzielle Offenlegung durch unsichere Zwischenspeicherung  

### 4. File Shredder

Mögliche Bedrohungen:

• versehentliche Löschung falscher Dateien  
• unvollständige Überschreibung auf bestimmten Speichermedien  
• Fehlannahme, Shredding garantiere auf jeder Hardware vollständige Irreversibilität  
• fehlende Wiederherstellungsmöglichkeit nach Bedienfehlern  

Auswirkungen:

• irreversibler Datenverlust  
• Fehlvertrauen in die Wirksamkeit  
• operative Schäden durch Fehlbedienung  

### 5. Logging und lokale Statusdaten

Mögliche Bedrohungen:

• Offenlegung sensibler Inhalte in Logs  
• Manipulation lokaler Statusdateien  
• Rückschlüsse auf Nutzungsmuster und Sicherheitsereignisse durch Dritte  

Auswirkungen:

• Vertraulichkeitsverlust  
• inkonsistente UI- oder Session-Zustände  
• erschwerte Forensik bei manipulierten Logs  

### 6. Build und Supply Chain

Mögliche Bedrohungen:

• kompromittierte Python-Abhängigkeiten  
• manipulierte Build-Umgebung  
• unsignierte oder veränderte EXE-Artefakte  
• inkonsistente Release-Metadaten  

Auswirkungen:

• Ausführung kompromittierter Software  
• Vertrauensverlust in Releases  
• schwer erkennbare Integritätsverletzungen  

### 7. Endpunktsicherheit

Mögliche Bedrohungen:

• Keylogger oder Malware auf dem lokalen System  
• unzureichende Benutzertrennung  
• fehlende Datenträgerverschlüsselung  
• physischer Zugriff auf das Gerät  

Auswirkungen:

• Abgriff von Passwörtern oder Inhalten  
• Kompromittierung trotz korrekter Anwendungslogik  
• Umgehung lokaler Schutzmaßnahmen  

## Risikobewertung

Die qualitative Bewertung erfolgt anhand von:

• Eintrittswahrscheinlichkeit  
• technischem Impact  
• Reichweite des Schadens  
• Erkennbarkeit  
• Umsetzungsaufwand für Gegenmaßnahmen  

Empfohlene Einstufung:

• **Kritisch**: direkte Gefährdung zentraler Geheimnisse oder Integrität ohne praktikable Ausweichmöglichkeit  
• **Hoch**: erheblicher Sicherheits- oder Betriebsimpact  
• **Mittel**: relevant, aber begrenzbar oder kontextabhängig  
• **Niedrig**: dokumentationswürdig, aber nicht unmittelbar geschäftskritisch  

## Priorisierte Top-Risiken

Aktuell prioritätsstark sind:

• fehlende vollständige Verschlüsselung aller Vault-Felder  
• fehlende sichere Passwort-Rotations- oder Re-Key-Logik  
• Vertrauensabhängigkeit von der Endpunktsicherheit  
• Supply-Chain- und Build-Integritätsrisiken  
• destruktive Fehlbedienung beim File Shredding  

## Bestehende Schutzmaßnahmen

Bereits erkennbare Schutzmechanismen umfassen:

• Master-Passwort-Modell  
• Passwort-Hashing und Sitzungskonzept  
• verschlüsselte Speicherung sensibler Vault-Inhalte  
• definierte Payload-Strukturen für Text und Dateien  
• wiederholtes Überschreiben für Shredding-Operationen  
• lokale Ausführung ohne verpflichtende Cloud-Abhängigkeit  
• Aktivitätsprotokollierung  

## Empfohlene Gegenmaßnahmen

Empfohlene priorisierte Maßnahmen:

• vollständige Feldverschlüsselung im Vault  
• sichere Re-Key-Logik für Passwortwechsel  
• automatische Session-Sperre und konsistente Schlüssel-Lebensdauer  
• Härtung von Logging und Statusdateien  
• Signierung von Release-Artefakten  
• Abhängigkeitsprüfung und Supply-Chain-Monitoring  
• klarere Sicherheitswarnungen im File-Shredder-Workflow  
• Dokumentation der Grenzen von Shredding auf SSDs und modernen Speichermedien  

## Residualrisiken

Auch nach Umsetzung der empfohlenen Maßnahmen verbleiben Restrisiken:

• kompromittierte Endpunkte können lokale Geheimnisse weiterhin gefährden  
• Benutzerfehler bleiben trotz guter UX nicht vollständig ausschließbar  
• forensische oder physische Spezialangriffe liegen außerhalb des typischen Produktschutzes  
• lokale Backups oder Kopien können Sicherheitsgrenzen unterlaufen, wenn sie unsachgemäß behandelt werden  

## Test- und Validierungsstrategie

Zur Absicherung des Bedrohungsmodells sind folgende Prüfungen sinnvoll:

• Tests für Hashing-, Verschlüsselungs- und Entschlüsselungslogik  
• Tests für Vault-Session-Zustände und Sperrverhalten  
• Validierung von Fehlerpfaden bei beschädigten Payloads  
• Tests für Shredding-Workflows und Fehlbedienungsschutz  
• Integritätsprüfungen des Build-Prozesses  
• Review der Logging-Inhalte auf Geheimnisfreiheit  

## Bezug zu Security Policy und Roadmap

Dieses Dokument ergänzt die `SECURITY_POLICY.md` um eine bedrohungsorientierte Sicht und liefert die fachliche Begründung für Prioritäten in der `SECURITY_ROADMAP.md`.

<br>

---

<br>

## Purpose

This document defines the threat model for **CipherCore Suite**. Its purpose is to make security-relevant attack paths, trust boundaries, protected assets and residual risks visible in a structured way. The goal is not only to list weaknesses, but to describe the broader security landscape of the application.

## System Context

CipherCore Suite is a locally executed desktop application centered on:

• text encryption and decryption  
• file encryption and decryption  
• a SQLite-backed Secure Vault  
• a master password and session lock model  
• password generation and evaluation  
• file shredding  
• statistical and technical analytics functions  
• a bilingual PySide6 desktop interface  

The application stores state, logs and vault data locally in the user context. It is primarily designed as an offline or local-first product.

## Assets

The most critical assets include:

• the master password  
• derived keys and session keys  
• encrypted text and file payloads  
• vault content and vault metadata  
• the local database file  
• state files and activity logs  
• build artifacts and executable binaries  
• dependencies and build scripts  

## Trust Boundaries

The main trust boundaries exist between:

• the user and the application  
• the application and the local file system  
• an unlocked session and a locked state  
• encrypted and unencrypted data states  
• source code and compiled release artifacts  
• trusted libraries and potentially compromised dependencies  

## Assumptions

This threat model assumes:

• the application runs on a basically functional operating system  
• the interface is used locally  
• the master password is chosen and managed by the user  
• endpoint hardening, user account separation and disk encryption are outside the direct control of the application  
• no cloud service is required for core functionality  

## Non Goals

This model does not attempt to fully address:

• specialized laboratory-grade physical attacks against storage media  
• complete defense on already compromised endpoints  
• regulatory detail analysis for every jurisdiction  
• social engineering outside the product context  

## Actors and Threat Sources

Relevant threat actors include:

• curious local third parties with access to the user account or device  
• malware on the endpoint  
• attackers with access to local files or backups  
• developer mistakes or flawed releases  
• maliciously altered dependencies or build environments  
• well-intentioned but unsafe user behavior  

## Attack Surfaces

The primary attack surfaces include:

• master password entry and session unlocking  
• the local SQLite vault database  
• encrypted file payloads and their import paths  
• text payload input and decryption paths  
• log files and state files  
• the build and packaging process  
• third-party dependencies  
• destructive shredding workflows  
• unencrypted vault metadata fields  

## Data Flows

Core security-relevant data flows:

1. The user sets or validates the master password.  
2. The application derives password-related and session-related material.  
3. The session becomes unlocked and enables access to protected vault content.  
4. Text or files are transformed into encrypted payloads.  
5. Vault records are stored in SQLite, partly encrypted and partly plaintext.  
6. Logs and state files are written locally.  
7. File shredding overwrites and removes local files.  

## Threat Categories

Risks are grouped into the following categories:

• **confidentiality**  
• **integrity**  
• **availability**  
• **authentication and authorization**  
• **supply chain and release**  
• **misuse and UX-driven risk**  

## Detailed Threats by Domain

### 1. Master Password and Session Model

Possible threats:

• weak or reused master passwords  
• offline attacks against locally stored password-related material  
• session keys remaining in memory too long  
• inconsistent lock or logout behavior  
• missing migration flow for password changes  

Impact:

• confidentiality loss of vault data  
• permanent inaccessibility of existing data  
• accidental unlock or inconsistent session state  

### 2. Secure Vault

Possible threats:

• plaintext leakage of `title`, `category` and `username`  
• manipulation of the SQLite database  
• unsecured backups or copies of the vault file  
• data loss caused by unsafe local intervention  

Impact:

• metadata leakage  
• loss of record integrity  
• confidentiality loss outside encrypted fields  

### 3. Text and File Encryption

Possible threats:

• tampered or corrupted payload input  
• file confusion between source and output  
• unsafe handling of temporary files  
• incorrect interpretation of payload formats by users or processes  

Impact:

• decryption failure  
• data loss or confusion  
• possible disclosure through insecure intermediate storage  

### 4. File Shredder

Possible threats:

• accidental destruction of the wrong files  
• incomplete overwrite on certain storage technologies  
• false trust that shredding guarantees total irreversibility on all hardware  
• no recovery path after user error  

Impact:

• irreversible data loss  
• misplaced trust in technical effectiveness  
• operational damage caused by misuse  

### 5. Logging and Local State

Possible threats:

• sensitive content exposure in logs  
• manipulation of local state files  
• behavioral inference from log or state patterns  

Impact:

• confidentiality loss  
• inconsistent UI or session behavior  
• weakened forensic usefulness when logs are tampered with  

### 6. Build and Supply Chain

Possible threats:

• compromised Python dependencies  
• manipulated build environments  
• unsigned or altered executable artifacts  
• inconsistent release metadata  

Impact:

• execution of compromised software  
• reduced trust in releases  
• difficult-to-detect integrity violations  

### 7. Endpoint Security

Possible threats:

• keyloggers or local malware  
• insufficient account separation  
• lack of disk encryption  
• physical access to the device  

Impact:

• password or content theft  
• compromise despite correct application logic  
• bypass of local protections  

## Risk Evaluation

Qualitative evaluation should consider:

• likelihood  
• technical impact  
• breadth of damage  
• detectability  
• implementation cost of mitigation  

Recommended levels:

• **Critical**: direct threat to central secrets or integrity without a practical workaround  
• **High**: major security or operational impact  
• **Medium**: relevant but limited or context-dependent  
• **Low**: worth documenting, but not immediately business-critical  

## Top Priority Risks

Current high-priority risks are:

• lack of full encryption for all vault fields  
• lack of a secure password rotation or re-key mechanism  
• dependence on endpoint trust  
• supply chain and build integrity risks  
• destructive misuse risk in the file shredding workflow  

## Existing Safeguards

Already visible safeguards include:

• master password model  
• password hashing and session concept  
• encrypted storage of sensitive vault contents  
• defined payload structures for text and file operations  
• repeated overwrite logic for shredding  
• local execution without mandatory cloud dependency  
• activity logging  

## Recommended Mitigations

Priority recommendations:

• full vault field encryption  
• secure re-key logic for password rotation  
• automatic session lock and better control of key lifetime  
• hardening of logging and local state files  
• signing of release artifacts  
• dependency auditing and supply chain monitoring  
• stronger warnings in the file shredder workflow  
• explicit documentation of shredding limits on SSDs and modern storage media  

## Residual Risks

Even after mitigation, residual risks remain:

• compromised endpoints can still endanger local secrets  
• user mistakes cannot be eliminated entirely  
• forensic or physical specialist attacks remain outside normal product protections  
• insecure backups or copied local artifacts can bypass intended safeguards  

## Testing and Validation Strategy

Useful validation measures include:

• tests for hashing, encryption and decryption logic  
• tests for vault session states and lock behavior  
• validation of failure handling for corrupted payloads  
• tests for shredding workflows and misuse protection  
• integrity checks for the build process  
• review of logging contents to ensure secret minimization  

## Alignment with Security Policy and Roadmap

This document complements `SECURITY_POLICY.md` with a threat-oriented view and provides the justification for priorities in `SECURITY_ROADMAP.md`.
