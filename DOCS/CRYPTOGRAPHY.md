# CRYPTOGRAPHY

### Deutsch
• [Kryptografie](#kryptografie)  
• [Zielsetzung](#zielsetzung)  
• [Kryptografische Bausteine](#kryptografische-bausteine)  
• [Passwortmodell](#passwortmodell)  
• [Schlüsselableitung](#schlüsselableitung)  
• [Payload-Modell](#payload-modell)  
• [Text- und Dateiverschlüsselung](#text--und-dateiverschlüsselung)  
• [Vault-Kryptografie](#vault-kryptografie)  
• [Sicherheitsannahmen](#sicherheitsannahmen)  
• [Bekannte Grenzen](#bekannte-grenzen)  
• [Empfohlene Weiterentwicklung](#empfohlene-weiterentwicklung)  

### English
• [English](#english)  
• [Cryptography](#cryptography)  
• [Objective](#objective)  
• [Cryptographic Building Blocks](#cryptographic-building-blocks)  
• [Password Model](#password-model)  
• [Key Derivation](#key-derivation)  
• [Payload Model](#payload-model)  
• [Text and File Encryption](#text-and-file-encryption)  
• [Vault Cryptography](#vault-cryptography)  
• [Security Assumptions](#security-assumptions)  
• [Known Boundaries](#known-boundaries)  
• [Recommended Evolution](#recommended-evolution)  

<br>

---

<br>

## Deutsch

## Kryptografie

CipherCore Suite verwendet passwortbasierte Kryptografie für Text-, Datei- und Vault-bezogene Schutzmechanismen. Die Implementierung ist auf lokale Nutzung, Wiederherstellbarkeit verschlüsselter Nutzdaten und nachvollziehbare Schlüsselerzeugung ausgelegt.

## Zielsetzung

Die kryptografische Architektur soll folgende Ziele erfüllen:

• nutzerseitige Verschlüsselung sensibler Inhalte  
• lokale Wiederherstellbarkeit verschlüsselter Artefakte  
• Schutz von Vault-Inhalten innerhalb der Anwendung  
• Ableitung stabiler kryptografischer Kontexte aus einem Master-Passwort  
• praktikable Integration in eine Desktop-Anwendung ohne externe Schlüsselserver  

## Kryptografische Bausteine

Die vorhandene Implementierung nutzt nach der dokumentierten Architektur unter anderem:

• PBKDF2-HMAC-SHA256 für Schlüsselableitung  
• Salt-basierte Passwortverarbeitung  
• Fernet-basierte symmetrische Verschlüsselung für Nutzdaten  
• Passwort-Hashing und Verifikation für das Master-Passwort  
• SHA-256 für analytische Integritäts- und Vergleichsausgaben  

## Passwortmodell

Das Master-Passwort dient als zentrale Benutzereingabe für den geschützten Zugriff auf Vault-Funktionen. Es wird nicht als Klartext gespeichert, sondern in gehashter Form verarbeitet.

Zentrale Merkmale:

• Benutzer definiert ein Master-Passwort  
• ein Salt wird genutzt, um die Ableitung zu härten  
• aus Passwort und Salt wird ein Schlüsselkontext erzeugt  
• dieser Kontext dient für Session-bezogene Vault-Zugriffe  
• ohne korrektes Passwort kann der gleiche Schlüsselkontext nicht sinnvoll rekonstruiert werden  

## Schlüsselableitung

Die Schlüsselableitung basiert auf einem passwortbasierten Derivationsverfahren.

### Zweck
• Reduzierung direkter Passwortverwendung als Schlüssel  
• Erhöhung der Kosten für Offline-Angriffe  
• deterministische Reproduzierbarkeit des Schlüssels bei gleicher Eingabe und gleichem Salt  

### Operative Bedeutung
Die Iterationsanzahl und das Salt sind sicherheitsrelevant. Sie beeinflussen die Widerstandsfähigkeit gegen brute-force- oder dictionary-basierte Angriffe.

## Payload-Modell

CipherCore Suite organisiert verschlüsselte Inhalte als logisch portable Payloads. Diese Struktur ist für Text- und Dateioperationen vorteilhaft, weil sie Metadaten, Nutzdaten und Wiederherstellungskontext in einem handhabbaren Format bündeln kann.

Ein robustes Payload-Modell sollte typischerweise enthalten:

• Formatversion  
• Salt oder benötigte Ableitungsparameter  
• verschlüsselte Nutzdaten  
• optionale Metadaten  
• Dateiendung oder Kennzeichnung für verschlüsselte Artefakte  

In der aktuellen Projektlogik ist `.ccore` als verschlüsselte Dateiendung vorgesehen.

## Text- und Dateiverschlüsselung

### Textverschlüsselung
Bei Textoperationen wird Klartext über den abgeleiteten Schlüsselkontext verschlüsselt und als transportierbare Nutzlast ausgegeben.

### Dateiverschlüsselung
Bei Dateioperationen werden Dateiinhalte gelesen, verschlüsselt und in einer geschützten Payload geschrieben. Die resultierenden Artefakte können lokal gespeichert und später entschlüsselt werden.

### Wiederherstellung
Für die Entschlüsselung ist ein konsistenter Schlüsselkontext erforderlich. Falsche Passwörter oder inkonsistente Payload-Daten verhindern die Wiederherstellung.

## Vault-Kryptografie

Der Secure Vault verwendet ein passwortgebundenes Session-Modell. Nach erfolgreicher Anmeldung werden bestimmte Eintragsfelder verschlüsselt gespeichert.

Nach dem dokumentierten Stand gilt:

• `secret` wird verschlüsselt gespeichert  
• `notes` wird verschlüsselt gespeichert  
• `title` bleibt im Klartext  
• `category` bleibt im Klartext  
• `username` bleibt im Klartext  

Diese Architektur schützt besonders sensible Inhalte, verschlüsselt aktuell aber nicht den vollständigen semantischen Datensatz eines Eintrags.

## Sicherheitsannahmen

Die Wirksamkeit des Modells hängt unter anderem von folgenden Annahmen ab:

• das Master-Passwort ist ausreichend stark  
• das Endgerät ist nicht bereits kompromittiert  
• lokaler Speicher ist nur kontrolliert zugänglich  
• Salt und Iterationsparameter sind korrekt implementiert  
• Logs enthalten keine sensiblen Klartextinhalte  
• die Anwendung verarbeitet Schlüsselmaterial nicht unsicher außerhalb des vorgesehenen Kontexts  

## Bekannte Grenzen

Die aktuelle Kryptografiearchitektur ist zweckmäßig, hat aber operative Grenzen:

• vollständige Vault-Feldverschlüsselung fehlt  
• Passwortwechsel ohne Migration kann bestehende Daten unzugänglich machen  
• keine dokumentierte Schlüsselrotation für bereits verschlüsselte Bestandsdaten  
• kein separates Key-Encryption-Key-Modell  
• keine Hardware-gebundene Schlüsselableitung  
• keine integrierte Signatur oder Authentizitätsprüfung außerhalb des verwendeten Payload-Schemas  

## Empfohlene Weiterentwicklung

Für den nächsten Sicherheitsreifegrad sind diese Maßnahmen sinnvoll:

• vollständige Verschlüsselung zusätzlicher Vault-Felder  
• Re-Key-Workflow für Master-Passwort-Wechsel  
• klare Payload-Versionierung für Langzeitkompatibilität  
• optionaler Einsatz eines Memory-Hard-KDF für erhöhte Passwortresistenz  
• sichere Export- und Backup-Strategie für verschlüsselte Daten  
• Signierung von Release-Artefakten und Dokumentation kryptografischer Parameter  

<br>

---

<br>

## English

## Cryptography

CipherCore Suite uses password-based cryptography for text, file and vault-related protection mechanisms. The implementation is designed for local usage, recoverable encrypted artifacts and traceable key generation.

## Objective

The cryptographic architecture is intended to achieve the following goals:

• user-side encryption of sensitive content  
• local recoverability of encrypted artifacts  
• protection of vault content inside the application  
• derivation of stable cryptographic contexts from a master password  
• practical integration into a desktop application without external key servers  

## Cryptographic Building Blocks

Based on the documented project architecture, the implementation uses among other things:

• PBKDF2-HMAC-SHA256 for key derivation  
• salt-based password processing  
• Fernet-based symmetric encryption for payloads  
• password hashing and verification for the master password  
• SHA-256 for analytic integrity and comparison output  

## Password Model

The master password serves as the central user input for protected access to vault functions. It is not stored in plaintext, but handled in hashed form.

Core properties:

• the user defines a master password  
• a salt is used to harden derivation  
• a key context is derived from password and salt  
• this context is used for session-bound vault access  
• without the correct password, the same key context cannot be meaningfully reconstructed  

## Key Derivation

Key derivation is based on a password-based derivation function.

### Purpose
• avoid direct password use as encryption key  
• increase the cost of offline attacks  
• provide deterministic key reconstruction from the same password and salt  

### Operational Relevance
Iteration count and salt are security-relevant. They influence resistance against brute-force and dictionary-based attacks.

## Payload Model

CipherCore Suite organizes encrypted content as logically portable payloads. This is useful for text and file operations because metadata, content and recovery context can be bundled in one manageable structure.

A robust payload model should typically include:

• format version  
• salt or required derivation parameters  
• encrypted payload data  
• optional metadata  
• suffix or marker for encrypted artifacts  

In the current project logic, `.ccore` is the configured encrypted file suffix.

## Text and File Encryption

### Text Encryption
For text operations, plaintext is encrypted through the derived key context and emitted as a transportable payload.

### File Encryption
For file operations, file contents are read, encrypted and written into a protected payload. The resulting artifacts can be stored locally and decrypted later.

### Recovery
Decryption requires a consistent key context. Wrong passwords or inconsistent payload data prevent recovery.

## Vault Cryptography

The Secure Vault uses a password-bound session model. After successful authentication, selected entry fields are stored encrypted.

According to the documented implementation state:

• `secret` is stored encrypted  
• `notes` is stored encrypted  
• `title` remains plaintext  
• `category` remains plaintext  
• `username` remains plaintext  

This architecture protects highly sensitive content, but does not yet encrypt the full semantic record of a vault entry.

## Security Assumptions

The effectiveness of the model depends on assumptions such as:

• the master password is sufficiently strong  
• the endpoint is not already compromised  
• local storage is access-controlled  
• salt and iteration parameters are correctly implemented  
• logs do not expose sensitive plaintext  
• key material is not processed unsafely outside the intended context  

## Known Boundaries

The current cryptography model is practical, but has operational boundaries:

• full vault field encryption is not yet implemented  
• password changes without migration can render existing data inaccessible  
• no documented key rotation for already encrypted records  
• no separate key-encryption-key model  
• no hardware-bound derivation  
• no integrated release signing or authenticity verification beyond the payload scheme in use  

## Recommended Evolution

For the next security maturity stage, the following measures would be valuable:

• full encryption of additional vault fields  
• re-key workflow for master password changes  
• explicit payload versioning for long-term compatibility  
• optional use of a memory-hard KDF for stronger password resistance  
• secure export and backup strategy for encrypted data  
• signing of release artifacts and documentation of cryptographic parameters  
