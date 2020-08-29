from initialize import Load_Namefile
from initialize import Get_Dread_Rank
from initialize import Get_Master_Titles
from initialize import Get_Letters

from cls_marine import cls_roster
from cls_marine import cls_marine
from cls_assets import cls_assets

from cls_settings import cls_chapter_settings

from random import randint as rand
from os import path
import os


class cls_chapter:
	def __init__(self):
		# Import Settings
		self.settings = cls_chapter_settings()

		# The year starts in 40k and increases in 10 year increments.
		self.year = 40000

		# This is incremented whenever a death occurs in the chapter.
		self.Dead_Count = 0
		self.CM_Count = 1

		# This is a list of marines who have died and been honoured by the chapter.
		self.Honour = cls_roster("Honour Roll", [])
		self.Tourney_Winners = []
		self.Tourney_Results = []
		#self.KIA = roster("KIA Roll", [])

		# This is a list which contains the dead who have died in the previous increment.
		# Currently unused.
		self.Butchers_Bill = []


		self.name = self.Get_Chapter_Name()
		self.assets = self.Pop_Assets()

		# These lists are books of names loaded into memory so the files arent opened
		# up every time a marine is generated.
		self.FNames = self.Pop_First_Namelist()
		self.LNames = self.Pop_Last_Namelist()

		# The Roster[x] contains every member of the chapter.
		# 0) The Command Roster. Every officer and trooper.
		# 1) The Dread Roster. Starts at 10. Caps at 20.
		# 2) The Armoury.
		# 3) The Apothecarion.
		# 4) The Reclusiam.
		# 5) The Librarius.
		# 6) The Honour Guard.
		self.Roster = self.Pop_Roster()

		# Titles are applied after every increment. This holds them.
		self.Master_Titles = Get_Master_Titles()

		# Titles are bestowed upon the founding members of the chapter.
		self.Bestow_Titles()

		# Epitaphs are given to a dead marine. These are loaded and held here.
		self.Basic_Epitaphs, self.Complex_Epitaphs = self.Load_Epitaphs()

		self.Age_Chapter()

	def Advance(self):
		# This is the heart that runs chapter. Its exists to call the other functions
		# in turn. Each cycle is a 10 year advancement of the chapter.
		# 1) The Year from which all time derives is advanced.
		# 2) The fate of the chapter is decided.(KIA determined 0=Alive, 1=KIA, 2=MIA, 3=Potential Dread
		# 3) Fates will is then enforced
		# 4) The Fleet is updated. (This should tie into an assets update perhaps)
		# 5) All chapter titles besides dreads are refreshed to reflect updated rankings.
		# 6) Every century a Tournament is held.

		self.Butchers_Bill = []
		self.year = self.year + 10

		self.Fate()
		self.Enforce_Fate()
		self.assets.Fleet_Update(self.year)

		self.Bestow_Titles()

		if self.year % 100 == 0:
			self.Tournament()

	def Fate(self):
		""" This func determines the fate of every individual of the chapter
			and advances their age 10 years as well. Certain things pop off
			in the age func too."""

		""" Roster[0] is the 'Command Roster' It contains all officers and
			troopers. KIA_Chance is the 1 in X chance that the marine is
			marked for death. Other and Dread_Chance are used to determine 
			if a KIA is suitable for dreadnought insertion."""

		index = [0, 2, 12, 32, 232, 1032]
		for x in range(0, len(self.Roster[0]) - 1):
			self.Roster[0][x].Advance_Age(self.year)

			# Chapter Master
			if x <= index[0]:
				KIA_Chance = self.settings.KIA_CM
				Other = self.settings.DREAD_ROLL
				Dread_Chance = self.settings.DR_CHANCE_CM

			# Commanders
			elif x <= index[1]:
				KIA_Chance = self.settings.KIA_CO
				Other = self.settings.DREAD_ROLL
				Dread_Chance = self.settings.DR_CHANCE_CO

			# Captains
			elif x <= index[2]:
				KIA_Chance = self.settings.KIA_CA
				Other = self.settings.DREAD_ROLL
				Dread_Chance = self.settings.DR_CHANCE_CA

			# Lieutenants
			elif x <= index[3]:
				KIA_Chance = self.settings.KIA_LT
				Other = self.settings.DREAD_ROLL
				Dread_Chance = self.settings.DR_CHANCE_LT

			# Sargeants
			elif x <= index[4]:
				KIA_Chance = self.settings.KIA_SG
				Other = self.settings.DREAD_ROLL * 5
				Dread_Chance = self.settings.DR_CHANCE_SG

			# Troopers
			else:
				KIA_Chance = self.settings.KIA_TR
				Other = self.settings.DREAD_ROLL * 100
				Dread_Chance = self.settings.DR_CHANCE_TR

			# now that the values have been set for the marine according
			# to his index the actual rolls are run.
			if rand(1, KIA_Chance) == 1:
				self.Roster[0][x].KIA = 1
				if rand(1, 300) <= self.Roster[0][x].xfactor:
					self.Roster[0][x].KIA = 0

				if rand(1, Other) <= Dread_Chance:
					self.Roster[0][x].KIA = 3

		# Dreads
		for Dread in self.Roster[1]:
			Dread.Advance_Age(self.year)
			if rand(1, self.settings.KIA_DR) == 1:
				Dread.KIA = 1

		# Fate for all specialty Rosters
		for Roll in (self.Roster[2],self.Roster[3],self.Roster[4],self.Roster[5],self.Roster[6]):
			for Marine in Roll:
				Marine.Advance_Age(self.year)

				if rand(1, self.settings.KIA_SR) == 1:
					Marine.KIA = 1

					fateroll = rand(1, self.settings.DREAD_ROLL * 2)
					if fateroll == 1:
						Marine.KIA = 2
					elif fateroll == 2:
						Marine.KIA = 3

					if rand(1, 300) <= Marine.xfactor:
						Marine.KIA = 0

	def Enforce_Fate(self):
		""" This deals with the KIA flag in each marine and deals with the consequences
			of that event. such as marine creation and destruction."""

		""" Rosters[0-6](All) are iterated through.
				Second we iterate through each individual Roster[0-6][x]
				
				If (KIA is set to 3) and (Roster[1](Dreads) is less than the chapter cap(24))
					and the marine is not a dread already.
				Then make a copy of that marine in the dread roster.
					 Kill the original marine.
					 Update the new Dread with the 'Dread Package'
				Otherwise
					Set his KIA flag to 1(Dead) and kill him.
					
					
				If the KIA is 1 or 2 kill him."""

		for x in range(0, 7, +1):
			for y in range(len(self.Roster[x]) - 1, -1, -1):
				if self.Roster[x][y].KIA == 3:
					if len(self.Roster[1]) < self.settings.R_DREAD_SIZE and self.Roster[x][y].isDread() is False:

						""" Some Console Logging Crust I'll leave for a bit.
						print()
						print("Dread Creation Triggered:")
						print("XY = {}.{}, Dread Roster Length = {}".format(x, y, len(self.Roster[1])))
						print("Before Enforce|{},{}:Roster-{}|{},{}:Dread-{}".format(x, y, self.Roster[x][y], 1, -1,
																					 self.Roster[1][-1]))
						"""

						self.Roster[1].append(self.Roster[x][y])
						self.Roster[x][y].KIA = 1
						self.Kill_Marine(x, y)
						self.Roster[1][-1].title = Get_Dread_Rank(x, y)
						self.Roster[1][-1].KIA = 0
						self.Roster[1][-1].Dread_Status = True
						self.Roster[1][-1].transcript.append(
							"{:d}: Permanantly interred in a dreadnought sarcophagus.".format(self.year))

					else:
						self.Roster[x][y].KIA = 1
						self.Kill_Marine(x, y)

				elif self.Roster[x][y].KIA == 1 or self.Roster[x][y].KIA == 2:
					self.Kill_Marine(x, y)
				else:
					pass

	def Kill_Marine(self, R, Index):
		""" This kills every marine in the chapter."""

		"""	First a check is run to make sure the Marine is actually KIA != 0
		 	Next the Dead_Count is incremented by 1
		 	The Dead Marine is added to the Butchers_Bill (Currently Unused)
		 	
		 	If he is special enough(index < 10) he is added to the Honour Roll
		 	Only if this is the case are his death stats filled out in the
			Honour roll call
			
		 	If the marine is from the command or specialty rosters another marine
				is generated in the command roster to replace them.
				
			If a specialist died they are replaced from a member of the first company.
		 		Which again causes a marine to be generated in the 10th.
		 		Finally the marine is removed from his roster."""

		if self.Roster[R][Index].KIA == 0:
			print("Kill_Marine:WTF MATE" + str(self.Roster[R][Index]))
			return

		if R == 0 and Index == 0:
			self.CM_Count += 1
			self.Roster[0][1].transcript.append("{:d}: Promoted to Chapter Master.".format(self.year))
		elif R == 0 and Index <= 2:
			self.Roster[0][3].transcript.append("{:d}: Promoted to Commander.".format(self.year))
		elif R == 0 and Index <= 12:
			self.Roster[0][13].transcript.append("{:d}: Promoted to Captain.".format(self.year))
		elif R == 0 and Index <= 32:
			self.Roster[0][33].transcript.append("{:d}: Promoted to Lieutenant.".format(self.year))
		elif R == 0 and Index <= 232:
			self.Roster[0][233].transcript.append("{:d}: Promoted to Sargeant.".format(self.year))

		self.Dead_Count += 1
		self.Butchers_Bill.append(self.Roster[R][Index])

		if (Index == 0) or \
			(Index <= 33 and len(self.Roster[R][Index].badges.badges) > 1) or \
			(Index <= 233 and len(self.Roster[R][Index].badges.badges) > 2):
			self.Add_Honoured(self.Roster[R][Index], Index)

		if R == 0:
			self.Roster[0].append(self.Create_Marine())
		elif R >= 2:
			self.Roster[0].append(self.Create_Marine())
			Selection = rand(233, 283)
			self.Roster[R].append(self.Roster[0][Selection])
			self.Roster[R][-1].transcript.append("{:d}: Inducted into a specialist roster.".format(self.year))
			self.Roster[0].pop(Selection)
		self.Roster[R].pop(Index)

	def Create_Marine(self):
		""" This is called when a marine is killed."""

		""" A marine generated and returned. he will subsequently be place at the end of Roster[0]
			which is the 9th or tenth company depending on casualty levels for the tick.."""

		fname = self.FNames[rand(0, len(self.FNames)-1)]
		lname = self.LNames[rand(0, len(self.LNames)-1)]
		Marine = cls_marine("New Recruit", self.year, fname, lname)

		# This "New Recruit" title should never be seen within the program
		# 	as it it immediatly overwritten with correct titles at chapter start.
		# I think this is here so that the "Ancient Ones" title can be bestowed
		# to founding dreadnought without too much hassle.

		return Marine

	def Add_Honoured(self, Marine, Index):
		""" This adds a given marine to the Honour Roll """

		""" First a check to make sure the marine is some sort of dead.
			This is the second such check in the chain.
			
			Epitaph is applied. Dreads are specific for now. Elsewise you get a flavored one.
			Transcript is applied.
			
			The marine is finally appended to the Honour Roll
			and finally a trap to keep out bugs I cant find yet."""

		if Marine.KIA != 0:
			if Marine.isDread() is True:
				Marine.epitaph = "He lived as he died. In a metal box."
			else:
				Marine.epitaph = self.Get_Epitaph()
			Marine.transcript.append("{:d}: Removed from roles. KIA.".format(self.year))
			Marine.death = self.year
			self.Honour.roll.append(Marine)

		else:
			print("WARNING THIS MARINE WAS ATTEMPTING TO SNEAK INTO THE HONOUR ROLL")
			print(str(Marine) + " X is: {}".format(Index))

	def Bestow_Titles(self):
		""" All chapter titles besides dreads are refreshed to reflect updated rankings.
			Dread titles are permanent and created upon death.
			They reflect the rank upon death and are never updated."""

		for z in range(len(self.Roster[0])):
			self.Roster[0][z].title = self.Master_Titles[0][z]
		for x in range(2, 7, +1):
			for y in range(len(self.Roster[x])):
				self.Roster[x][y].title = self.Master_Titles[x][y]

		self.Roster[0][0].title = Get_Letters(self.CM_Count-1) + " " + self.Roster[0][0].title

	def Tournament(self):
		""" Every century a tournament is conducted. Special transcripts and badges will be added. """

		""" Running, Wrestling, WeightLifting, Pugilism """

		# This is the award for bolter discipline. This is given out on a 5% chance basis.
		for entry in self.Roster[0]:
			if rand(1, 20) == 1:
				entry.transcript.append("{}: Bolter Discipline Medal awarded for marksmanship.".format(self.year))
				entry.badges.add_badge("B", "Bolter Discipline", "Red")

		# This is the award for Valour. This is given out on a 5% chance basis.
		for entry in (self.Roster[0]):
			if rand(1, 20) == 1:
				entry.transcript.append("{}: Medal Awarded for Valour.".format(self.year))
				entry.badges.add_badge("V", "Medal for Valour", "Yellow")
				entry.xfactor += 3

		# This determines which dreadnought hosts the opening ceremonies of the tournament
		Contestant_Max = int(len(self.Roster[1])/2)
		self.Roster[1][rand(0, Contestant_Max)].transcript.append("{}: Hosted the opening ceremonies of the Tournament.".format(self.year))


		# This is the tournament of blades:single elimination.
		Contestants = []
		Index_List = []

		for x in range(1, 257):
			Contestants.append(self.Roster[0][x])
			Index_List.append(x)

		if len(Contestants) % 2 != 0:
			print("PROBLEMO", len(Contestants))


		CM_Name = self.Roster[0][0].title + " " + self.Roster[0][0].name
		self.Tourney_Results.append("\n")
		self.Tourney_Results.append("{}: The Tournament has begun! Hosted by {}.".format(self.year, CM_Name))



		A_Bracket = []
		B_Bracket = []
		A_Index = []
		B_Index = []

		keepgoing = True
		cnt = 0
		while keepgoing:
			keepgoing = False
			cnt += 1



			for x in range(0, len(Contestants)//2):
				A_Bracket.append(Contestants[0])
				B_Bracket.append(Contestants[-1])
				Contestants.pop(0)
				Contestants.pop(-1)

				A_Index.append(Index_List[0])
				B_Index.append(Index_List[-1])
				Index_List.pop(0)
				Index_List.pop(-1)

			Contestants = []
			Index_List = []

			if len(A_Bracket) <= 4:
				self.Tourney_Results.append("\n")
				self.Tourney_Results.append("Round {} has begun!".format(cnt))
				self.Tourney_Results.append("═══════════════════════════════════════════════════════════")

			for x in range(0, len(A_Bracket)):
				A_Results = A_Bracket[x].xfactor + rand(1, A_Bracket[x].xfactor) + rand(1, A_Bracket[x].exp)
				B_Results = B_Bracket[x].xfactor + rand(1, B_Bracket[x].xfactor) + rand(1, B_Bracket[x].exp)

				if A_Results > B_Results:
					Contestants.append(A_Bracket[x])
					Index_List.append(A_Index[x])


				elif A_Results < B_Results:
					Contestants.append(B_Bracket[x])
					Index_List.append(B_Index[x])
				else:
					fateroll = rand(1,2)
					if fateroll == 1:
						Contestants.append(A_Bracket[x])
						Index_List.append(A_Index[x])
					else:
						Contestants.append(B_Bracket[x])
						Index_List.append(B_Index[x])
				if len(A_Bracket) <= 4:
					self.Tourney_Results.append("{:>28}    {:<28}".format(A_Bracket[x].title,
																		  B_Bracket[x].title))
					self.Tourney_Results.append("{:>28} vs {:<28}".format(A_Bracket[x].name,
																		  B_Bracket[x].name))
					self.Tourney_Results.append("                   ({:>3},{:>3})    ({:>3},{:>3})".format(A_Bracket[x].xfactor,
																			  A_Bracket[x].exp,
																			  B_Bracket[x].xfactor,
																			  B_Bracket[x].exp))
					self.Tourney_Results.append("-----------------------------------------------------------".format())

					results = " {} to {}".format(A_Results, B_Results)
					name = Contestants[-1].title + " " + Contestants[-1].name + " Won!" + results
					self.Tourney_Results.append("{:^60}".format(name))
					self.Tourney_Results.append("═══════════════════════════════════════════════════════════")

			A_Bracket = []
			B_Bracket = []
			A_Index = []
			B_Index = []

			if len(Contestants) == 2:
				self.Roster[0][Index_List[0]].transcript.append("{}: Reached the final circle in the Tournament of Blades.".format(self.year))
				self.Roster[0][Index_List[1]].transcript.append("{}: Reached the final circle in the Tournament of Blades.".format(self.year))
				self.Roster[0][Index_List[0]].badges.add_badge("T", "Tournament of Blades Finalist", "White")
				self.Roster[0][Index_List[1]].badges.add_badge("T", "Tournament of Blades Finalist", "White")
			if len(Contestants) > 1:
				keepgoing = True

		self.Roster[0][Index_List[0]].transcript.pop(-1)
		self.Roster[0][Index_List[0]].transcript.append("{}: Won the tournament of blades.".format(self.year))
		self.Tourney_Winners.append("{}|{}, XF={}, XP={}".format(self.year, Contestants[0],Contestants[0].xfactor, Contestants[0].exp ))

	def Get_Company(self, Company):
		""" Builds a list of the requested Company with all auxilliary specialists (Except Dreads).
			Then it returns that list to requesting func."""

		"""	Following are starting indexes in the respective roster for each companys men
			Honestly I made this before i started commenting things. Need to wrap my head around
			this more to write a proper comment."""


		#           0   1   2    3    4   5   6   7   8   9  10  11  12  13  14  15   16
		Offset = (( 3, 13, 14,  33, 233,  0,  6, 16,  6,  7,  6, 16, 15, 25, 20, 30,  40),
				  ( 4, 15, 16,  53, 313,  2,  7, 20,  8,  9,  7, 17, 16, 26, 21, 31,  48),
				  ( 5, 17, 18,  73, 393,  4,  8, 24, 10, 11,  8, 18, 17, 27, 22, 32,  56),
				  ( 6, 19, 20,  93, 473,  6,  9, 28, 12, 13,  9, 19, 18, 28, 23, 33,  64),
				  ( 7, 21, 22, 113, 553,  8, 10, 32, 14, 15, 10, 20, 19, 29, 24, 34,  72),
				  ( 8, 23, 24, 133, 633, 10, 11, 36, 16, 17, 11, 21, 20, 30, 25, 35,  80),
				  ( 9, 25, 26, 153, 713, 12, 12, 40, 18, 19, 12, 22, 21, 31, 26, 36,  88),
				  (10, 27, 28, 173, 793, 14, 13, 44, 20, 21, 13, 23, 22, 32, 27, 37,  96),
				  (11, 29, 30, 193, 873, 16, 14, 48, 22, 23, 14, 24, 23, 33, 28, 38, 104),
				  (12, 31, 32, 213, 953, 18, 15, 52, 24, 25, 15, 25, 24, 34, 29, 39, 112))
		Temp_Roll = []
		Company = Company - 1

		# Captain and 2 Lieutenants
		Temp_Roll.append(self.Roster[0][Offset[Company][0]])
		Temp_Roll.append(self.Roster[0][Offset[Company][1]])
		Temp_Roll.append(self.Roster[0][Offset[Company][2]])

		""" This is where the dreads would go and of course the Offset table would
			have to be updated too. Get around to this."""

		# Armoury
		Temp_Roll.append(self.Roster[2][Offset[Company][6]])
		y = Offset[Company][7]
		for x in range(4):
			Temp_Roll.append(self.Roster[2][y])
			y = y + 1

		# Apothacerion, Reclusiam, Librarius, Veteran
		Temp_Roll.append(self.Roster[3][Offset[Company][8]])
		Temp_Roll.append(self.Roster[3][Offset[Company][9]])
		Temp_Roll.append(self.Roster[4][Offset[Company][10]])
		Temp_Roll.append(self.Roster[4][Offset[Company][11]])
		Temp_Roll.append(self.Roster[5][Offset[Company][12]])
		Temp_Roll.append(self.Roster[5][Offset[Company][13]])
		Temp_Roll.append(self.Roster[6][Offset[Company][14]])
		Temp_Roll.append(self.Roster[6][Offset[Company][15]])
		y = Offset[Company][16]
		for x in range(8):
			Temp_Roll.append(self.Roster[6][y])
			y = y + 1

		# Sargeants
		y = Offset[Company][3]
		for x in range(20):
			Temp_Roll.append(self.Roster[0][y])
			y = y + 1

		# Troopers
		y = Offset[Company][4]
		for x in range(80):
			Temp_Roll.append(self.Roster[0][y])
			y = y + 1

		return Temp_Roll

	def High_Lords(self):
		""" This is unused these days but is how the High Lords of Terra should
			be organized.

			With the big 3 at the top.
			Next the most important orgs that keep the imperium running like on a basic
			defend at all costs basis. And Inquisitors because fluff.

			Followed by a lower council that has the leaders of all the bitch adeptas.

			Fight me.
		"""

		print()
		print("The High Lords of Terra")
		print("-----------------------------------------------")
		print("Lord Commander of the Imperium")
		print()
		print("Master of the Administratum")
		print("Ecclesiarch of the Adeptus Ministorum")
		print("Fabricator-General of the Mechanicum")
		print()
		print("Knight Captain of the Custodes")
		print("Master of the Astronomicon")
		print("Mistress of the Black Ships")
		print("Master of the Astra Telepathica")
		print("Paternoval Envoy of the Navis Noblite")
		print("Lord Inquisitor of the Inquisition")
		print()
		print("-----------------------------------------------")
		print("Lord Commander of the Segmentum Solar")
		print("Commander Militant")
		print("Commander Naval")
		print("Abessa of the Sister of Battle")
		print("Representative for the Assassin Orders")
		print("Grand Provost Marshall of the Adeptus Arbites")
		print()
		print("Chancellor of the Estate Imperium")
		print("Director of the Sigint Imperium")
		print("Cardinal of the Holy Synod")
		print("Speaker for the Chartist Captains")
		print("Representative for the Astartes Chapters")

	def Pop_Roster(self):
		""" This builds the initial Roster{x]s of the chapter once the class is initialized. Used Once."""

		# This name_list isnt used right now but I hate to remove it and need to type it out all
		# over some day.

		Name_List = ["Command: Marines of the Chapter", "Dreadnoughts of the Chapter",
					 "Armoury: Tech-Marines of the Chapter", "Apothecarion: Apothecaries of the Chapter",
					 "Reclusiam: Chaplains of the Chapter", "Librarius: Librarians of the Chapter",
					 "Honour Guard: Veterans of the Chapter"]
		Count_List = [self.settings.R_COMMAND_SIZE,
					  self.settings.R_DREAD_SIZE,
					  self.settings.R_ARMOURY_SIZE,
					  self.settings.R_APOTHECARION_SIZE,
					  self.settings.R_RECLUSIAM_SIZE,
					  self.settings.R_LIBRARIUS_SIZE,
					  self.settings.R_VETERAN_SIZE]
		Roster = []
		for x in range(len(Name_List)):
			list = []
			for y in range(Count_List[x]):
				if x == 0 or x >= 2:
					fname = self.FNames[rand(0, len(self.FNames)-1)]
					lname = self.LNames[rand(0, len(self.LNames)-1)]
					list.append(cls_marine("New Recruit", self.year, fname, lname))
					list[-1].transcript[0] = "{:5d}: Founding member of the chapter.".format(self.year)

				elif x == 1:
					fname = self.FNames[rand(0, len(self.FNames)-1)]
					lname = self.LNames[rand(0, len(self.LNames)-1)]
					list.append(cls_marine("Ancient One", self.year, fname, lname))
					list[-1].transcript[0] = "{:5d}: Founding member of the chapter, Dreanought style.".format(self.year)
					for z in range(rand(50, 70)):
						list[-1].Advance_Age(self.year)
			Roster.append(list)
		return Roster

	def Pop_Assets(self):
		""" This builds the initial Assets of the Chapter in the initialization sequence. Used once.
		    Used only for fleets at present."""

		return cls_assets()

	def Age_Chapter(self):
		""" Ages each member of the chapter upon initialization. Called once."""

		# Command Roster
		for x in range(0, len(self.Roster[0])-1):
			if x == 0:
				Low = 45
				High = 55
			elif x <= 2:
				Low = 40
				High = 50
			elif x <= 12:
				Low = 30
				High = 40
			elif x <= 32:
				Low = 25
				High = 35
			elif x <= 232:
				Low = 15
				High = 25
			else:
				Low = 4
				High = 6

			for _ in range(rand(Low, High)):
				self.Roster[0][x].Advance_Age(self.year)



		# Dreads are aged at dread creation in Pop_Roster

		# Specialty Rosters
		Low = 10
		High = 20
		for x in range (2, 7):
			for y in range(0, len(self.Roster[x])):
				for _ in range(Low, High):
					self.Roster[x][y].Advance_Age(self.year)




	def Pop_First_Namelist(self):
		""" Loads and Coalates various first names into one namebook(2d list) """

		namelist = Load_Namefile("resources/first_names.txt")

		return namelist

	def Pop_Last_Namelist(self):
		""" Loads and Coalates various last names into one namebook(2d list) """

		namelist = Load_Namefile('resources/last_names.txt')

		return namelist

	def Get_Chapter_Name(self):
		""" This loads the chapter_names.txt file and returns one for
		    the chapter at initialization."""

		namelist = Load_Namefile('resources/chapter_names.txt')
		return namelist[rand(0, len(namelist) - 1)]

	def Load_Epitaphs(self):
		""" This calls the Load_Filename func to open the epitaphs and loads them into memory."""


		# Then the file is split into the basic and complex epitaphs.
		# These are initialized at chapter creation. Get_Epitaph is
		# used to generate an epitaph from these values.

		Basic_Epitaphs = []
		Complex_Epitaphs = []

		list = Load_Namefile('resources/epitaphs.txt')

		num = int(list[0])
		list.pop(0)

		for x in range(0, num-1):
			Basic_Epitaphs.append(list[x])

		for _ in range(num):
			list.pop(0)

		for entry in list:
			Complex_Epitaphs.append(entry)

		return Basic_Epitaphs, Complex_Epitaphs

	def Get_Epitaph(self):
		""" This chooses an epitaph for the marine and is returned."""

		# 1 in 100 it is a basic epitaph.
		# Otherwise it is a complex epitaph
		#
		# Complex epitaph is chosen at random. then the first
		# value is appended with one of any additional values

		fateroll = rand(1,100)
		if fateroll == 1:
			return self.Basic_Epitaphs[rand(0,len(self.Basic_Epitaphs)-1)]
		else:
			string = self.Complex_Epitaphs[rand(0,len(self.Complex_Epitaphs)-1)]
			new_string = string.split("#", )
			return new_string[0] + " " + new_string[rand(1, len(new_string)-1)] + "."
