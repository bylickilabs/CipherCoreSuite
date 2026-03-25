# USER_GUIDE

### Deutsch
• [Benutzerhandbuch](#benutzerhandbuch)  
• [Zielgruppe](#zielgruppe)  
• [Erster Start](#erster-start)  
• [Dashboard](#dashboard)  
• [Text Cryptography](#text-cryptography)  
• [File Cryptography](#file-cryptography)  
• [Secure Vault](#secure-vault)  
• [Password Center](#password-center)  
• [Security Analytics](#security-analytics)  
• [File Shredder](#file-shredder)  
• [Settings](#settings)  
• [Information](#information)  
• [Wichtige Hinweise](#wichtige-hinweise)  

### English
• [English](#english)  
• [User Guide](#user-guide)  
• [Target Audience](#target-audience)  
• [First Start](#first-start)  
• [Dashboard](#dashboard-1)  
• [Text Cryptography](#text-cryptography-1)  
• [File Cryptography](#file-cryptography-1)  
• [Secure Vault](#secure-vault-1)  
• [Password Center](#password-center-1)  
• [Security Analytics](#security-analytics-1)  
• [File Shredder](#file-shredder-1)  
• [Settings](#settings-1)  
• [Information](#information-1)  
• [Important Notes](#important-notes)  

<br>

---

<br>

## Deutsch

## Benutzerhandbuch

Dieses Dokument beschreibt die grundlegende Bedienung von CipherCore Suite aus Anwendersicht.

## Zielgruppe

Geeignet für Benutzer, die lokal:

• Texte schützen möchten  
• Dateien verschlüsseln möchten  
• sensible Einträge in einem Vault verwalten möchten  
• Passwörter generieren oder bewerten möchten  
• Dateien kontrolliert vernichten möchten  
• technische Analysewerte auswerten möchten  

## Erster Start

1. Anwendung starten  
2. Sprache und grundlegende Bedienoberfläche prüfen  
3. Master-Passwort festlegen, sofern noch keines definiert ist  
4. Sitzung entsperren  
5. gewünschtes Modul aufrufen  

## Dashboard

Das Dashboard dient als zentraler Einstiegspunkt. Es bietet einen Überblick und ermöglicht den schnellen Zugriff auf die Hauptmodule.

## Text Cryptography

Hier können Texte verschlüsselt oder entschlüsselt werden.

Typischer Ablauf:
1. Text eingeben  
2. Verschlüsselung oder Entschlüsselung wählen  
3. Ergebnis prüfen  
4. verschlüsselte Nutzlast bei Bedarf speichern oder weiterverwenden  

## File Cryptography

Hier können Dateien verschlüsselt oder entschlüsselt werden.

Typischer Ablauf:
1. Datei auswählen  
2. Zielaktion wählen  
3. Ergebnisdatei erzeugen  
4. verschlüsselte Dateien anhand der `.ccore`-Endung erkennen  

## Secure Vault

Der Secure Vault dient der lokalen Verwaltung sensibler Einträge.

Typischer Ablauf:
1. aktive Sitzung sicherstellen  
2. neuen Eintrag anlegen  
3. Titel, Kategorie, Benutzername, Geheimnis und Notizen pflegen  
4. Eintrag speichern  
5. Eintrag später innerhalb derselben oder einer neuen entsperrten Sitzung wieder aufrufen  

Wichtiger Hinweis:
Aktuell werden nur `secret` und `notes` verschlüsselt gespeichert.

## Password Center

Dieser Bereich unterstützt bei passwortbezogenen Aufgaben.

Mögliche Funktionen:
• Passwortgenerator  
• Passwortbewertung  
• Stärkeindikation  
• technische Einordnung einfacher oder komplexer Passwörter  

## Security Analytics

Hier können technische Kennzahlen für Texte, Passwörter und Dateien berechnet werden.

Mögliche Kennzahlen:
• Entropie  
• SHA-256  
• Zeichensatzgröße  
• Unique Ratio  
• Chi-Quadrat-Uniformität  
• serielle Korrelation  
• Dateivergleich  

## File Shredder

Der File Shredder dient der kontrollierten Überschreibung und Löschung von Dateien.

Typischer Ablauf:
1. Testdatei oder Zieldatei auswählen  
2. Löschvorgang bewusst starten  
3. Ergebnis kontrollieren  

Wichtiger Hinweis:
Die Funktion ist destruktiv und nicht reversibel gedacht.

## Settings

Hier werden Sprach- und allgemeine Bedienparameter verwaltet.

Nach dokumentiertem Stand:
• Sprache kann persistent gespeichert werden  
• Theme-Verhalten ist nicht in gleicher Form persistent umgesetzt  

## Information

Der Bereich Information stellt projektinterne Hinweise, Erläuterungen und weitere Inhalte zur Verfügung.

## Wichtige Hinweise

• Master-Passwort sicher aufbewahren  
• Passwortwechsel ohne Migrationslogik kann Vault-Daten unzugänglich machen  
• File Shredding nur bewusst einsetzen  
• analytische Kennzahlen sind technische Indikatoren, keine Garantieaussagen  
• lokale Sicherheit hängt auch von Betriebssystem, Zugriffsrechten und Backup-Konzept ab  

<br>

---

<br>

## English

## User Guide

This document describes the basic use of CipherCore Suite from an end-user perspective.

## Target Audience

Suitable for users who want to locally:

• protect text  
• encrypt files  
• manage sensitive entries in a vault  
• generate or evaluate passwords  
• destroy files in a controlled manner  
• review technical analysis values  

## First Start

1. Start the application  
2. review language and basic interface  
3. set a master password if none exists yet  
4. unlock the session  
5. open the desired module  

## Dashboard

The dashboard serves as the central entry point. It provides overview access to the main modules.

## Text Cryptography

This section allows users to encrypt or decrypt text.

Typical flow:
1. enter text  
2. choose encryption or decryption  
3. review the result  
4. store or reuse the encrypted payload if needed  

## File Cryptography

This section allows users to encrypt or decrypt files.

Typical flow:
1. choose a file  
2. select the target action  
3. generate the output file  
4. recognize encrypted files by the `.ccore` suffix  

## Secure Vault

The Secure Vault is used for local management of sensitive entries.

Typical flow:
1. ensure an active session  
2. create a new entry  
3. maintain title, category, username, secret and notes  
4. save the entry  
5. reopen the entry later during the same or a new unlocked session  

Important note:
At the current implementation state, only `secret` and `notes` are stored encrypted.

## Password Center

This area supports password-related tasks.

Possible functions:
• password generator  
• password evaluation  
• strength indication  
• technical classification of simple or complex passwords  

## Security Analytics

This module can compute technical metrics for text, passwords and files.

Possible metrics:
• entropy  
• SHA-256  
• character set size  
• unique ratio  
• chi-square uniformity  
• serial correlation  
• file comparison  

## File Shredder

The file shredder supports controlled overwrite-based deletion.

Typical flow:
1. choose a test file or target file  
2. intentionally start deletion  
3. verify the result  

Important note:
This function is destructive and intended to be irreversible.

## Settings

This area manages language and general operating parameters.

According to the documented implementation state:
• language can be persisted  
• theme behavior is not persisted in the same way  

## Information

The Information area provides internal project notes, explanations and related content.

## Important Notes

• keep the master password secure  
• password changes without migration logic can make vault data inaccessible  
• use file shredding deliberately  
• analytic metrics are technical indicators, not guarantees  
• local security also depends on operating system security, access control and backup strategy  
