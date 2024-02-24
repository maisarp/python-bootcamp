# Sistema para adoção de gatinhos 

from abc import ABC, abstractmethod

class Animal(ABC): 
    def __init__(self, nome, idade, cor): #<--- costrutor (diz o qu ele precisa ter pra ser criado) 
        # __ = totalmente privado (só devem ser acessados dentro da classe)
        # _ = privado || não público (não deve ser acessado fora da classe)
        #    = publico

        self.__nome = nome
        self.__idade = idade
        self.__cor = cor

    def get_nome(self): #get = método/comportamento
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_cor(self):
        return self.__cor
    
    @abstractmethod
    def fazer_som(self): #metodo abstrato que deve ser implementado nas subclasses
        pass

# Herança simples
class Gato(Animal):
    def __init__(self, nome, idade, cor, raca):
        super().__init__(nome, idade, cor)
        self.__raca = raca 
    
    def get_raca(self):
        return self.__raca
    
    def fazer_som(self):
        return "Miau"
    
       
        #self permite que os comportamentos acessem os valores/atributos // aponta para os valores (ponteiro?)

# Herança múltipla

class Adotante:
    def __init__(self, nome):
        self.nome = nome

class AdocaoGatinho:
    def __init__(self, animal, adotante):
        self.animal = animal
        self.adotante = adotante
    
animal01 = Animal("Maker", 2, "branco")
adotante01 = Adotante("Isadora")

# Criar uma instância de adoção
adocao01 = AdocaoGatinho(animal01, adotante01)

print("Nome do gatinho:", adocao01.animal.get_nome())
print("Idade do gatinho adotado:", adocao01.animal.get_idade())
print("Nome do adotante:", adocao01.adotante.nome)

#gatinho1 = Animal("Bolinha", 2, "branco") # 1ºanimal criado, gatinho1 é um OBJETO da classe animal com os atributos NOME, IDADE E COR
#gatinho2 = Animal("Python", 30, "verde")
#gatinho3 = Gato("Frajola", 3, "Preto e Branco", "Vira-lata")
#print(gatinho2.get_nome())
#print(gatinho2.get_cor())
#print(gatinho3.get_raca())