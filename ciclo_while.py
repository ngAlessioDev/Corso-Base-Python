# ==========================================================
# TUTORIAL PYTHON: IL CICLO WHILE (ciclo_while.py)
# ==========================================================

# Il ciclo 'while' (mentre) permette di ripetere un blocco di codice 
# finché una determinata condizione rimane VERA (True).
# A differenza del ciclo 'for' (usato quando si conosce a priori il numero di iterazioni),
# il ciclo 'while' si usa principalmente quando NON si sa quante volte andrà eseguito il codice.


# --- 1. SINTASSI BASE E CONTATORE ---

# Sintassi:
# while condizione:
#     istruzioni da ripetere

# IMPORTANTE: È fondamentale aggiornare la variabile di controllo all'interno del ciclo,
# altrimenti la condizione rimarrà sempre True generando un CICLO INFINITO!

contatore = 1

while contatore <= 5:
    print(f"Numero iterazione: {contatore}")
    contatore += 1  # Incremento fondamentale (equivale a contatore = contatore + 1)

print("Ciclo completato!\n")


# --- 2. VALIDAZIONE DELL'INPUT (ESEMPIO PRATICO) ---

# Uno degli usi più comuni del ciclo while è costringere l'utente 
# ad inserire un dato valido prima di proseguire con il programma.

# Esempio simula la richiesta di una password corretta:
password_corretta = "python123"
tentativo = ""

# Il ciclo continua finché il tentativo è DIVERSO dalla password corretta
# (Nota: qui usiamo un contatore simulato per scopo dimostrativo)
tentativi_rimasti = 3

while tentativi_rimasti > 0:
    # In un vero programma useresti: tentativo = input("Inserisci password: ")
    tentativo = "python123"  # Simuliamo l'inserimento corretto
    
    if tentativo == password_corretta:
        print("Accesso consentito!")
        break  # Interrompe immediatamente il ciclo
    else:
        tentativi_rimasti -= 1
        print(f"Password errata. Tentativi rimasti: {tentativi_rimasti}")


# --- 3. ISTRUZIONI BREAK E CONTINUE ---

# break: interrompe immediatamente l'esecuzione del ciclo e passa alla prima istruzione esterna.
# continue: salta il resto del codice nell'iterazione corrente e passa subito al controllo successivo.

print("\n--- Esempio con CONTINUE (stampa solo numeri dispari) ---")
numero = 0

while numero < 6:
    numero += 1
    if numero % 2 == 0:
        continue  # Se il numero è pari, salta il print e torna all'inizio del while
    print(f"Numero dispari: {numero}")


# --- 4. CICLO INFINITO E BREAK (PATTERN COMMON) ---

# Un pattern molto diffuso in Python è creare un ciclo 'while True' (infinito)
# ed uscire solo quando si verifica una specifica condizione tramite 'break'.

conteggio = 10

while True:
    print(f"Countdown: {conteggio}")
    conteggio -= 1
    
    if conteggio == 0:
        print("VIA!")
        break  # Condizione di uscita dal ciclo infinito


# --- 5. CLAUSOLA ELSE NEL WHILE ---

# Python permette di aggiungere un blocco 'else' associato al 'while'.
# Il codice dentro 'else' viene eseguito SOLO SE il ciclo termina normalmente 
# (cioè quando la condizione diventa False) e NON se viene interrotto da un 'break'.

n = 1

while n <= 3:
    print(f"Passo {n}")
    n += 1
else:
    print("Il ciclo è terminato regolarmente senza essere interrotto da un break.")