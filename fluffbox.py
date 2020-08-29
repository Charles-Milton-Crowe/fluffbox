# A program built on random inputs is a program in which edge cases become a constant reality.

from cls_chapter import cls_chapter
from c_main_menu import C_Main_Menu

from os import path
import os


def folders():

    if path.exists('records/') is False:
        os.mkdir('records')

    if path.exists('resources/') is False:
        print("Resources dont exit. FUBAR!")



######################################################################################
# Main Program Start           #######################################################
######################################################################################

# Checks to make sure certain needed paths exist.
folders()


# Creates Chapter
SMC = cls_chapter()


# Loads Chapter into the curses Gui.
C_Main_Menu(SMC)


# Prints files upon end of program.
with open("records/Tournament_Recap.txt", 'w', encoding="utf-8") as f:
    for entry in SMC.Tourney_Winners:
        f.write(entry + "\n")

with open("records/Tournament_of_Blades.txt", 'w', encoding="utf-8") as f:
    for entry in SMC.Tourney_Results:
        f.write(entry + "\n")
    f.write("\n")





"""

Most Wanted Problem
0) [Up-Down] do not work initially when displaying the honour roll. the roll must be visited twice.
    as in [F5]->[F6]->[F5]->[F4]->[F5]->[F6] works around this bug.
--------------------   
1) Transcripts that mention when an individual is promoted sometimes doesnt work.
    (e.g. Promoted to Chapter Master. <- these are in cls_chapter.kill_marine)
--------------------     
2) Program Explodes when the window is resized.
3) Dreads have never shown in the chapter roster cause im a lazy piece of shit.
4) Transcripts and Badges need variation and WORK.


BACK-BURNER WISHLIST SHIT
------------------------------
Implement other startship types
    + the navy assets in general

Implement Assets and STC collections
Implement Industry Points
Implement Gene-Seed
Implement Muliple -Section Command Structures
Eventualy keep track of discrete dreadnought hulls. ( with History)



X = 10000
while X > 0:
    print("-----------------------------")
    print("{} Space Marines on the wall.".format(X))
    print("{} Space Marines.".format(X))
    print("Angron drops down.")
    print("Slaughters all-round")
    X -= 20
    print("{} Space Marines on the wall.".format(X))
    print()
"""

# all shame and no praise make lorgar a chaos boy.
# All shame and no praise make Lorgar a chaos boy.
# all SHAME and no PRAISE make lorgar a CHAOS BOY.
# alL shamE anD nO praisE makE lorgaR A chaoS boY.
# all shame aNd NO praise make Lorgar a CHAOS BOY.
# ALL SHAME AND NO PRAISE MAKE LORGAR A CHAOS BOY!!
