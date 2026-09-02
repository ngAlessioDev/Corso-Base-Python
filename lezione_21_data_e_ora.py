# ==========================================================
# TUTORIAL PYTHON: DATA E ORA (data_e_ora.py)
# ==========================================================

# La gestione di date e orari in Python viene affidata principalmente al modulo 
# integrato `datetime`.
#
# Le classi principali fornite da questo modulo sono:
# - datetime.date: Gestisce solo la data (anno, mese, giorno).
# - datetime.time: Gestisce solo l'ora (ore, minuti, secondi, microsecondi).
# - datetime.datetime: Gestisce sia la data sia l'ora insieme.
# - datetime.timedelta: Rappresenta una durata o differenza tra due date/orari.


# --- 1. IMPORTARE IL MODULO ED OTTENERE DATA E ORA ATTUALE ---

import datetime

# Data e ora corrente (timestamp locale)
ora_attuale = datetime.datetime.now()
print("Data e ora corrente:", ora_attuale)

# Solo la data di oggi
oggi = datetime.date.today()
print("Data di oggi:", oggi)

# Accesso ai singoli componenti di un oggetto datetime
print(f"Anno: {ora_attuale.year} | Mese: {ora_attuale.month} | Giorno: {ora_attuale.day}")
print(f"Ora: {ora_attuale.hour} | Minuti: {ora_attuale.minute} | Secondi: {ora_attuale.second}")


# --- 2. CREARE OGGETTI DATE E DATETIME PERSONALIZZATI ---

# Sintassi date: datetime.date(anno, mese, giorno)
data_evento = datetime.date(2026, 12, 25)

# Sintassi datetime: datetime.datetime(anno, mese, giorno, ora, minuto, secondo)
momento_esatto = datetime.datetime(2026, 10, 15, 14, 30, 0)

print("\nData evento personalizzata:", data_evento)
print("Momento esatto:", momento_esatto)


# --- 3. FORMATTAZIONE DELLE DATE IN STRINGHE (STRFTIME) ---

# Il metodo .strftime() (String Format Time) converte un oggetto datetime 
# in una stringa formattata secondo codici specifici (%Y, %m, %d, ecc.).

ora_ora = datetime.datetime.now()

# Direttive comuni:
# %d = Giorno del mese (01-31)      | %m = Mese (01-12)
# %Y = Anno a 4 cifre (es. 2026)    | %y = Anno a 2 cifre (es. 26)
# %H = Ora in formato 24h (00-23)   | %M = Minuti (00-59)
# %S = Secondi (00-59)              | %A = Nome completo del giorno della settimana

data_formattata = ora_ora.strftime("%d/%m/%Y %H:%M:%S")
print("\nData formattata (GG/MM/AAAA HH:MM:SS):", data_formattata)

formato_esteso = ora_ora.strftime("%A, %d %B %Y")
print("Formato esteso:", formato_esteso)


# --- 4. CONVERTIRE STRINGHE IN OGGETTI DATETIME (STRPTIME) ---

# Il metodo .strptime() (String Parse Time) fa l'operazione opposta:
# trasforma una stringa contenente una data in un vero oggetto datetime manipolabile.

stringa_data = "2026-09-15 18:45:00"
formato_input = "%Y-%m-%d %H:%M:%S"

data_oggettivata = datetime.datetime.strptime(stringa_data, formato_input)

print("\nStringa convertita in oggetto datetime:", type(data_oggettivata))
print("Anno estratto dalla stringa parsed:", data_oggettivata.year)


# --- 5. CALCOLI CON DATE E TIMEDELTA ---

# `timedelta` permette di eseguire somme, sottrazioni e calcoli di intervalli temporali.

d1 = datetime.datetime(2026, 5, 1, 10, 0, 0)
d2 = datetime.datetime(2026, 5, 10, 15, 30, 0)

# Calcolo della differenza tra due date
differenza = d2 - d1  # Restituisce un oggetto timedelta
print(f"\nDifferenza tra le due date: {differenza.days} giorni e {differenza.seconds // 3600} ore.")

# Sommare o sottrarre tempo a una data con timedelta
oggi_dt = datetime.date.today()

dieci_giorni = datetime.timedelta(days=10)
data_futura = oggi_dt + dieci_giorni
data_passata = oggi_dt - dieci_giorni

print("Tra 10 giorni sarà:", data_futura)
print("10 giorni fa era:", data_passata)


# --- 6. CONFRONTO TRA DATE ---

# Gli oggetti date e datetime possono essere confrontati direttamente 
# con i classici operatori di confronto (<, >, ==, !=).

scadenza = datetime.date(2026, 12, 31)

if oggi_dt < scadenza:
    print("\nLa data di scadenza NON è ancora passata.")
else:
    print("\nAttenzione: il termine è scaduto!")


# --- 7. ACCENNO AI FUSI ORARI (TIMEZONE) ---

# Di default, gli oggetti datetime in Python sono "naive" (non conoscono il fuso orario).
# Dal modulo `zoneinfo` (Python 3.9+) o `datetime.timezone` è possibile gestire gli orari "aware".

from datetime import timezone

# UTC Time
ora_utc = datetime.datetime.now(timezone.utc)
print("\nOra corrente in formato UTC:", ora_utc)