# ==========================================================
# TUTORIAL PYTHON: FORMATTAZIONE AVANZATA STRINGHE (formattazione_stringhe.py)
# ==========================================================

# In Python esistono diversi modi per formattare le stringhe.
# Dai metodi storici (% e .format()) fino agli f-string (introdotti in Python 3.6+),
# la formattazione consente di inserire variabili, applicare arrotondamenti,
# allineare testi e formattare numeri, date e valori monetari con precisione.


# --- 1. PANORAMICA DEI METODI DI FORMATTAZIONE ---

nome = "Alice"
punteggio = 95.5

# A) Operatore % (Stile legacy / C-style - sconsigliato nei nuovi progetti)
legacy = "Utente: %s | Punteggio: %.1f" % (nome, punteggio)

# B) Metodo str.format() (Python 2.7+ / 3.0+)
str_format = "Utente: {} | Punteggio: {:.1f}".format(nome, punteggio)

# C) F-String (Formatted String Literals - Lo standard moderno raccomandato!)
f_string = f"Utente: {nome} | Punteggio: {punteggio:.1f}"

print("--- 1. Confronto Metodi ---")
print(f_string)


# --- 2. FORMATTAZIONE NUMERICA AVANZATA (F-STRINGS) ---

prezzo = 1234567.8910
percentuale = 0.756
numero_intero = 42

print("\n--- 2. Formattazione Numerica ---")

# Arrotondamento decimali (: .Nf)
print(f"Decimali (2 cifre): {prezzo:.2f} €")          # Output: 1234567.89 €

# Separatore delle migliaia (: , oppure : _)
print(f"Migliaia con virgola: {prezzo:,.2f}")        # Output: 1,234,567.89
print(f"Migliaia con underscore: {prezzo:_}")        # Output: 1_234_567.891

# Formattazione percentuale (: .N%) -> Moltiplica x100 e aggiunge %
print(f"Percentuale: {percentuale:.1%}")            # Output: 75.6%

# Padding / Zeri iniziali (: 0Nd) -> Riempie con zeri a sinistra fino a N cifre
print(f"ID Utente con zeri: {numero_intero:06d}")   # Output: 000042


# --- 3. ALLINEAMENTO, SPAZIATURA E RIGHELLO (TEXT ALIGNMENT) ---

testo = "PYTHON"

print("\n--- 3. Allineamento e Padding ---")

# : < N  -> Allinea a sinistra (spazi a destra)
print(f"|{testo:<15}|")

# : > N  -> Allinea a destra (spazi a sinistra)
print(f"|{testo:>15}|")

# : ^ N  -> Centra il testo
print(f"|{testo:^15}|")

# Personalizzare il carattere di riempimento (es. '=' o '*')
print(f"{testo:=^20}")                            # Output: =======PYTHON=======
print(f"{testo:*<12}")                            # Output: PYTHON******


# --- 4. TRUCCHI AVANZATI CON GLI F-STRINGS (PYTHON 3.8+) ---

a = 10
b = 25
lista = [1, 2, 3]

print("\n--- 4. Trucchi e Segnalibri Avanzati ---")

# A) Debugging veloce con l'operatore '='
# Stampa il nome della variabile/espressione E il suo valore automatico!
print(f"{a=}")                                    # Output: a=10
print(f"{a + b=}")                                # Output: a + b=35
print(f"{len(lista)=}")                           # Output: len(lista)=3

# B) Invocazione di funzioni ed espressioni direttamente negli f-string
stringa = "  hello world  "
print(f"Maiuscolo e stripped: '{stringa.strip().upper()}'")

# C) Conversione esplicita (!r per repr(), !s per str(), !a per ascii())
oggetto_testo = "Testo con \n a capo"
print(f"Rappresentazione grezza (!r): {oggetto_testo!r}")


# --- 5. FORMATTAZIONE DI DATE E TEMPI (DATETIME) ---

import datetime

ora_attuale = datetime.datetime.now()

print("\n--- 5. Formattazione Date ---")

# Uso delle direttive strftime direttamente all'interno dell'f-string
print(f"Data formattata: {ora_attuale:%d/%m/%Y}")
print(f"Ora e minuti: {ora_attuale:%H:%M:%S}")
print(f"Giorno della settimana: {ora_attuale:%A}")


# --- 6. COSTAMPAGGIO E TABELLE DINAMICHE ---

prodotti = [
    ("Laptop", 1299.99, 4),
    ("Mouse", 25.50, 15),
    ("Tastiera Meccanica", 89.00, 8)
]

print("\n--- 6. Esempio Pratico: Generazione Tabella ---")
print(f"{'PRODOTTO':<20} | {'PREZZO':>10} | {'QTA':>5} | {'TOTALE':>10}")
print("-" * 53)

for nome_prod, prezzo_unit, qta in prodotti:
    totale = prezzo_unit * qta
    print(f"{nome_prod:<20} | {prezzo_unit:>9.2f}€ | {qta:>5d} | {totale:>9.2f}€")