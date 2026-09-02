# ==========================================================
# TUTORIAL PYTHON: CLASSI E OGGETTI (classi_e_oggetti.py)
# ==========================================================

# La Programmazione Orientata agli Oggetti (OOP) è un paradigma di programmazione
# basato sul concetto di "oggetti", che possono contenere dati (attributi) 
# e codice sotto forma di procedure (metodi).
#
# - CLASSE: È il modello/progetto astratto (la "fabbrica" o lo stampo).
# - OGGETTO: È la singola istanza concreta creata a partire da quel modello.


# --- 1. DEFINIZIONE DI UNA CLASSE E IL METODO __init__ ---

# Per definire una classe si usa la parola chiave 'class' con il nome in PascalCase (iniziali maiuscole).

class Auto:
    # Il metodo speciale __init__ è il COSTRUTTORE della classe.
    # Viene eseguito automaticamente ogni volta che creiamo un nuovo oggetto.
    # Il parametro 'self' rappresenta l'istanza specifica dell'oggetto che si sta creando.
    
    def __init__(self, marca, modello, anno):
        # ATTRIBUTI DI ISTANZA: memorizzano i dati dell'oggetto
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.motore_acceso = False  # Valore di default

    # METODO DI ISTANZA: una funzione definita dentro la classe che agisce sugli attributi
    def accendi_motore(self):
        if not self.motore_acceso:
            self.motore_acceso = True
            print(f"Il motore della {self.marca} {self.modello} si è acceso!")
        else:
            print("Il motore è già acceso.")

    def descrivi(self):
        stato = "Accesa" if self.motore_acceso else "Spenta"
        return f"Auto: {self.marca} {self.modello} ({self.anno}) - Stato: {stato}"


# --- 2. CREAZIONE (ISTANZIARIONE) DI OGGETTI ---

# Creiamo due oggetti distinti (istanze) della classe Auto:
auto1 = Auto("Alfa Romeo", "Giulia", 2021)
auto2 = Auto("Fiat", "500", 2019)

# Accesso agli attributi degli oggetti:
print(auto1.marca)  # Output: Alfa Romeo
print(auto2.marca)  # Output: Fiat

# Chiamata ai metodi degli oggetti:
print(auto1.descrivi())
auto1.accendi_motore()
print(auto1.descrivi())


# --- 3. ATTRIBUTI DI CLASSE vs ATTRIBUTI DI ISTANZA ---

class Dipendente:
    # ATTRIBUTO DI CLASSE: condiviso da TUTTE le istanze della classe
    numero_totale_dipendenti = 0
    azienda = "Tech Solutions"

    def __init__(self, nome, stipendio):
        # ATTRIBUTI DI ISTANZA: unici per ciascun oggetto
        self.nome = nome
        self.stipendio = stipendio
        
        # Incrementiamo il contatore di classe ad ogni nuova creazione
        Dipendente.numero_totale_dipendenti += 1

d1 = Dipendente("Marco", 2500)
d2 = Dipendente("Elena", 3000)

print(f"\nDipendenti creati in {Dipendente.azienda}: {Dipendente.numero_totale_dipendenti}")


# --- 4. INCAPSULAMENTO (ATTRIBUTI PRIVATI) ---

# In Python non esistono veri e propri modificatori di accesso rigidi come 'private' in C++ o Java.
# Per convenzione:
# - Un underscore (_attributo): indica che l'attributo è PROTETTO (uso interno raccomandato).
# - Due underscore (__attributo): attiva il "Name Mangling" rendendo l'attributo PRIVATO.

class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        self.titolare = titolare
        self.__saldo = saldo_iniziale  # Attributo privato

    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"Depositati {importo}€. Nuovo saldo: {self.__saldo}€")

    # METODO GETTER: permette di leggere un attributo privato in modo controllato
    def get_saldo(self):
        return self.__saldo

conto = ContoBancario("Luca Rossi", 1000)
conto.deposita(500)
print("Saldo verificato tramite getter:", conto.get_saldo())

# Tentare di accedere direttamente ad __saldo genererebbe un AttributeError:
# print(conto.__saldo)  -> ERRORE!


# --- 5. EREDITARIETÀ (INHERITANCE) ---

# L'ereditarietà permette a una classe figli (derivata) di ereditare attributi e metodi 
# da una classe padre (base), favorendo il riuso del codice.

class Animale:  # Classe Padre
    def __init__(self, nome):
        self.nome = nome

    def verso(self):
        print("L'animale fa un verso generico.")

class Cane(Animale):  # Classe Figlia (eredita da Animale)
    def __init__(self, nome, razza):
        # Usa super() per richiamare il costruttore della classe padre
        super().__init__(nome)
        self.razza = razza

    # OVERRIDING: sovrascriviamo il metodo della classe padre per personalizzarlo
    def verso(self):
        print(f"{self.nome} (il Cane {self.razza}) fa: Bau Bau!")

mio_cane = Cane("Fido", "Pastore Tedesco")
mio_cane.verso()  # Output: Fido (il Cane Pastore Tedesco) fa: Bau Bau!


# --- 6. METODI SPECIALI (DUNDER METHODS) ---

# I metodi che iniziano e finiscono con doppio underscore (__metodo__) permettono
# di personalizzare il comportamento degli oggetti con funzioni built-in come print(), len(), ecc.

class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # __str__: definisce cosa viene stampato quando si passa l'oggetto a print() o str()
    def __str__(self):
        return f"'{self.titolo}' di {self.autore}"

    # __len__: definisce il valore restituito quando si usa len(oggetto)
    def __len__(self):
        return self.pagine

libro1 = Libro("1984", "George Orwell", 328)

print("\nStampa oggetto con __str__:", libro1)
print("Numero di pagine con __len__:", len(libro1))