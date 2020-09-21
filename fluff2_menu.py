

from initialize import Load_Namefile

import curses


class cls_menu_info:
    def __init__(self, height ):
        self.height = height

        self.echelon = 0
        self.echelon_selection = 0
        self.index = 0
        self.roster_selection = 0

        self.show_troopers =       False
        self.show_sargeants =      False
        self.show_lieutenants =    True
        self.show_captains =       True
        
        self.show_dreads =         False
        self.show_techmarines =    False
        self.show_jr_techmarines = False
        self.show_apothecaries =   False
        self.show_nurses =         False
        self.show_chaplains =      False
        self.show_jr_chaplains =   False
        self.show_lexicanii =      False
        self.show_adnuntii =       False

        self.show_honour_guards =  False
        self.show_ancients =       False
        self.show_champions =      False

        self.show_companies = []
        self.show_companies.append(False) # Vet
        self.show_companies.append(True)  # 1st
        self.show_companies.append(True)  # 2
        self.show_companies.append(True)  # 3
        self.show_companies.append(True)  # 4
        self.show_companies.append(True)  # 5
        self.show_companies.append(True)  # 6
        self.show_companies.append(False)  # 7
        self.show_companies.append(False)  # 8
        self.show_companies.append(False)  # 9
        self.show_companies.append(False)  # 10
        self.show_companies.append(False)  # 11
        self.show_companies.append(False)  # 12

        self.honour_toggle = False
        
    def F6_toggle_menu(self, screen):
        
        begin_x = 42
        begin_y = 1
        height = 18
        width = 18

        self.rank_list = ["Captains     ",
                          "Lieutenants  ",
                          "Sargeants    ",
                          "Troopers     ",
                          "Dreads       ",
                          "Techmarines  ",
                          "Jr. Techs    ",
                          "Apothecaries ",
                          "Nurses       ",
                          "Chaplains    ",
                          "Jr. Chaps    ",
                          "Lexicanii    ",
                          "Adnuntii     ",
                          "Honour_Guards",
                          "Ancients     ",
                          "Champions    "]
        self.rank_dict = {1:self.show_captains,
                          2:self.show_lieutenants,
                          3:self.show_sargeants,
                          4:self.show_troopers,
                          5:self.show_dreads,
                          6:self.show_techmarines,
                          7:self.show_jr_techmarines,
                          8:self.show_apothecaries,
                          9:self.show_nurses,
                          10:self.show_chaplains,
                          11:self.show_jr_chaplains,
                          12:self.show_lexicanii,
                          13:self.show_adnuntii,
                          14:self.show_honour_guards,
                          15:self.show_ancients,
                          16:self.show_champions}

        self.menu_window = curses.newwin(height, width, begin_y, begin_x)
        self.menu_selection = 1

        keepgoing = True
        while keepgoing == True:

            self.F6_toggle_menu_update(width)
            key = screen.getch()
            if key == curses.KEY_F2:
                pass

            elif key == curses.KEY_UP:
                if self.menu_selection > 1:
                    self.menu_selection -= 1

            elif key == curses.KEY_DOWN:
                if self.menu_selection < len(self.rank_list):
                    self.menu_selection += 1

            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.rank_dict[self.menu_selection] == True:
                    self.rank_dict[self.menu_selection] = False
                else:
                    self.rank_dict[self.menu_selection] = True

                if self.menu_selection == 1:
                    if self.show_captains == True:
                        self.show_captains = False
                    else:
                        self.show_captains = True
                elif self.menu_selection == 2:
                    if self.show_lieutenants == True:
                        self.show_lieutenants = False
                    else:
                        self.show_lieutenants = True
                elif self.menu_selection == 3:
                    if self.show_sargeants == True:
                        self.show_sargeants = False
                    else:
                        self.show_sargeants = True
                elif self.menu_selection == 4:
                    if self.show_troopers == True:
                        self.show_troopers = False
                    else:
                        self.show_troopers = True
                elif self.menu_selection == 5:
                    if self.show_dreads == True:
                        self.show_dreads = False
                    else:
                        self.show_dreads = True
                elif self.menu_selection == 6:
                    if self.show_techmarines == True:
                        self.show_techmarines = False
                    else:
                        self.show_techmarines = True
                elif self.menu_selection == 7:
                    if self.show_jr_techmarines == True:
                        self.show_jr_techmarines = False
                    else:
                        self.show_jr_techmarines = True
                elif self.menu_selection == 8:
                    if self.show_apothecaries == True:
                        self.show_apothecaries = False
                    else:
                        self.show_apothecaries = True
                elif self.menu_selection == 9:
                    if self.show_nurses == True:
                        self.show_nurses = False
                    else:
                        self.show_nurses = True
                elif self.menu_selection == 10:
                    if self.show_chaplains == True:
                        self.show_chaplains = False
                    else:
                        self.show_chaplains = True
                elif self.menu_selection == 11:
                    if self.show_jr_chaplains == True:
                        self.show_jr_chaplains = False
                    else:
                        self.show_jr_chaplains = True
                elif self.menu_selection == 12:
                    if self.show_lexicanii == True:
                        self.show_lexicanii = False
                    else:
                        self.show_lexicanii = True
                elif self.menu_selection == 13:
                    if self.show_adnuntii == True:
                        self.show_adnuntii = False
                    else:
                        self.show_adnuntii = True
                elif self.menu_selection == 14:
                    if self.show_honour_guards == True:
                        self.show_honour_guards = False
                    else:
                        self.show_honour_guards = True
                elif self.menu_selection == 15:
                    if self.show_ancients == True:
                        self.show_ancients = False
                    else:
                        self.show_ancients = True
                elif self.menu_selection == 16:
                    if self.show_champions == True:
                        self.show_champions = False
                    else:
                        self.show_champions = True


            elif key == curses.KEY_F6:
                keepgoing = False
        
        return screen
    def F6_toggle_menu_update(self, width):
        cnt = 1
        for rank in self.rank_list:

            if self.rank_dict[cnt] == True:
                button = "[X]"
            else:
                button = "[ ]"

            if self.menu_selection == cnt:
                self.menu_window.attron(curses.color_pair(2))
                self.menu_window.addstr(cnt, 1, rank)
                self.menu_window.addstr(cnt, width - 4, button)
                self.menu_window.attroff(curses.color_pair(2))

            else:
                self.menu_window.attron(curses.color_pair(1))
                self.menu_window.addstr(cnt, 1, rank)
                self.menu_window.addstr(cnt, width - 4, button)
                self.menu_window.attroff(curses.color_pair(1))
            cnt += 1
        self.menu_window.attron(curses.color_pair(1))
        self.menu_window.border()
        self.menu_window.attroff(curses.color_pair(1))
        self.menu_window.refresh()

    def F5_toggle_menu(self, screen):

        begin_x = 29
        begin_y = 1
        height = 16
        width = 20

        self.company_list = [" Com - Command ",
                             " Vet - Veteran ",
                             " 1st - First   ",
                             " 2nd - Second  ",
                             " 3rd - Third   ",
                             " 4th - Fourth  ",
                             " 5th - Fifth   ",
                             " 6th - Sixth   ",
                             " 7th - Seventh ",
                             " 8th - Eighth  ",
                             " 9th - Ninth   ",
                             "10th - Tenth   ",
                             "11th - Eleventh",
                             "12th - Twelfth "]

        self.menu_window = curses.newwin(height, width, begin_y, begin_x)
        self.menu_selection = -1

        keepgoing = True
        while keepgoing == True:

            self.F5_toggle_menu_update(width)
            key = screen.getch()
            if key == curses.KEY_F2:
                pass

            elif key == curses.KEY_UP:
                if self.menu_selection > -1:
                    self.menu_selection -= 1

            elif key == curses.KEY_DOWN:
                if self.menu_selection < len(self.company_list):
                    self.menu_selection += 1

            elif key == curses.KEY_ENTER or key in [10, 13]:
                if self.show_companies[self.menu_selection] == True:
                    self.show_companies[self.menu_selection] = False
                else:
                    self.show_companies[self.menu_selection] = True

            elif key == curses.KEY_F5:
                keepgoing = False

        return screen
    def F5_toggle_menu_update(self, width):
        cnt = -1
        for company in self.company_list:

            if self.show_companies[cnt] == True:
                button = "[X]"
            else:
                button = "[ ]"

            if self.menu_selection == cnt:
                self.menu_window.attron(curses.color_pair(2))
                self.menu_window.addstr(cnt+2, 1, company)
                self.menu_window.addstr(cnt+2, width - 4, button)
                self.menu_window.attroff(curses.color_pair(2))

            else:
                self.menu_window.attron(curses.color_pair(1))
                self.menu_window.addstr(cnt+2, 1, company)
                self.menu_window.addstr(cnt+2, width - 4, button)
                self.menu_window.attroff(curses.color_pair(1))
            cnt += 1
        self.menu_window.attron(curses.color_pair(1))
        self.menu_window.border()
        self.menu_window.attroff(curses.color_pair(1))
        self.menu_window.refresh()

    def get_selectindex(self):
        return self.roster_selection + self.index



