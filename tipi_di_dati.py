# ==================================================
# TUTORIAL PYTHON: I TIPI DI DATI (tipi_di_dati.py)
# ==================================================

# In Python, ogni valore memorizzato in una variabile appartiene a un tipo di dato specifico.
# Il tipo di dato definisce quali operazioni possiamo o non possiamo eseguire su quel valore.

# I principali tipi di dati base (built-in) in Python si dividono in tre macro-categorie:
# 1. Tipi Numerici (int, float, complex)
# 2. Tipo Testuale (str)
# 3. Tipo Booleano (bool)
#
# (Nota: Esistono anche le collezioni di dati come liste, tuple, dizionari e set, 
#  ma verranno spiegate nei moduli dedicati più avanti).


# --- 1. TIPI NUMERICI ---

# int (Integer): numeri interi, positivi o negativi, SENZA virgola
numero_studenti = 25
temperatura_minima = -5

# float (Floating Point): numeri reali CON virgola (in Python si usa il punto .)
prezzo = 19.99
pi_greco = 3.14159

# Nota sui float: puoi usare anche la notazione scientifica con 'e' per indicare le potenze di 10
distanza_metri = 1.5e3  # Equivale a 1.5 * 10^3 = 1500.0

# complex: numeri complessi con parte reale e parte immaginaria (indicata con 'j')
numero_complesso = 3 + 5j

print("Esempi numerici:", numero_studenti, prezzo, numero_complesso)


# --- 2. TIPO TESTUALE (Stringhe - str) ---

# Le stringhe rappresentano sequenze di testo e si creano racchiudendo i caratteri
# tra virgolette doppie ("...") o virgolette singole ('...'). Non c'è differenza di funzionamento.

nome = "Alice"
cognome = 'Rossi'

# Se il testo contiene un apostrofo, è consigliabile usare le virgolette doppie all'esterno,
# oppure la barra rovesciata (\) come carattere di escape prima dell'apostrofo:
frase1 = "L'ambiente di sviluppo è pronto"
frase2 = 'L\'ambiente di sviluppo è pronto'

# Stringhe multiriga: usando tre virgolette (""" oppure ''') puoi creare testo sviluppato su più righe
# (Da non confondere con i commenti: questo è vero e proprio testo salvato nella variabile!)
testo_lungo = """Questo è un testo
che prosegue su più righe
senza generare errori di sintassi."""

print(nome, cognome)


# --- 3. TIPO BOOLEANO (bool) ---

# Il tipo booleano può assumere esclusivamente due valori: True (Vero) oppure False (Falso).
# ATTENZIONE: True e False si scrivono obbligatoriamente con la lettera iniziale MAIUSCOLA!

utente_attivo = True
pagamento_effettuato = False

# I booleani sono fondamentali in programmazione perché vengono usati per controllare
# il flusso delle decisioni nel codice (es. con le istruzioni if/else).
print("Stato utente attivo:", utente_attivo)


# --- VERIFICARE IL TIPO DI DATO ---

# Per scoprire a quale tipo appartiene un valore o una variabile, Python mette a disposizione
# la funzione integrata type()

x = 42
y = "42"
z = 42.0

print(type(x)) # Output: <class 'int'>   -> Numero intero
print(type(y)) # Output: <class 'str'>   -> Testo (stringa)
print(type(z)) # Output: <class 'float'> -> Numero con virgola