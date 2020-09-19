

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
        self.show_lieutenants =    False
        self.show_captains =       True

        
        self.show_dreads =         True
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
        
    def F6_toggle_menu(self, screen):
        
        begin_x = 43
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


def print_about(screen):
    """ This prints the  file resources/about.txt"""

    screen.clear()

    about = Load_Namefile("resources/about.txt")
    for Index, line in enumerate(about):
        screen.addstr(Index + 2, 0, about[Index])

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


def top_ticker(screen, menuinfo):
    menu = ['[F3]-Chapter',
            '[F4]-Command',
            '[F5]-Company',
            '[F6]-Filters']

    screen.attron(curses.color_pair(1))
    screen.addstr(0, 0, "->:            :            :            :            :[F7]-Help:[F8]-Quit:")
    screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 0:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 3, menu[0])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 3, menu[0])
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 1:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 16, menu[1])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 16, menu[1])
        screen.attroff(curses.color_pair(1))

    if menuinfo.echelon == 2:
        screen.attron(curses.color_pair(2))
        screen.addstr(0, 29, menu[2])
        screen.attroff(curses.color_pair(2))
    else:
        screen.attron(curses.color_pair(1))
        screen.addstr(0, 29, menu[2])
        screen.attroff(curses.color_pair(1))

    screen.attron(curses.color_pair(1))
    screen.addstr(0, 42, menu[3])
    screen.attroff(curses.color_pair(1))

    return screen

def get_roster(chapter, menuinfo):
    roster = []


    # Captains
    if menuinfo.show_captains == True:
        for x in range(0 , 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for captain in company.captains:
                            roster.append(captain)

    # Lieutenants
    if menuinfo.show_lieutenants == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for lieutenant in company.lieutenants:
                            roster.append(lieutenant)

    # Sargeants
    if menuinfo.show_sargeants == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for sargeant in company.sargeants:
                            roster.append(sargeant)

    # Dreads
    if menuinfo.show_techmarines == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for techmarine in company.techmarines:
                            roster.append(techmarine)

    if menuinfo.show_jr_techmarines == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for jr_techmarine in company.jr_techmarines:
                            roster.append(jr_techmarine)

    if menuinfo.show_apothecaries == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for apothecary in company.apothecaries:
                            roster.append(apothecary)

    if menuinfo.show_nurses == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for nurse in company.nurses:
                            roster.append(nurse)

    if menuinfo.show_chaplains == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for chaplain in company.chaplains:
                            roster.append(chaplain)

    if menuinfo.show_jr_chaplains == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for jr_chaplain in company.jr_chaplains:
                            roster.append(jr_chaplain)

    if menuinfo.show_lexicanii == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for lexicanius in company.lexicanii:
                            roster.append(lexicanius)

    if menuinfo.show_adnuntii == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for adnuntius in company.adnuntii:
                            roster.append(adnuntius)

    if menuinfo.show_dreads == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for dread in company.dreads:
                            roster.append(dread)

    # Champions
    if menuinfo.show_champions == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for champion in company.champions:
                            roster.append(champion)

    # Ancients
    if menuinfo.show_ancients == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for ancient in company.ancients:
                            roster.append(ancient)

    # Honour Guards
    if menuinfo.show_honour_guards == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
                        for honour_guard in company.honour_guards:
                            roster.append(honour_guard)

    # Troopers
    if menuinfo.show_troopers == True:
        for x in range(0, 13):
            for command in chapter.commands:
                for company in command.companies:
                    if company.company_number == x:
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
        High = menuinfo.height

    # Display in [Selected], [Watchlist], or [Normal] colour modes.
    for x in range(0, High, +1):
        if menuinfo.roster_selection == x:
            screen.attron(curses.color_pair(2))
            screen.addstr(x+1, 0, roster[x+menuinfo.index].C_Get_Statline())
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
    screen.clear()
    screen = top_ticker(screen, menuinfo)

    roster = get_roster(chapter, menuinfo)
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
        key = screen.getch()

        if key == curses.KEY_F3:
            chapter.advance()

        elif key == curses.KEY_F4:
            for x in range(100):
                chapter.advance()
                if x % 5 == 0:
                    display_full_screen(screen, menuinfo, chapter)

        elif key == curses.KEY_F6:
            screen = menuinfo.F6_toggle_menu(screen)


        elif key == curses.KEY_F7:
            print_about(screen)

        elif key == curses.KEY_F8:
            keepgoing = False

        elif key == curses.KEY_UP:
            menuinfo.roster_selection -= 1

        elif key == curses.KEY_DOWN:
            menuinfo.roster_selection += 1

        elif key == curses.KEY_ENTER or key in [10 ,13]:
            roster = get_roster(chapter, menuinfo)
            screen = print_transcript(screen, roster[menuinfo.roster_selection])

        display_full_screen(screen, menuinfo, chapter)
        screen.refresh()
    

def fluff_menu(chapter):
    """ This is the go func. Press button to go.
        called by program.py, Probably superfluous."""
    curses.wrapper(gui, chapter)




