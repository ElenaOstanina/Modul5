class House:
    def __inint__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):

        if new_floor < 1:
            print("Такого этажа не существует")

        else:
            i = 1
            while i <= new_floor:
                print(" ")
                print(i, end=" ")
                i += 1

    go_to("Этаж", 6)
    print(" ")

max = House()
max.name = "Max"
max.number_of_floors = 25