def print_about(screen, menuinfo, chapter):
    """ This prints the  file resources/about.txt"""

    screen.clear()

    about = Load_Namefile("resources/fluff2_about.txt")

    screen.clear()
    screen = top_ticker(screen, menuinfo, len(get_roster(chapter, menuinfo)))

    for Index, line in enumerate(about):
        screen.addstr(Index+1, 0, about[Index])

    screen = bottom_ticker(screen, menuinfo, chapter)
    screen.refresh()
    key = screen.getch()

    return screen

def print_transcript(screen, marine):
    """ This displays the transcript of the currently selected marine."""

    screen.clear()

    #h, w = screen.getmaxyx()
    screen.addstr(1, 0, "Transcript for {}| Entries {}".format(marine.rank + " " + marine.name, len(marine.transcript)))
    screen.addstr(2, 0, "--------------------------------------------------------------------------------")

    for Index, line in enumerate(marine.transcript):
        screen.addstr(Index + 3, 0, marine.transcript[Index])

    key = screen.getch()
    screen.refresh()
    return screen


def top_ticker(screen, menuinfo, roster_length):
    menu = ['[F3]-10yrADV',
            '[F4]-Advance',
            '[F5]-Company',
            '[F6]-Filters']

    menu_stub = "->:            :            :            :            :[F7]-Help:[F8]-Quit:"
    menu_stub += "{}(S:{},I:{}){}".format(roster_length, menuinfo.roster_selection, menuinfo.index, menuinfo.roster_selection + menuinfo.index+1)

    screen.attron(curses.color_pair(1))
    screen.addstr(0, 0, menu_stub)
    screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 0:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 0, "->")
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 0, "->")
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 1:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 3, menu[0])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 3, menu[0])
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 2:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 16, menu[1])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 16, menu[1])
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 3:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 29, menu[2])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 29, menu[2])
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 4:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 42, menu[3])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 42, menu[3])
        screen.attroff(curses.color_pair(1))

    return screen

