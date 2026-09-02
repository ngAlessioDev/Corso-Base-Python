# ==========================================================
# TUTORIAL PYTHON: IL MODULO MATH (modulo_math.py)
# ==========================================================

# Il modulo integrato `math` fornisce l'accesso a funzioni matematiche avanzate 
# per numeri reali (float), costanti fondamentali e operazioni trigonometriche, 
# logaritmiche ed esponenziali.
#
# A differenza delle funzioni base (come abs(), round(), min(), max()), 
# le funzionalità di `math` richiedono l'importazione esplicita del modulo.


# --- 1. IMPORTAZIONE E COSTANTI FONDAMENTALI ---

import math

# Il modulo mette a disposizione alcune costanti matematiche note:
print("Pi Greco (pi):", math.pi)            # 3.141592653589793
print("Numero di Eulero (e):", math.e)        # 2.718281828459045
print("Infinito positivo (inf):", math.inf)   # Utilissimo nei confronti o algoritmi
print("Not a Number (nan):", math.nan)        # Rappresenta un valore non numerico


# --- 2. ARROTONDAMENTI E VALORI ASSOLUTI ---

x = 4.7
y = -3.2

# math.ceil(): Arrotonda SEMPRE per ECCESSO all'intero superiore
print(f"Ceil di {x}:", math.ceil(x))    # Output: 5

# math.floor(): Arrotonda SEMPRE per DIFETTO all'intero inferiore
print(f"Floor di {x}:", math.floor(x))  # Output: 4

# math.trunc(): Tronca i decimali eliminando la parte frazionaria (taglia senza arrotondare)
print(f"Troncamento di {x}:", math.trunc(x))  # Output: 4

# math.fabs(): Restituisce il valore assoluto sempre come numero decimale (float)
print(f"Valore assoluto di {y}:", math.fabs(y))  # Output: 3.2


# --- 3. POTENZE, RADICI E FATTORIALE ---

# math.sqrt(x): Radice quadrata di x (x deve essere >= 0)
radice = math.sqrt(25)
print("\nRadice quadrata di 25:", radice)  # Output: 5.0

# math.pow(x, y): Calcola x elevato alla y (restituisce sempre un float)
potenza = math.pow(2, 3)
print("2 elevato alla 3:", potenza)       # Output: 8.0

# math.factorial(n): Calcola il fattoriale di un intero n (es. 5! = 5 * 4 * 3 * 2 * 1)
fattoriale = math.factorial(5)
print("Fattoriale di 5 (!5):", fattoriale)  # Output: 120


# --- 4. MASSIMO COMUNE DIVISORE (MCD) E MINIMO COMUNE MULTIPLO (MCM) ---

a = 12
b = 18

# math.gcd(): Calcola il Massimo Comune Divisore (Greatest Common Divisor)
mcd = math.gcd(a, b)
print(f"\nMCD tra {a} e {b}:", mcd)  # Output: 6

# math.lcm(): Calcola il Minimo Comune Multiplo (Least Common Multiple)
mcm = math.lcm(a, b)
print(f"MCM tra {a} e {b}:", mcm)  # Output: 36


# --- 5. LOGARITMI ED ESPONENZIALI ---

valore = 100

# math.log(x, base): Logaritmo di x nella base specificata (di default base e - naturale)
log_naturale = math.log(math.e)
log_base10 = math.log(100, 10)  # Oppure math.log10(100)
log_base2 = math.log2(8)

print(f"\nLogaritmo naturale di e:", log_naturale)  # Output: 1.0
print(f"Logaritmo base 10 di 100:", log_base10)    # Output: 2.0
print(f"Logaritmo base 2 di 8:", log_base2)        # Output: 3.0

# math.exp(x): Calcola e^x (Eulero elevato alla x)
esponenziale = math.exp(2)
print("e^2:", esponenziale)


# --- 6. TRIGONOMETRIA E CONVERSIONI DI ANGOLI ---

# ATTENZIONE: Le funzioni trigonometriche in Python lavorano in RADIANTI, non in gradi!

angolo_gradi = 180

# Conversioni da Gradi a Radianti e viceversa
angolo_radianti = math.radians(angolo_gradi)
print(f"\n180 gradi in radianti:", angolo_radianti)  # Output: ~3.14159 (Pi)
print(f"Pi radianti in gradi:", math.degrees(math.pi)) # Output: 180.0

# Funzioni Trigonometriche (sin, cos, tan)
seno = math.sin(angolo_radianti)      # sin(Pi) -> 0 (con approssimazione float)
coseno = math.cos(math.radians(0))    # cos(0) -> 1.0

print(f"Seno di 180 gradi:", round(seno, 5))  # Arrotondato a 0
print("Coseno di 0 gradi:", coseno)


# --- 7. VERIFICA DI VALORI SPECIALI ED ISCLOSE ---

# math.isnan(x) e math.isinf(x): Verificano se un valore è NaN o Infinito
print("\n3.14 è un numero valido?", not math.isnan(3.14))

# math.isclose(a, b): Verifica se due numeri decimali sono quasi uguali
# Utile per evitare i classici errori di approssimazione delle operazioni float!
somma_float = 0.1 + 0.2  # In Python fa 0.30000000000000004
print("0.1 + 0.2 == 0.3 con isclose?:", math.isclose(somma_float, 0.3))  # Output: True