# ==========================================================
# TUTORIAL PYTHON: MATH AVANZATO E COMPLETO (modulo_math_avanzato.py)
# ==========================================================

# Questo file completa la panoramica del modulo `math`, coprendo le funzioni 
# per la teoria dei numeri, il calcolo combinatorio avanzato, la trigonometria
# iperbolica e le funzioni speciali di fisica e statistica.

import math


# --- 1. TEORIA DEI NUMERI E MANIPOLAZIONE DI FLOAT ---

x = 10.75

# math.modf(x): Separa la parte frazionaria e la parte intera di un numero
frazionaria, intera = math.modf(x)
print(f"modf({x}) -> Parte frazionaria: {frazionaria}, Parte intera: {intera}")

# math.copysign(a, b): Restituisce il valore assoluto del primo numero con il segno del secondo
print("copysign(10, -1):", math.copysign(10, -1))  # Output: -10.0

# math.fsum(iterabile): Calcola la somma precisa a virgola mobile di una sequenza
# A differenza della funzione integrata sum(), evita l'accumulo di errori di arrotondamento float!
lista_float = [0.1] * 10
print("Somma con sum() standard:", sum(lista_float))    # Può accumulare imprecisioni
print("Somma con math.fsum():", math.fsum(lista_float))  # Esattamente 1.0

# math.frexp(x) e math.ldexp(x, i): Mantissa ed esponente in base 2 (notazione scientifica binaria)
mantissa, esponente = math.frexp(8.0)  # 8.0 = 0.5 * 2^4
print(f"frexp(8.0) -> Mantissa: {mantissa}, Esponente: {esponente}")
print("ldexp(0.5, 4):", math.ldexp(mantissa, esponente))  # Ricostruisce 8.0


# --- 2. COMBINATORIA E STATISTICA AVANZATA ---

# math.perm(n, k): Calcola il numero di permutazioni di n elementi presi k alla volta (senza ripetizione)
# Corrisponde a: n! / (n - k)!
permutazioni = math.perm(5, 2)
print("\nPermutazioni P(5, 2):", permutazioni)  # Output: 20

# math.comb(n, k): Calcola il coefficiente binomiale (combinazioni di n elementi presi k alla volta)
# Corrisponde a: n! / (k! * (n - k)!)
combinazioni = math.comb(5, 2)
print("Combinazioni C(5, 2):", combinazioni)  # Output: 10

# math.prod(iterabile): Calcola il prodotto di tutti gli elementi in una sequenza (come sum(), ma moltiplica)
prodotto = math.prod([2, 3, 4])
print("Prodotto di [2, 3, 4]:", prodotto)  # Output: 24

# math.dist(p1, p2): Calcola la distanza euclidea tra due punti n-dimensionali
punto_a = (0, 0)
punto_b = (3, 4)
distanza = math.dist(punto_a, punto_b)
print("Distanza Euclidea tra (0,0) e (3,4):", distanza)  # Output: 5.0 (triangolo 3-4-5)

# math.hypot(*coordinate): Calcola l'ipotenusa o la norma euclidea di un vettore dall'origine
print("Ipotenusa math.hypot(3, 4):", math.hypot(3, 4))  # Output: 5.0


# --- 3. TRIGONOMETRIA INVERSA ED IPERBOLICA ---

# Trigonometria Inversa (Arcoseno, Arcocoseno, Arcotangente) -> restituiscono radianti
print("\nArcocoseno di 1 (in rad):", math.acos(1.0))  # Output: 0.0
print("Arcotangente di 1 (in gradi):", math.degrees(math.atan(1.0)))  # Output: 45.0

# math.atan2(y, x): Arcotangente di y/x tenendo conto dei quadranti (fondamentale in grafica 2D)
print("atan2(1, 1) in gradi:", math.degrees(math.atan2(1, 1)))  # Output: 45.0

# Funzioni Iperboliche (sinh, cosh, tanh) e le loro inverse (asinh, acosh, atanh)
print("Coseno iperbolico cosh(0):", math.cosh(0))  # Output: 1.0


# --- 4. FUNZIONI SPECIALI (FISICA / STATISTICA / MATEMATICA AVANZATA) ---

# math.erf(x): Funzione Errore di Gauss (usata in probabilità e statistica per le distribuzioni normali)
print("\nFunzione Errore erf(1):", math.erf(1.0))

# math.erfc(x): Funzione Errore Complementare (1 - erf(x))
print("Funzione Errore Complementare erfc(1):", math.erfc(1.0))

# math.gamma(x): Funzione Gamma di Eulero (estensione del fattoriale ai numeri reali: gamma(n) = (n-1)!)
print("Gamma(6) [equivale a 5!]:", math.gamma(6))  # Output: 120.0

# math.lgamma(x): Logaritmo naturale del valore della funzione Gamma (usato per evitare overflow con n grandi)
print("Logaritmo di Gamma(6):", math.lgamma(6))


# --- 5. ALTRE COSTANTI SCIENTIFICHE ---

# math.tau: La costante Tau (2 * Pi Greco = 6.283185...)
print("\nCostante Tau (2 * pi):", math.tau)