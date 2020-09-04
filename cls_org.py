

from initialize import Load_Namefile

from cls_org_company import cls_marine_generator
from cls_org_company import cls_company
from cls_org_company import cls_chapter_command
from cls_org_command import cls_command

from cls_assets import cls_assets

from random import randint as rand

def date(year):
    """ Not in use. Designed to display years in 40k format ex M42.360"""
    millenium = year % 1000
    while year > 1000:
        year -= 1000        
    return "M{}.{}".format(millenium, year)

class cls_chapter:
    """ This is the work in progress analog to the cls_chapter found in
    cls_chapter.py"""
    def __init__(self, name):



        self.name = self.get_chapter_name()
        self.year = 40000

        # The organization framework for the chapter.
        # build_org_framework() builds it, display_commands whows how its connected.
        self.scout_source, self.commands, self.veteran_company, self.chapter_command = self.build_org_framework()

        self.honoured = []
        self.dead_cnt = 0
        self.cm_cnt = 1

        # Not currently used.
        self.assets = self.pop_assets()

        self.basic_epitaphs, self.complex_epitaphs = self.load_epitaphs()

        # This kicks off the entire chapter to populate.
        self.veteran_company.reinforce()
        self.chapter_command.init_command()

        self.age_chapter()


    def build_org_framework(self):
        """ This build the chapter org framework and returns it to the chapter __init__."""

        commands = []

        # Instantiate the Scout Generator
        scout_source = cls_marine_generator("Unblooded Scout Pool")

        # Instantiate the 3 Commands with 4 companies each.
        index = 1
        ending_company_number = 12
        for x in range(3, 0, -1):
            commands.append(cls_command(x, ending_company_number, scout_source))
            ending_company_number -= 1
            index += 5
        commands.reverse()

        # Instantiate the Veteran Company
        input_list = []
        input_list.append(commands[0].companies[0])
        input_list.append(commands[1].companies[0])
        input_list.append(commands[2].companies[0])
        veteran_company = (cls_company(input_list, 0, True))

        # Hook the Veteran Company into the Generator.
        scout_source.init_sp_input_company(veteran_company)

        # Instantiate the Chapter Command
        chapter_command = (cls_chapter_command(veteran_company))

        return scout_source, commands, veteran_company, chapter_command

    def display_commands(self):
        """ Displays the org framework in a much more user friendly way."""
        print("\nChapter Org Display\n".format())
        print("[Name of Company]            [Recruitment Source]")
        print("-------------------------------------------------")
        print("{:25} <- {}, {}, {}".format(self.veteran_company.name,
                                       self.veteran_company.input_company[0].name,
                                       self.veteran_company.input_company[1].name,
                                       self.veteran_company.input_company[2].name))

        for command in self.commands:
            print("\n{}".format(command.name))
            for company in command.companies:
                print(" {:25} <- {}".format(company.name, company.input_company.name))
        print()
        print(self.scout_source.display_input())
        print()

    def display_troop_strength(self):
        """ This is a temporary func to detect anomolies before all this gets
            hooked into the curses gui."""

        print("------------------------------------------------------------")
        self.veteran_company.display_marines()
        print("------------------------------------------------------------")

        for command in self.commands:
            for company in command.companies:
                company.display_marines()
                print("------------------------------------------------------------")


    def display_roster(self):
        """ Builds a roster. currently unused."""

        roster = []
        for command in self.commands:
            roster.extend(command.get_command_roster())

        for line in roster:
            print(line)

    def roll_fate(self):
        """ Calls roll_fate in veteran company and then in each command."""

        #print("Chapter fate_roll()")

        self.veteran_company.roll_fate()
        self.dead_cnt += self.veteran_company.dead_cnt
        for marine in self.veteran_company.honoured:
            self.honoured.append(marine)

        for command in self.commands:
            command.roll_fate()
            self.dead_cnt += command.dead_cnt
            for marine in command.honoured:
                marine.epitaph = self.get_epitaph()
                self.honoured.append(marine)
                
    def advance(self):
        """ One day.."""
        pass

    def pop_assets(self):
        """ This builds the initial Assets of the Chapter in the initialization sequence. Used once.
            Used only for fleets at present."""

        return cls_assets()

    def get_chapter_name(self):
        """ This loads the chapter_names.txt file and returns one for
            the chapter at initialization."""

        namelist = Load_Namefile('resources/chapter_names.txt')
        return namelist[rand(0, len(namelist) - 1)]

    def load_epitaphs(self):
        """ This calls the Load_Filename func to open the epitaphs and loads them into memory."""

        # Then the file is split into the basic and complex epitaphs.
        # These are initialized at chapter creation. Get_Epitaph is
        # used to generate an epitaph from these values.

        Basic_Epitaphs = []
        Complex_Epitaphs = []

        list = Load_Namefile('resources/epitaphs.txt')

        num = int(list[0])
        list.pop(0)

        for x in range(0, num - 1):
            Basic_Epitaphs.append(list[x])

        for _ in range(num):
            list.pop(0)

        for entry in list:
            Complex_Epitaphs.append(entry)

        return Basic_Epitaphs, Complex_Epitaphs

    def get_epitaph(self):
        """ This chooses an epitaph for the marine and is returned."""

        # 1 in 100 it is a basic epitaph.
        # Otherwise it is a complex epitaph
        #
        # Complex epitaph is chosen at random. then the first
        # value is appended with one of any additional values

        fateroll = rand(1, 100)
        if fateroll == 1:
            return self.basic_epitaphs[rand(0, len(self.basic_epitaphs) - 1)]
        else:
            string = self.complex_epitaphs[rand(0, len(self.complex_epitaphs) - 1)]
            new_string = string.split("#", )
            return new_string[0] + " " + new_string[rand(1, len(new_string) - 1)] + "."
    
    def age_chapter(self):
        """ This will age the founding chapter members the appropriate ammount."""

        self.veteran_company.age_company()
        for command in self.commands:
            for company in command.companies:
                company.age_company()













