# ==========================================================
# TUTORIAL PYTHON: OPERAZIONI ARITMETICHE (operazioni_aritmetiche.py)
# ==========================================================

# In Python è possibile eseguire operazioni matematiche sui tipi numerici (int e float).
# Gli operatori aritmetici fondamentali sono simili a quelli usati in matematica,
# ma con alcune particolarità importanti riguardanti la divisione e le potenze.


# --- 1. OPERATORI FONDAMENTALI ---

a = 10
b = 3

# Addizione (+)
somma = a + b              # 10 + 3 = 13

# Sottrazione (-)
differenza = a - b         # 10 - 3 = 7

# Moltiplicazione (*)
prodotto = a * b           # 10 * 3 = 30

# Potenza (**) -> Nota: in Python si usa il doppio asterisco **, NON il simbolo ^
potenza = a ** b           # 10^3 = 10 * 10 * 10 = 1000

print(f"Somma: {somma}, Differenza: {differenza}, Prodotto: {prodotto}, Potenza: {potenza}")


# --- 2. LE TRE DIVISIONI IN PYTHON ---

# Python gestisce la divisione in modo molto preciso attraverso tre operatori distinti:

# 1. Divisione Classica (/)
# Restituisce SEMPRE un numero decimale (float), anche se il risultato è un numero intero esatto!
div_classica = 10 / 2      # Risultato: 5.0 (tipo float, non int)
div_decimale = 10 / 3      # Risultato: 3.3333333333333335

# 2. Divisione Intera (//)
# Restituisce solo la parte intera del quoziente, scartando tutti i decimali (senza arrotondare!)
div_intera = 10 // 3       # Risultato: 3

# 3. Modulo (%)
# Restituisce il RESTO della divisione intera. È utilissimo per verificare se un numero è pari o dispari!
resto = 10 % 3             # Risultato: 1 (perché 10 diviso 3 fa 3 con resto 1)

print(f"Divisione classica: {div_classica} ({type(div_classica)})")
print(f"Divisione intera: {div_intera}")
print(f"Resto (Modulo): {resto}")

# Esempio pratico del Modulo: verificare se un numero è pari
numero = 8
is_pari = (numero % 2 == 0) # Se il resto della divisione per 2 è 0, il numero è pari
print(f"Il numero {numero} è pari? {is_pari}")


# --- 3. PRECEDENZA DEGLI OPERATORI (PEMDAS) ---

# Python rispetta le classiche regole matematiche della precedenza delle operazioni:
# 1. Parentesi ()
# 2. Esponenti **
# 3. Moltiplicazioni e Divisioni (*, /, //, %)
# 4. Addizioni e Sottrazioni (+, -)

risultato1 = 2 + 3 * 4     # Prima 3*4 = 12, poi 2+12 = 14
risultato2 = (2 + 3) * 4   # Prima (2+3) = 5, poi 5*4 = 20

print(f"Senza parentesi: {risultato1} | Con parentesi: {risultato2}")


# --- 4. OPERATORI DI ASSEGNAZIONE COMPOSTA (SCORCIATOIE) ---

# Quando devi aggiornare il valore di una variabile eseguendo un'operazione su se stessa,
# puoi usare gli operatori di assegnazione sintetica:

punteggio = 100

punteggio += 10    # Equivale a: punteggio = punteggio + 10  (Diventa 110)
punteggio -= 20    # Equivale a: punteggio = punteggio - 20  (Diventa 90)
punteggio *= 2     # Equivale a: punteggio = punteggio * 2   (Diventa 180)
punteggio //= 3    # Equivale a: punteggio = punteggio // 3  (Diventa 60)

print(f"Punteggio finale aggiornato: {punteggio}")


# --- 5. FUNZIONI MATEMATICHE UTILI (BUILT-IN) ---

# Python include alcune funzioni matematiche integrate pronte all'uso:

# Valore assoluto: abs()
distanza = abs(-15)        # Risultato: 15

# Arrotondamento: round(numero, cifre_decimali)
numero_decimale = 3.14159
arrotondato = round(numero_decimale, 2) # Risultato: 3.14

# Minimo e Massimo: min() e max()
valore_min = min(5, 2, 9, 1) # Risultato: 1
valore_max = max(5, 2, 9, 1) # Risultato: 9

print(f"Assoluto: {distanza}, Arrotondato: {arrotondato}, Min: {valore_min}, Max: {valore_max}")