# PRIVACY

### Deutsch
• [Datenschutz und lokale Datenverarbeitung](#datenschutz-und-lokale-datenverarbeitung)  
• [Grundsatz](#grundsatz)  
• [Welche Daten lokal verarbeitet werden](#welche-daten-lokal-verarbeitet-werden)  
• [Speicherorte](#speicherorte)  
• [Zweck der Verarbeitung](#zweck-der-verarbeitung)  
• [Was nicht vorgesehen ist](#was-nicht-vorgesehen-ist)  
• [Grenzen der lokalen Vertraulichkeit](#grenzen-der-lokalen-vertraulichkeit)  
• [Empfehlungen für Nutzer](#empfehlungen-für-nutzer)  

### English
• [English](#english)  
• [Privacy and Local Data Processing](#privacy-and-local-data-processing)  
• [Principle](#principle)  
• [What Data Is Processed Locally](#what-data-is-processed-locally)  
• [Storage Locations](#storage-locations)  
• [Purpose of Processing](#purpose-of-processing)  
• [What Is Not Intended](#what-is-not-intended)  
• [Limits of Local Confidentiality](#limits-of-local-confidentiality)  
• [Recommendations for Users](#recommendations-for-users)  

<br>

---

<br>

## Deutsch

## Datenschutz und lokale Datenverarbeitung

## Grundsatz

CipherCore Suite ist als lokal arbeitende Desktop-Anwendung konzipiert. Die primäre Datenverarbeitung erfolgt auf dem Endgerät des Benutzers. Ziel ist es, kryptografische, analytische und speicherbezogene Arbeitsabläufe lokal bereitzustellen.

## Welche Daten lokal verarbeitet werden

Je nach Nutzung können lokal verarbeitet oder gespeichert werden:

• Texte zur Ver- und Entschlüsselung  
• ausgewählte Datei-Inhalte zur Ver- und Entschlüsselung  
• Vault-Einträge  
• App-Zustände und Spracheinstellungen  
• Aktivitätsprotokolle  
• Analysekennzahlen wie Hashwerte, Entropie oder statistische Metriken  

## Speicherorte

Typische lokale Speicherorte sind:

```text
~/.ciphercore_suite/
```

Darin beispielsweise:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

Zusätzlich können benutzerseitig verschlüsselte Datei-Artefakte mit der Endung `.ccore` erzeugt werden.

## Zweck der Verarbeitung

Die lokale Verarbeitung dient insbesondere:

• der Verschlüsselung und Entschlüsselung von Nutzdaten  
• der Verwaltung sensibler Vault-Inhalte  
• der Steuerung lokaler Anwendungssitzungen  
• der Analyse technischer Eigenschaften von Texten und Dateien  
• der Nachvollziehbarkeit betrieblicher Vorgänge  

## Was nicht vorgesehen ist

Nach der dokumentierten Architektur ist Folgendes nicht Kernbestandteil des Produkts:

• zentrale Cloud-Speicherung als Standardfunktion  
• serverseitige Kontenverwaltung  
• netzwerkbasierte Mehrbenutzer-Synchronisation  
• automatische externe Weitergabe sensibler Nutzdaten als Kernfunktion  

## Grenzen der lokalen Vertraulichkeit

Lokale Verarbeitung bedeutet nicht automatisch vollständige Sicherheit. Die Vertraulichkeit hängt auch ab von:

• Sicherheit des Betriebssystems  
• lokaler Benutzer- und Rechteverwaltung  
• Malware-Freiheit des Endgeräts  
• sicherer Aufbewahrung des Master-Passworts  
• Backup- und Wiederherstellungsstrategie  
• sicherem Umgang mit Logs, Dateien und Exporten  

Wichtiger Hinweis:
Nicht alle Vault-Felder sind aktuell verschlüsselt. Nach dokumentiertem Stand werden `secret` und `notes` geschützt gespeichert, während `title`, `category` und `username` im Klartext vorliegen.

## Empfehlungen für Nutzer

• starkes Master-Passwort verwenden  
• Gerät durch aktuelle Sicherheitsupdates schützen  
• lokale Zugriffsrechte absichern  
• regelmäßige Backups bewusst planen  
• Logs und lokale Datenverzeichnisse kontrolliert behandeln  
• produktive Social- und Kontaktwerte vor Veröffentlichung prüfen  

<br>

---

<br>

## English

## Privacy and Local Data Processing

## Principle

CipherCore Suite is designed as a locally operating desktop application. Primary data processing takes place on the user's endpoint. The goal is to provide cryptographic, analytic and storage-related workflows locally.

## What Data Is Processed Locally

Depending on usage, the following may be processed or stored locally:

• text for encryption and decryption  
• selected file contents for encryption and decryption  
• vault entries  
• app state and language settings  
• activity logs  
• analytic values such as hashes, entropy or statistical metrics  

## Storage Locations

Typical local storage locations include:

```text
~/.ciphercore_suite/
```

For example:

• `data/vault.db`  
• `data/app_state.json`  
• `logs/activity.log`  

In addition, user-generated encrypted file artifacts with the `.ccore` suffix may be created.

## Purpose of Processing

Local processing mainly serves:

• encryption and decryption of user content  
• management of sensitive vault content  
• control of local application sessions  
• analysis of technical properties of text and files  
• traceability of operational events  

## What Is Not Intended

According to the documented architecture, the following are not core product characteristics:

• centralized cloud storage as a default function  
• server-side account management  
• network-based multi-user synchronization  
• automatic external transmission of sensitive user data as a core function  

## Limits of Local Confidentiality

Local processing does not automatically guarantee full security. Confidentiality also depends on:

• operating system security  
• local user and permission management  
• absence of malware on the endpoint  
• safe handling of the master password  
• backup and recovery strategy  
• careful handling of logs, files and exports  

Important note:
Not all vault fields are currently encrypted. According to the documented implementation state, `secret` and `notes` are protected, while `title`, `category` and `username` remain plaintext.

## Recommendations for Users

• use a strong master password  
• protect the device with current security updates  
• secure local access rights  
• plan regular backups deliberately  
• handle logs and local data folders with care  
• validate production social and contact values before publishing  
