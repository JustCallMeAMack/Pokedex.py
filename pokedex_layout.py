class Pokemon:
  def __init__(self, num, name, kind, ability):
    self.num = num
    self.name = name
    self.kind = kind
    self.ability = ability
  
  def display_info(self):
    print(f'Pokemon no.{self.num}')
    print(f'Name - {self.name}')
    print(f'Pokemon type(s) - {self.kind}')
    print(f'Abilites - {self.ability}')

Bulbasaur = Pokemon(num= 1, name= 'Bulbasaur', kind= ['Grass', 'Poison'], ability= 'Overgrow')
Charmander = Pokemon(num= 4, name= 'Charmander', kind= ['Fire'], ability= 'Blaze')
Squirtle = Pokemon(num= 7, name= 'Squirtle', kind= ['Water'], ability= 'Torrent')

class Evolution(Pokemon):
  def __init__(self, num, name, kind, ability, evolve):
    super().__init__(num, name, kind, ability)
    self.evolve = evolve
  def display_info(self):
    super().display_info()
    print(f'Pokemon no.{self.num}')
    print(f'Name - {self.name}')
    print(f'Pokemon type(s) - {self.kind}')
    print(f'Abilites - {self.ability}')
    print(f'Evolves into {self.evolve}')

Bulbasaur = Evolution(num= 1, name= 'Bulbasaur', kind= ['Grass', 'Poison'], ability= 'Overgrow', evolve= 'Ivysaur')
Charmander = Evolution(num= 4, name= 'Charmander', kind= ['Fire'], ability= 'Blaze', evolve= 'Charmeleon')
Squirtle = Evolution(num= 7, name= 'Squirtle', kind= ['Water'], ability= 'Torrent', evolve= 'Wartotle')

Bulbasaur.display_info()
Charmander.display_info()
Squirtle.display_info()

vulpix = Evolution(num= 37, name= "Vulpix", kind= ["Fire"], ability= ["Flash Fire"], evolve= 'Ninetails')
dragonair = Evolution(num= 149, name= "Dragonair", kind= ["Dragon"], ability= ["Shed Skin"], evolve='Dragonite')
magikarp = Evolution(num= 129, name= "Magikarp", kind= ["Water"], ability= ["Swift Swim"], evolve= 'Gyarados')

vulpix.display_info()
dragonair.display_info()
magikarp.display_info()
