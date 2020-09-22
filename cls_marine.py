

from cls_settings import cls_marine_settings

from initialize import Get_Letters

from random import randint as rand

class cls_roster:
	""" This is only used for the Honour Roll and only beacause its old and I'm lazy."""
	def __init__(self, rname, roll):
		self.rname = rname
		self.roll = roll

class cls_badge:
	""" This is a Badge"""

	def __init__(self, badge, name, color):
		self.badge = badge
		self.name = name
		self.color = color

class cls_badge_rack:
	""" This holds many badges"""

	def __init__(self):
		self.badges = []

	def show_badges(self):
		rack = ""

		for entry in self.badges:
			rack = rack + entry.badge

		return "[{:6}]".format(rack)

	def add_badge(self, badge, name, color):
		self.badges.append(cls_badge(badge, name, color))

class cls_marine:
	def __init__(self, rank, Year, fname, lname):
		self.settings = cls_marine_settings()
		self.name = fname + " " + lname
		self.rank = rank
		self.company_number = 13

		self.title = ""

		self.age = self.settings.MARINE_START_AGE
		self.servicelength = 0
		self.KIA = 0
		self.watchlist = False
		self.birth = Year
		self.death = 0
		self.epitaph = ""
		self.exp = self.settings.MARINE_START_EXP



		self.physicality = self.Get_Rand(1, 10)
		self.quickness   = self.Get_Rand(1, 10)
		self.reaction    = self.Get_Rand(1, 10)

		self.xfactor = self.physicality + self.quickness + self.reaction



		self.Dread_Status = False

		self.badges = cls_badge_rack()

	def Advance_Age(self, Year):
		self.age += 10
		self.servicelength += 10
		if self.servicelength % self.settings.MARINE_EXP_INTERVAL == 0:
			self.exp += self.settings.MARINE_EXP_INCREMENT
		if self.servicelength % self.settings.MARINE_SERVICE_MEDAL == 0:
			self.transcript.append("{:d}: Service Medal awarded for 500yrs active duty.".format(Year))

	def C_Get_Statline(self):
		if self.KIA == 0:
			return "{:>21s} {:21s}{}, Age:{:4d}, (Alive): ({:2},{:3})".format(self.get_title(),
																  self.name,
																  self.badges.show_badges(),

																  self.age,
																  self.xfactor,
																  self.exp,)

		elif self.KIA == 1 or self.KIA == 2:
			return "{:>22s} {:21s}{}, Age:{:4d}, (Dead):{:<5d} | {:22s}".format(self.get_title(),
																			self.name,
																			self.badges.show_badges(),
																			self.age,
																			self.death,
																			self.epitaph)
		else:
			return "Get_Statline: Receiving KIA that is NOT 0,1,2."

	def get_title(self):
		return "{}, {:>3}".format(str.capitalize(self.rank), Get_Letters(self.company_number))

	def Toggle_Watchlist(self):
		if self.watchlist is True:
			self.watchlist = False
		else:
			self.watchlist = True

	def Get_Rand(self, low, high):
		return rand(low,high)

	def isDread(self):
		return self.Dread_Status

	def __str__(self):
		return ":{:30}| {:30}:KIA({})".format(self.get_title(), self.name, self.KIA)
