

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


def top_ticker(screen, menuinfo):
    menu = ['[F3]-Chapter',
            '[F4]-Command',
            '[F5]-Company',
            '[F6]-RanksOn']

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

def get_roster( chapter, menuinfo):

    roster = []

    for command in chapter.commands:
        for company in command.companies:
            
            # Captains
            if menuinfo.show_captains == True:
                for captain in company.captains:
                    roster.append(captain)

            # Lieutenants
            if menuinfo.show_lieutenants == True:
                for lieutenant in company.lieutenants:
                    roster.append(lieutenant)

            # Sargeants
            if menuinfo.show_sargeants == True:
                for sargeant in company.sargeants:
                    roster.append(sargeant)
                    
            # Dreads
            if menuinfo.show_techmarines == True:
                for techmarine in company.techmarines:
                    roster.append(techmarine)
                    
            if menuinfo.show_jr_techmarines == True:
                for jr_techmarine in company.jr_techmarines:
                    roster.append(jr_techmarine)
                    
            if menuinfo.show_apothecaries == True:
                for apothecary in company.apothecaries:
                    roster.append(apothecary)
                    
            if menuinfo.show_nurses == True:
                for nurse in company.nurses:
                    roster.append(nurse)

            if menuinfo.show_chaplains == True:
                for chaplain in company.chaplains:
                    roster.append(chaplain)
                    
            if menuinfo.show_jr_chaplains == True:
                for jr_chaplain in company.jr_chaplains:
                    roster.append(jr_chaplain)
                    
            if menuinfo.show_lexicanii == True:
                for lexicanius in company.lexicanii:
                    roster.append(lexicanius)
                    
            if menuinfo.show_adnuntii == True:
                for adnuntius in company.adnuntii:
                    roster.append(adnuntius)
                    
            if menuinfo.show_dreads == True:
                for dread in company.dreads:
                    roster.append(dread)
                    
            # Champions
            if menuinfo.show_champions == True:
                for champion in company.champions:
                    roster.append(champion)
                    
            # Ancients
            if menuinfo.show_ancients == True:
                for ancient in company.ancients:
                    roster.append(ancient)
                    
            # Honour Guards
            if menuinfo.show_honour_guards == True:
                for honour_guard in company.honour_guards:
                    roster.append(honour_guard)

            # Troopers
            if menuinfo.show_troopers == True:
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


def gui(screen, chapter):
    h, w = screen.getmaxyx()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    
    menuinfo = cls_menu_info(h-2)

    screen = top_ticker(screen,menuinfo)
    roster = get_roster(chapter, menuinfo)

    screen = print_roster(screen, roster, menuinfo)

    key = screen.getch()
    

def fluff_menu(chapter):
    """ This is the go func. Press button to go.
        called by program.py, Probably superfluous."""
    curses.wrapper(gui, chapter)




