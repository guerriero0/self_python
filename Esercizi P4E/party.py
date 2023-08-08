'''stuff = list()
stuff.append("a")
print(dir(stuff))
print(stuff.__getitem__(0))'''

# stuff è un oggetto di tipo lista creato tramite funzione list(),
# ad un oggetto di tipo lista sono associate alcune funzioni che chiameremo
# metodi

'''class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)

print("Type", type(an))
print("Dir", type(an))
print("Type", type(an.x))
print("Type", type(an.party()))'''

'''class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far',self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)'''





class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self) :
        self.x = self.x + 1
        print(self.name,'party count',self.x)

'''s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
s.party()
j.party()
s.party()'''


