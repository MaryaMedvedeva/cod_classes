class Human:
    def __init__(self, name, age, pet_species, pet_name):
        self.name = name
        self.age = age
        self.pet = Animal(pet_species, pet_name)

    def speak(self, message):
        print(f"{self.name}: {message}")

    def introduce(self):
        print(f"Привіт! Мене звуть {self.name}. Мені {self.age} років.")
        print(f"У мене є тваринний друг. Його/її звуть {self.pet.name}, і це {self.pet.species}.")

    def interact_with_pet(self):
        print(f"{self.name}, у вас є {self.pet.species} з ім'ям {self.pet.name}.")
        for i in range(6):
            print(f"Раунд {i + 1}: виберіть дію для взаємодії з твариною:")
            print("1 - погодувати")
            print("2 - пограти")
            print("3 - відпочити")
            action = input()

            if action == "1":
                self.pet.react_to_action("погодувати")
            elif action == "2":
                self.pet.react_to_action("пограти")
            elif action == "3":
                self.pet.react_to_action("відпочити")
            else:
                print("Недопустима дія! Спробуйте ще раз.")

            if self.pet.hunger == 2 and self.pet.boredom == 2:
                print(f"{self.pet.name} переїла і втомилася. Ви програли!")
                return
            elif self.pet.hunger == 2:
                print(f"{self.pet.name} переїла. Ви програли!")
                return
            elif self.pet.boredom == 2:
                print(f"{self.pet.name} втомилася. Ви програли!")
                return
            elif i == 5:
                print("Ви виграли!")

            if i < 5:
                print(f"Залишилося спроб: {5 - i - 1}")


class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def make_sound(self, sound):
        print(f"{self.name} видає звук: {sound}")

    def description(self):
        print(f"Це {self.species} звуть {self.name}.")

    def react_to_action(self, action):
        if action == "погодувати":
            self.hunger -= 1
            print(f"{self.name} покуштував.")
        elif action == "пограти":
            self.boredom -= 1
            print(f"{self.name} погрався.")
        elif action == "відпочити":
            self.hunger += 1
            self.boredom += 1
            print(f"{self.name} відпочив.")


def story_telling():
    player1_name = input("Введіть ім'я першої дійової особи: ")
    player1_age = int(input("Введіть вік першої дійової особи: "))
    player1_pet_species = input("Введіть вид тварини для першої дійової особи (Кішка, Собака, тощо): ")
    player1_pet_name = input("Введіть ім'я тварини для першої дійової особи: ")

    player2_name = input("Введіть ім'я другої дійової особи: ")
    player2_age = int(input("Введіть вік другої дійової особи: "))
    player2_pet_species = input("Введіть вид тварини для другої дійової особи (Кішка, Собака, тощо): ")
    player2_pet_name = input("Введіть ім'я тварини для другої дійової особи: ")

    player1 = Human(player1_name, player1_age, player1_pet_species, player1_pet_name)
    player2 = Human(player2_name, player2_age, player2_pet_species, player2_pet_name)

    print("----- Зустріч -----")
    player1.introduce()
    player2.introduce()

    print("----- Діалог -----")
    player1.speak(f"Привіт! Мене звати {player1.name}. Мені {player1_age} років. А тебе як звати?")
    player2.speak(f"Привіт! Мене зовуть {player2.name}. Мені {player2_age} років. Дуже приємно познайомитися!")
    player1.speak("Також приємно познайомитися!")

    print("----- Взаємодія з твариною -----")
    player1.interact_with_pet()
    player2.interact_with_pet()


story_telling()
