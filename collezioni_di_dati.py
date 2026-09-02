# ==========================================================
# TUTORIAL PYTHON: COLLEZIONI DI DATI (collezioni_di_dati.py)
# ==========================================================

# In Python esistono quattro strutture dati fondamentali (built-in) per memorizzare 
# gruppi o collezioni di dati in un'unica variabile:
#
# 1. LISTE (List): Ordinate, Modificabili, Permettono duplicati.
# 2. TUPLE (Tuple): Ordinate, IMMUTABILI, Permettono duplicati.
# 3. SET / INSIEMI (Set): NON ordinate, Modificabili, NON permettono duplicati.
# 4. DIZIONARI (Dictionary): Ordinati*, Modificabili, Chiave-Valore (Chiavi uniche).
#
# (*Nota: I dizionari mantengono l'ordine di inserimento a partire da Python 3.7+)


# --- 1. LISTE (LIST) ---

# Le liste si creano con le parentesi quadre [ ]. 
# Sono la struttura dati più flessibile e utilizzata in Python.

frutti = ["mela", "banana", "ciliegia", "mela"] # Permette duplicati

# Accesso agli elementi tramite indice (partono da 0)
print("Primo frutto:", frutti[0])

# Modifica di un elemento (sono mutabili)
frutti[1] = "kiwi"

# Aggiunta e rimozione di elementi
frutti.append("arancia") # Aggiunge in fondo
frutti.remove("mela")   # Rimuove la prima occorrenza di "mela"

print(f"Lista aggiornata: {frutti} | Lunghezza: {len(frutti)}")


# --- 2. TUPLE (TUPLE) ---

# Le tuple si creano con le parentesi tonde ( ).
# Sono simili alle liste, ma con una differenza fondamentale: sono IMMUTABILI!
# Una volta creata una tupla, non puoi aggiungere, rimuovere o modificare i suoi elementi.

coordinate = (45.4642, 9.1900) # Es. Latitudine e Longitudine di Milano

# Accesso agli elementi tramite indice
print(f"Latitudine: {coordinate[0]}")

# Tentare di modificare una tupla genererebbe un TypeError:
# coordinate[0] = 50.0  -> ERRORE!

# Vantaggio: Le tuple sono più veloci delle liste e proteggono i dati da modifiche accidentali.


# --- 3. SET / INSIEMI (SET) ---

# I set si creano con le parentesi graffe { } contenenti elementi singoli.
# Caratteristiche principali: NON hanno un ordine e ELIMINANO automaticamente i duplicati!

colori = {"rosso", "verde", "blu", "rosso", "verde"}

print("Set di colori (i duplicati vengono ignorati):", colori)

# Aggiunta e rimozione elementi
colori.add("giallo")
colori.discard("blu")

# Operazioni matematiche sugli insiemi (Unione, Intersezione)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
intersezione = set_a & set_b # Elementi comuni
print("Intersezione set:", intersezione) # Output: {3}


# --- 4. DIZIONARI (DICTIONARY) ---

# I dizionari si creano con le parentesi graffe { } e memorizzano coppie chiave: valore.
# Invece di accedere agli elementi tramite indice numerico, si usa il nome della CHIAVE.

studente = {
    "nome": "Marco",
    "cognome": "Rossi",
    "eta": 22,
    "corsi": ["Python", "SQL"] # I valori possono essere qualsiasi tipo di dato!
}

# Accesso ai valori tramite chiave
print("Nome studente:", studente["nome"])

# Uso del metodo .get() (sicuro: non genera errore se la chiave non esiste)
print("Città:", studente.get("citta", "Non specificata"))

# Aggiunta/Modifica di coppie chiave-valore
studente["eta"] = 23              # Modifica
studente["citta"] = "Torino"      # Aggiunta nuova chiave

# Iterazione su un dizionario
print("\n--- Iterazione su Chiave-Valore ---")
for chiave, valore in studente.items():
    print(f"{chiave.capitalize()}: {valore}")


# --- RIASSUNTO PRATICO DELLE DIFFERENZE ---

# Usa una LISTA quando: ti serve una collezione ordinata di elementi che può cambiare nel tempo.
# Usa una TUPLA quando: i dati devono rimanere costanti e protetti per tutta la durata del programma.
# Usa un SET quando: vuoi garantire che tutti gli elementi siano unici o devi fare confronti tra insiemi.
# Usa un DIZIONARIO quando: devi associare etichette/chiavi ai tuoi dati per recuperarli facilmente.