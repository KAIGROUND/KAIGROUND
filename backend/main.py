

class Attitem:
    def __init__(self, name, itemimage, attackpower, attackdistance):
        self.name=name
        self.itemimg=itemimage
        self.attpower=attackpower
        self.attdis=attackdistance

[Attitem('퀴즈', '', 2, 2)]
[Attitem('무거운 전공책', '', 2, 2)]
[Attitem('아침 수업', '', 2, 4)]
[Attitem('연습반', '', 4, 2)]
[Attitem('기숙사 호실 이동', '', 4, 1)]
[Attitem('과제', '', 4, 3)]
[Attitem('계절 학기', '', 4, 3)]
[Attitem('중간고사', '', 6, 2)]
[Attitem('기말고사', '', 6, 4)]
[Attitem('실험 수업', '', 2, 3)]
[Attitem('A약하다', '', 1, 5)]
[Attitem('B내리기', '', 3, 3)]
[Attitem('C뿌리기', '', 5, 2)]
[Attitem('D스트로이어', '', 6, 4)]
[Attitem('F-킬라', '', 10, 2)]


class Defitem:
    def __init__(self, name, itemimage, defencepower, additionalhealth):
        self.name=name
        self.itemimg=itemimage
        self.defpower=defencepower
        self.addhealth=additionalhealth

[Defitem('예습복습', '', 2, 0)]
[Defitem('낮잠', '', 2, 0)]
[Defitem('야식', '', 2, 0)]
[Defitem('튜터링', '', 2, 0)]
[Defitem('족보', '', 3, 0)]
[Defitem('공강', '', 3, 0)]
[Defitem('딸기 파티', '', 3, 0)]
[Defitem('축제', '', 3, 0)]
[Defitem('라이프', '', 5, 0)]
[Defitem('수강 철회', '', 5, 0)]
[Defitem('카이 야잠', '', 0, 3)]
[Defitem('카이 돕바', '', 0, 3)]
[Defitem('청바지', '', 0, 1)]
[Defitem('카고바지', '', 0, 1)]
[Defitem('체크남방', '', 0, 1)]
[Defitem('카이 후드티', '', 0, 2)]


class Team:
    def __init__(self, T_id, health, points, attitemlist, defitemlist, sleep):
        self.T_id=T_id
        self.pos=0 #section no.
        self.hp=health
        self.points=points
        self.attitemlist=attitemlist
        self.defitemlist=defitemlist
        self.sleep=sleep

    def update_health(self, health):
        self.hp+=health

    def update_point(self, point):
        self.points+=point

    def add_attitem(self, attitem):
        self.attitemlist.append(attitem)

    def remove_attitem(self, attitem):
        self.attitemlist.remove(attitem)

    def add_defitem(self, defitem):
        self.defitemlist.append(defitem)

    def remove_defitem(self, defitem):
        self.defitemlist.remove(defitem)

    def setdata(self, health, points, attitemlist, defitemlist, sleep):
        self.T_id=T_id
        self.hp=health
        self.points=points
        self.attitemlist=attitemlist
        self.defitemlist=defitemlist
        self.sleep=sleep



def MOVE:
    position=input()



def ATTACK:
    if attacking_team in range(howmanyteam) and attacking_item in nowteam.attitemlist:
        for i in range(len(team_list)):
            if team_list[i+1].T_id==attacking_team:
                def_item=None
                team_list[i+1].deflist_new.append([nowteam, attacking_item, def_item])
                nowteam.attitemlist.remove(attacking_item)
                return 0
            else:
                pass
    else:
        return 'Error'

def DEFENCE:
    for i in range(len(nowteam.deflist_old)):
        print(nowteam.deflist_old)
        defencing_item=jokbo
        if defencing_item in nowteam.defitemlist:
            nowteam.deflist_old[i][2]=defencing_item
            nowteam.defitemlist.remove(defencing_item)
            return 0
        else:
            return 'Error'

def AFTERBATTLE:
    for i in range(len(nowteam.deflist_old))
        if nowteam.deflist_old[i][2]!=None:
            damage=nowteam.deflist_old[i][1].attpower-nowteam.deflist_old[i][2].defpower
            if damage<0:
                damage=0
            else:
                pass
        else:
            damage=nowteam.deflist_old[i][1].attpower

        nowteam.hp=nowteam.hp-damage
        if nowteam.hp<=0:
            nowteam.hp=0
            nowteam.sleep=True
        else:
            pass

        if nowteam.sleep
            nowteam.deflist_old[i][0].points+=10
            nowteam.points-=5
        else:
            nowteam.deflist_old[i][0].points+=damage

    nowteam.deflist_old=nowteam.deflist_new
    nowteam.deflist_new=[]



















