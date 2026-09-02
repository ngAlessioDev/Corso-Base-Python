# ==========================================================
# TUTORIAL PYTHON: GESTIONE DEGLI ERRORI (try_except.py)
# ==========================================================

# In Python, un errore che si verifica durante l'esecuzione del programma
# prende il nome di **Eccezione** (Exception).
#
# Se un'eccezione non viene gestita, il programma si interrompe bruscamente (crash).
# Usando i blocchi `try` ed `except`, possiamo intercettare gli errori e gestire
# la situazione in modo controllato senza far fallire il programma.


# --- 1. STRUTTURA BASE: TRY / EXCEPT ---

# Nel blocco `try` inseriamo il codice "a rischio" errore.
# Nel blocco `except` inseriamo il codice da eseguire SE si verifica un errore.

print("--- 1. Gestione Base ---")
try:
    risultato = 10 / 0  # Questo genera un ZeroDivisionError!
    print("Questa riga non verrà mai eseguita.")
except:
    print("Si è verificato un errore durante il calcolo!")

print("Il programma continua normalmente...")


# --- 2. CATTURARE ECCEZIONI SPECIFICHE ---

# È pessima pratica usare un `except` generico senza specificare il tipo di errore.
# È sempre preferibile gestire ogni tipo di eccezione in modo mirato.

print("\n--- 2. Eccezioni Specifiche ---")

try:
    # Decommenta una delle righe sotto per testare i diversi comportamenti:
    
    numero = int("abc")              # Genera ValueError
    # risultato = 10 / 0             # Genera ZeroDivisionError
    # print(variabile_inesistente)   # Genera NameError

except ZeroDivisionError:
    print("Errore: Impossibile dividere un numero per zero!")

except ValueError:
    print("Errore: Impossibile convertire la stringa in un numero intero!")

except Exception as e:
    # `Exception` è la classe base di quasi tutte le eccezioni standard.
    # Usando 'as e' possiamo stampare il messaggio di errore originale fornito da Python.
    print(f"Errore generico non previsto: {e}")


# --- 3. I BLOCCHI ELSE E FINALLY ---

# Un blocco completo di gestione errori può contenere fino a 4 parti:
# - try: codice a rischio
# - except: eseguito SOLO se c'è stato un errore
# - else: eseguito SOLO se NON c'è stato alcun errore nel try
# - finally: eseguito SEMPRE (sia in caso di successo che di errore), utilissimo per pulire risorse

print("\n--- 3. Struttura Completa (try-except-else-finally) ---")

try:
    num1 = int("20")
    num2 = int("5")
    divisione = num1 / num2

except ValueError:
    print("Errore di conversione dei dati!")

except ZeroDivisionError:
    print("Errore: Divisione per zero!")

else:
    # Viene eseguito solo se il blocco try ha successo al 100%
    print(f"Operazione riuscita! Il risultato è: {divisione}")

finally:
    # Viene eseguito in ogni caso (utile per chiudere file, connessioni a DB, ecc.)
    print("Blocco 'finally': Pulizia risorse completata.")


# --- 4. RILANCIARE ECCEZIONI CON RAISE ---

# Usiamo la parola chiave `raise` quando vogliamo creare e lanciare intenzionalmente 
# un'eccezione personalizzata se non vengono rispettate determinate condizioni.

print("\n--- 4. Lanciare Eccezioni (raise) ---")

def imposta_eta(eta):
    if eta < 0:
        # Lanciamo manualmente un ValueError con un messaggio personalizzato
        raise ValueError("L'età non può essere un numero negativo!")
    elif eta > 120:
        raise ValueError("L'età inserita non è plausibile!")
    
    print(f"Età impostata con successo: {eta}")

try:
    imposta_eta(-5)
except ValueError as err:
    print(f"Eccezione intercettata: {err}")


# --- 5. CREARE ECCEZIONI PERSONALIZZATE ---

# In progetti complessi è possibile creare tipi di eccezione su misura 
# ereditando dalla classe base `Exception`.

class CreditoInsufficienteError(Exception):
    """Eccezione lanciata quando il saldo del conto è troppo basso."""
    pass

def preleva(saldo, importo):
    if importo > saldo:
        raise CreditoInsufficienteError(f"Prelievo di {importo}€ fallito. Saldo disponibile: {saldo}€")
    return saldo - importo

try:
    nuovo_saldo = preleva(100, 250)
except CreditoInsufficienteError as e:
    print(f"\n[ERRORE BANCARIO] {e}")