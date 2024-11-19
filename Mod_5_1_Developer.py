# Mod_5_1_Developer - не только разработчик

class House :
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(name,number_of_floors, 'этажа/этажей')

    def go_to (self, new_floor):
        #print(self.name)
        self.new_floor = new_floor
        print('в ',self.name, 'нужно попасть на ', new_floor,'Этаж')
        if new_floor > self.number_of_floors or new_floor < 1:
            print('такого этажа несуществует')
        else:
            for i in range (1,new_floor +1) :
                print(i)



h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)
h2.go_to(0)