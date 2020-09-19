
from cls_settings import cls_initialize_settings


""" All of this is used to build the Master Title List for the chapter.
    Beyond that it seems self explanatory."""


def Get_Letters(num):
    """ This func is given a number and returns that number with a few letters representing the
        place of the number(e.g. 1st, 2nd, etc)."""

    if num == 0:
    	return "{:>4}".format("VET")
    elif num == 1 or num % 10 == 1:
        if num == 11:
            return str("{:2}th".format(num))
        else:
            return str("{:2}st".format(num))
    elif num == 2 or num % 10 == 2:
        if num == 12:
            return str("{:2}th".format(num))
        else:
            return str("{:2}nd".format(num))
    elif num == 3 or num % 10 == 3:
        if num == 13:
            return str("{:2}th".format(num))
        else:
            return str("{:2}rd".format(num))
    elif num >= 4:
        return str("{:2}th".format(num))


def Get_Command_Title():
    """ Provides a list of titles(strings) that includes every position in the Command Roster"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.TITLE_CM)
    for x in range(2):
        titlelist.append(Get_Letters(x) + settings.TITLE_CO)
    for x in range(10):
        titlelist.append(Get_Letters(x) + settings.TITLE_CA)
    for x in range(10):
        for y in range(2):
            titlelist.append(Get_Letters(y) + settings.TITLE_LT + Get_Letters(x) + "")
    for x in range(10):
        for y in range(20):
            titlelist.append(Get_Letters(y) + settings.TITLE_SG + Get_Letters(x) + "")
    for x in range(10):
        for y in range(80):
            titlelist.append(Get_Letters(y) + settings.TITLE_TR + Get_Letters(x) + "")
    # for x in range(500):
    #	titlelist.append(Get_Letters(y) + "WARNING YOU SHOULD NEVER SEE THIS MESSAGE")
    return titlelist


def Get_Dread_Rank(Roster, Index):
    """ Provides a list of titles(strings) that includes every title that could be given to a new dread."""
    settings = cls_initialize_settings()

    prefix = "Dread"

    if Roster == 0:
        if Index == 0:
            title =  settings.DT_CHAPTER_MASTER
        elif Index <= 2:
            title =  settings.DT_COMMANDER
        elif Index <= 12:
            title =  settings.DT_CAPTAIN
        elif Index <= 32:
            title =  settings.DT_LIEUTENANT
        elif Index <= 232:
            title =  settings.DT_SARGEANT
        else:
            title =  settings.DT_TROOPER

    elif Roster == 2:
            title =  settings.DT_TECHNATUS

    elif Roster == 3:
        if Index == 0:
            title =  settings.DT_CHIEF_APOTHECARY
        else:
            title =  settings.DT_APOTHECARY

    elif Roster == 4:
        if Index == 0:
            title =  settings.DT_SANCTUS
        else:
            title =  settings.DT_CHAPLAIN

    elif Roster == 5:
        if Index == 0:
            title =  settings.DT_CHIEF_LIBRARIAN
        elif Index <= 5:
            title =  settings.DT_EPISTOLARY
        elif Index <= 14:
            title =  settings.DT_CODICIER
        elif Index <= 24:
            title =  settings.DT_LEXICANIUM
        else:
            title =  settings.DT_ADNUNTIUS

    elif Roster == 6:
        if Index == 0:
            title =  settings.DT_CHAMPION
        elif Index <= 2:
            title =  settings.DT_ANCIENT
        elif Index <= 18:
            title =  settings.DT_GUARD
        else:
            title =  settings.DT_VETERAN
    else:
        title = "Theres a problem hearabouts.."

    return "{:5} {:<6}".format(prefix, title)


def Get_Armoury_Title():
    """ Provides a list of titles(strings) that includes every position in the Armoury"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.AR_TITLE_MASTER_OF_FORGE)

    for x in range(5):
        titlelist.append(settings.AR_TITLE_SENIOR_TECHMARINE)

    for x in range(10):
        titlelist.append(settings.AR_TITLE_TECHMARINE + " " + Get_Letters(x) + "")

    for x in range(10):
        for y in range(4):
            titlelist.append(Get_Letters(y) + " " + settings.AR_TITLE_TECH_ACOLYTE + " " + Get_Letters(x) + "")

    titlelist.append("Armoury:SHITSHIT")
    return titlelist


