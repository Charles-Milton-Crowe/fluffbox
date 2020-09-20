from cls_org_company import cls_company

from initialize import Get_Letters

class cls_command:
    """ The purpose of this class is to reside in chapter.commands and hold a given number of companies."""

    def __init__(self, command_number, company_number, recruitment_source):
        self.command_number = command_number
        self.name = self.get_name()
        #print(self.name + " created. <COMMAND>")
        self.companies = self.init_companies(company_number, recruitment_source)
        self.commander = []

        self.honoured = []
        self.dead_cnt =  0


    def init_companies(self, company_number, recruitment_source):
        company_list = []

        company_list.append(cls_company(recruitment_source, company_number, False))
        for x in range(3):
            company_list.append(cls_company(company_list[-1], company_number -3 - (x*3), False))

        company_list.reverse()
        return company_list

    def get_command_roster(self):
        roster = []
        for company in self.companies:
            roster.extend(company.get_roster())
        return roster

    def roll_fate(self):
        """ Calls the fate_roll() for each company, collects honoured dead, and dead counts."""
        #print("Command fate_roll()" + self.name)

        self.honoured = []
        self.dead_cnt = 0

        for company in self.companies:
            company.roll_fate()
            self.dead_cnt += company.dead_cnt

            for marine in company.honoured:
                self.honoured.append(marine)

    def get_name(self):
        return "{:>4} Crusade Fleet".format(Get_Letters(self.command_number))