def get_roster(chapter, menuinfo):
    roster = []

    if menuinfo.honour_toggle == True:
        return chapter.honoured

    company_list = []

    if menuinfo.show_companies[0] == True:
        company_list.append(chapter.veteran_company)

    for x in range(0, 13):
        if menuinfo.show_companies[x] == True:
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        company_list.append(company)

    # Captains
    if menuinfo.show_captains == True:
        for company in company_list:
            for captain in company.captains:
                roster.append(captain)

    # Lieutenants
    if menuinfo.show_lieutenants == True:
        for company in company_list:
            for lieutenant in company.lieutenants:
                roster.append(lieutenant)

    # Sargeants
    if menuinfo.show_sargeants == True:
        for company in company_list:
            for sargeant in company.sargeants:
                roster.append(sargeant)

    # Dreads
    if menuinfo.show_dreads == True:
        for company in company_list:
            for dread in company.dreads:
                roster.append(dread)

    # Techmarine
    if menuinfo.show_techmarines == True:
        for company in company_list:
            for techmarine in company.techmarines:
                roster.append(techmarine)

    # Jr_Techmarines
    if menuinfo.show_jr_techmarines == True:
        for company in company_list:
            for jr_techmarine in company.jr_techmarines:
                roster.append(jr_techmarine)

    # Apothecaries
    if menuinfo.show_apothecaries == True:
        for company in company_list:
            for apothecary in company.apothecaries:
                roster.append(apothecary)

    # Nurses
    if menuinfo.show_nurses == True:
        for company in company_list:
            for nurse in company.nurses:
                roster.append(nurse)

    # Chaplains
    if menuinfo.show_chaplains == True:
        for company in company_list:
            for chaplain in company.chaplains:
                roster.append(chaplain)

    # Jr_Chaplains
    if menuinfo.show_jr_chaplains == True:
        for company in company_list:
            for jr_chaplain in company.jr_chaplains:
                roster.append(jr_chaplain)

    # Lexicanii
    if menuinfo.show_lexicanii == True:
        for company in company_list:
            for lexicanius in company.lexicanii:
                roster.append(lexicanius)

    if menuinfo.show_adnuntii == True:
        for company in company_list:
            for adnuntius in company.adnuntii:
                roster.append(adnuntius)

    # Champions
    if menuinfo.show_champions == True:
        for company in company_list:
            for champion in company.champions:
                roster.append(champion)

    # Ancients
    if menuinfo.show_ancients == True:
        for company in company_list:
            for ancient in company.ancients:
                roster.append(ancient)

    # Honour Guards
    if menuinfo.show_honour_guards == True:
        for company in company_list:
            for honour_guard in company.honour_guards:
                roster.append(honour_guard)

    # Troopers
    if menuinfo.show_troopers == True:
        for company in company_list:
            for trooper in company.troopers:
                roster.append(trooper)

    return roster

