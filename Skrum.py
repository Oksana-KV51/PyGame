#Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта
# по этапам/или создать kanban доску для работы над данным проектом Общее описание:
#Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками.
# Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
#Требования:
#1. Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
#2. Игра должна быть реализована как консольное приложение.
#Классы:
#Класс `Hero`:
#- Атрибуты:
#- Имя (`name`)
#- Здоровье (`health`), начальное значение 100
#- Сила удара (`attack_power`), начальное значение 20
#- Методы:
#- `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
#- `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
#Класс `Game`:
#- Атрибуты:
#- Игрок (`player`), экземпляр класса `Hero`
#- Компьютер (`computer`), экземпляр класса `Hero`
#- Методы:
#- `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о
# каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.player.attack(self.computer)
                print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            else:
                self.computer.attack(self.player)
                print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            turn += 1

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


# Создание героев и начало игры
player_name = input("Введите имя вашего героя: ")
player_hero = Hero(player_name)
computer_hero = Hero("Компьютер")

game = Game(player_hero, computer_hero)
game.start()