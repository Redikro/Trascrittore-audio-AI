import warnings
import os
import subprocess
import logging

# ===========================
# NASCONDI TUTTI I WARNING
# ===========================

warnings.filterwarnings("ignore")

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["HF_HUB_DISABLE_IMPLICIT_TOKEN_WARNING"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

logging.getLogger("huggingface_hub").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)


# ===========================
# IMPORT
# ===========================

from faster_whisper import WhisperModel
from tqdm import tqdm


# ===========================
# CARTELLE
# ===========================

CARTELLA_AUDIO = r"C:\Users\forza\OneDrive\Desktop\AI\Registrazioni"

CARTELLA_OUTPUT = r"C:\Users\forza\OneDrive\Desktop\AI\Trascrizioni"


os.makedirs(CARTELLA_AUDIO, exist_ok=True)
os.makedirs(CARTELLA_OUTPUT, exist_ok=True)



# ===========================
# SCELTA MODELLO
# ===========================

modelli_disponibili = [
    "tiny",
    "base",
    "small",
    "medium",
    "large-v3"
]


print("\nModelli disponibili:")
print("--------------------")

for i, modello in enumerate(modelli_disponibili, start=1):
    print(f"{i}) {modello}")


scelta = input("\nScegli modello (numero): ").strip()


try:
    modello = modelli_disponibili[int(scelta)-1]

except:
    print("Scelta non valida. Uso medium.")
    modello = "medium"



print(f"\nModello selezionato: {modello}")



# ===========================
# INPUT FILE
# ===========================

nome_audio = input(
    "\nNome del file audio/video (es. lezione.m4a): "
).strip()


nome_output = input(
    "Nome del file di trascrizione (senza .txt): "
).strip()


if nome_output == "":
    nome_output = "Trascrizione"



percorso_audio = os.path.join(
    CARTELLA_AUDIO,
    nome_audio
)


percorso_output = os.path.join(
    CARTELLA_OUTPUT,
    nome_output + ".txt"
)



# ===========================
# CONTROLLO FILE
# ===========================

if not os.path.exists(percorso_audio):

    print("\nERRORE: file non trovato!")
    print(percorso_audio)
    exit()



# ===========================
# DURATA FILE
# ===========================

try:

    durata = float(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                percorso_audio
            ],
            text=True
        ).strip()
    )


except:

    print("\nErrore lettura durata file.")
    print("Controlla FFmpeg.")
    exit()



# ===========================
# CARICAMENTO WHISPER
# ===========================

print("\nCaricamento modello Whisper...\n")


model = WhisperModel(
    modello,
    device="cuda",
    compute_type="float16"
)



# ===========================
# TRASCRIZIONE
# ===========================

print("Trascrizione iniziata...\n")


segments, info = model.transcribe(

    percorso_audio,

    beam_size=5,

    vad_filter=True,

    condition_on_previous_text=True,

    word_timestamps=False,

    temperature=0.0,

    initial_prompt=(
        "Questa è una lezione universitaria in italiano. "
        "Mantieni una punteggiatura corretta."
    )
)



# ===========================
# SCRITTURA TXT
# ===========================

with open(
    percorso_output,
    "w",
    encoding="utf-8"
) as file:


    file.write("="*70 + "\n")
    file.write("TRASCRIZIONE AUDIO\n")
    file.write("="*70 + "\n\n")


    file.write(f"Modello usato: {modello}\n")
    file.write(f"File originale: {nome_audio}\n")
    file.write(f"Lingua: {info.language}\n")
    file.write(
        f"Probabilità lingua: "
        f"{info.language_probability:.2f}\n\n"
    )


    barra = tqdm(
        total=durata,
        unit="sec",
        desc="Trascrizione",
        ncols=100
    )


    ultimo = 0


    for segment in segments:


        barra.update(
            segment.end - ultimo
        )

        ultimo = segment.end


        testo = segment.text.strip()


        start = int(segment.start)
        end = int(segment.end)


        timestamp = (
            f"[{start//3600:02}:"
            f"{(start%3600)//60:02}:"
            f"{start%60:02}"
            f" - "
            f"{end//3600:02}:"
            f"{(end%3600)//60:02}:"
            f"{end%60:02}]"
        )


        print(timestamp)
        print(testo)
        print()


        file.write(timestamp + "\n")
        file.write(testo + "\n\n")


    barra.close()



# ===========================
# FINE
# ===========================

print("\n" + "="*70)
print("TRASCRIZIONE COMPLETATA!")
print("="*70)

print("\nSalvato in:")
print(percorso_output)