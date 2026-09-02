# ===============================================
# TUTORIAL PYTHON: I BOOLEANI (booleani.py)
# ===============================================

# In Python, i booleani (tipo di dato 'bool') rappresentano uno dei due possibili valori di verità:
# True (Vero) oppure False (Falso).
# 
# ATTENZIONE: Python è case-sensitive! Si scrivono obbligatoriamente con la prima lettera MAIUSCOLA.
# True e False senza maiuscola o tra virgolette ("True") NON sono booleani (verrebbero visti come variabili o stringhe).

is_online = True
has_errors = False

print(type(is_online))  # Output: <class 'bool'>


# --- 1. OPERATORI DI CONFRONTO ---

# Molto spesso i valori booleani non si scrivono direttamente a mano, ma nascono come
# risultato di un confronto o di una verifica matematica tra due valori:

x = 10
y = 5

# Uguale a (==) -> Nota: si usano DUE segni uguale per confrontare! (Un solo = assegna)
print(x == y)  # False

# Diverso da (!=)
print(x != y)  # True

# Maggiore di (>) e Minore di (<)
print(x > y)   # True
print(x < y)   # False

# Maggiore o uguale a (>=) e Minore o uguale a (<=)
print(x >= 10) # True
print(y <= 2)  # False


# --- 2. OPERATORI LOGICI (and, or, not) ---

# Servono per combinare insieme più condizioni booleane in una singola espressione.

eta = 20
ha_patente = True

# AND: restituisce True SOLO SE TUTTE le condizioni sono vere
puo_guidare = (eta >= 18) and ha_patente
print("Può guidare?", puo_guidare)  # True

# OR: restituisce True SE ALMENO UNA delle condizioni è vera
is_weekend = False
is_festivo = True
si_riposa = is_weekend or is_festivo
print("Si riposa?", si_riposa)      # True

# NOT: inverte il valore booleano (True diventa False, False diventa True)
is_bloccato = False
print("È sbloccato?", not is_bloccato) # True


# --- 3. VALORI TRUTHY E FALSY (VALUTAZIONE LOGICA) ---

# In Python, qualsiasi valore o oggetto può essere valutato in un contesto booleano
# attraverso la funzione bool().

# La maggior parte dei valori viene valutata come TRUE (detti valori "Truthy").
# Esistono pochissimi valori specifici che vengono valutati come FALSE (detti valori "Falsy"):

# I VALORI FALSY PRINCIPALI SONO:
# - Il numero 0 e 0.0
# - Le stringhe vuote ""
# - La costante speciale None (che rappresenta l'assenza di un valore)
# - Le collezioni vuote: liste [], tuple (), dizionari {}, set ()

print("0 è booleano:", bool(0))         # False
print("Stringa vuota:", bool(""))       # False
print("None è booleano:", bool(None))   # False

# QUALSIASI ALTRO VALORE È TRUTHY:
print("Numero diverso da 0:", bool(42)) # True
print("Stringa non vuota:", bool("ok")) # True


# --- 4. I BOOLEANI E LE CONDIZIONI ---

# I booleani sono il motore fondamentale che permette al programma di prendere decisioni
# tramite l'istruzione 'if' (che approfondiremo nella lezione dedicata al flusso di controllo).

utente_autenticato = True

if utente_autenticato:
    print("Benvenuto nella tua area riservata!")
else:
    print("Accesso negato. Effettua il login.")