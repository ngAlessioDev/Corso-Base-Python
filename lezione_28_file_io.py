# ==========================================================
# TUTORIAL PYTHON: LETTURA E SCRITTURA FILE (file_io.py)
# ==========================================================

# La gestione dei file (I/O - Input/Output) consente di rendere persistenti
# i dati elaborati da un programma salvandoli su disco, o di leggere informazioni
# da sorgenti esterne (file di testo, log, dati binari, ecc.).


# --- 1. MODALITÀ DI APERTURA DEI FILE (MODES) ---

# Le modalità principali di apertura della funzione `open(file, mode)` sono:
# - 'r' (Read)   : Lettura (default). Genera errore FileNotFoundError se il file non esiste.
# - 'w' (Write)  : Scrittura. Crea un nuovo file o sovrascrive completamente un file esistente!
# - 'a' (Append) : Aggiunta. Scrive dati alla fine del file senza cancellare il contenuto preesistente.
# - 'x' (Create) : Creazione esclusiva. Fallisce se il file esiste già.
# - 'b' (Binary) : Modalità binaria (es. 'rb' o 'wb', per immagini, audio, PDF, ecc.).
# - '+' (Update) : Modalità di aggiornamento (es. 'r+' consente sia lettura che scrittura).


# --- 2. IL CONTESTO `with` (CONTEXT MANAGER) ---

# È PESSIMA PRATICA aprire i file manualmente con `f = open()` e ricordarsi di usare `f.close()`.
# Se si verifica un errore durante l'esecuzione, il file potrebbe rimanere aperto bloccando risorse!
#
# L'approccio moderno e sicuro è l'uso del blocco `with open(...) as file:`
# Garantisce la CHIUSURA AUTOMATICA del file al termine del blocco, anche in caso di eccezioni.


# --- 3. SCRITTURA DI FILE DI TESTO ('w' e 'a') ---

print("--- 1. Scrittura e Aggiunta Dati ---")

# A) Scrittura da zero o sovrascrittura ('w')
# È sempre consigliato specificare l'encoding (es. encoding='utf-8') per evitare problemi con accenti/simboli.
with open("esempio.txt", "w", encoding="utf-8") as file:
    file.write("Riga 1: Benvenuto nel tutorial I/O di Python.\n")
    file.write("Riga 2: Stiamo scrivendo del testo nel file.\n")

print("File 'esempio.txt' creato e scritto con successo.")

# B) Aggiunta di testo in coda ('a')
with open("esempio.txt", "a", encoding="utf-8") as file:
    file.write("Riga 3: Questa riga è stata aggiunta in seguito.\n")

# C) Scrittura di righe multiple da una lista con .writelines()
righe_extra = ["Riga 4: Elemento A\n", "Riga 5: Elemento B\n"]
with open("esempio.txt", "a", encoding="utf-8") as file:
    file.writelines(righe_extra)


# --- 4. LETTURA DI FILE DI TESTO ('r') ---

print("\n--- 2. Tecniche di Lettura ---")

# Metodo 1: Iterazione diretta riga per riga (Migliore per file di GRANDI DIMENSIONI - Memoria efficiente)
print("-> Lettura riga per riga tramite ciclo for:")
with open("esempio.txt", "r", encoding="utf-8") as file:
    for numero_riga, contenuto in enumerate(file, start=1):
        # .strip() rimuove gli spazi e i caratteri di a capo (\n) in eccesso
        print(f"Linea {numero_riga}: {contenuto.strip()}")

# Metodo 2: .read() -> Legge l'INTERO contenuto in una singola stringa
with open("esempio.txt", "r", encoding="utf-8") as file:
    tutto_il_testo = file.read()
    print(f"\n-> Contenuto completo (lunghezza {len(tutto_il_testo)} caratteri):")

# Metodo 3: .readlines() -> Legge tutte le righe e le restituisce sotto forma di LISTA di stringhe
with open("esempio.txt", "r", encoding="utf-8") as file:
    lista_righe = file.readlines()
    print(f"-> Numero totale di righe lette con readlines(): {len(lista_righe)}")


# --- 5. GESTIONE SICURA DEI PERCORSI CON PATHLIB ---

# Usare stringhe semplici per i percorsi (es. "cartella/file.txt") può causare errori su Windows 
# a causa dei backslash (\). Il modulo standard `pathlib` gestisce i percorsi in modo multipiattaforma.

from pathlib import Path

# Creazione di un oggetto Path relativo alla cartella di lavoro
percorso_file = Path("cartella_dati") / "mio_file.txt"

# Creare una cartella se non esiste
percorso_file.parent.mkdir(parents=True, exist_ok=True)

# Scrittura e lettura rapida tramite Path (Senza dover gestire il blocco with!)
percorso_file.write_text("Testo scritto direttamente tramite pathlib!", encoding="utf-8")
contenuto_letto = percorso_file.read_text(encoding="utf-8")

print("\n--- 3. Uso di Pathlib ---")
print("File creato in:", percorso_file.resolve())
print("Contenuto letto:", contenuto_letto)

# Verifiche utili con pathlib
print("Il file esiste?", percorso_file.exists())
print("È un file?", percorso_file.is_file())


# --- 6. PULIZIA E RIMOZIONE FILE ---

# Per eliminare file o directory possiamo usare pathlib o il modulo os/shutil.
if percorso_file.exists():
    percorso_file.unlink()  # Rimuove il file
    print("\nFile di test eliminato pulitamente.")

# Rimuovere la cartella temporanea (se vuota)
if percorso_file.parent.exists():
    percorso_file.parent.rmdir()