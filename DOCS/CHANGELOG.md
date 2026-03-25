# CHANGELOG

### Deutsch
• [Changelog](#changelog)  
• [Hinweis zur Pflege](#hinweis-zur-pflege)  
• [Version 1.0.0](#version-100)  
• [Geplante nächste Änderungen](#geplante-nächste-änderungen)  

### English
• [English](#english)  
• [Changelog](#changelog-1)  
• [Maintenance Note](#maintenance-note)  
• [Version 1.0.0](#version-100-1)  
• [Planned Next Changes](#planned-next-changes)  

<br>

---

<br>

## Deutsch

## Changelog

Dieses Dokument dient der nachvollziehbaren Dokumentation von Änderungen, Erweiterungen, Fixes und sicherheitsrelevanten Anpassungen innerhalb von CipherCore Suite.

## Hinweis zur Pflege

Empfohlene Pflegeprinzipien:

• jede veröffentlichte Version dokumentieren  
• neue Features und Fixes getrennt aufführen  
• Breaking Changes klar kennzeichnen  
• sicherheitsrelevante Änderungen explizit markieren  
• Build- und Packaging-Änderungen mit aufnehmen  

## Version 1.0.0

### Initialer dokumentierter Funktionsstand
• modulare Desktop-Anwendung auf Basis von Python und PySide6  
• Textverschlüsselung und Textentschlüsselung  
• Dateiverschlüsselung und Dateientschlüsselung  
• Secure Vault auf Basis von SQLite  
• Master-Passwort und Session-Modell  
• Passwortgenerator und Passwortbewertung  
• File Shredder mit überschreibender Löschlogik  
• Security Analytics für Texte, Passwörter und Dateien  
• Randomness Lab  
• deutsche und englische Benutzeroberfläche  
• Aktivitätslog und Informationszentrum  
• Windows-Build über PyInstaller mit Metadaten  

### Bekannte technische Merkmale
• Vault speichert aktuell `secret` und `notes` verschlüsselt  
• `title`, `category` und `username` bleiben im Klartext  
• Sprache wird persistent gespeichert  
• Theme-Auswahl ist derzeit nicht in gleicher Form persistent  
• Social-Links sind teilweise noch Platzhalter  

## Geplante nächste Änderungen

• vollständige Verschlüsselung weiterer Vault-Felder  
• sichere Migrationslogik für Passwortwechsel  
• persistente Theme-Speicherung  
• Bereinigung produktiver Kontakt- und Social-Links  
• Export- und Backup-Funktionen  
• Release-Signierung und weiteres Hardening  

<br>

---

<br>

## English

## Changelog

This document provides traceable documentation of changes, feature additions, fixes and security-relevant adjustments within CipherCore Suite.

## Maintenance Note

Recommended maintenance principles:

• document every released version  
• separate new features from fixes  
• clearly mark breaking changes  
• explicitly identify security-relevant changes  
• include build and packaging changes  

## Version 1.0.0

### Initial documented feature baseline
• modular desktop application based on Python and PySide6  
• text encryption and text decryption  
• file encryption and file decryption  
• SQLite-backed Secure Vault  
• master password and session model  
• password generator and password evaluation  
• file shredder with overwrite-based deletion logic  
• security analytics for text, passwords and files  
• Randomness Lab  
• German and English user interface  
• activity log and information center  
• Windows build via PyInstaller with metadata  

### Known technical properties
• vault currently stores `secret` and `notes` encrypted  
• `title`, `category` and `username` remain plaintext  
• language is persisted  
• theme selection is currently not persisted in the same manner  
• some social links are still placeholders  

## Planned Next Changes

• full encryption of additional vault fields  
• secure migration logic for password changes  
• persistent theme storage  
• production-ready contact and social links  
• export and backup features  
• release signing and further hardening  
