# This whole file burns my eyes.

import curses
from initialize import Load_Namefile


class menu_info:
    """ Contains a few bits and bobs that need to be passed back and forth."""

    def __init__(self, selection, high, mod, active_roster):

        # The index of the currently selected marine.
        self.selection = selection

        # The number of marines that will be fit on screen.
        self.high = high

        # The starting index of the marines to be displayed.
        self.mod = mod

        # The currently selected Roster.
        # 0-Command, 1-Dread, 2-Armoury, 3-Apothecarion, 4-Reclusiam, 5-Librarius, 6-Veterans.
        # [-1 Honour Roll]
        # 11-20 Company composite Roster.
        self.active_roster = active_roster



def print_about(screen):
    """ This prints the  file resources/about.txt"""

    about = Load_Namefile("resources/about.txt")
    for Index, line in enumerate(about):
        screen.addstr(Index + 2, 0, about[Index])

    return screen

def print_F5Menu(screen, roster_choice):
    """ Displays a menu for changing active_roster.
        This feels jankey but I dont know how to do it better at the moment."""

    begin_x = 32
    begin_y = 1
    height = 6
    width = 22
    dropdown = curses.newwin(height, width, begin_y, begin_x)

    dropdown.addstr(1, 1, "[F3]-Command Roster")
    dropdown.addstr(2, 1, "[F4]-Company Roster")
    dropdown.addstr(3, 1, "[F5]-Specialist")
    dropdown.addstr(4, 1, "[F6]-Honour Roll")
    dropdown.border()
    dropdown.refresh()

    key = screen.getch()

    if key == curses.KEY_F2:
        pass
    elif key == curses.KEY_F3:
        roster_choice = 0

    elif key == curses.KEY_F4:
        if roster_choice < 7:
            roster_choice = 11
        elif roster_choice >= 11 and roster_choice <= 19:
            roster_choice += 1
        elif roster_choice >= 20:
            roster_choice = 11

    elif key == curses.KEY_F5:
        if roster_choice >= 6:
            roster_choice = 1
        else:
            roster_choice += 1

    elif key == curses.KEY_F6:
        roster_choice = -1

    return screen, roster_choice

def print_control_menu(screen, Menu_Info):
    """ This displays the top ticker. currently used to display control options"""

    menu = ["[F3]-Advance,",
            "[F4]-Super Advance,",
            "[F5]-Display Chapter,",
            "[F7]-About,",
            "[F8]-EXIT,"]

    full_menu = ""
    
    for item in menu:
        full_menu += item

    full_menu += "AR={}({},{})".format(Menu_Info.active_roster, Menu_Info.selection, Menu_Info.mod)
        
    screen.attron(curses.color_pair(1))
    screen.addstr(0, 0, full_menu)
    screen.attroff(curses.color_pair(1))
    
    return screen

def print_ticker(screen, chapter):
    """ This displays the bottom ticker. Used for chapter stats."""

    name = "The " + chapter.name
    Ticker = "{:^20s}-  Year:{:5d}  Dead: {:<6d}  Honoured: {:<4d}  Dreads:{:2}  Starships:1+{}".format(name, chapter.year,
                                                                                        chapter.Dead_Count,
                                                                                        len(chapter.Honour.roll),
                                                                                        len(chapter.Roster[1]),
                                                                                        len(chapter.assets.fleet)-1)
    screen.attron(curses.color_pair(1))
    h, w = screen.getmaxyx()
    screen.addstr(h - 1, 0, Ticker)
    screen.attroff(curses.color_pair(1))
    return screen

def print_transcript(screen, marine):
    """ This displays the transcript of the currently selected marine."""

    h, w = screen.getmaxyx()
    screen.addstr(1, 0, "Transcript for {}| Entries {}".format(marine.title + " " + marine.name, len(marine.transcript)))
    screen.addstr(2, 0, "--------------------------------------------------------------------------------")

    for Index, line in enumerate(marine.transcript):
        screen.addstr(Index + 3, 0, marine.transcript[Index])

    screen.refresh()
    return screen

def print_roster(screen, roll, Menu_Info):
    """ This is the heart of the roster display """

    h, w = screen.getmaxyx()

    """ Determines how many marines to display. If the list is short then that is how many are displayed.
        If the list is long. It will fill the screen instead."""
    if len(roll) < h-2:
        High = len(roll)-1
    else:
        High = Menu_Info.high

    # Display in [Selected], [Watchlist], or [Normal] colour modes.
    for x in range(0, High, +1):
        if Menu_Info.selection == x:
            screen.attron(curses.color_pair(2))
            screen.addstr(x+1, 0, roll[x+Menu_Info.mod].C_Get_Statline())
            screen.attroff(curses.color_pair(2))

        elif roll[x+Menu_Info.mod].watchlist is True:
            screen.attron(curses.color_pair(3))
            screen.addstr(x + 1, 0, roll[x + Menu_Info.mod].C_Get_Statline())
            screen.attroff(curses.color_pair(3))
        else:
            screen.addstr(x+1, 0, roll[x+Menu_Info.mod].C_Get_Statline())

    return screen

