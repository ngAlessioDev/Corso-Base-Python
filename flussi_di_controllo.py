# ==========================================================
# TUTORIAL PYTHON: FLUSSI DI CONTROLLO (flussi_di_controllo.py)
# ==========================================================

# I flussi di controllo permettono al programma di prendere decisioni ed eseguire
# blocchi di codice differenti in base al verificarsi o meno di determinate condizioni.
# In Python le strutture condizionali principali sono: if, elif ed else.


# --- 1. ISTRUZIONE IF (SE) ---

# Il blocco 'if' valuta un'espressione booleana (True o False).
# Se la condizione è True, il blocco di codice indentato sotto l'if viene eseguito.

eta = 20

if eta >= 18:
    print("Sei maggiorenne.")  # Eseguito solo se eta >= 18 è True


# --- 2. ISTRUZIONE ELSE (ALTRIMENTI) ---

# Il blocco 'else' è opzionale e definisce l'azione da eseguire 
# nel caso in cui la condizione dell'if risulti False.

temperatura = 15

if temperatura >= 22:
    print("Fa caldo, puoi mettere le maniche corte.")
else:
    print("Fa fresco, meglio coprirsi.")


# --- 3. ISTRUZIONE ELIF (ALTRIMENTI SE) ---

# Quando ci sono più condizioni mutualmente esclusive da verificare in sequenza,
# si usa 'elif' (contrattione di "else if").
# Python valuta le condizioni dall'alto verso il basso e blocca l'esecuzione
# appena ne trova una VERA (True).

punteggio = 85

if punteggio >= 90:
    giudizio = "Eccellente"
elif punteggio >= 75:
    giudizio = "Buono"
elif punteggio >= 60:
    giudizio = "Sufficiente"
else:
    giudizio = "Insufficiente"

print(f"Esito valutazione: {giudizio}")


# --- 4. IF ANNIDATI (NESTED IF) ---

# È possibile inserire un blocco 'if' all'interno di un altro 'if'.
# Nota come l'indentazione aumenti di livello (4 spazi -> 8 spazi).

ha_patente = True
eta_conducente = 17

if ha_patente:
    if eta_conducente >= 18:
        print("Puoi guidare l'automobile.")
    else:
        print("Hai la patente ma non sei ancora maggiorenne!")
else:
    print("Non puoi guidare: non hai la patente.")


# --- 5. OPERATORE TERNARIO (IF IN LINEA) ---

# Python permette di scrivere un semplice controllo if/else su una sola riga.
# Sintassi: valore_se_vero IF condizione ELSE valore_se_falso

eta_utente = 16
stato = "Maggiorenne" if eta_utente >= 18 else "Minorenne"

print(f"L'utente è: {stato}")


# --- 6. APPARTENENZA NELLE CONDIZIONI (IN / NOT IN) ---

# Gli operatori 'in' e 'not in' sono molto usati nelle condizioni
# per verificare se un elemento è presente in una sequenza (es. stringa o lista).

ruolo = "admin"
ruoli_autorizzati = ["admin", "editor", "moderatore"]

if ruolo in ruoli_autorizzati:
    print("Accesso consentito al pannello di controllo.")
else:
    print("Accesso negato: permessi insufficienti.")


# --- 7. ISTRUZIONE PASS (PLACEHOLDER) ---

# In Python un blocco di codice sotto un 'if' non può essere vuoto (genererebbe un IndentationError).
# Se vuoi definire una struttura condizionale ma scriverne il codice in seguito, usa 'pass'.

servizio_attivo = False

if servizio_attivo:
    pass  # TODO: implementare la logica in seguito senza bloccare il programma
else:
    print("Servizio temporaneamente disattivato.")