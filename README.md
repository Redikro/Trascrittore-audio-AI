========================================
ITALIANO
AI TRANSCRIBER - GUIDA ALL'INSTALLAZIONE
========================================

REQUISITI:

- Sistema operativo Windows
- Python 3.12.x
- FFmpeg 8.1.2 Essentials Build
- Connessione Internet (solo al primo avvio, se il modello AI deve essere scaricato)

--------------------------------------------------
1. ESTRARRE IL PROGETTO
--------------------------------------------------

Estrarre il file ZIP del progetto in una cartella a scelta.

--------------------------------------------------
2. INSTALLARE PYTHON
--------------------------------------------------

Installare Python versione 3.12.x.

ATTENZIONE:
Versioni successive (ad esempio Python 3.14) potrebbero non essere compatibili con alcune librerie utilizzate dal progetto.

--------------------------------------------------
3. CREARE L'AMBIENTE VIRTUALE (VENV)
--------------------------------------------------

Aprire il Prompt dei comandi nella cartella principale del progetto ed eseguire:

python -m venv venv

--------------------------------------------------
4. ATTIVARE IL VENV
--------------------------------------------------

Sempre dal Prompt dei comandi eseguire:

venv\Scripts\activate

Se l'attivazione è avvenuta correttamente, all'inizio della riga del Prompt comparirà:

(venv)

--------------------------------------------------
5. INSTALLARE LE DIPENDENZE
--------------------------------------------------

Con il venv attivo eseguire:

pip install -r requirements.txt

Attendere il completamento dell'installazione.

--------------------------------------------------
6. INSTALLARE FFMPEG
--------------------------------------------------

Scaricare FFmpeg 8.1.2 Essentials Build dal sito ufficiale.

Estrarre il contenuto dell'archivio e aggiungere la cartella "bin" di FFmpeg alla variabile d'ambiente PATH di Windows.

Per verificare che l'installazione sia corretta, aprire un Prompt dei comandi ed eseguire:

ffmpeg -version

Se viene mostrata la versione installata, FFmpeg è configurato correttamente.

--------------------------------------------------
7. CONFIGURARE I PERCORSI
--------------------------------------------------

Aprire il file:

trascrivi.py

Verificare e modificare, se necessario, i percorsi delle cartelle utilizzate dal programma.

In particolare:

- Cartella di input: deve contenere i file audio e/o video da trascrivere.
- Cartella di output: conterrà i file di testo (.txt) generati dalla trascrizione.

ATTENZIONE:
I percorsi delle cartelle cambieranno quasi sicuramente da un computer all'altro, quindi devono essere modificati prima del primo utilizzo del programma.

--------------------------------------------------
8. AVVIARE IL PROGRAMMA
--------------------------------------------------

Con il venv attivo eseguire:

python trascrivi.py

Il programma inizierà automaticamente a trascrivere tutti i file presenti nella cartella di input e salverà i risultati in formato .txt nella cartella di output.

--------------------------------------------------
NOTE
--------------------------------------------------

- Al primo avvio potrebbe essere scaricato automaticamente il modello AI utilizzato per la trascrizione.
- Il download avviene una sola volta. I successivi avvii utilizzeranno il modello già presente sul computer.
- È consigliato mantenere sempre attivo il venv quando si utilizza il programma.

--------------------------------------------------
RISOLUZIONE DEI PROBLEMI
--------------------------------------------------

ERRORE:
'python' non è riconosciuto come comando interno o esterno.

SOLUZIONE:
Verificare che Python sia installato correttamente e che sia stato aggiunto al PATH durante l'installazione.

--------------------------------------------------

ERRORE:
'ffmpeg' non è riconosciuto come comando interno o esterno.

SOLUZIONE:
Verificare di aver aggiunto correttamente la cartella "bin" di FFmpeg alla variabile d'ambiente PATH.

--------------------------------------------------

ERRORE:
Il venv non si attiva.

SOLUZIONE:
Assicurarsi di trovarsi nella cartella principale del progetto ed eseguire:

venv\Scripts\activate