def print_screen(screen, chapter, Menu_Info, Panel2_Mode):
    """ Displays the entire screen. Ties in the Top and Bottom tickers with the display screen. """

    # Clears the screen and Displays the top Ticker.
    screen.clear()
    screen = print_control_menu(screen, Menu_Info)

    # Mode = 1 displays the currently selected roster.
    if Panel2_Mode == 1:
        if Menu_Info.active_roster == -1:
            screen = print_roster(screen, chapter.Honour.roll, Menu_Info)

        elif Menu_Info.active_roster <= 6:
            screen = print_roster(screen, chapter.Roster[Menu_Info.active_roster], Menu_Info)

        elif Menu_Info.active_roster >= 11 and Menu_Info.active_roster <= 20:
            company = Menu_Info.active_roster % 10
            company = chapter.Get_Company(company)

            chapter.Roster.pop(-1)
            chapter.Roster.append(company)

            screen = print_roster(screen, company, Menu_Info)

    # Mode = 2 displays the currently selected transcript.
    elif Panel2_Mode == 2:
        if Menu_Info.active_roster == -1:
            screen = print_transcript(screen, chapter.Honour.roll[Menu_Info.selection + Menu_Info.mod])

        elif Menu_Info.active_roster <= 6:
            screen = print_transcript(screen, chapter.Roster[Menu_Info.active_roster][Menu_Info.selection+ Menu_Info.mod])

        elif Menu_Info.active_roster >= 11 and Menu_Info.active_roster <= 20:
            company = Menu_Info.active_roster % 10
            company = chapter.Get_Company(company)

            chapter.Roster.pop(-1)
            chapter.Roster.append(company)

            screen = print_transcript(screen, company[Menu_Info.selection + Menu_Info.mod])

        key = screen.getch()

    # Mode = 3 displays about.txt
    elif Panel2_Mode == 3:
        screen = print_about(screen)
        key = screen.getch()

    # Display the bottom ticker then update the screen.
    screen = print_ticker(screen, chapter)
    screen.refresh()


def graphics(screen, chapter):
    """ Initializes the curses graphics and handles the keyboard inputs."""

    h, w = screen.getmaxyx()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)


    # Menu_Info is documented in its own class declaration
    Menu_Info = menu_info(0, h-2, 0, 0)

    # These blanks are appended so that Roster[9] can be used for Composite Rosters (Companies)
    chapter.Roster.append([])
    chapter.Roster.append([])
    chapter.Roster.append([])

    print_screen(screen, chapter, Menu_Info, 1)

    keepgoing = True
    while keepgoing:
        key = screen.getch()

        # F3 advances the chapter by 1 tick(10 yrs)
        # F4 advances the chapter by 100 ticks (1000 yrs)
        if key == curses.KEY_F3:
            chapter.Advance()

        elif key == curses.KEY_F4:
            for x in range(100):
                chapter.Advance()
                if x % 5 == 0:
                    print_screen(screen, chapter, Menu_Info, 1)


        # F5 opens a drop down menu so that which roster is displayed can be changed.
        elif key == curses.KEY_F5:
            screen, Menu_Info.active_roster = print_F5Menu(screen, Menu_Info.active_roster)
            Menu_Info.selection = 0
            Menu_Info.mod = 0

        # F7 prints an about.txt to the Roster panel. Currently used to display commands.
        elif key == curses.KEY_F7:
            print_screen(screen, chapter, Menu_Info, 3)

        # F8 Quits the program.
        elif key == curses.KEY_F8:
            keepgoing = False

        ################################################################


        # [Up] and [Down] change the currently selected marine in the roster.
        elif key == curses.KEY_UP:
            if Menu_Info.active_roster <= 6 or (Menu_Info.active_roster >= 11 and Menu_Info.active_roster <= 20) or Menu_Info.active_roster == -1:
                if Menu_Info.selection > 0:
                    if Menu_Info.selection < 4 and Menu_Info.mod > 0:
                        Menu_Info.mod -= 1
                    else:
                        Menu_Info.selection -= 1

        elif key == curses.KEY_DOWN:
            if Menu_Info.active_roster <= 6 or Menu_Info.active_roster == -1:
                if Menu_Info.selection + Menu_Info.mod <= len(chapter.Roster[Menu_Info.active_roster]) - 2:
                    if Menu_Info.selection > Menu_Info.high-4 and Menu_Info.mod<len(chapter.Roster[Menu_Info.active_roster])-h+2 :
                        Menu_Info.mod += 1
                    else:
                        Menu_Info.selection += 1

            elif Menu_Info.active_roster >= 11 and Menu_Info.active_roster <= 20:
                if Menu_Info.selection + Menu_Info.mod <= len(chapter.Roster[9]) - 2:
                    if Menu_Info.selection > Menu_Info.high-4 and Menu_Info.mod<len(chapter.Roster[9])-h+2 :
                        Menu_Info.mod += 1
                    else:
                        Menu_Info.selection += 1

        elif key == curses.KEY_HOME:
            Menu_Info.selection = 0
            Menu_Info.mod = 0

        elif key == curses.KEY_END:
            if Menu_Info.active_roster <= 6 or Menu_Info.active_roster == -1:
                Menu_Info.selection = Menu_Info.mod + Menu_Info.high - 1
                Menu_Info.mod = (len(chapter.Roster[Menu_Info.active_roster]) - 1) - (Menu_Info.high - 1)

            elif Menu_Info.active_roster >= 11 and Menu_Info.active_roster <= 20:
                Menu_Info.selection = Menu_Info.mod + Menu_Info.high - 1
                Menu_Info.mod = (len(chapter.Roster[9]) - 1) - (Menu_Info.high - 1)





        # [Enter] displays the transcript of the currently selected marine.
        elif key == curses.KEY_ENTER or key in [10 ,13]:
            print_screen(screen, chapter, Menu_Info, 2)

        # [Space] toggles the watchlist for a given individual. Watched marines display red.
        elif key == ord(' '):
            chapter.Roster[Menu_Info.active_roster][Menu_Info.selection].Toggle_Watchlist()

    
        print_screen(screen, chapter, Menu_Info, 1)
        screen.refresh()


def C_Main_Menu(chapter):
    """ This is the go func. Press button to go.
        called by program.py, Probably superfluous."""
    curses.wrapper(graphics, chapter)




