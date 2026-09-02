# ==========================================
# TUTORIAL PYTHON: LE VARIABILI (variabili.py)
# ==========================================

# In Python una variabile è semplicemente un "contenitore" per memorizzare dei dati in memoria.
# A differenza di altri linguaggi (come C++ o Java), in Python NON serve dichiarare il tipo di variabile
# né usare parole chiave specifiche: una variabile viene creata nel momento stesso in cui le assegni un valore.

# Per assegnare un valore a una variabile si usa l'operatore di assegnazione =

nome = "Mario"      # Variabile di tipo stringa (testo)
eta = 25           # Variabile di tipo intero (numero intero)
altezza = 1.75     # Variabile di tipo float (numero decimale con il punto)
is_studente = True # Variabile di tipo boolean (valore logico: True o False)

# Possiamo stampare i valori memorizzati nelle variabili passando il loro nome alla funzione print()
print(nome)
print(eta)


# --- TIPIZZAZIONE DINAMICA E RIASSEGNAZIONE ---

# Python usa la "tipizzazione dinamica": il tipo di una variabile viene determinato automaticamente 
# in base al valore che le assegni. Inoltre, puoi cambiare il tipo di dato contenuto in una variabile in qualsiasi momento!

x = 10        # x ora è un numero intero (int)
print(x)

x = "Dieci"   # Ora x è diventata una stringa (str)!
print(x)


# --- REGOLE PER I NOMI DELLE VARIABILI ---

# Quando crei una variabile devi seguire alcune regole fondamentali della sintassi Python:

# 1. Il nome può contenere solo lettere (a-z, A-Z), cifre (0-9) e il carattere underscore (_)
# 2. Il nome deve INIZIARE obbligatoriamente con una lettera o con un underscore, MAI con un numero
# 3. I nomi delle variabili sono CASE-SENSITIVE (sensibili alle maiuscole/minuscole)

eta = 20
Eta = 30
ETA = 40
# Le tre variabili qui sopra sono TRE VARIABILI DIVERSE tra loro!
print(eta, Eta, ETA)

# Esempi di nomi VALIDOR:
# _utente = "Anna"
# nome_completo = "Luca Rossi"
# numero1 = 5

# Esempi di nomi NON VALIDI (generano errore di sintassi):
# 1numero = 5       -> Errore: non può iniziare con un numero!
# nome-utente = "A" -> Errore: il trattino '-' non è consentito (viene visto come sottrzione)
# nome utente = "A" -> Errore: non ci possono essere spazi nel nome!


# --- CONVENZIONI DI STILE (PEP 8) ---

# Per scrivere codice pulito e professionale, la guida ufficiale di Python (PEP 8) raccomanda:
# - Usare lo stile "snake_case" per le variabili: tutto in minuscolo, con parole separate da underscore (_)
# - Scegliere nomi significativi che descrivano cosa contiene la variabile (evita nomi generici come a, b, x se non necessario)

# Buon esempio di naming:
prezzo_totale = 99.90
numero_di_tentativi = 3

# Esempio sconsigliato (funziona, ma rende il codice poco leggibile):
pt = 99.90
n = 3


# --- ASSEGNAZIONE MULTIPLA ---

# Python permette di assegnare valori a più variabili contemporaneamente in un'unica riga di codice:

a, b, c = 1, 2, 3
print(a, b, c)

# Oppure puoi assegnare lo stesso valore a più variabili contemporaneamente:

x = y = z = 0
print(x, y, z)


# --- SCOPRIRE IL TIPO DI UNA VARIABILE ---

# Se vuoi verificare il tipo di dato contenuto in una variabile, puoi usare la funzione integrata type()

messaggio = "Ciao Python!"
voto = 30

print(type(messaggio)) # Output: <class 'str'> (stringa)
print(type(voto))      # Output: <class 'int'> (intero)