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
        self.gives_product -= volume_product

    def food(self, feed):
        self.hungry = False
        self.weight += feed


class Goose(Animals):
    speech = 'Га-га'
    gives_product = 1  # яйцо


class Cow(Animals):
    speech = 'Муу'
    gives_product = 25  # л молока


class Sheep(Animals):
    speech = 'Бее'
    gives_product = 14  # кг шерсти


class Chicken(Animals):
    speech = 'Ко-ко-ко'
    gives_product = 1  # яйцо


class Goat(Animals):
    speech = 'Мее'
    gives_product = 3  # л молока


class Duck(Animals):
    speech = 'Кря-кря'
    gives_product = 1  # кг мяса


goose_1 = Goose('Серый', 3)
goose_2 = Goose('Белый', 2)
cow = Cow('Манька', 500)
sheep_1 = Sheep('Барашек', 80)
sheep_2 = Sheep('Кудрявый', 120)
chicken_1 = Chicken('Ко-ко', 1)
chicken_2 = Chicken('Кукареку', 2)
goat_1 = Goat('Рога', 60)
goat_2 = Goat('Копыта', 70)
duck = Duck('Кряква', 1)

goose_1.collect_product(3)
goose_2.collect_product(3)
cow.collect_product(25)
sheep_1.collect_product(14)
sheep_2.collect_product(14)
chicken_1.collect_product(1)
chicken_2.collect_product(1)
goat_1.collect_product(3)
goat_2.collect_product(3)
duck.collect_product(1)

goose_1.food(1)
goose_2.food(1)
cow.food(10)
sheep_1.food(5)
sheep_2.food(5)
chicken_1.food(1)
chicken_2.food(1)
goat_1.food(3)
goat_2.food(3)
duck.food(1)

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
