# ==========================================================
# TUTORIAL PYTHON: I SET / INSIEMI (set.py)
# ==========================================================

# Un Set (o insieme) in Python è una collezione di elementi **NON ordinata**,
# **modificabile** e che **NON consente valori duplicati**.
#
# I set sono ideali quando occorre garantire l'univocità degli elementi
# o quando è necessario eseguire operazioni matematiche sugli insiemi.


# --- 1. CREAZIONE E ASSENZA DI DUPLICATI ---

# Si creano racchiudendo gli elementi tra parentesi graffe { } separati da virgole.
colori = {"rosso", "verde", "blu", "rosso", "verde"}  # I duplicati vengono eliminati automaticamente

print("Set di colori (senza duplicati):", colori)

# ATTENZIONE: Per creare un set VUOTO, DEVI usare la funzione set(), NON le parentesi graffe vuote {}
# (usare {} creerebbe un dizionario vuoto!).
set_vuoto = set()
dizionario_vuoto = {}  # Tipo <class 'dict'>

print("Tipo set vuoto:", type(set_vuoto))  # Tipo <class 'set'>


# --- 2. CARATTERISTICHE DI UN SET ---

# 1. NON ORDINATI: Gli elementi non mantengono un ordine fisso.
# 2. NON INDICIZZATI: NON è possibile accedere agli elementi tramite indice o slicing!
#    colori[0] -> Genererebbe un TypeError: 'set' object is not subscriptable

# Per verificare se un elemento fa parte di un set, si usa l'operatore 'in' (molto veloce nei set):
print("C'è il rosso?", "rosso" in colori)  # Output: True


# --- 3. AGGIUNGERE E RIMUOVERE ELEMENTI ---

frutti = {"mela", "banana"}

# AGGIUNGERE:
frutti.add("kiwi")              # Aggiunge un singolo elemento
frutti.update(["pera", "uva"])  # Aggiunge più elementi contemporaneamente (da una lista o un altro set)

print("Set dopo inserimenti:", frutti)

# RIMUOVERE:
frutti.remove("banana")  # Rimuove "banana". Se l'elemento NON esiste, genera un KeyError!
frutti.discard("mango")  # Rimuove "mango" SE presente. Se NON esiste, NON genera errori (più sicuro).

elemento_rimosso = frutti.pop()  # Rimuove e restituisce un elemento CASUALE (poiché il set non è ordinato)

print(f"Estratto casualmente: {elemento_rimosso} | Rimasti: {frutti}")


# --- 4. OPERAZIONI MATEMATICHE SUGLI INSIEMI ---

# I set permettono di eseguire facilmente le classiche operazioni della teoria degli insiemi.

insieme_a = {1, 2, 3, 4}
insieme_b = {3, 4, 5, 6}

# UNIONE (| oppure .union()): Unisce gli elementi di entrambi gli insiemi (senza duplicati)
unione = insieme_a | insieme_b  # {1, 2, 3, 4, 5, 6}
print("Unione:", unione)

# INTERSEZIONE (& oppure .intersection()): Mantiene solo gli elementi comuni a entrambi
intersezione = insieme_a & insieme_b  # {3, 4}
print("Intersezione:", intersezione)

# DIFFERENZA (- oppure .difference()): Elementi presenti nel primo set ma NON nel secondo
differenza = insieme_a - insieme_b  # {1, 2}
print("Differenza (A - B):", differenza)

# DIFFERENZA SIMMETRICA (^ oppure .symmetric_difference()): Elementi presenti in un set o nell'altro, ma NON in entrambi
diff_simmetrica = insieme_a ^ insieme_b  # {1, 2, 5, 6}
print("Differenza simmetrica:", diff_simmetrica)


# --- 5. RIMOZIONE DUPLICATI DA UNA LISTA (TRUCCO DEL CASTING) ---

# Uno degli usi più comuni dei set nella pratica quotidiana è rimuovere al volo 
# i valori duplicati da una lista.

lista_con_duplicati = [1, 2, 2, 3, 4, 4, 4, 5]

# Convertiamo la lista in set (elimina i duplicati) e poi di nuovo in lista:
lista_pulita = list(set(lista_con_duplicati))

print("Lista originale:", lista_con_duplicati)
print("Lista senza duplicati:", lista_pulita)