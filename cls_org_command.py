from cls_org_company import cls_company

class cls_command:
    """ The purpose of this class is to reside in chapter.commands and hold a given number of companies."""
    def __init__(self, names, recruitment_source):
        self.name = names[0]
        #print(self.name + " created. <COMMAND>")
        self.companies = self.init_companies(names, recruitment_source)
        self.commander = []

        self.honoured = []
        self.dead_cnt =  0

    def init_companies(self, names, recruitment_source):
        company_list = []

        company_list.append(cls_company(recruitment_source, names[1], False))
        for x in range(3):
            company_list.append(cls_company(company_list[-1], names[x+2], False))

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