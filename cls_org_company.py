

from cls_settings import cls_org_settings
from cls_marine import cls_marine

from initialize import Load_Namefile
from initialize import Get_Letters

from random import randint as rand


class cls_chapter_command:

    def __init__(self, input_company):
        self.chapter_master = []
        self.commanders = []
        self.input_company = input_company

    def init_command(self):
        while len(self.commanders) < 3:
            self.commanders.append(self.input_company.marine_requested('captain'))

        while len(self.chapter_master) == 0:
            self.chapter_master.append(self.commanders[0])
            self.commanders.pop(0)
            self.commanders.append(self.input_company.marine_requested('captain'))


class cls_company:
    """ This class is used to represent each company within cls_command"""
    def __init__(self, input_company, company_number, multi_input_mode):
        self.SETTINGS = cls_org_settings()
        self.year = 40000
        self.company_number = company_number
        self.name = self.get_name()
        #print(self.name + " created.")

        self.input_company = input_company
        self.multi_input_mode = multi_input_mode

        self.captains = []
        self.lieutenants = []
        self.sargeants = []
        self.troopers = []
        self.dreads = []

        self.techmarines = []
        self.jr_techmarines = []
        self.apothecaries = []
        self.nurses = []
        self.chaplains = []
        self.jr_chaplains = []
        self.lexicanii = []
        self.adnuntii = []

        self.honour_guards = []
        self.ancients = []
        self.champions = []

        self.dread_potentials = []
        self.honoured = []

        self.rank = {'trooper': self.troopers,
                     'sargeant': self.sargeants,
                     'lieutenant': self.lieutenants,
                     'captain': self.captains,
                     'dread': self.dreads,
                     'techmarine': self.techmarines,
                     'jr_techmarine': self.jr_techmarines,
                     'apothecary': self.apothecaries,
                     'nurse': self.nurses,
                     'chaplain': self.chaplains,
                     'jr_chaplain': self.jr_chaplains,
                     'lexicanium': self.lexicanii,
                     'adnuntius': self.adnuntii,
                     'honour_guard': self.honour_guards,
                     'ancient': self.ancients,
                     'champion': self.champions}
        self.rank_list = {'trooper',
                          'sargeant',
                          'lieutenant',
                          'captain',
                          'dread',
                          'jr_techmarine',
                          'techmarine',
                          'nurse',
                          'apothecary',
                          'jr_chaplain',
                          'chaplain',
                          'adnuntius',
                          'lexicanium',
                          'honour_guard',
                          'ancient',
                          'champion'}
        self.settings_dict = {'trooper': self.SETTINGS.COMPANY_MAX_TROOPERS,
                              'sargeant': self.SETTINGS.COMPANY_MAX_SARGEANTS,
                              'lieutenant': self.SETTINGS.COMPANY_MAX_LIEUTENANTS,
                              'captain': self.SETTINGS.COMPANY_MAX_CAPTAINS,
                              'dread': self.SETTINGS.COMPANY_MAX_DREADS,
                              'techmarine': self.SETTINGS.COMPANY_MAX_TECHMARINES,
                              'jr_techmarine': self.SETTINGS.COMPANY_MAX_JR_TECHMARINES,
                              'apothecary': self.SETTINGS.COMPANY_MAX_APOTHECARIES,
                              'nurse': self.SETTINGS.COMPANY_MAX_NURSES,
                              'chaplain': self.SETTINGS.COMPANY_MAX_CHAPLAINS,
                              'jr_chaplain': self.SETTINGS.COMPANY_MAX_JR_CHAPLAINS,
                              'lexicanium': self.SETTINGS.COMPANY_MAX_LEXICANII,
                              'adnuntius': self.SETTINGS.COMPANY_MAX_ADNUNTII,
                              'honour_guard': self.SETTINGS.COMPANY_MAX_HONOUR_GUARD,
                              'ancient': self.SETTINGS.COMPANY_MAX_ANCIENTS,
                              'champion': self.SETTINGS.COMPANY_MAX_CHAMPIONS
                              }
        self.fateroll_dict = {'trooper': self.SETTINGS.KIACHANCE_TROOPERS,
                              'sargeant': self.SETTINGS.KIACHANCE_SARGEANTS,
                              'lieutenant': self.SETTINGS.KIACHANCE_LIEUTENANTS,
                              'captain': self.SETTINGS.KIACHANCE_CAPTAINS,
                              'dread': self.SETTINGS.KIACHANCE_DREADS,
                              'jr_techmarine': self.SETTINGS.KIACHANCE_JR_TECHMARINES,
                              'techmarine': self.SETTINGS.KIACHANCE_TECHMARINES,
                              'nurse': self.SETTINGS.KIACHANCE_NURSES,
                              'apothecary': self.SETTINGS.KIACHANCE_APOTHECARIES,
                              'jr_chaplain': self.SETTINGS.KIACHANCE_JR_CHAPLAIN,
                              'chaplain': self.SETTINGS.KIACHANCE_CHAPLAIN,
                              'adnuntius': self.SETTINGS.KIACHANCE_ADNUNTII,
                              'lexicanium': self.SETTINGS.KIACHANCE_LEXICANII,
                              'honour_guard': self.SETTINGS.KIACHANCE_HONOUR_GUARDS,
                              'ancient': self.SETTINGS.KIACHANCE_ANCIENTS,
                              'champion': self.SETTINGS.KIACHANCE_CHAMPIONS}
        self.dreadchance_dict = {'trooper': self.SETTINGS.DREADCHANCE_TROOPERS,
                                 'sargeant': self.SETTINGS.DREADCHANCE_SARGEANTS,
                                 'lieutenant': self.SETTINGS.DREADCHANCE_LIEUTENANTS,
                                 'captain': self.SETTINGS.DREADCHANCE_CAPTAINS,
                                 'dread': self.SETTINGS.DREADCHANCE_DREADS,
                                 'jr_techmarine': self.SETTINGS.DREADCHANCE_JR_TECHMARINES,
                                 'techmarine': self.SETTINGS.DREADCHANCE_TECHMARINES,
                                 'nurse': self.SETTINGS.DREADCHANCE_NURSES,
                                 'apothecary': self.SETTINGS.DREADCHANCE_APOTHECARIES,
                                 'jr_chaplain': self.SETTINGS.DREADCHANCE_JR_CHAPLAIN,
                                 'chaplain': self.SETTINGS.DREADCHANCE_CHAPLAIN,
                                 'adnuntius': self.SETTINGS.DREADCHANCE_ADNUNTII,
                                 'lexicanium': self.SETTINGS.DREADCHANCE_LEXICANII,
                                 'honour_guard': self.SETTINGS.DREADCHANCE_HONOUR_GUARDS,
                                 'ancient': self.SETTINGS.DREADCHANCE_ANCIENTS,
                                 'champion': self.SETTINGS.DREADCHANCE_CHAMPIONS}
        self.ranknum_dict = {'trooper':      1,
                             'sargeant':      2,
                             'lieutenant':    3,
                             'captain':       4,
                             'dread':         5,
                             'techmarine':    6,
                             'jr_techmarine': 7,
                             'apothecary':    8,
                             'nurse':         9,
                             'chaplain':     10,
                             'jr_chaplain':  11,
                             'lexicanium':   12,
                             'adnuntius':    13,
                             'honour_guard': 14,
                             'ancient':      15,
                             'champion':     16}
        self.starting_age_dict = {'trooper':self.SETTINGS.STARTING_AGE_TROOPERS,
                                    'sargeant':self.SETTINGS.STARTING_AGE_SARGEANTS,
                                    'lieutenant':self.SETTINGS.STARTING_AGE_LIEUTENANTS,
                                    'captain':self.SETTINGS.STARTING_AGE_CAPTAINS,
                                    'dread':self.SETTINGS.STARTING_AGE_DREADS,
                                    'jr_techmarine':self.SETTINGS.STARTING_AGE_JR_TECHMARINES,
                                    'techmarine':self.SETTINGS.STARTING_AGE_TECHMARINES,
                                    'nurse':self.SETTINGS.STARTING_AGE_NURSES,
                                    'apothecary':self.SETTINGS.STARTING_AGE_APOTHECARIES,
                                    'jr_chaplain':self.SETTINGS.STARTING_AGE_JR_CHAPLAIN,
                                    'chaplain':self.SETTINGS.STARTING_AGE_CHAPLAIN,
                                    'adnuntius':self.SETTINGS.STARTING_AGE_ADNUNTII,
                                    'lexicanium':self.SETTINGS.STARTING_AGE_LEXICANII,
                                    'honour_guard':self.SETTINGS.STARTING_AGE_HONOUR_GUARDS,
                                    'ancient':self.SETTINGS.STARTING_AGE_ANCIENTS,
                                    'champion':self.SETTINGS.STARTING_AGE_CHAMPIONS}

        self.dead_cnt = 0
        self.butchers_bill = []

    def marine_requested(self, selected_type):
        """ The given rank is requested from the input chapter.
            This method is always called from another instance of the class, higher in the chain."""

        #print("{} has requested {} from".format(self.name, selected_type))

        """ If the requested rank is not available, 
            request the same rank from the next company in the chain"""
        if len(self.rank[selected_type]) == 0:
            return self.input_company.marine_requested(selected_type)

        else:
            marine = self.rank[selected_type][0]
            self.rank[selected_type].pop(0)

            if self.multi_input_mode == False:
                self.rank[selected_type].append(self.input_company.marine_requested(selected_type))
            else:
                choice = rand(0, len(self.input_company) - 1)
                self.rank[selected_type].append(self.input_company[choice].marine_requested(selected_type))

        return marine

    def reinforce_rank(self, selected_type):
        #print("Reinforcing {} with {}".format(self.name, selected_type.capitalize()))
        #time.sleep(.025)


        while len(self.rank[selected_type]) < self.settings_dict[selected_type]:
            if self.multi_input_mode == False:
                marine = self.input_company.marine_requested(selected_type)
                self.rank[selected_type].append(marine)
            else:
                choice = rand(0, len(self.input_company) - 1)
                marine = self.input_company[choice].marine_requested(selected_type)
                self.rank[selected_type].append(marine)

        if self.multi_input_mode == False:
            self.input_company.reinforce_rank(selected_type)
        else:
            for input in self.input_company:
                input.reinforce_rank(selected_type)

    def reinforce(self):

        for entry in ('trooper', 'sargeant', 'lieutenant', 'captain',
                      'dread', 'jr_techmarine' ,'techmarine', 'nurse', 'apothecary',
                      'jr_chaplain', 'chaplain',  'adnuntius', 'lexicanium',
                      'honour_guard', 'ancient', 'champion'):

            self.reinforce_rank(entry)


    def display_input(self):
        return "{:25} <- {:25}".format(self.name, self.input_company.name)

    def display_marines(self):
        print("{:25}-TRP:{:2},SGT:{:2},LTN:{:2},CAP:{:2}".format(self.name,len(self.troopers),
                                                                          len(self.sargeants),
                                                                          len(self.lieutenants),
                                                                          len(self.captains)
                                                                          ))

        print("{:25}-TEK:{:2},JTK:{:2},APO:{:2},NUR:{:2}".format("",len(self.techmarines),
                                                                    len(self.jr_techmarines),
                                                                    len(self.apothecaries),
                                                                    len(self.nurses)))

        print("{:25}-CHP:{:2},JCH:{:2},LEX:{:2},ADN:{:2}".format("",len(self.chaplains),
                                                                    len(self.jr_chaplains),
                                                                    len(self.lexicanii),
                                                                    len(self.adnuntii),
                                                                          ))
        print("{:25}-HON:{:2},ANC:{:2},CMP:{:2},DRD:{:2}".format("", len(self.honour_guards),
                                                                    len(self.ancients),
                                                                    len(self.champions),
                                                                    len(self.dreads)))

    def get_roster(self):
        roster = []

        for entry in ('trooper', 'sargeant', 'lieutenant', 'captain',
                      'dread', 'jr_techmarine', 'techmarine', 'nurse', 'apothecary',
                      'jr_chaplain', 'chaplain', 'adnuntius', 'lexicanium',
                      'honour_guard', 'ancient', 'champion'):

            for marine in self.rank[entry]:
                #marine.company_number = self.company_number
                roster.append(marine.C_Get_Statline())

        return roster

    def bestow_titles(self):
        pass

    def roll_fate(self):
        """ Rolls the fate of every marine in the company"""

        self.honoured = []
        self.butchers_bill = []
        self.dead_cnt = 0

        # For each listed rank..
        for type in ('trooper', 'sargeant', 'lieutenant', 'captain',
                     'dread', 'jr_techmarine' ,'techmarine', 'nurse', 'apothecary',
                     'jr_chaplain', 'chaplain',  'adnuntius', 'lexicanium',
                     'honour_guard', 'ancient', 'champion'):

            new_list = []
            # For each marine in that rank..

            for marine in self.rank[type]:
                marine.Advance_Age(self.year)

                if rand(1, 200) == 1:
                    marine.transcript.append("{}: Medal Awarded for Valour.".format(self.year))
                    marine.badges.add_badge("V", "Medal for Valour", "Yellow")
                    marine.xfactor += 3

                if rand(1, 150) == 1:
                    marine.transcript.append("{}: Bolter Discipline Medal awarded for marksmanship.".format(self.year))
                    marine.badges.add_badge("B", "Bolter Discipline", "Red")

                # Death is a 1 in X chance, where X is dependent on the given marines
                # rank. These values are stores in the SETTINGS for the company.
                if rand(1, self.fateroll_dict[marine.rank]) == 1:
                    self.dead_cnt += 1
                    marine.KIA = 1

                    marine.transcript.append("{}: KIA.".format(self.year))

                    # Dreadnought immersion -AVAILABILTY- is Dreadchance[based on rank] in Dread Chance Max
                    if (rand(1 ,self.SETTINGS.DREADCHANCEMAX) > self.dreadchance_dict[marine.rank]) \
                            and (marine.isDread() == False):

                        self.dread_potentials.append(marine)

                    self.butchers_bill.append(marine)
                else:
                    new_list.append(marine)

            # Update roster sans dead marines.

            # I dont know why the code requires this line and that huge elif block
            # to function correctly, but it does. I would think it would take either or.
            # But i am clearly mistaken.
            self.rank[type] = new_list

            # But this does.
            if self.ranknum_dict[type] == 1:
                self.troopers = new_list
            elif self.ranknum_dict[type] == 2:
                self.sargeants = new_list
            elif self.ranknum_dict[type] == 3:
                self.lieutenants = new_list
            elif self.ranknum_dict[type] == 4:
                self.captains = new_list
            elif self.ranknum_dict[type] == 5:
                self.dreads = new_list
            elif self.ranknum_dict[type] == 6:
                self.techmarines = new_list
            elif self.ranknum_dict[type] == 7:
                self.jr_techmarines = new_list
            elif self.ranknum_dict[type] == 8:
                self.apothecaries = new_list
            elif self.ranknum_dict[type] == 9:
                self.nurses = new_list
            elif self.ranknum_dict[type] == 10:
                self.chaplains = new_list
            elif self.ranknum_dict[type] == 11:
                self.jr_chaplains = new_list
            elif self.ranknum_dict[type] == 12:
                self.lexicanii = new_list
            elif self.ranknum_dict[type] == 13:
                self.adnuntii = new_list
            elif self.ranknum_dict[type] == 14:
                self.honour_guards = new_list
            elif self.ranknum_dict[type] == 15:
                self.ancients = new_list
            elif self.ranknum_dict[type] == 16:
                self.champions = new_list


        # forward all fowarded and created Dread potentials to input company
        for marine in self.dread_potentials:
            if self.multi_input_mode == False:
                self.input_company.dread_potentials.append(marine)
            else:
                choice = 0
                self.input_company[choice].dread_potentials.append(marine)

        self.dread_potentials = []

        # Test members of the butchers bill for Honourability
        for marine in self.butchers_bill:
            if self.ranknum_dict[marine.rank] == 1 and len(marine.badges.badges) > 2:
                self.honoured.append(marine)
            elif self.ranknum_dict[marine.rank] == 2 and len(marine.badges.badges) > 3:
                self.honoured.append(marine)
            elif self.ranknum_dict[marine.rank] == 3 and len(marine.badges.badges) > 2:
                self.honoured.append(marine)
            elif self.ranknum_dict[marine.rank] == 4 and len(marine.badges.badges) > 2:
                self.honoured.append(marine)

    def age_company(self):
        for type in ('trooper', 'sargeant', 'lieutenant', 'captain',
                 'dread', 'jr_techmarine' ,'techmarine', 'nurse', 'apothecary',
                 'jr_chaplain', 'chaplain',  'adnuntius', 'lexicanium',
                 'honour_guard', 'ancient', 'champion'):

            for marine in self.rank[type]:

                for x in range(self.starting_age_dict[type]):
                    marine.Advance_Age(self.year)

    def get_name(self):

        subtype_dict = {0:'Veteran',
                        1:'Assault',
                        2:'Assault',
                        3:'Assault',
                        4:'Battle',
                        5:'Battle',
                        6:'Battle',
                        7:'Reserves',
                        8:'Reserves',
                        9:'Reserves',
                        10:'Scouts',
                        11:'Scouts',
                        12:'Scouts',
                        }

        return "{:>4} Company: {}".format(Get_Letters(self.company_number), subtype_dict[self.company_number])
    def set_company_numbers(self):

        for entry in ('trooper', 'sargeant', 'lieutenant', 'captain',
                      'dread', 'jr_techmarine', 'techmarine', 'nurse', 'apothecary',
                      'jr_chaplain', 'chaplain', 'adnuntius', 'lexicanium',
                      'honour_guard', 'ancient', 'champion'):

            for marine in self.rank[entry]:
                marine.company_number = self.company_number


