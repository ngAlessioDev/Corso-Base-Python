# ===============================================
# TUTORIAL PYTHON: IL CASTING (casting.py)
# ===============================================

# Il "casting" è l'operazione che permette di convertire una variabile o un valore 
# da un tipo di dato a un altro (ad esempio da stringa a numero intero, o da intero a float).

# In Python esistono due tipi di conversione:
# 1. Conversione Implicita (gestita automaticamente da Python)
# 2. Conversione Esplicita o "Casting" (forzata dal programmatore tramite funzioni dedicate)


# --- 1. CONVERSIONE IMPLICITA ---

# Python converte automaticamente i tipi di dati quando non c'è perdita di informazioni,
# ad esempio durante le operazioni matematiche tra int e float:

a = 10      # tipo int
b = 2.5     # tipo float

risultato = a + b

# Python converte automaticamente 'a' in float per eseguire la somma senza perdere i decimali:
print(risultato)        # Output: 12.5
print(type(risultato))  # Output: <class 'float'>


# --- 2. CONVERSIONE ESPLICITA (FUNZIONI DI CASTING) ---

# Quando dobbiamo forzare la conversione tra tipi diversi, usiamo le funzioni trasformatrici built-in:
# - int()   -> Converte in numero intero
# - float() -> Converte in numero decimale
# - str()   -> Converte in stringa (testo)
# - bool()  -> Converte in valore booleano (True/False)


# --- CASTING A INTERO: int() ---

# Converte stringhe numeriche o numeri decimali in numeri interi.

# Da stringa a intero (molto utile quando si legge l'input dell'utente):
stringa_numero = "100"
numero = int(stringa_numero)
print(numero + 50)  # Output: 150 (possiamo fare operazioni matematiche!)

# Da float a intero:
# ATTENZIONE: la parte decimale viene TRONCATA (eliminata), non arrotondata!
voto = 28.9
voto_troncato = int(voto)
print(voto_troncato)  # Output: 28 (non 29!)


# --- CASTING A DECIMALE: float() ---

# Converte numeri interi o stringhe numeriche in decimali.

x = float(5)        # Diventa 5.0
y = float("3.14")   # Diventa il numero decimale 3.14

print(x, type(x))
print(y, type(y))


# --- CASTING A STRINGA: str() ---

# Converte qualsiasi tipo di dato in una stringa di testo.
# È fondamentale quando si vogliono unire (concatenare) numeri e testo insieme.

eta = 25

# L'istruzione seguente genererebbe un ERRORE di tipo (TypeError):
# messaggio = "Ho " + eta + " anni" 

# Per evitarlo, convertiamo l'intero in stringa:
messaggio = "Ho " + str(eta) + " anni"
print(messaggio)  # Output: Ho 25 anni


# --- CASTING A BOOLEANO: bool() ---

# Converte un valore in True o False basandosi sulle regole della logica Python:
# - Valori considerati Falsi (Falsy): il numero 0, 0.0, le stringhe vuote "" e il valore None.
# - Valori considerati Veri (Truthy): qualsiasi numero diverso da 0 e qualsiasi stringa non vuota.

print(bool(1))       # Output: True
print(bool(0))       # Output: False
print(bool("Ciao"))  # Output: True
print(bool(""))      # Output: False


# --- GESTIONE DEGLI ERRORI NEL CASTING ---

# Non tutti i valori possono essere convertiti!
# Se si prova a convertire una stringa che non contiene un numero valido, Python restituirà un ValueError.

# Esempio di errore (se decommentato genererà un blocco del programma):
# testo = "Python"
# numero = int(testo)  # ValueError: invalid literal for int() with base 10: 'Python'