from initialize import Load_Namefile
from random import randint

# None of this is used at present within the Curses supported program.
# It still happens its just not shown.

class cls_vessel:
    def __init__(self, name, type, age, status):
        self.name = name
        self.type = type
        self.age = age
        self.status = status

class cls_assets:
    def __init__(self):
        self.fleet = self.Pop_Fleet()

    def Fleet_Update(self, Year):
        for ship in self.fleet:
            ship.age = ship.age + 10
            if randint(1, 200) == 1:
                ship.status = 1

        for x in range(len(self.fleet) - 1, 0, -1):
            if self.fleet[x].status == 1:
                self.fleet.pop(x)
        if (Year % 200) == 0:
            self.fleet.append(cls_vessel(self.Get_Vessel_Name(), "Strike Cruiser", randint(10, 50), 0))

    def Print_Fleet(self, Roster):
        for x in range(0, len(self.fleet)):
            name = Roster[0][x].fname + " " + Roster[0][x].lname
            print("{:5d}:{:22s} : {:20s} : {:>20s} : {:20s}".format(self.fleet[x].age, self.fleet[x].name, self.fleet[x].type,
                                                                    Roster[0][x].title, name))
        return

    def Pop_Fleet(self):
        Fleet = []
        Fleet.append(cls_vessel(self.Get_Vessel_Name(), "Holy Battle Barge", randint(10, 50), 0))
        for _ in range(10):
            Fleet.append(cls_vessel(self.Get_Vessel_Name(), "Strike Cruiser", randint(10, 50), 0))
        return Fleet

    def Get_Vessel_Name(self):
        namelist = Load_Namefile('resources/vessel_names.txt')
        return namelist[randint(0, len(namelist) - 1)]