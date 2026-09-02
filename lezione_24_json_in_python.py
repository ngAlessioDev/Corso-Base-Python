# ==========================================================
# TUTORIAL PYTHON: IL FORMATO JSON (json_in_python.py)
# ==========================================================

# JSON (JavaScript Object Notation) è un formato di scambio dati leggero, 
# basato su testo, ampiamente utilizzato per la comunicazione tra Web API,
# client-server e per i file di configurazione.
#
# Python include il modulo nativo `json` per convertire facilmente
# strutture dati Python (dizionari, liste, ecc.) in stringhe/file JSON e viceversa.


# --- 1. TABELLA DI CONVERSIONE (MAPPING DEI TIPI) ---

# Python        <--->   JSON
# dict                  Object { "key": "value" }
# list, tuple           Array [ 1, 2 ]
# str                   String "testo"
# int, float            Number 123 / 12.3
# True / False          Boolean true / false
# None                  null


import json


# --- 2. CONVERTIRE STRUTTURE PYTHON IN JSON (SERIALIZZAZIONE) ---

# "Serializzare" (o fare il Marshalling) significa trasformare un oggetto Python 
# in una stringa o file JSON. Si usano le funzioni con la 's' finale (dumps/dump).

dati_utente = {
    "id": 101,
    "nome": "Marco Rossi",
    "is_admin": True,
    "competenze": ["Python", "SQL", "Git"],
    "recapito": None
}

# A) json.dumps(): converte un oggetto Python in una STRINGA JSON (dumps = Dump String)
stringa_json = json.dumps(dati_utente)

print("--- Stringa JSON compatta ---")
print(stringa_json)
# Nota: in JSON 'True' diventa 'true', 'None' diventa 'null', e le chiavi usano doppi apici!

# B) FORMATTAZIONE PULITA (INDENTAZIONE E ORDINAMENTO)
# Usando i parametri `indent` e `sort_keys` rendiamo il JSON ben leggibile (Pretty Print).

stringa_json_formattata = json.dumps(dati_utente, indent=4, sort_keys=True)

print("\n--- Stringa JSON formattata (Pretty Print) ---")
print(stringa_json_formattata)


# --- 3. CONVERTIRE JSON IN STRUTTURE PYTHON (DESERIALIZZAZIONE) ---

# "Deserializzare" significa leggere una stringa o file JSON e ricostruire 
# il corrispondente oggetto Python (es. Dizionario). Si usano le funzioni loads/load.

json_input = '{"titolo": "Corso Python", "durata_ore": 20, "attivo": true}'

# json.loads(): converte una STRINGA JSON in un oggetto Python (loads = Load String)
dati_python = json.loads(json_input)

print("\n--- Oggetto Python deserializzato ---")
print("Tipo di dato restituito:", type(dati_python))  # <class 'dict'>
print("Titolo corso:", dati_python["titolo"])
print("Stato attivo:", dati_python["attivo"])          # Riconvertito nel booleano True


# --- 4. LETTURA E SCRITTURA DI FILE JSON ---

# Quando lavoriamo direttamente con i FILE (anziché stringhe), usiamo `dump` e `load` 
# (senza la 's' finale) passando il riferimento al file aperto.

configurazione = {
    "ambiente": "produzione",
    "porta": 8080,
    "debug": False
}

# A) json.dump(): SCRITTURA su file .json
print("\n--- Scrittura su file 'config.json' ---")
with open("config.json", "w", encoding="utf-8") as file_json:
    json.dump(configurazione, file_json, indent=4)
    print("File 'config.json' salvato con successo!")

# B) json.load(): LETTURA da file .json
print("\n--- Lettura dal file 'config.json' ---")
with open("config.json", "r", encoding="utf-8") as file_json:
    dati_letti = json.load(file_json)

print("Dati letti dal file:", dati_letti)
print("Porta di rete:", dati_letti["porta"])


# --- 5. GESTIONE DEI CARATTERI NON-ASCII (ES. ACCENTI) ---

# Di default, json.dumps() converte i caratteri speciali in codici unicode (es. \u00e0).
# Per mantenere i caratteri accentati o simboli speciali così come sono, usa `ensure_ascii=False`.

dati_ita = {"messaggio": "Caffè e città"}

json_unicode = json.dumps(dati_ita)
json_leggibile = json.dumps(dati_ita, ensure_ascii=False)

print("\n--- Gestione Caratteri Speciali ---")
print("Default (escaped):", json_unicode)    # Output: {"messaggio": "Caff\u00e8 e citt\u00e0"}
print("ensure_ascii=False:", json_leggibile) # Output: {"messaggio": "Caffè e città"}