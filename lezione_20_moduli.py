# ==========================================================
# TUTORIAL PYTHON: MODULI E PACCHETTI (moduli.py)
# ==========================================================

# Un **Modulo** in Python è semplicemente un file con estensione .py contenente 
# codice Python (funzioni, classi o variabili) che può essere riutilizzato in altri file.
# 
# Un **Pacchetto** (Package) è una cartella che raccoglie più moduli correlati tra loro,
# organizzando la struttura di progetti più complessi.
#
# L'uso dei moduli promuove il riuso del codice, la manutenibilità e la modularità.


# --- 1. IMPORTARE MODULI DELLA LIBRERIA STANDARD ---

# Python viene fornito con una vasta serie di moduli integrati ("Batteries Included").
# Per usare un modulo si utilizza la parola chiave `import`.

import math  # Importa il modulo matematico standard

# Per accedere alle funzioni o costanti del modulo si usa la sintassi: nome_modulo.elemento
risultato_radice = math.sqrt(16)
valore_pi = math.pi

print(f"Radice quadrata di 16: {risultato_radice}")
print(f"Valore di Pi Greco: {valore_pi}")


# --- 2. SINTASSI ALTERNATIVE DI IMPORTAZIONE ---

# A) Importare solo elementi specifici da un modulo (usando `from ... import ...`):
# In questo modo non serve anteporre il nome del modulo.
from random import randint, choice

numero_casuale = randint(1, 10)  # Genera un intero tra 1 e 10 (inclusi)
colore_scelto = choice(["rosso", "verde", "blu"])

print(f"Numero estratto: {numero_casuale} | Colore estratto: {colore_scelto}")


# B) Assegnare un ALIAS a un modulo o elemento (usando `as`):
# Utilissimo per abbreviare nomi di moduli lunghi o molto usati (es. numpy as np, pandas as pd).
import datetime as dt

ora_attuale = dt.datetime.now()
print(f"Data e ora corrente: {ora_attuale.strftime('%H:%M:%S - %d/%m/%Y')}")


# C) Importare TUTTO da un modulo (da EVITARE di norma):
# from math import *
# Sconsigliato perché può causare conflitti di nomi ("namespace pollution") con le tue variabili!


# --- 3. CREARE ED IMPORTARE UN MODULO PERSONALIZZATO ---

# Immagina di avere un file chiamato `mio_modulo.py` nella stessa cartella con questo codice:
"""
# --- Contenuto ipotetico di mio_modulo.py ---
def saluta_utente(nome):
    return f"Ciao {nome}, benvenuto dal modulo personalizzato!"

PI_APPROSSIMATO = 3.14
"""

# Nel tuo file principale potrai quindi importarlo ed usarlo semplicemente così:
# import mio_modulo
# messaggio = mio_modulo.saluta_utente("Marco")
# print(messaggio)


# --- 4. LA VARIABILE SPECIALE __name__ == "__main__" ---

# Ogni file Python possiede la variabile speciale `__name__`.
# - Se il file viene eseguito direttamente, `__name__` vale `"__main__"`.
# - Se il file viene importato come modulo in un altro script, `__name__` conterrà il nome del file.

# Questo blocco permette di inserire codice di test che viene eseguito SOLO se fai partire 
# direttamente questo file, ma viene IGNORATO se il file viene importato altrove!

def funzione_principale():
    print("Esecuzione del programma principale...")

if __name__ == "__main__":
    # Codice eseguito solo se lanci direttamente `python moduli.py`
    print("Il file è stato eseguito direttamente!")
    funzione_principale()
else:
    print("Il file è stato importato come modulo in un altro script.")


# --- 5. STRUTTURA DI UN PACCHETTO (PACKAGE) ---

# Un Pacchetto è una directory contenente moduli Python.
# In versioni precedenti di Python (e tuttora per buona pratica), la cartella deve
# contenere un file speciale denominato `__init__.py` (anche vuoto) per essere riconosciuta.

# Esempio di struttura su disco:
# mio_progetto/
# │
# ├── main.py
# └── mio_pacchetto/
#     ├── __init__.py
#     ├── calcoli.py
#     └── utilita.py

# Come importare da un pacchetto nel tuo main.py:
# from mio_pacchetto.calcoli import somma
# oppure:
# import mio_pacchetto.utilita as util