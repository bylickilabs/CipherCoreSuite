# RELEASE_SECURITY_CHECKLIST

### Deutsch
• [Release Security Checklist](#release-security-checklist)  
• [Ziel](#ziel)  
• [Vor dem Build](#vor-dem-build)  
• [Während des Builds](#während-des-builds)  
• [Vor Veröffentlichung](#vor-veröffentlichung)  
• [Nach Veröffentlichung](#nach-veröffentlichung)  

### English
• [English](#english)  
• [Release Security Checklist](#release-security-checklist-1)  
• [Goal](#goal)  
• [Before Build](#before-build)  
• [During Build](#during-build)  
• [Before Release](#before-release)  
• [After Release](#after-release)  

<br>

---

<br>

## Deutsch

## Release Security Checklist

## Ziel

Diese Checkliste dient dazu, Releases von CipherCore Suite technisch, organisatorisch und sicherheitsbezogen kontrolliert freizugeben.

## Vor dem Build

• Quellcode auf Platzhalter, Testdaten und Debug-Artefakte prüfen  
• sicherstellen, dass keine Secrets, Zugangsdaten oder Schlüssel im Repository enthalten sind  
• `requirements.txt` auf nachvollziehbare und gewünschte Versionen prüfen  
• `version_info.txt` auf korrekte Produktdaten prüfen  
• Icons, Ressourcen und Pfade validieren  
• Logging auf sensible Klartextdaten prüfen  
• Social- und Kontaktlinks auf produktive Werte prüfen  
• bekannte Sicherheitsgrenzen gegen Release-Risiko abwägen  
• aktuelle Dokumentation gegen Implementierung gegenprüfen  

## Während des Builds

• Build nur aus sauberem Projektzustand starten  
• Onefile-Output erfolgreich erzeugen  
• Build-Logs auf Fehler oder Warnhinweise prüfen  
• sicherstellen, dass alle benötigten Assets eingebunden sind  
• EXE startet ohne offensichtliche Laufzeitfehler  
• Dateipfade, lokale Speicherpfade und App-State-Verhalten validieren  

## Vor Veröffentlichung

• EXE manuell starten und Kernfunktionen testen  
• Textverschlüsselung und Entschlüsselung prüfen  
• Dateiverschlüsselung und Entschlüsselung prüfen  
• Secure Vault mit neuem Eintrag testen  
• Session-Lock und erneute Anmeldung testen  
• File Shredder kontrolliert an Testdatei prüfen  
• Analytics-Funktionen exemplarisch prüfen  
• lokales Datenverzeichnis auf unerwartete Klartextinhalte prüfen  
• Dokumentation aktualisieren  
• Changelog ergänzen  
• Release-Artefakte optional signieren  
• Prüfsummen optional erzeugen und dokumentieren  

## Nach Veröffentlichung

• Release-Artefakte archivieren  
• zugehörige Dokumentation versionieren  
• Rückmeldungen und Fehlermeldungen sammeln  
• sicherheitsrelevante Hinweise priorisiert bewerten  
• bei Bedarf Hotfix-Entscheidung treffen  

<br>

---

<br>

## English

## Release Security Checklist

## Goal

This checklist is intended to support controlled technical, organizational and security-oriented release approval for CipherCore Suite.

## Before Build

• review source code for placeholders, test data and debug artifacts  
• ensure no secrets, credentials or keys are present in the repository  
• review `requirements.txt` for intended and traceable versions  
• validate `version_info.txt` product metadata  
• validate icons, resources and paths  
• review logging for sensitive plaintext exposure  
• validate social and contact links for production use  
• assess known security boundaries against release risk  
• cross-check documentation against implementation state  

## During Build

• start the build from a clean project state  
• verify successful onefile output generation  
• review build logs for errors or warnings  
• ensure all required assets are embedded  
• verify EXE starts without obvious runtime failures  
• validate file paths, local storage paths and app-state behavior  

## Before Release

• manually start the EXE and test core functions  
• verify text encryption and decryption  
• verify file encryption and decryption  
• test Secure Vault with a new entry  
• test session lock and reauthentication  
• validate file shredder on a controlled test file  
• sample-check analytics features  
• inspect local data directory for unexpected plaintext exposure  
• update documentation  
• extend changelog  
• optionally sign release artifacts  
• optionally generate and document checksums  

## After Release

• archive release artifacts  
• version related documentation  
• collect feedback and failure reports  
• prioritize security-relevant findings  
• decide on hotfix action if necessary  
