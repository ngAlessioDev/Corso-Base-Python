# ==========================================================
# TUTORIAL PYTHON: EREDITARIETÀ E POLIMORFISMO (ereditarieta.py)
# ==========================================================

# L'Ereditarietà è un pilastro della Programmazione Orientata agli Oggetti (OOP).
# Permette a una classe figlia (derivata) di acquisire attributi e metodi 
# da una classe padre (base), riducendo le duplicazioni e organizzando il codice
# in strutture gerarchiche pulite.


# --- 1. EREDITARIETÀ SINGOLA ED USO DI super() ---

class Veicolo:  # Classe Padre / Base
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        self.velocita = 0

    def accelera(self, incremento):
        self.velocita += incremento
        print(f"{self.marca} {self.modello} accelera a {self.velocita} km/h.")

    def frena(self):
        self.velocita = 0
        print(f"{self.marca} {self.modello} si è fermato.")


class Moto(Veicolo):  # Classe Figlia / Derivata
    def __init__(self, marca, modello, cilindrata):
        # super() richiama il costruttore __init__ della classe Padre (Veicolo)
        super().__init__(marca, modello)
        self.cilindrata = cilindrata  # Attributo specifico della Moto

    # Metodo specifico della sola classe Moto
    def impenna(self):
        if self.velocita > 0:
            print(f"La {self.marca} {self.modello} sta impennando!")
        else:
            print("Devi prima accelerare per impennare!")


# Creazione dell'istanza figlia
mia_moto = Moto("Yamaha", "MT-07", 689)

# La Moto ha accesso sia ai suoi metodi sia a quelli ereditati da Veicolo
mia_moto.accelera(50)  # Ereditato da Veicolo
mia_moto.impenna()     # Metodo proprio di Moto


# --- 2. OVERRIDE DEI METODI (METHOD OVERRIDING) ---

# Una classe figlia può ridefinire un metodo già presente nella classe padre
# per personalizzarne il comportamento.

class Animale:
    def fa_suono(self):
        print("L'animale emette un suono generico.")


class Gatto(Animale):
    # Sovrascriviamo (override) il metodo fa_suono
    def fa_suono(self):
        print("Il gatto fa: Miao!")


class Cane(Animale):
    # Sovrascriviamo (override) il metodo fa_suono
    def fa_suono(self):
        print("Il cane fa: Bau!")


# --- 3. POLIMORFISMO ---

# Il polimorfismo permette a oggetti di classi diverse di rispondere 
# alla stessa chiamata di metodo, ciascuno col proprio comportamento specifico.

animali = [Gatto(), Cane(), Animale()]

print("\n--- Dimostrazione Polimorfismo ---")
for animale in animali:
    # Richiamiamo lo stesso metodo su oggetti diversi:
    animale.fa_suono()


# --- 4. EREDITARIETÀ MULTIPLA ---

# In Python una classe può ereditare da PIÙ di una classe padre contemporaneamente.

class Volante:
    def vola(self):
        print("Sto volando in alto nel cielo!")


class Nuotatore:
    def nuota(self):
        print("Sto nuotando nell'acqua!")


# Anatra eredita sia da Volante che da Nuotatore
class Anatra(Volante, Nuotatore):
    def __init__(self, nome):
        self.nome = nome


anatra = Anatra("Donald")
print(f"\n{anatra.nome}:")
anatra.vola()   # Ereditato da Volante
anatra.nuota()  # Ereditato da Nuotatore


# --- 5. ISINSTANCE() E ISSUBCLASS() ---

# Python mette a disposizione due funzioni di controllo molto utili:

# 1. isinstance(oggetto, classe): verifica se un oggetto è istanza di una classe (o di una sua derivata)
print("\n--- Verifiche di Tipo ---")
print("mia_moto è un Veicolo?", isinstance(mia_moto, Veicolo))  # True (grazie all'ereditarietà)
print("mia_moto è una Moto?", isinstance(mia_moto, Moto))        # True

# 2. issubclass(classe_figlia, classe_padre): verifica la gerarchia tra classi
print("Moto è sottoclasse di Veicolo?", issubclass(Moto, Veicolo))      # True
print("Veicolo è sottoclasse di Moto?", issubclass(Veicolo, Moto))      # False