# ==========================================================
# TUTORIAL PYTHON: LO SCOPE E LE AMBITI DELLE VARIABILI (scope.py)
# ==========================================================

# Lo "Scope" (o ambito) definisce la visibilità e la durata di vita di una variabile
# all'interno di un programma Python.
#
# Per cercare il valore di una variabile, Python segue rigidamente la regola **LEGB**:
# 1. L - Local (Locale)
# 2. E - Enclosing (Ambito esterno/non-locale)
# 3. G - Global (Globale)
# 4. B - Built-in (Istruzioni integrate di Python)


# --- 1. LOCAL SCOPE (AMBITO LOCALE) ---

# Le variabili create all'interno di una funzione appartengono allo scope LOCALE di quella funzione.
# Esistono solo durante l'esecuzione della funzione e vengono distrutte al suo termine.

def funzione_locale():
    messaggio_locale = "Sono una variabile locale"
    print(messaggio_locale)

funzione_locale()
# print(messaggio_locale)  -> ERRORE! NameError: 'messaggio_locale' non è accessibile all'esterno.


# --- 2. GLOBAL SCOPE (AMBITO GLOBALE) ---

# Le variabili create nel corpo principale del file (fuori da qualsiasi funzione) sono GLOBALI.
# Sono accessibili da qualsiasi punto del codice, anche dall'interno delle funzioni.

variabile_globale = "Sono una variabile globale"

def leggi_globale():
    print("Dall'interno della funzione:", variabile_globale)

leggi_globale()


# --- 3. LA PAROLA CHIAVE 'global' ---

# Se provi a MODIFICARE una variabile globale dentro una funzione, Python per sicurezza
# ne crea una NUOVA locale con lo stesso nome (Variable Shadowing), senza alterare quella globale.

x = 10

def modifica_errata():
    x = 20  # Crea una nuova variabile locale 'x', NON modifica quella globale!
    print("x locale dentro la funzione:", x)

modifica_errata()
print("x globale rimane invariata:", x)  # Output: 10

# Per MODIFICARE effettivamente la variabile globale dall'interno di una funzione,
# si deve dichiarare esplicitamente con la parola chiave 'global':

def modifica_corretta():
    global x  # Dice a Python di usare la variabile globale 'x'
    x = 99

modifica_corretta()
print("x globale dopo 'global':", x)  # Output: 99


# --- 4. ENCLOSING SCOPE E LA PAROLA CHIAVE 'nonlocal' ---

# L'ambito ENCLOSING riguarda le funzioni annidate (funzioni dentro altre funzioni).
# Una funzione interna può leggere le variabili della funzione esterna.

def funzione_esterna():
    testo = "Testo esterno"

    def funzione_interna():
        # Con 'nonlocal' modifichiamo la variabile della funzione madre (esterna),
        # senza che sia una variabile globale!
        nonlocal testo
        testo = "Testo modificato dalla funzione interna"
        print("Dentro interna:", testo)

    funzione_interna()
    print("Dentro esterna dopo la chiamata:", testo)

funzione_esterna()


# --- 5. BUILT-IN SCOPE (AMBITO INTEGRATO) ---

# È il livello più esterno che contiene tutte le parole chiave, funzioni e moduli integrati di Python
# (es. print(), len(), sum(), range(), ValueError).

# ATTENZIONE: Evita di usare nomi di funzioni built-in per le tue variabili!
# Esempio di ERRORE comune (Shadowing di built-in):
# sum = 10  # Ora 'sum' è un numero, non potrai più usare la funzione sum()!


# --- 6. RIEPILOGO DELLA REGOLA L-E-G-B ---

# Quando cerchi di stampare o usare una variabile 'v', Python la cerca in quest'ordine:

variabile_demo = "GLOBALE"

def esterna_demo():
    variabile_demo = "ENCLOSING"

    def interna_demo():
        # Se decommenti la riga sotto, vince il livello LOCAL:
        # variabile_demo = "LOCALE"
        print("Valore trovato secondo la regola LEGB:", variabile_demo)

    interna_demo()

esterna_demo()  # Stampa "ENCLOSING" perché 'LOCALE' manca, ma 'ENCLOSING' esiste prima di 'GLOBALE'.