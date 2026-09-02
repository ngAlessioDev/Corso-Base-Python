# ==========================================================
# TUTORIAL PYTHON: LAVORO CON LE STRINGHE (lavoro_con_stringhe.py)
# ==========================================================

# In Python le stringhe sono sequenze INMUTABILI di caratteri. 
# "Immutabili" significa che una volta creata una stringa, i singoli caratteri 
# che la compongono non possono essere modificati direttamente.


# --- 1. INDICIZZAZIONE (INDEXING) ---

# Ogni carattere all'interno di una stringa ha una posizione precisa chiamata "indice".
# Gli indici partono SEMPRE da 0 per il primo carattere.

testo = "Python"

#  P   y   t   h   o   n
#  0   1   2   3   4   5  <- Indici positivi
# -6  -5  -4  -3  -2  -1  <- Indici negativi (partono dal fondo)

primo_carattere = testo[0]      # "P"
terzo_carattere = testo[2]      # "t"
ultimo_carattere = testo[-1]    # "n" (modo pratico per prendere l'ultimo elemento)

print("Primo e ultimo:", primo_carattere, ultimo_carattere)


# --- 2. TAGLIO DELLE STRINGHE (SLICING) ---

# È possibile estrarre una porzione (sottostringa) usando la sintassi: stringa[inizio:fine:passo]
# IMPORTANTE: l'indice di 'inizio' è INCLUSO, mentre l'indice di 'fine' è ESCLUSO!

frase = "Programmazione Python"

# Estrae dal carattere 0 al carattere 12 (il 13 è escluso)
sub1 = frase[0:13]       # "Programmazione"

# Se ometti 'inizio', Python parte dal principio (indice 0)
sub2 = frase[:13]        # "Programmazione"

# Se ometti 'fine', Python va fino alla fine della stringa
sub3 = frase[15:]        # "Python"

# Invertire una stringa usando un passo negativo (-1)
stringa_invertita = testo[::-1] # "nohtyP"

print("Slicing:", sub1, "|", sub3)


# --- 3. CONCATENAZIONE E RIPETIZIONE ---

# Si usano gli operatori matematici + e * tra stringhe:

nome = "Mario"
cognome = "Rossi"

# Concatenazione con + (unisce le stringhe)
nome_completo = nome + " " + cognome
print(nome_completo)     # Output: Mario Rossi

# Ripetizione con * (ripete la stringa N volte)
eco = "Ciao! " * 3
print(eco)               # Output: Ciao! Ciao! Ciao! 


# --- 4. FORMATTAZIONE DELLE STRINGHE (f-strings) ---

# A partire da Python 3.6, il modo migliore, più leggibile ed efficiente per inserire 
# variabili all'interno di una stringa è usare le f-strings.
# Si mette la lettera 'f' prima delle virgolette e si usano le parentesi graffe {} per le variabili.

eta = 30
citta = "Roma"

# Senza f-string dovremmo fare il casting: "Mi chiamo " + nome + " e ho " + str(eta) + " anni"
# Con le f-string è molto più pulito:
messaggio = f"Mi chiamo {nome}, ho {eta} anni e vivo a {citta}."
print(messaggio)


# --- 5. METODI PRINCIPALI DELLE STRINGHE ---

# Python mette a disposizione molti metodi integrati per manipolare il testo.
# Ricorda: i metodi NON modificano la stringa originale, ma ne restituiscono una NUOVA!

s = "  Benvenuti nel Corso Python!  "

# Lunghezza della stringa (funzione len)
print("Lunghezza:", len(s)) # Conta tutti i caratteri, inclusi gli spazi

# Conversione maiuscole/minuscole
print(s.upper())      # Tutto in MAIUSCOLO
print(s.lower())      # Tutto in minuscolo
print(s.title())      # Prima Lettera Di Ogni Parola Maiuscola

# Rimuovere gli spazi vuoti agli estremi
print(s.strip())      # Rimuove spazi a inizio e fine stringa

# Sostituzione di testo
nuovo_testo = s.replace("Python", "Avanzato")
print(nuovo_testo)

# Divisione di una stringa in una lista di parole (split)
parole = "pane,latte,uova,farina".split(",")
print(parole)         # Output: ['pane', 'latte', 'uova', 'farina']


# --- 6. VERIFICA E RICERCA NELLE STRINGHE ---

# Verificare se una sottostringa è presente (operatore 'in')
frase_test = "Studiare Python è divertente"

print("Python" in frase_test)   # Output: True
print("Java" in frase_test)     # Output: False

# Trovare la posizione di una parola (restituisce l'indice di inizio)
posizione = frase_test.find("Python")
print("Posizione della parola Python:", posizione) # Output: 9