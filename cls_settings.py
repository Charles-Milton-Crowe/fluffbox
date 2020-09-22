

class cls_org_settings:
    def __init__(self):

        # Coming soon.. options for Double Strength Companies.
        self.COMPANY_MAX_CAPTAINS = 1
        self.COMPANY_MAX_LIEUTENANTS = 2
        self.COMPANY_MAX_SARGEANTS = 20
        self.COMPANY_MAX_TROOPERS = 80

        self.COMPANY_MAX_DREADS = 2

        self.COMPANY_MAX_TECHMARINES = 2
        self.COMPANY_MAX_JR_TECHMARINES = 2
        self.COMPANY_MAX_APOTHECARIES = 2
        self.COMPANY_MAX_NURSES = 2
        self.COMPANY_MAX_CHAPLAINS = 2
        self.COMPANY_MAX_JR_CHAPLAINS = 2
        self.COMPANY_MAX_LEXICANII = 2
        self.COMPANY_MAX_ADNUNTII = 2

        self.COMPANY_MAX_HONOUR_GUARD = 8
        self.COMPANY_MAX_ANCIENTS = 1
        self.COMPANY_MAX_CHAMPIONS = 1

        # These are the 1 in X chance that a member of a given rank.
        self.KIACHANCE_TROOPERS = 10
        self.KIACHANCE_SARGEANTS = 15
        self.KIACHANCE_LIEUTENANTS = 20
        self.KIACHANCE_CAPTAINS = 25
        self.KIACHANCE_COMMANDERS = 30
        self.KIACHANCE_CHAPTER_MASTERS = 35
        self.KIACHANCE_DREADS = 50
        self.KIACHANCE_JR_TECHMARINES = 20
        self.KIACHANCE_TECHMARINES = 25
        self.KIACHANCE_NURSES = 20
        self.KIACHANCE_APOTHECARIES = 25
        self.KIACHANCE_JR_CHAPLAIN = 20
        self.KIACHANCE_CHAPLAIN = 25
        self.KIACHANCE_ADNUNTII = 15
        self.KIACHANCE_LEXICANII = 20
        self.KIACHANCE_HONOUR_GUARDS = 15
        self.KIACHANCE_ANCIENTS = 20
        self.KIACHANCE_CHAMPIONS = 25

        # This is chances in X to be available for dreadnought insertion .
        self.DREADCHANCEMAX = 20

        # These are X Chances in DREADCHANCEMAX to be available for dreadnough insertion.
        self.DREADCHANCE_TROOPERS = 1
        self.DREADCHANCE_SARGEANTS = 4
        self.DREADCHANCE_LIEUTENANTS = 6
        self.DREADCHANCE_CAPTAINS = 10
        self.DREADCHANCE_COMMANDERS = 6
        self.DREADCHANCE_CHAPTER_MASTERS = 4
        self.DREADCHANCE_DREADS = 0
        self.DREADCHANCE_JR_TECHMARINES = 1
        self.DREADCHANCE_TECHMARINES = 2
        self.DREADCHANCE_NURSES = 1
        self.DREADCHANCE_APOTHECARIES = 1
        self.DREADCHANCE_JR_CHAPLAIN = 1
        self.DREADCHANCE_CHAPLAIN = 1
        self.DREADCHANCE_ADNUNTII = 1
        self.DREADCHANCE_LEXICANII = 1
        self.DREADCHANCE_HONOUR_GUARDS = 2
        self.DREADCHANCE_ANCIENTS = 1
        self.DREADCHANCE_CHAMPIONS = 1

        # These are the number of decades each rank is aged at chapter creation.
        # Marines begin at 30yrs old + STARTING_AGE
        self.STARTING_AGE_TROOPERS = 5
        self.STARTING_AGE_SARGEANTS = 15
        self.STARTING_AGE_LIEUTENANTS = 25
        self.STARTING_AGE_CAPTAINS = 35
        self.STARTING_AGE_COMMANDERS = 45
        self.STARTING_AGE_CHAPTER_MASTERS = 50
        self.STARTING_AGE_DREADS = 60
        self.STARTING_AGE_JR_TECHMARINES = 20
        self.STARTING_AGE_TECHMARINES = 25
        self.STARTING_AGE_NURSES = 20
        self.STARTING_AGE_APOTHECARIES = 25
        self.STARTING_AGE_JR_CHAPLAIN = 20
        self.STARTING_AGE_CHAPLAIN = 25
        self.STARTING_AGE_ADNUNTII = 20
        self.STARTING_AGE_LEXICANII = 25
        self.STARTING_AGE_HONOUR_GUARDS = 20
        self.STARTING_AGE_ANCIENTS = 25
        self.STARTING_AGE_CHAMPIONS = 30

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
