# ==========================================================
# TUTORIAL PYTHON: LE TUPLE (tuple.py)
# ==========================================================

# Una tupla in Python è una collezione di elementi **ordinata**, **IMMUTABILE** 
# e che **consente valori duplicati**.
#
# La caratteristica fondamentale che distingue una tupla da una lista è l'immutabilità:
# una volta creata, una tupla non può più essere modificata (non si possono aggiungere,
# rimuovere o sostituire elementi).


# --- 1. CREAZIONE E ACCESSO AGLI ELEMENTI ---

# Si creano racchiudendo gli elementi tra parentesi tonde ( ) separati da virgole.
coordinate = (45.4642, 9.1900)  # Es. Latitudine e Longitudine di Milano
colori_rgb = ("rosso", "verde", "blu", "rosso")  # Ammettono valori duplicati

# Accesso tramite indice (partono da 0 come nelle liste)
print("Latitudine:", coordinate[0])
print("Ultimo colore:", colori_rgb[-1])  # Indice negativo parte dal fondo

# Slicing (estrazione di una sottotupla: [inizio:fine])
primi_due_colori = colori_rgb[0:2]
print("Sottotupla:", primi_due_colori)

# ATTENZIONE: Se vuoi creare una tupla con UN SOLO elemento, DEVI mettere una virgola finale!
tupla_singola = ("Python",)  # Corretto -> tipo <class 'tuple'>
non_una_tupla = ("Python")   # ERRORE -> Python la considera una semplice stringa <class 'str'>


# --- 2. IMMUTABILITÀ E SICUREZZA DEI DATI ---

# Le tuple non possono essere modificate direttamente.

punto = (10, 20)

# Tentare di modificare un elemento genererà un TypeError (decommenta per verificare):
# punto[0] = 15  # TypeError: 'tuple' object does not support item assignment

# VANTAGGI DELL'IMMUTABILITÀ:
# 1. Sicurezza: Protegge i dati sensibili o le configurazioni da modifiche accidentali.
# 2. Prestazioni: Le tuple sono leggermente più veloci ed efficienti in memoria rispetto alle liste.
# 3. Possono essere usate come chiavi nei dizionari (a differenza delle liste).


# --- 3. OPERAZIONI E METODI DELLE TUPLE ---

# Poiché le tuple non possono cambiare, hanno solo DUE metodi integrati:

valori = (1, 2, 3, 2, 4, 2, 5)

# 1. count(valore): conta quante volte un elemento appare nella tupla
conteggio_due = valori.count(2)
print("Il numero 2 appare:", conteggio_due, "volte")  # Output: 3

# 2. index(valore): restituisce la posizione (indice) della PRIMA occorrenza di un valore
posizione_quattro = valori.index(4)
print("Il numero 4 si trova all'indice:", posizione_quattro)  # Output: 4

# CONCATENAZIONE E RIPETIZIONE:
# È possibile unire due tuple per crearne una nuova (senza modificare quelle originali)
t1 = (1, 2)
t2 = (3, 4)
t_unita = t1 + t2
print("Tupla concatenata:", t_unita)  # (1, 2, 3, 4)


# --- 4. PACKING E UNPACKING (DISIMBALLAGGIO) ---

# PACKING: Assegnare più valori a una tupla senza parentesi (Python crea la tupla automaticamente)
persona = "Marco", 28, "Ingegnere"  # Equivale a ("Marco", 28, "Ingegnere")

# UNPACKING: Estrarre i valori della tupla direttamente in variabili separate
nome, eta, professione = persona

print(f"Nome: {nome}, Età: {eta}, Professione: {professione}")

# Unpacking avanzato con l'operatore asterisco (*):
numeri = (10, 20, 30, 40, 50)
primo, *centrali, ultimo = numeri

print("Primo:", primo)        # 10
print("Centrali:", centrali)  # [20, 30, 40] (raccolti in una lista)
print("Ultimo:", ultimo)      # 50


# --- 5. COME "MODIFICARE" UNA TUPLA (TRUCCO DEL CASTING) ---

# Se hai la necessità assoluta di modificare una tupla, devi convertirla in una lista,
# apportare le modifiche desiderate e riconvertirla in tupla.

citta_tupla = ("Roma", "Milano", "Napoli")

# 1. Converti in lista
citta_lista = list(citta_tupla)

# 2. Modifica la lista
citta_lista.append("Torino")

# 3. Riconverti in tupla
citta_tupla = tuple(citta_lista)

print("Tupla 'aggiornata':", citta_tupla)