def Get_Apothecarion_Title():
    """ Provides a list of titles(strings) that includes every position in the Apothecarion"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.AR_TITLE_CHIEF_APOTHECARY)

    for x in range(5):
        titlelist.append(settings.AR_TITLE_MASTER_APOTHECARY)


    for x in range(10):
        for y in range(2):
            titlelist.append(Get_Letters(y) + " " + settings.AR_TITLE_APOTHECARY + " " + Get_Letters(x) + "")

    titlelist.append("Apothecarion:SHITSHIT")
    return titlelist


def Get_Reclusiam_Title():
    """ Provides a list of titles(strings) that includes every position in the Reclusiam"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.AR_TITLE_MASTER_OF_SANCTITY)
    titlelist.append(settings.AR_TITLE_RECLUSIARCH)

    for x in range(4):
        titlelist.append(Get_Letters(x) + " " + settings.AR_TITLE_SENIOR_CHAPLAIN)

    for x in range(10):
        titlelist.append(settings.AR_TITLE_CHAPLAIN + " " + Get_Letters(x) + "")

    for x in range(10):
        titlelist.append(settings.AR_TITLE_CHAPLAIN_ACOLYTE + " " + Get_Letters(x) + "")

    titlelist.append("Reclusiam:SHITSHIT")
    return titlelist


def Get_Librarius_Title():
    """ Provides a list of titles(strings) that includes every position in the Librarius"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.AR_TITLE_CHIEF_LIBRARIAN)

    for x in range(5):
        titlelist.append(Get_Letters(x) + " " + settings.AR_TITLE_EPISTOLARY)

    for x in range(9):
        titlelist.append(Get_Letters(x) + " " + settings.AR_TITLE_CODICIER)

    for x in range(10):
        titlelist.append(settings.AR_TITLE_LEXICANIUM + " " + Get_Letters(x) + "")

    for x in range(10):
        titlelist.append(settings.AR_TITLE_ADNUNTIUS + " " + Get_Letters(x) + "")

    titlelist.append("Librarius:SHITSHIT")
    return titlelist


def Get_Veteran_Title():
    """ Provides a list of titles(strings) that includes every position in the Veteran Guard"""
    settings = cls_initialize_settings()
    titlelist = []

    titlelist.append(settings.AR_TITLE_CHAPTER_CHAMPION)
    titlelist.append(settings.AR_TITLE_CHAPTER_ANCIENT)

    for x in range(18):
        titlelist.append(Get_Letters(x) + " " + settings.AR_TITLE_HONOUR_GUARD)

    for x in range(10):
        titlelist.append(settings.AR_TITLE_CHAMPION + " " + Get_Letters(x) + "")

    for x in range(10):
        titlelist.append(settings.AR_TITLE_ANCIENT + " " + Get_Letters(x) + "")

    for x in range(10):
        for y in range(8):
            titlelist.append(Get_Letters(y) + " " + settings.AR_TITLE_VETERAN + " " + Get_Letters(x) + "")

    titlelist.append("Veteran:SHITSHIT")
    return titlelist


def Get_Master_Titles():
    Command_Title_List = Get_Command_Title()
    Armoury_Title_List = Get_Armoury_Title()
    Apothecarion_Title_List = Get_Apothecarion_Title()
    Reclusiam_Title_List = Get_Reclusiam_Title()
    Librarius_Title_List = Get_Librarius_Title()
    Veteran_Title_List = Get_Veteran_Title()
    Master_Titles = (
    Command_Title_List, [], Armoury_Title_List, Apothecarion_Title_List, Reclusiam_Title_List, Librarius_Title_List,
    Veteran_Title_List)

    Master_Titles = tuple(Master_Titles)
    return (Master_Titles)


def Load_Namefile(afile):
    with open(afile, 'r') as f:
        rows = f.readlines()

        for x in range(len(rows) - 1, -1, -1):
            if rows[x][0] == "\n" or rows[x][0] == "#":
                rows.pop(x)

    list = []
    for x in range(len(rows)):
        list.append(rows[x])
        list[-1] = list[-1].rstrip("\n")

    return list
