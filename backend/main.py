

class Attitem:
    def __init__(self, name, itemimage, attackpower, attackdistance):
        self.name=name
        self.itemimg=itemimage
        self.attpower=attackpower
        self.attdis=attackdistance
    def setdata(self, name, itemimage, attackpower, attackdistance):
        self.name=name
        self.itemimg=itemimage
        self.attpower=attackpower
        self.attdis=attackdistance
class Defitem:
    def __init__(self, name, itemimage, defencepower):
        self.name=name
        self.itemimg=itemimage
        self.defpower=defencepower
    def setdata(self, name, itemimage, defencepower):
        self.name=name
        self.itemimg=itemimage
        self.defpower=defencepower

class Sector:
    def __init__(self, name, code, teamlist, itemsetlist):
        self.name=name
        self.code=code
        self.teamlist=teamlist
        self.itemsetlist=itemsetlist
    def setdata(self, name, code, teamlist, itemsetlist):
        self.name=name
        self.code=code
        self.teamlist=teamlist
        self.itemsetlist=itemsetlist

class Team:
    def __init__(self, T_id, position, health, points, attitemlist, defitemlist, defencelist_old, defencelist_new, sleep):
        self.T_id=T_id
        self.pos=position
        self.hp=health
        self.pt=points
        self.attitemlist=attitemlist
        self.defitemlist=defitemlist
        self.deflist_old=defencelist_old
        self.deflist_new=defencelist_new
        self.sleep=sleep
    def setdata(self, T_id, position, health, points, attitemlist, defitemlist, defencelist_old, defencelist_new, sleep):
        self.T_id=T_id
        self.pos=position
        self.hp=health
        self.pt=points
        self.attitemlist=attitemlist
        self.defitemlist=defitemlist
        self.deflist_old=defencelist_old
        self.deflist_new=defencelist_new
        self.sleep=sleep
team_id=1
team1=Team(1)
team2=Team(2)
team3=Team(3)
team4=Team(4)
team5=Team(5)
team6=Team(6)
team7=Team(7)
team8=Team(8)
team9=Team(9)
team10=Team(10)
team11=Team(11)
team12=Team(12)
team13=Team(13)
team14=Team(14)
team15=Team(15)
team_list=(team1, team2, team3, team4, team5)

nowteam=Team()
sector1=Sector()
sector2=Sector()
begining=Attitem()
jokbo=Defitem()

attacking_team=2
attacking_item=begining
defencing_item=jokbo
howmanyteam=15


sectorlist=[sector1, sector2]

def MOVE:
    position=input()
    pass

def ATTACK:
    if attacking_team in range(howmanyteam) and attacking_item in nowteam.attitemlist:
        for i in range(len(team_list)):
            if team_list[i+1].T_id==attacking_team:
                def_item=None
                team_list[i+1].deflist_new.append([nowteam, attacking_item, defencing_item])
                return 0
            else:
                pass
    else:
        return 'Error'

def DEFENCE:
    for i in range(len(nowteam.deflist_old)):
        print(nowteam.deflist_old)
        defencing_item=
        if defencing_item in nowteam.defitemlist:
            nowteam.deflist_old[i]