--------------------------------------------------
UTILIZZO QUOTIDIANO
--------------------------------------------------

Per utilizzare il programma sarà sufficiente:

1. Aprire il Prompt dei comandi nella cartella del progetto.

2. Attivare il venv:

venv\Scripts\activate

3. Avviare il programma:

python trascrivi.py

4. Attendere il completamento della trascrizione.

5. I file di testo (.txt) verranno salvati nella cartella di output specificata nel file "trascrivi.py".


========================================
ENGLISH
AI TRANSCRIBER - INSTALLATION GUIDE
========================================

REQUIREMENTS

- Windows operating system
- Python 3.12.x
- FFmpeg 8.1.2 Essentials Build
- Internet connection (only required on the first launch if the AI model needs to be downloaded)

--------------------------------------------------
1. EXTRACT THE PROJECT
--------------------------------------------------

Extract the project ZIP file to any folder of your choice.

--------------------------------------------------
2. INSTALL PYTHON
--------------------------------------------------

Install Python version 3.12.x.

WARNING:
Later versions (for example Python 3.14) may not be compatible with some of the libraries used by this project.

--------------------------------------------------
3. CREATE THE VIRTUAL ENVIRONMENT (VENV)
--------------------------------------------------

Open Command Prompt in the project's root folder and run:

python -m venv venv

--------------------------------------------------
4. ACTIVATE THE VIRTUAL ENVIRONMENT
--------------------------------------------------

In the same Command Prompt, run:

venv\Scripts\activate

If the activation is successful, you should see:

(venv)

at the beginning of the command line.

--------------------------------------------------
5. INSTALL THE DEPENDENCIES
--------------------------------------------------

With the virtual environment activated, run:

pip install -r requirements.txt

Wait until the installation is complete.

--------------------------------------------------
6. INSTALL FFMPEG
--------------------------------------------------

Download FFmpeg 8.1.2 Essentials Build from the official website.

Extract the archive and add the "bin" folder to the Windows PATH environment variable.

To verify that FFmpeg has been installed correctly, open Command Prompt and run:

ffmpeg -version

If the installed version is displayed, FFmpeg has been configured correctly.

--------------------------------------------------
7. CONFIGURE THE FOLDERS
--------------------------------------------------

Open the file:

trascrivi.py

Check and modify, if necessary, the folder paths used by the program.

In particular:

- Input folder: contains the audio and/or video files to be transcribed.
- Output folder: will contain the generated transcription files in .txt format.

IMPORTANT:
These folder paths will almost certainly be different on every computer, so they must be updated before running the program for the first time.

--------------------------------------------------
8. RUN THE PROGRAM
--------------------------------------------------

With the virtual environment activated, run:

python trascrivi.py

The program will automatically transcribe all supported audio/video files found in the input folder and save the generated .txt files in the output folder.

--------------------------------------------------
NOTES
--------------------------------------------------

- On the first launch, the AI model used for transcription may be downloaded automatically.
- This download only happens once. Future executions will use the locally cached model.
- It is recommended to keep the virtual environment activated whenever you use the program.

--------------------------------------------------
TROUBLESHOOTING
--------------------------------------------------

ERROR:
'python' is not recognized as an internal or external command.

SOLUTION:
Make sure Python is installed correctly and has been added to the Windows PATH during installation.

--------------------------------------------------

ERROR:
'ffmpeg' is not recognized as an internal or external command.

SOLUTION:
Verify that the FFmpeg "bin" folder has been added correctly to the Windows PATH environment variable.

--------------------------------------------------

ERROR:
The virtual environment cannot be activated.

SOLUTION:
Make sure you are in the project's root folder and run:

venv\Scripts\activate

--------------------------------------------------
DAILY USAGE
--------------------------------------------------

To use the program:

1. Open Command Prompt in the project's root folder.

2. Activate the virtual environment:

venv\Scripts\activate

3. Run the program:

python trascrivi.py

4. Wait for the transcription process to finish.

5. The generated .txt files will be saved in the output folder specified in "trascrivi.py".