def print_roster(screen, roster, menuinfo):
    """ This is the heart of the roster display """

    h, w = screen.getmaxyx()

    """ Determines how many marines to display. If the list is short then that is how many are displayed.
        If the list is long. It will fill the screen instead."""
    if len(roster) < h-2:
        High = len(roster)-1
    else:
        High = menuinfo.height -1

    # Display in [Selected], [Watchlist], or [Normal] colour modes.
    for x in range(0, High + 1, +1):
        if menuinfo.roster_selection == x:
            screen.attron(curses.color_pair(2))
            screen.addstr(x + 1, 0, roster[x + menuinfo.index].C_Get_Statline())
            screen.attroff(curses.color_pair(2))

        elif roster[x+menuinfo.index].watchlist is True:
            screen.attron(curses.color_pair(3))
            screen.addstr(x + 1, 0, roster[x + menuinfo.index].C_Get_Statline())
            screen.attroff(curses.color_pair(3))
        else:
            screen.addstr(x+1, 0, roster[x+menuinfo.index].C_Get_Statline())

    return screen

def bottom_ticker(screen, menuinfo, chapter):
    """ This displays the bottom ticker. Used for chapter stats."""

    name = "The " + chapter.name
    Ticker = "{:^20s}-  Year:{:5d}  Dead: {:<6d}  Honoured: {:<4d}  Starships:1+{}".format(name,
                                                                                                        chapter.year,
                                                                                                        chapter.dead_cnt,
                                                                                                        len(chapter.honoured),
                                                                                                        len(chapter.assets.fleet) - 1)
    screen.attron(curses.color_pair(1))
    h, w = screen.getmaxyx()
    screen.addstr(h - 1, 0, Ticker)
    screen.attroff(curses.color_pair(1))
    return screen

def display_full_screen(screen, menuinfo, chapter):
    roster = get_roster(chapter, menuinfo)

    screen.clear()
    screen = top_ticker(screen, menuinfo, len(roster))


    screen = print_roster(screen, roster, menuinfo)

    screen = bottom_ticker(screen, menuinfo, chapter)
    screen.refresh()
    return screen

