class Animals:
    name = 'Name'
    weight = 0
    speech = 'Speech'
    gives_product = 0
    hungry = True


    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


    def collect_product(self, volume_product):
        self.volume_product -= gives_product


    def food(self, feed):
        sele.hungry = Folse
        sele.weight += feed


class Geese(Animals):
   speech = 'Га-га'
   gives_product = 1    #яйцо


class Cows(Animals):
    speech = 'Муу'
    gives_product = 25    #л молока


class Sheeps(Animals):
    speech = 'Бее'
    gives_product = 14   #кг шерсти


class Chickens(Animals):
    speech = 'Ко-ко-ко'
    gives_product = 1  #яйцо


class Goats(Animals):
    speech = 'Мее'
    gives_product = 3  #л молока


class Ducks(Animals):
    speech = 'Кря-кря'
    gives_product = 1  #кг мяса


goose_1 = Geese('Серый', 3)
goose_2 = Geese('Белый', 2)
cow = Cows('Манька', 500)
sheep_1 = Sheeps('Барашек', 80)
sheep_2 = Sheeps('Кудрявый', 120)
chicken_1 = Chickens('Ко-ко', 1)
chicken_2 = Chickens('Кукареку', 2)
goat_1 = Goats('Рога', 60)
goat_2 = Goats('Копыта', 70)
duck = Ducks('Кряква', 1)


animal_list = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]


total_weight = 0
max_weight = 0
heaviest_animal = str()
for animal in animal_list:
  total_weight += animal.weight
  if animal.weight > max_weight:
    max_weight = animal.weight
    heaviest_animal = animal.name
print('Суммарный вес всех животных {} кг'.format(total_weight))
print('Самое тяжелое животное зовут {}'.format(heaviest_animal))