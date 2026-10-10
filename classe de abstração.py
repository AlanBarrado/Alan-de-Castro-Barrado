print("Aula de abstração")
print("")

class Animal:

    def nome(self):
        print("Animal")

    def comida(self):
        print("Comida")

    def habitat(self):
        print("Terra")

class Cachorro(Animal):

    def nome(self):
        print("Cachorro")

    def comida(self):
        print("Ração")

    def habitat(self):
        print("Casa")

    def latir(self):
        print("Auau")

class Gato(Animal):

    def nome(self):
        print("Gato")

    def comida(self):
        print("Ração")

    def habitat(self):
        print("Casa")

    def latir(self):
        print("Miau")

animal = Animal()

animal.nome()
animal.comida()
animal.habitat()
print("")

cachorro = Cachorro()
print("Dados do cachorro")
cachorro.nome()
cachorro.comida()
cachorro.habitat()
print("")

gato = Gato()
print("Dados do gato")
gato.nome()
gato.comida()
gato.habitat()
print("")