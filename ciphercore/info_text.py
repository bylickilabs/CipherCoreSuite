from __future__ import annotations

INFO_TEXT = {
    'de': """
<h2>CipherCore Suite 1.0.0</h2>

<p><b>CipherCore Suite</b> ist eine mehrsprachige Desktop Sicherheitsplattform für Verschlüsselung, Entschlüsselung, geschützte Datenspeicherung, kontrollierte Dateivernichtung und statistische Sicherheitsanalyse. Die Anwendung verbindet klassische kryptographische Schutzmechanismen mit einer modernen Analytics Schicht und vereint mehrere sicherheitsrelevante Arbeitsbereiche in einer zentralen, professionell aufgebauten Benutzeroberfläche.</p>

<p>Die Plattform wurde entwickelt, um sensible Inhalte nicht nur sicher zu verarbeiten, sondern zusätzlich deren technische Struktur, Verteilungseigenschaften und statistische Auffälligkeiten analysierbar zu machen. Dadurch entsteht eine kombinierte Security und Analytics Workbench für anspruchsvolle Desktop Nutzung.</p>

<h3>Kernbereiche</h3>
<ul>
<li>Text Verschlüsselung und Entschlüsselung</li>
<li>Datei Verschlüsselung und Entschlüsselung mit geschützter Verarbeitung</li>
<li>Secure Vault mit lokal verschlüsselten Datensätzen</li>
<li>Master Passwort, Session Lock, Passwortgenerator und Stärkeanzeige</li>
<li>File Shredder mit mehrfacher Überschreibung</li>
<li>Security Analytics für Texte, Passwörter, Dateien und Dateivergleiche</li>
<li>Randomness Lab zur technischen Bewertung zufallsbasierter Daten</li>
<li>vollständige deutsche und englische Sprachumschaltung</li>
<li>modulare Desktop Struktur mit klar getrennten Sicherheitsbereichen</li>
</ul>

<h3>Funktionsübersicht</h3>
<p>Die Anwendung gliedert sich in mehrere operative Module, die jeweils auf einen bestimmten Sicherheits oder Analysebereich ausgerichtet sind.</p>
<ul>
<li><b>Textmodul</b> zur sicheren Verschlüsselung und Entschlüsselung vertraulicher Textinhalte</li>
<li><b>Dateimodul</b> zur geschützten Verarbeitung lokaler Dateien mit passwortbasierter Ver und Entschlüsselung</li>
<li><b>Analytics Modul</b> zur strukturellen und statistischen Bewertung unterschiedlicher Datenformen</li>
<li><b>Secure Vault</b> zur lokalen Speicherung sensibler Datensätze in geschützter Form</li>
<li><b>Passwortzentrum</b> zur Verwaltung von Master Passwort, Anmeldung, Sitzung und Passwortbewertung</li>
<li><b>Shredder Modul</b> zur irreversiblen und kontrollierten Löschung ausgewählter Dateien</li>
<li><b>Einstellungsbereich</b> für Sprache und visuelle Darstellung</li>
<li><b>Informationszentrum</b> mit strukturierten Hintergrundinformationen zur Anwendung</li>
</ul>

<h3>Analytics Layer</h3>
<p>Die Analytics Ebene bewertet Inhalte nicht semantisch, sondern strukturell und statistisch. Je nach Modul werden unter anderem Entropie, Byte Verteilungen, Chi Quadrat Uniformität, serielle Korrelation, Distanzmaße, Verteilungsmuster und weitere technische Kennzahlen berechnet. Dadurch können auffällige Strukturen, hohe Gleichförmigkeit, starke Musterbildung oder erhöhte Zufälligkeit sichtbar gemacht werden.</p>

<p>Diese Analysefunktionen erweitern die Anwendung über klassische Sicherheitswerkzeuge hinaus und schaffen eine zusätzliche Bewertungsebene für Texte, Passwörter, Dateien und zufallsbasierte Daten.</p>

<h3>Architektur</h3>
<p>Die Benutzeroberfläche basiert auf <b>PySide6</b> und ist als moderne Desktop Oberfläche mit modularer Navigation aufgebaut. Die kryptographische Verarbeitung nutzt <code>cryptography</code>. Die Analytics Schicht verwendet <code>numpy</code> und <code>scipy</code> für statistische und numerische Auswertungen. Die lokale Persistenz erfolgt über <b>SQLite</b>. Die Anwendung ist damit als modulare Security und Analytics Workbench für anspruchsvolle Desktop Nutzung ausgelegt.</p>

<h3>Sicherheitsworkflow</h3>
<ul>
<li>Ein Master Passwort wird gesetzt und lokal abgesichert.</li>
<li>Nach erfolgreicher Anmeldung wird eine freigeschaltete Sitzung aufgebaut.</li>
<li>Sensible Datensätze können im Secure Vault verschlüsselt gespeichert werden.</li>
<li>Texte und Dateien können geschützt ver oder entschlüsselt werden.</li>
<li>Nicht mehr benötigte Dateien können über den File Shredder kontrolliert vernichtet werden.</li>
<li>Analysefunktionen können ergänzend eingesetzt werden, um Inhalte technisch zu bewerten.</li>
</ul>

<h3>Datenhaltung</h3>
<p>Die Anwendung speichert lokale Zustandsdaten, Vault Inhalte und Protokolle in einem versteckten Anwendungsordner innerhalb des Benutzerverzeichnisses. Die Verarbeitung erfolgt standardmäßig lokal. Dazu gehören unter anderem Sitzungszustände, Master Passwort Metadaten, Vault Datensätze, Log Einträge und weitere anwendungsbezogene Informationen.</p>

<h3>Betriebshinweise</h3>
<ul>
<li>Starke Passwörter bleiben ein zentraler Bestandteil der Sicherheit des Systems.</li>
<li>Dateivernichtung ist irreversibel und sollte nur nach bewusster Prüfung ausgeführt werden.</li>
<li>Analysewerte sind technische Kennzahlen und kein Ersatz für forensische Gutachten, Audits oder formale Compliance Bewertungen.</li>
<li>Für produktive Nutzung in sensiblen Umgebungen sind Backups, Systemhärtung und organisatorische Sicherheitsmaßnahmen weiterhin erforderlich.</li>
<li>Die sichere Nutzung der Anwendung hängt nicht nur von der Software, sondern auch vom verantwortungsvollen Umgang mit Passwörtern, Dateien und lokalen Systemen ab.</li>
</ul>

<h3>Zielsetzung</h3>
<p>CipherCore Suite wurde mit dem Ziel entwickelt, Sicherheit, kontrollierte Datenverarbeitung und technische Analyse in einer einzigen Desktop Anwendung zusammenzuführen. Der Fokus liegt auf klarer Benutzerführung, modularer Erweiterbarkeit, professioneller Struktur und praxisnaher Nutzbarkeit für moderne Sicherheits und Analyseanforderungen.</p>

<h3>Copyright</h3>
<p>© Thorsten Bylicki · BYLICKILABS. Alle Rechte vorbehalten.</p>
""",

    'en': """
<h2>CipherCore Suite 1.0.0</h2>

<p><b>CipherCore Suite</b> is a multilingual desktop security platform for encryption, decryption, protected data storage, controlled file destruction and statistical security analysis. The application combines classical cryptographic protection mechanisms with a modern analytics layer and brings multiple security relevant workflows together in one central and professionally structured interface.</p>

<p>The platform was designed not only to securely process sensitive content, but also to make its technical structure, distribution properties and statistical characteristics analyzable. This creates a combined security and analytics workbench for demanding desktop usage.</p>

<h3>Core areas</h3>
<ul>
<li>text encryption and decryption</li>
<li>file encryption and decryption with protected processing</li>
<li>Secure Vault with locally encrypted records</li>
<li>master password, session lock, password generator and strength indicator</li>
<li>file shredder with repeated overwrite</li>
<li>security analytics for text, passwords, files and file comparison</li>
<li>Randomness Lab for technical evaluation of random based data</li>
<li>complete German and English language switching</li>
<li>modular desktop structure with clearly separated security areas</li>
</ul>

<h3>Feature overview</h3>
<p>The application is divided into several operational modules, each focusing on a dedicated security or analytics domain.</p>
<ul>
<li><b>Text module</b> for secure encryption and decryption of confidential text content</li>
<li><b>File module</b> for protected handling of local files with password based encryption and decryption</li>
<li><b>Analytics module</b> for structural and statistical evaluation of different data types</li>
<li><b>Secure Vault</b> for protected local storage of sensitive records</li>
<li><b>Password center</b> for managing master password, authentication, sessions and password evaluation</li>
<li><b>Shredder module</b> for irreversible and controlled deletion of selected files</li>
<li><b>Settings area</b> for language and visual presentation</li>
<li><b>Information center</b> with structured background information about the application</li>
</ul>

<h3>Analytics layer</h3>
<p>The analytics layer evaluates content structurally and statistically rather than semantically. Depending on the module, entropy, byte distributions, chi square uniformity, serial correlation, distance metrics, distribution patterns and related technical indicators are calculated. This makes it possible to surface unusual structures, high uniformity, strong pattern formation or elevated randomness.</p>

<p>These analytics capabilities extend the application beyond traditional security utilities and provide an additional evaluation layer for text, passwords, files and random based data.</p>

<h3>Architecture</h3>
<p>The user interface is built with <b>PySide6</b> and organized as a modern desktop interface with modular navigation. The cryptographic processing uses <code>cryptography</code>. The analytics layer uses <code>numpy</code> and <code>scipy</code> for numerical and statistical processing. Local persistence is handled through <b>SQLite</b>. The application is therefore designed as a modular security and analytics workbench for demanding desktop scenarios.</p>

<h3>Security workflow</h3>
<ul>
<li>A master password is created and stored locally in protected form.</li>
<li>After successful authentication, an unlocked session is established.</li>
<li>Sensitive records can be stored inside the encrypted Secure Vault.</li>
<li>Text and files can be securely encrypted or decrypted when required.</li>
<li>Files that are no longer needed can be destroyed through the controlled file shredder.</li>
<li>Analytics functions can be used additionally to evaluate content on a technical level.</li>
</ul>

<h3>Data handling</h3>
<p>The application stores local state data, vault content and logs inside a hidden application folder within the user home directory. Processing is local by default. This includes session state, master password metadata, vault records, log entries and other application related information.</p>

<h3>Operational guidance</h3>
<ul>
<li>Strong passwords remain a central part of the overall security posture.</li>
<li>File destruction is irreversible and should only be executed after deliberate review.</li>
<li>Analysis values are technical indicators and not a substitute for forensic reports, audits or formal compliance assessments.</li>
<li>For productive use in sensitive environments, backups, system hardening and organizational security controls are still required.</li>
<li>The secure use of the application depends not only on the software itself, but also on responsible handling of passwords, files and local systems.</li>
</ul>

<h3>Project objective</h3>
<p>CipherCore Suite was developed with the goal of combining security, controlled data handling and technical analytics in a single desktop application. The focus lies on clear user guidance, modular extensibility, professional structure and practical usability for modern security and analytics requirements.</p>

<h3>Copyright</h3>
<p>© Thorsten Bylicki · BYLICKILABS. All rights reserved.</p>
""",
}