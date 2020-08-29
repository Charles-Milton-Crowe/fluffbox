

class cls_chapter_settings:
    def __init__(self):
        """ These are the settings for the chapter in 1 place for easy updating.
            I would eventually like these moved to a text file to be loaded upon init.
            This way they could be edited by a user without editing this."""

        """ Settings for func in chapter.Fate"""
        # This is the 1 in x chance that a given rank has of dying"""
        self.KIA_CM = 35
        self.KIA_CO = 30
        self.KIA_CA = 25
        self.KIA_LT = 20
        self.KIA_SG = 15
        self.KIA_TR = 10

        self.KIA_DR = 50
        self.KIA_SR = 15

        # The is x to -> after KIA, the chance in X to be available for dread immersion"""
        self.DREAD_ROLL = 20

        # These are the chances in DREAD_ROLL to be available"""
        self.DR_CHANCE_CM = 4
        self.DR_CHANCE_CO = 6
        self.DR_CHANCE_CA =10
        self.DR_CHANCE_LT = 6
        self.DR_CHANCE_SG = 4
        self.DR_CHANCE_TR = 1

        self.DR_CHANCE_SR = 1

        """ Settings for initial Roster sizes. Messing with these numbers will break shit."""
        self.R_COMMAND_SIZE = 1033
        self.R_DREAD_SIZE = 24
        self.R_ARMOURY_SIZE = 56
        self.R_APOTHECARION_SIZE = 26
        self.R_RECLUSIAM_SIZE = 26
        self.R_LIBRARIUS_SIZE = 35
        self.R_VETERAN_SIZE = 120


class cls_marine_settings:
    def __init__(self):
        """ These are the settings for the marine class in 1 place for easy updating.
            I would eventually like these moved to a text file to be loaded upon init.
            This way they could be edited by a user without editing this."""

        self.MARINE_START_AGE = 30

        self.MARINE_START_EXP = 1
        self.MARINE_EXP_INTERVAL = 40 # Years
        self.MARINE_EXP_INCREMENT = 3

        self.MARINE_SERVICE_MEDAL = 500

class cls_initialize_settings:
    def __init__(self):
        """ These are the various rank stubs that when assembled form everyones rank.
            I would eventually like these moved to a text file to be loaded upon init.
            This way they could be edited by a user without editing this."""

        # Command Roster Titles
        self.TITLE_CM = " Chapter Master"
        self.TITLE_CO = " Commander"
        self.TITLE_CA = " Captain"
        self.TITLE_LT = " Lieutenant, "
        self.TITLE_SG = " Sargeant, "
        self.TITLE_TR = " Trooper , "

        # Dread Roster Titles (Permanently received upon death)
        self.DT_CHAPTER_MASTER =   "Master"
        self.DT_COMMANDER =        "Commander"
        self.DT_CAPTAIN =          "Captain"
        self.DT_LIEUTENANT =       "Lieutenant"
        self.DT_SARGEANT =         "Sargeant"
        self.DT_TROOPER =          "Trooper"

        self.DT_TECHNATUS =        "Technatus"

        self.DT_CHIEF_APOTHECARY = "Chf-Apoth"
        self.DT_APOTHECARY =       "Apothecary"

        self.DT_SANCTUS =          "Sanctus"
        self.DT_CHAPLAIN =         "Chaplain"

        self.DT_CHIEF_LIBRARIAN =  "Librus"
        self.DT_EPISTOLARY =       "Epistolary"
        self.DT_CODICIER =         "Codicier"
        self.DT_LEXICANIUM =       "Lexicanium"
        self.DT_ADNUNTIUS =        "Adnunitus"

        self.DT_CHAMPION =         "Champion"
        self.DT_ANCIENT =          "Ancient"
        self.DT_GUARD =            "Guard"
        self.DT_VETERAN =          "Veteran"

        # Armoury Roster Titles
        self.AR_TITLE_MASTER_OF_FORGE =    "Forge-Master"
        self.AR_TITLE_SENIOR_TECHMARINE =  "Sr-Techmarine"
        self.AR_TITLE_TECHMARINE =         "Techmarine"
        self.AR_TITLE_TECH_ACOLYTE =       "Jr-Tech"
        # Apothecarion Roster Titles
        self.AR_TITLE_CHIEF_APOTHECARY =   "Chief-Apothecary"
        self.AR_TITLE_MASTER_APOTHECARY =  "Master-Apothecary"
        self.AR_TITLE_APOTHECARY =         "Apothecary"
        self.AR_TITLE_APOTHECARY_ACOLYTE = "Nurse"
        # Reclusiam Roster Titles
        self.AR_TITLE_MASTER_OF_SANCTITY = "Master Sanctus"
        self.AR_TITLE_RECLUSIARCH =        "Reclusiarch"
        self.AR_TITLE_SENIOR_CHAPLAIN =    "Sr-Chaplain"
        self.AR_TITLE_CHAPLAIN =           "Chaplain"
        self.AR_TITLE_CHAPLAIN_ACOLYTE =   "Jr-Chaplain"
        # Librarius Roster Titles
        self.AR_TITLE_CHIEF_LIBRARIAN =    "Chief Librarian"
        self.AR_TITLE_EPISTOLARY =         "Epistolary"
        self.AR_TITLE_CODICIER =           "Codicier"
        self.AR_TITLE_LEXICANIUM =         "Lexicanium"
        self.AR_TITLE_ADNUNTIUS =          "Aduntius"
        # Veteran Roster Titles
        self.AR_TITLE_CHAPTER_CHAMPION =   "Chapter-Champion"
        self.AR_TITLE_CHAPTER_ANCIENT =    "Chapter-Ancient"
        self.AR_TITLE_HONOUR_GUARD =       "Honour-Guard"
        self.AR_TITLE_CHAMPION =           "Champion"
        self.AR_TITLE_ANCIENT =            "Ancient"
        self.AR_TITLE_VETERAN =            "Veteran"

