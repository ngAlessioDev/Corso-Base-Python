# ==========================================================
# TUTORIAL PYTHON: SINTASSI E STRUTTURA (sintassi.py)
# ==========================================================

# In Python la sintassi è progettata per essere pulita, leggibile e minimale.
# A differenza di altri linguaggi (come C++, Java o JavaScript), Python riduce al minimo
# l'uso di parentesi graffe o punti e virgola, affidandosi invece alla struttura del testo.


# --- 1. I COMMENTI ---

# I commenti si scrivono con il simbolo #
# Tutto quello che segue su quella riga viene ignorato dal programma durante l'esecuzione,
# come ad esempio questa spiegazione.

# In Python NON esistono commenti multiriga nativi con sintassi dedicate (come /* ... */ in altri linguaggi).
# Se vuoi scrivere un commento su più righe, devi mettere il simbolo # all'inizio di ogni riga.

# Questo perché in Python l'andare a capo ha un significato fondamentale:
# indica la fine di un'istruzione! Per questo motivo, per estendere un commento
# su più righe è necessario ripetere il simbolo # riga per riga.


# --- 2. L'INDENTAZIONE (SPAZIATURA DEL CODICE) ---

# Oltre all'andare a capo, l'INDENTAZIONE è la caratteristica più importante della sintassi Python.
# L'indentazione (cioè lo spazio vuoto a inizio riga) definisce la struttura logica e indica
# a quale blocco di codice appartiene una determinata istruzione.

# In altri linguaggi si usano le parentesi graffe { }, in Python si usano gli spazi!

# Esempio: le seguenti spaziatore indicano che le istruzioni print appartengono ai rispettivi blocchi if ed else:

if 1 + 1 == 2:
    print("Condizione vera: l'operazione fa 2")
    print("Anche questa riga fa parte dello stesso blocco dell'if")
else:
    print("Condizione falsa")

# Se un'istruzione non è indentata, significa che è tornata al livello principale del programma:
print("Questa riga è fuori dal blocco condizionale e viene eseguita sempre.")


# --- 3. REGOLE E BUONE PRATICHE DI INDENTAZIONE ---

# Gli editor di codice di qualità (come VS Code, PyCharm, ecc.) gestiscono automaticamente
# l'indentazione o guidano il programmatore a scrivere codice ben strutturato.
# Tuttavia, se stai scrivendo codice in un editor di testo semplice (come il Blocco Note),
# devi fare molta attenzione a indentare correttamente, altrimenti otterrai errori di sintassi (IndentationError).

# Regole chiave per la spaziatura:
# 1. La spaziatura standard raccomandata dalla guida PEP 8 è di 4 SPAZI per ogni livello di indentazione.
# 2. Puoi usare anche il tasto TAB 1 volta, che in molti editor è già configurato per inserire 4 spazi.
# 3. L'importante è ESSERE COERENTI: non mescolare mai spazi e TAB nello stesso file per evitare errori invisibili!


# --- 4. ISTRUZIONI SU PIÙ RIGHE E PUNTI E VIRGOLA ---

# Di norma, ogni istruzione termina andando a capo. Il punto e virgola (;) NON è necessario.
# Tuttavia, è possibile usare il punto e virgola per scrivere più istruzioni sulla stessa riga (sconsigliato):
x = 5; y = 10; print(x + y)

# Se invece un'istruzione è molto lunga e vuoi spezzarla su più righe per leggibilità,
# puoi usare la barra rovesciata (\) oppure racchiuderla tra parentesi:
somma_lunga = 1 + 2 + 3 + \
              4 + 5 + 6

somma_con_parentesi = (
    1 + 2 + 3 +
    4 + 5 + 6
)
print("Risultato somma:", somma_con_parentesi)