# ==========================================================
# TUTORIAL PYTHON: GESTIONE PACCHETTI CON PIP (gestione_pip.py)
# ==========================================================

# `pip` (Preferred Installer Program) è il gestore ufficiale di pacchetti per Python.
# Consente di scaricare, installare, aggiornare e rimuovere librerie esterne 
# pubblicate su PyPI (Python Package Index - https://pypi.org).
#
# NOTA: I comandi `pip` vanno eseguiti nel TERMINALE / PROMPT DEI COMANDI,
# e non all'interno di uno script Python!


# --- 1. COMANDI FONDAMENTALI DA TERMINALE ---

"""
1. Verificare la versione di pip installata:
   $ pip --version
   (Oppure: python -m pip --version)

2. Aggiornare pip alla versione più recente:
   $ python -m pip install --upgrade pip

3. Installare un pacchetto (es. la libreria 'requests' per richieste HTTP):
   $ pip install requests

4. Installare una versione specifica di un pacchetto:
   $ pip install requests==2.31.0

5. Aggiornare un pacchetto già installato:
   $ pip install --upgrade requests

6. Disinstallare / Rimuovere un pacchetto:
   $ pip uninstall requests

7. Elencare tutti i pacchetti installati nell'ambiente corrente:
   $ pip list

8. Mostrare informazioni dettagliate su un pacchetto specifico:
   $ pip show requests
"""


# --- 2. GESTIONE DELLE DIPENDENZE (requirements.txt) ---

# Nei progetti reali si usano file chiamati `requirements.txt` per elencare 
# tutte le librerie necessarie al funzionamento dell'applicazione.

"""
Come esportare l'elenco dei pacchetti attuali in un file:
   $ pip freeze > requirements.txt

Contenuto tipico di un file requirements.txt:
   requests==2.31.0
   pandas>=2.0.0
   numpy

Come installare tutte le dipendenze elencate nel file in un solo comando:
   $ pip install -r requirements.txt
"""


# --- 3. AMBIENTI VIRTUALI (venv) ---

# È BUONA PRATICA non installare mai pacchetti globalmente nel sistema operativo,
# ma creare un "Ambiente Virtuale" isolato per ciascun progetto.

"""
1. Creare un ambiente virtuale chiamato 'env' nella cartella del progetto:
   $ python -m venv env

2. Attivare l'ambiente virtuale:
   - Su Linux / macOS:
     $ source env/bin/activate
   - Su Windows (Command Prompt):
     > env\Scripts\activate.bat
   - Su Windows (PowerShell):
     PS> env\Scripts\Activate.ps1

3. Una volta attivato, il prompt mostrerà "(env)". Ora ogni 'pip install' 
   avverrà SOLO all'interno di questo ambiente isolato!

4. Disattivare l'ambiente virtuale:
   $ deactivate
"""


# --- 4. VERIFICARE O IMPORTARE UN PACCHETTO INSTALLATO DA CODICE ---

# Una volta installato un pacchetto con pip (es. `pip install requests`),
# è possibile importarlo normalmente nei propri script Python:

try:
    import requests
    
    # Eseguiamo una semplice richiesta HTTP GET di prova
    risposta = requests.get("https://api.github.com")
    print("--- Verifica Installazione Pacchetto 'requests' ---")
    print("Codice Stato HTTP:", risposta.status_code) # 200 = Successo
    print("Tipo di contenuto:", risposta.headers['content-type'])

except ImportError:
    print("\n[ERRORE] Il pacchetto 'requests' non risulta installato!")
    print("Per installarlo, esegui da terminale: pip install requests")


# --- 5. ESEGUIRE COMANDI PIP DIRETTAMENTE DA PYTHON (SUBPROCESS) ---

# Sebbene sia preferibile usare il terminale, è possibile eseguire comandi pip
# anche programmaticamente usando il modulo `subprocess`:

import subprocess
import sys

def installa_pacchetto(nome_pacchetto):
    """Funzione di utilità per installare un pacchetto da codice."""
    print(f"\nInstallazione di '{nome_pacchetto}' in corso...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", nome_pacchetto])

# Esempio di utilizzo (decommentare per testare):
# installa_pacchetto("colorama")