class Animal:
    #Atributo da classe
    planeta = "Terra"

    # Metodo da classe
    def nascer(self):
        print(f"Eu nasci no {self.planeta}")

    def comer(self):
        print("Estou comendo")

class Mamifero(Animal):
    def comer(self):
        print("Eu estou bebendo leite")
class Oviparos(Animal):

    def nascer(self):
        print(f"acabei de quebrar o ovo no {self.planeta}")
