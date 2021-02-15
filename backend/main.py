# -*- coding: euc-kr -*-
n_team = 26
n_node = 42

attitem_list = {'개강':{'attack':1, 'range':2}, '퀴즈':{'attack':2, 'range':2}, '무거운 전공책':{'attack':2, 'range':2}, '아침 수업':{'attack':2, 'range':4}, '연습반':{'attack':4, 'range':2}, '기숙사 호실 이동':{'attack':4, 'range':1}, '과제':{'attack':4, 'range':3}, '계절 학기':{'attack':4, 'range':3}, '중간고사':{'attack':5, 'range':2}, '기말고사':{'attack':6, 'range':4}, '실험 수업':{'attack':2, 'range':3}, 'A약하다':{'attack':1, 'range':5}, 'B내리기':{'attack':3, 'range':3}, 'C뿌리기':{'attack':5, 'range':2}, 'D스트로이어':{'attack':6, 'range':4}, 'F-킬라':{'attack':10, 'range':2}}
defitem_list = {'예습복습':{'defense':2, 'armor':0}, '낮잠':{'defense':2, 'armor':0}, '야식':{'defense':2, 'armor':0}, '튜터링':{'defense':2, 'armor':0}, '족보':{'defense':3, 'armor':0}, '공강':{'defense':3, 'armor':0}, '딸기 파티':{'defense':3, 'armor':0}, '축제':{'defense':3, 'armor':0}, '라이프':{'defense':5, 'armor':0}, '수강 철회':{'defense':5, 'armor':0}, '카이 야잠':{'defense':0, 'armor':3}, '카이 돕바':{'defense':0, 'armor':3}, '청바지':{'defense':0, 'armor':1}, '카고바지':{'defense':0, 'armor':1}, '체크남방':{'defense':0, 'armor':1}, '카이 후드티':{'defense':0, 'armor':2}}

class Attitem:
    def __init__(self, name, itemimage, attackpower, attackdistance):
        self.name = name
        self.itemimg = itemimage
        self.attpower = attackpower
        self.attdis = attackdistance


class Defitem:
    def __init__(self, name, itemimage, defencepower):
        self.name = name
        self.itemimg = itemimage
        self.defpower = defencepower


class Node:
    def __init__(self, nd_id, items, teams, adj):
        self.nd_id = nd_id
        self.items = items  # items dictionary list
        self.teams = teams  # deployed teams
        self.adj = adj  # adjacent node id


class graph:
    def __init__(self, n_node=n_node):
        self.g = []  # 차례로 1번 노드부터~ ~!!!! 0번째 노드는 사용하지 않음
        self.d = [[1e10 for _ in range(n_node + 1)] for i in range(n_node + 1)]
        for i in range(n_node + 1): self.d[i][i] = 0
        adj = [[], [2, 4, 20], [1, 3], [2, 8], [1, 5], [4, 6], [5, 7, 10], [6, 8], [3, 7, 9, 17], [8, 10], [6, 9, 11],
               [10, 12], [11, 13, 32], [12, 14], [15, 27, 13], [16, 14], [17, 15], [8, 16, 18], [17, 19], [18, 20, 26],
               [1, 19, 21], [20, 22], [21, 23], [22, 24], [23, 25, 42], [24, 26, 27], [19, 25], [14, 25, 28],
               [27, 29, 40], [28, 30], [29, 31], [30, 32], [12, 31, 33], [32, 34], [33, 35], [34, 36], [35, 37],
               [38, 39, 41, 36], [37, 42], [40, 37], [28, 39], [37, 42], [41, 38, 24]]  # 직접 만들기
        item = [[] for i in range(n_node + 1)]
        team = [[i for i in range(1, n_team + 1, 1)]] + [[] for i in
                                                         range(n_node)]  # 초기화시 모든 팀은 0에 있음 i를 team object로 바꾸자
        for i in range(n_node + 1):
            self.g.append(Node(i, item[i], team[i], adj[i]))
        for i in range(n_node + 1):
            for j in self.g[i].adj:
                self.d[i][j] = 1
        for k in range(n_node + 1):
            for i in range(n_node + 1):
                for j in range(n_node + 1):
                    self.d[i][j] = min(self.d[i][k] + self.d[k][j], self.d[i][j])

    def dis_node(self, a, b):
        return self.d[a][b]

    def move_g(self, nd_id, team_pos, team_id):  # nd_id로 team 객체가 이동
        if self.dis_node(team_pos, nd_id) > 3:
            return 0
        self.g[team_pos].teams.remove(team_id)
        self.g[nd_id].teams.append(team_id)
        return 1

    def add_item(self, nd_id, item):
        self.g[nd_id].items.append(item)

    def del_item(self, nd_id, item):
        self.g[nd_id].items.remove(item)

    def show_item(self, nd_id):
        for i in self.g[nd_id].items:
            print(i.name)


map = graph(n_node)


class Team:
    def __init__(self, id, health, points, attitemlist, defitemlist, sleep):
        self.id = id
        self.pos = 0  # section no.
        self.hp = health
        self.points = points
        self.attitemlist = attitemlist
        self.defitemlist = defitemlist
        self.sleep = sleep

    def update_health(self, health):
        self.hp += health

    def update_point(self, point):
        self.points += point

    def add_attitem(self, attitem):
        self.attitemlist.append(attitem)

    def add_defitem(self, defitem):
        self.defitemlist.append(defitem)

    def remove_defitem(self, defitem):
        self.defitemlist.remove(defitem)

    def remove_attitem(self, attitem):
        self.attitemlist.remove(attitem)

    def move_team(self, nd_id, mp=map):
        if not mp.move_g(nd_id, self.pos, self.id):
            print("Invalid Move")
            return
        self.pos = nd_id


Team_list = [Team(0, 0, 0, 0, 0, 0)] + [Team(i + 1, 10, 0, [], [], 0) for i in range(n_team)]


////////////////////////////////////////////////////////////////////////

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
    for i in range(len(nowteam.deflist_old)):
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



















