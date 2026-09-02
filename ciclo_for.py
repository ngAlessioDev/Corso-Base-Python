# ==========================================================
# TUTORIAL PYTHON: IL CICLO FOR (ciclo_for.py)
# ==========================================================

# Il ciclo 'for' in Python viene utilizzato per iterare (scorrere) su una sequenza
# (come una lista, una stringa, una tupla o un intervallo di numeri).
# A differenza del ciclo 'while', il ciclo 'for' si usa principalmente quando 
# si conosce a priori il numero di iterazioni o la sequenza di elementi da elaborare.


# --- 1. ITERARE SU UNA STRUNGA O LISTA ---

# Ad ogni iterazione, la variabile di controllo (es. 'lettera' o 'frutto')
# assume il valore dell'elemento corrente della sequenza.

parola = "Python"

print("Iterazione sui caratteri di una stringa:")
for lettera in parola:
    print(lettera)


frutti = ["mela", "banana", "ciliegia"]

print("\nIterazione sugli elementi di una lista:")
for frutto in frutti:
    print(f"Frutto: {frutto}")


# --- 2. LA FUNZIONE RANGE() ---

# La funzione integrata range() genera una sequenza numerica ed è utilissima
# quando si vuole ripetere un blocco di codice un numero ben preciso di volte.

# range(fine) -> genera numeri da 0 fino a fine-1
print("\n--- range(5) ---")
for i in range(5):
    print(i)  # Stampa da 0 a 4

# range(inizio, fine) -> genera numeri da inizio fino a fine-1
print("\n--- range(2, 6) ---")
for i in range(2, 6):
    print(i)  # Stampa da 2 a 5

# range(inizio, fine, passo) -> genera numeri incrementando del valore di 'passo'
print("\n--- range(0, 10, 2) (numeri pari) ---")
for i in range(0, 10, 2):
    print(i)  # Stampa 0, 2, 4, 6, 8

# È possibile usare anche un passo negativo per un conteggio alla rovescia:
print("\n--- Conteggio alla rovescia ---")
for i in range(5, 0, -1):
    print(i)  # Stampa 5, 4, 3, 2, 1


# --- 3. USO DI ENUMERATE() PER OTTENERE L'INDICE ---

# Se durante l'iterazione hai bisogno sia dell'elemento che della sua posizione (indice),
# la funzione integrata enumerate() è la soluzione più elegante e usata in Python.

linguaggi = ["Python", "Java", "C++"]

print("\n--- Uso di enumerate() ---")
for indice, linguaggio in enumerate(linguaggi):
    print(f"Posizione {indice}: {linguaggio}")


# --- 4. ISTRUZIONI BREAK E CONTINUE NEL FOR ---

# break: interrompe immediatamente il ciclo prima che abbia terminato tutti gli elementi.
# continue: salta l'iterazione corrente e passa all'elemento successivo.

print("\n--- Esempio BREAK (si ferma se trova 'stop') ---")
comandi = ["avvia", "elabora", "stop", "concludi"]

for comando in comandi:
    if comando == "stop":
        print("Trovato comando di arresto! Interruzione ciclo.")
        break
    print(f"Esecuzione: {comando}")


print("\n--- Esempio CONTINUE (salta i numeri negativi) ---")
numeri = [10, -5, 20, -3, 30]

for n in numeri:
    if n < 0:
        continue  # Salta l'elaborazione per i numeri negativi
    print(f"Numero valido: {n}")


# --- 5. CLAUSOLA ELSE NEL CICLO FOR ---

# Come per il ciclo while, anche il ciclo 'for' può avere un blocco 'else'.
# Il blocco 'else' viene eseguito SOLO SE il ciclo termina normalmente tutte le sue iterazioni
# (cioè se NON incontra un'istruzione 'break').

numeri_da_cercare = [1, 3, 5, 7]
target = 4

print("\n--- Ricerca elemento con for/else ---")
for numero in numeri_da_cercare:
    if numero == target:
        print(f"Elemento {target} trovato!")
        break
else:
    print(f"Elemento {target} NON presente nella lista.")