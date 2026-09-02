# ==========================================================
# TUTORIAL PYTHON: I DIZIONARI (dizionari.py)
# ==========================================================

# Un Dizionario (dict) in Python è una collezione di elementi **ordinata** (da Python 3.7+),
# **modificabile** e basata su coppie **chiave: valore**.
#
# A differenza di liste e tuple, i valori nei dizionari non si recuperano tramite un indice numerico,
# ma mediante una CHIAVE univoca (etichetta).


# --- 1. CREAZIONE E ACCESSO AI VALORI ---

# Si creano usando le parentesi graffe { } con la sintassi `chiave: valore`.
studente = {
    "nome": "Marco",
    "cognome": "Rossi",
    "eta": 22,
    "materia": "Python",
    "promosso": True
}

# Accesso diretto tramite la CHIAVE racchiusa tra parentesi quadre:
print("Nome dello studente:", studente["nome"])

# ATTENZIONE: Cercare una chiave inesistente con le parentesi quadre genera un KeyError!
# print(studente["media_voti"])  -> KeyError!

# ACCESSO SICURO tramite il metodo .get():
# Se la chiave non esiste, restituisce None (oppure un valore di default specificato) senza bloccare il programma.
voto = studente.get("voto_finale", "Dato non presente")
print("Voto finale:", voto)  # Output: Dato non presente


# --- 2. MODIFICA, AGGIUNTA E RIMOZIONE ---

# I dizionari sono MUTABILI: puoi aggiornare i valori esistenti o aggiungere nuove coppie chiave-valore.

# AGGIORNARE un valore esistente:
studente["eta"] = 23

# AGGIUNGERE una nuova coppia chiave-valore:
studente["citta"] = "Torino"

print("\nDizionario aggiornato:")
print(studente)

# RIMUOVERE elementi:
# 1. .pop("chiave"): rimuove la chiave e restituisce il suo valore
citta_rimossa = studente.pop("citta")
print(f"Rimosso: {citta_rimossa}")

# 2. del: rimuove la coppia direttamente
del studente["promosso"]

# 3. .popitem(): rimuove l'ULTIMA coppia inserita nel dizionario
# 4. .clear(): svuota completamente il dizionario


# --- 3. METODI PRINCIPALI ED ITERAZIONE ---

# I dizionari offrono metodi dedicati per accedere a chiavi, valori o coppie complete.

auto = {
    "marca": "Alfa Romeo",
    "modello": "Giulia",
    "anno": 2021
}

# 1. .keys() -> Restituisce una vista di tutte le CHIAVI
print("\nChiavi del dizionario:", auto.keys())

# 2. .values() -> Restituisce una vista di tutti i VALORI
print("Valori del dizionario:", auto.values())

# 3. .items() -> Restituisce una vista di tutte le COPPIE (chiave, valore) sotto forma di tuple
print("Coppie (items):", auto.items())

# ITERAZIONE CON IL CICLO FOR:

print("\n--- Iterazione sulle sole chiavi ---")
for chiave in auto:
    print(chiave)

print("\n--- Iterazione su chiavi e valori insieme (Uso raccomandato) ---")
for chiave, valore in auto.items():
    print(f"{chiave.capitalize()}: {valore}")


# --- 4. DIZIONARI ANNIDATI (NESTED DICTIONARIES) ---

# Un dizionario può contenere altri dizionari, liste o qualsiasi altro tipo di dato.

classe = {
    "studente_1": {"nome": "Anna", "voto": 28},
    "studente_2": {"nome": "Luca", "voto": 30}
}

# Accesso ai dati nei dizionari annidati (si concatenano le chiavi tra parentesi quadre):
voto_luca = classe["studente_2"]["voto"]
print(f"\nVoto di Luca: {voto_luca}")


# --- 5. DICTIONARY COMPREHENSION ---

# Analogamente alle liste, è possibile creare dizionari in modo sintetico con la comprehension.
# Sintassi: {chiave: valore FOR elemento IN sequenza}

quadrati_diz = {x: x ** 2 for x in range(1, 6)}
print("\nDizionario dei quadrati (1-5):", quadrati_diz)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}