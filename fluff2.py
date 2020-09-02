

from cls_org import cls_chapter


# Program Start #############################
print(
""" This is the prototype for the new cls_chapter system.\n
Instead of a roster(conga-line) of marines, chapters 
will have a veteran company and 3 commands comprising 
4 companies each.\n
 Each company will have a mini roster for all ranks in the company\n""")

chapter = cls_chapter("Chapter Crusade Fleet")
chapter.display_commands()
input("[Enter Anything]")

chapter.display_troop_strength()
keepgoing = int(input("Press 0 to keep going"))

while keepgoing == 0:

    # ALL COMPANIES RETURN TO FULL STRENGTH. OR NEVER REALLY LOSE GUYS. WTF
    # FIGURE THIS OUT.
    chapter.roll_fate()
    chapter.display_troop_strength()

    keepgoing = int(input("Press 0 to keep going"))