# ==========================================================
# TUTORIAL PYTHON: LE LISTE (liste.py)
# ==========================================================

# Una lista in Python è una collezione di elementi **ordinata**, **modificabile** (mutabile)
# e che **consente valori duplicati**.
#
# Le liste sono estremamente flessibili: possono contenere tipi di dati differenti 
# (interi, stringhe, booleani, o persino altre liste) nella stessa collezione.


# --- 1. CREAZIONE E ACCESSO AGLI ELEMENTI ---

# Si creano racchiudendo gli elementi tra parentesi quadre [ ] separati da virgole.
frutti = ["mela", "banana", "ciliegia", "kiwi", "mela"]  # I duplicati sono ammessi

# Accesso tramite indice (gli indici partono SEMPRE da 0)
print("Primo elemento (indice 0):", frutti[0])      # "mela"
print("Ultimo elemento (indice -1):", frutti[-1])   # "mela" (indice negativo parte dal fondo)

# Slicing (estrazione di una sottolista: [inizio:fine:passo])
# Ricorda: l'indice 'inizio' è incluso, 'fine' è escluso!
primi_due = frutti[0:2]   # ["mela", "banana"]
sottolista = frutti[1:4]  # ["banana", "ciliegia", "kiwi"]


# --- 2. MODIFICA ED ELEMENTI MUTABILI ---

# A differenza delle stringhe o delle tuple, le liste sono MUTABILI:
# puoi modificare i singoli elementi direttamente tramite il loro indice.

linguaggi = ["Python", "Java", "C++"]
linguaggi[1] = "JavaScript"  # Sostituisce "Java" con "JavaScript"
print("Lista modificata:", linguaggi)


# --- 3. AGGIUNGERE E RIMUOVERE ELEMENTI (METODI PRINCIPALI) ---

numeri = [10, 20, 30]

# AGGIUNGERE:
numeri.append(40)        # Aggiunge un elemento in FONDO alla lista
numeri.insert(1, 15)     # Inserisce l'elemento 15 all'indice 1 (sposta gli altri a destra)
numeri.extend([50, 60])  # Unisce un'altra lista in coda

print("Dopo inserimenti:", numeri)  # [10, 15, 20, 30, 40, 50, 60]

# RIMUOVERE:
numeri.remove(15)        # Rimuove la PRIMA occorrenza del valore 15
elemento_estratto = numeri.pop(2)  # Rimuove e restituisce l'elemento all'indice 2 (es. 30)
del numeri[0]            # Rimuove l'elemento all'indice 0 usando l'istruzione 'del'

print(f"Estratto con pop: {elemento_estratto} | Lista rimasta: {numeri}")

# Svuotare completamente la lista:
# numeri.clear()


# --- 4. ORDINAMENTO E RICERCA ---

lettere = ["d", "a", "c", "b"]

# Verifica presenza (operatore 'in')
if "a" in lettere:
    print("La lettera 'a' è presente nella lista.")

# Trovare la posizione (indice) di un elemento
posizione = lettere.index("c")
print("Indice di 'c':", posizione) # Output: 2

# Ordinare la lista (modifica la lista originale)
lettere.sort()
print("Ordinata in modo crescente:", lettere)  # ['a', 'b', 'c', 'd']

lettere.sort(reverse=True)
print("Ordinata in modo decrescente:", lettere) # ['d', 'c', 'b', 'a']

# Invertire l'ordine degli elementi senza ordinare
lettere.reverse()


# --- 5. LIST COMPREHENSION (SINTASSI CONCISA) ---

# La "List Comprehension" è una caratteristica potente e molto usata in Python 
# per creare nuove liste a partire da sequenze esistenti in un'unica riga di codice.
# Sintassi: [espressione FOR elemento IN sequenza IF condizione]

quadrati = [x ** 2 for x in range(1, 6)]
print("Quadrati da 1 a 5:", quadrati)  # Output: [1, 4, 9, 16, 25]

# Esempio con filtro IF (seleziona solo i numeri pari):
pari = [n for n in range(10) if n % 2 == 0]
print("Numeri pari sotto il 10:", pari) # Output: [0, 2, 4, 6, 8]


# --- 6. COPIA DI UNA LISTA (ATTENZIONE AI RIFERIMENTI!) ---

# Assegnare semplicemente a = b NON crea una nuova lista, ma solo un riferimento allo stesso oggetto!
lista_originale = [1, 2, 3]
lista_riferimento = lista_originale  # Condividono la stessa memoria!

# Per creare una copia INDIPENDENTE usa il metodo .copy() o lo slicing [:]:
lista_copia = lista_originale.copy()

lista_originale.append(99)

print("Originale:", lista_originale)   # [1, 2, 3, 99]
print("Riferimento:", lista_riferimento) # [1, 2, 3, 99] (si è modificata anche questa!)
print("Copia vera:", lista_copia)       # [1, 2, 3] (rimasta intatta)