class cls_marine_generator:
    """ This class serves as the 'endcap' to the snakelike companies.
        marine_requested generated new troopers and handles the marines
        through rank changes."""

    def __init__(self, name):
        self.settings = cls_org_settings()
        self.name = name

        self.FNames = self.Pop_First_Namelist()
        self.LNames = self.Pop_Last_Namelist()

        self.sp_input_company = cls_company(self, 0, False)

        self.dread_potentials = []

        self.year = 40000


    def marine_requested(self, selected_type):
        """ This does all the magic"""

        type_dict = {'trooper':       1,
                     'sargeant':      2,
                     'lieutenant':    3,
                     'captain':       4,
                     'dread':         5,
                     'techmarine':    6,
                     'jr_techmarine': 7,
                     'apothecary':    8,
                     'nurse':         9,
                     'chaplain':     10,
                     'jr_chaplain':  11,
                     'lexicanium':   12,
                     'adnuntius':    13,
                     'honour_guard': 14,
                     'ancient':      15,
                     'champion':     16}

        if type_dict[selected_type] == 1:
            fname = self.FNames[rand(0, len(self.FNames) - 1)]
            lname = self.LNames[rand(0, len(self.LNames) - 1)]

            marine = cls_marine(selected_type, 40000, fname, lname)

            marine.transcript = [
                "{:d}: Accepted into the chapter as a battle-brother of the scout companies.".format(self.year)]

            return marine

        elif type_dict[selected_type] == 2:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Sargeant.".format(self.year))
        elif type_dict[selected_type] == 3:
            marine = self.sp_input_company.marine_requested('sargeant')
            marine.transcript.append("{:d}: Earned the rank of Lieutenant.".format(self.year))
        elif type_dict[selected_type] == 4:
            marine = self.sp_input_company.marine_requested('lieutenant')
            marine.transcript.append("{:d}: Earned the rank of Captain.".format(self.year))


        elif type_dict[selected_type] == 5:
            if len(self.dread_potentials) > 0:
                choice = rand(0, len(self.dread_potentials))
                marine = self.dread_potentials[choice]
                self.dread_potentials.pop(choice)
            else:
                marine = self.sp_input_company.marine_requested('trooper')


        elif type_dict[selected_type] == 6:
            marine = self.sp_input_company.marine_requested('jr_techmarine')
            marine.transcript.append("{:d}: Earned the rank of Tech-Marine.".format(self.year))
        elif type_dict[selected_type] == 7:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Jr. Tech-Marine.".format(self.year))
        elif type_dict[selected_type] == 8:
            marine = self.sp_input_company.marine_requested('nurse')
            marine.transcript.append("{:d}: Earned the rank of Apothecary.".format(self.year))
        elif type_dict[selected_type] == 9:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Nurse.".format(self.year))
        elif type_dict[selected_type] ==10:
            marine = self.sp_input_company.marine_requested('jr_chaplain')
            marine.transcript.append("{:d}: Earned the rank of Chaplain.".format(self.year))
        elif type_dict[selected_type] ==11:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Jr. Chaplain.".format(self.year))
        elif type_dict[selected_type] ==12:
            marine = self.sp_input_company.marine_requested('adnuntius')
            marine.transcript.append("{:d}: Earned the rank of Lexicanium.".format(self.year))
        elif type_dict[selected_type] ==13:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Adnuntius.".format(self.year))
        elif type_dict[selected_type] ==14:
            marine = self.sp_input_company.marine_requested('trooper')
            marine.transcript.append("{:d}: Earned the rank of Honour-Guard.".format(self.year))
        elif type_dict[selected_type] ==15:
            marine = self.sp_input_company.marine_requested('honour_guard')
            marine.transcript.append("{:d}: Earned the rank of Ancient.".format(self.year))
        elif type_dict[selected_type] ==16:
            marine = self.sp_input_company.marine_requested('ancient')
            marine.transcript.append("{:d}: Earned the rank of Champion.".format(self.year))

        marine.rank = selected_type
        return marine

    def reinforce(self):
        pass

    def reinforce_rank(self, selected_type):
        pass


    def roll_fate(self):
        pass

    def display_input(self):
        return "{:25}  <- (Source)".format(self.name)

    def Pop_First_Namelist(self):
        """ Loads and Coalates various first names into one namebook(2d list) """
        namelist = Load_Namefile("resources/first_names.txt")
        return namelist

    def Pop_Last_Namelist(self):
        """ Loads and Coalates various last names into one namebook(2d list) """
        namelist = Load_Namefile('resources/last_names.txt')
        return namelist

    def init_sp_input_company(self, input_company):
        # This is the hook in for the veteran company and the ranks above trooper.
        self.sp_input_company = input_company