def gui(screen, chapter):
    h, w = screen.getmaxyx()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    menuinfo = cls_menu_info(h-2)

    display_full_screen(screen, menuinfo, chapter)

    keepgoing = True
    while keepgoing:
        roster_length = len(get_roster(chapter, menuinfo))
        key = screen.getch()

        if key == curses.KEY_F2:
            if menuinfo.honour_toggle == True:
                menuinfo.honour_toggle = False
            else:
                menuinfo.honour_toggle = True

        if key == curses.KEY_F3:
            chapter.advance()

        elif key == curses.KEY_F4:
            menuinfo.echelon = 2
            for x in range(100):
                chapter.advance()
                if x % 5 == 0:
                    display_full_screen(screen, menuinfo, chapter)
            menuinfo.echelon = 0

        elif key == curses.KEY_F5:
            menuinfo.echelon = 3
            display_full_screen(screen, menuinfo, chapter)
            screen.refresh()
            screen = menuinfo.F5_toggle_menu(screen)
            menuinfo.echelon = 0
        elif key == curses.KEY_F6:
            menuinfo.echelon = 4
            display_full_screen(screen, menuinfo, chapter)
            screen.refresh()
            screen = menuinfo.F6_toggle_menu(screen)
            menuinfo.echelon = 0


        elif key == curses.KEY_F7:
            print_about(screen, menuinfo, chapter)

        elif key == curses.KEY_F8:
            keepgoing = False

        ####################################################################

        elif key == curses.KEY_UP:
            if menuinfo.roster_selection > 0 or menuinfo.index > 0:
                if menuinfo.roster_selection < 4 and menuinfo.index > 0:
                    menuinfo.index -= 1
                else:
                    menuinfo.roster_selection -= 1

        elif key == curses.KEY_DOWN:

            if menuinfo.get_selectindex() < (roster_length - 1):
                if menuinfo.roster_selection > menuinfo.height - 4 and \
                        menuinfo.index < (roster_length - menuinfo.height + 2):
                    menuinfo.index += 1
                else:
                    menuinfo.roster_selection += 1

                if menuinfo.index > (roster_length - menuinfo.height) and roster_length > menuinfo.height:
                    menuinfo.index -= 1
                    menuinfo.roster_selection += 1


        elif key == curses.KEY_ENTER or key in [10 ,13]:
            roster = get_roster(chapter, menuinfo)
            screen = print_transcript(screen, roster[menuinfo.roster_selection + menuinfo.index])

        ####################################################################

        elif key == curses.KEY_HOME:
            menuinfo.roster_selection = 0
            menuinfo.index = 0
            
        elif key == curses.KEY_END:
            if menuinfo.height > roster_length:
                menuinfo.roster_selection = roster_length - 1
            else:
                menuinfo.roster_selection = menuinfo.index + menuinfo.height - 1
                menuinfo.index = (roster_length) - (menuinfo.height)

        elif key == curses.KEY_PPAGE:
            menuinfo.index -= menuinfo.height
            menuinfo.roster_selection = 0

            if menuinfo.index < 0:
                menuinfo.index = 0

        elif key == curses.KEY_NPAGE:
            if menuinfo.height > roster_length:
                menuinfo.roster_selection = roster_length - 1
            else:
                menuinfo.index += menuinfo.height
                menuinfo.roster_selection = 25
                if menuinfo.index > (roster_length - 1) - (menuinfo.height - 1):
                    menuinfo.index = (roster_length) - (menuinfo.height)
                    menuinfo.roster_selection = menuinfo.height - 1


        """elif key == ord(' '):
            roster = get_roster(chapter, menuinfo)
            roster[menuinfo.roster_selection].Toggle_Watchlist()"""

        display_full_screen(screen, menuinfo, chapter)
        screen.refresh()
    

def fluff_menu(chapter):
    """ This is the go func. Press button to go.
        called by program.py, Probably superfluous."""
    curses.wrapper(gui, chapter)
