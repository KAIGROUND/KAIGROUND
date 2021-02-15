# -*- coding: euc-kr -*-
n_team = 26
n_node = 42

attitem_list = {'����':{'attack':1, 'range':2}, '����':{'attack':2, 'range':2}, '���ſ� ����å':{'attack':2, 'range':2}, '��ħ ����':{'attack':2, 'range':4}, '������':{'attack':4, 'range':2}, '����� ȣ�� �̵�':{'attack':4, 'range':1}, '����':{'attack':4, 'range':3}, '���� �б�':{'attack':4, 'range':3}, '�߰����':{'attack':5, 'range':2}, '�⸻���':{'attack':6, 'range':4}, '���� ����':{'attack':2, 'range':3}, 'A���ϴ�':{'attack':1, 'range':5}, 'B������':{'attack':3, 'range':3}, 'C�Ѹ���':{'attack':5, 'range':2}, 'D��Ʈ���̾�':{'attack':6, 'range':4}, 'F-ų��':{'attack':10, 'range':2}}
defitem_list = {'��������':{'defense':2, 'armor':0}, '����':{'defense':2, 'armor':0}, '�߽�':{'defense':2, 'armor':0}, 'Ʃ�͸�':{'defense':2, 'armor':0}, '����':{'defense':3, 'armor':0}, '����':{'defense':3, 'armor':0}, '���� ��Ƽ':{'defense':3, 'armor':0}, '����':{'defense':3, 'armor':0}, '������':{'defense':5, 'armor':0}, '���� öȸ':{'defense':5, 'armor':0}, 'ī�� ����':{'defense':0, 'armor':3}, 'ī�� ����':{'defense':0, 'armor':3}, 'û����':{'defense':0, 'armor':1}, 'ī�����':{'defense':0, 'armor':1}, 'üũ����':{'defense':0, 'armor':1}, 'ī�� �ĵ�Ƽ':{'defense':0, 'armor':2}}

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
        self.g = []  # ���ʷ� 1�� ������~ ~!!!! 0��° ���� ������� ����
        self.d = [[1e10 for _ in range(n_node + 1)] for i in range(n_node + 1)]
        for i in range(n_node + 1): self.d[i][i] = 0
        adj = [[], [2, 4, 20], [1, 3], [2, 8], [1, 5], [4, 6], [5, 7, 10], [6, 8], [3, 7, 9, 17], [8, 10], [6, 9, 11],
               [10, 12], [11, 13, 32], [12, 14], [15, 27, 13], [16, 14], [17, 15], [8, 16, 18], [17, 19], [18, 20, 26],
               [1, 19, 21], [20, 22], [21, 23], [22, 24], [23, 25, 42], [24, 26, 27], [19, 25], [14, 25, 28],
               [27, 29, 40], [28, 30], [29, 31], [30, 32], [12, 31, 33], [32, 34], [33, 35], [34, 36], [35, 37],
               [38, 39, 41, 36], [37, 42], [40, 37], [28, 39], [37, 42], [41, 38, 24]]  # ���� �����
        item = [[] for i in range(n_node + 1)]
        team = [[i for i in range(1, n_team + 1, 1)]] + [[] for i in
                                                         range(n_node)]  # �ʱ�ȭ�� ��� ���� 0�� ���� i�� team object�� �ٲ���
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

    def move_g(self, nd_id, team_pos, team_id):  # nd_id�� team ��ü�� �̵�
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

[Attitem('����', '', 2, 2)]
[Attitem('���ſ� ����å', '', 2, 2)]
[Attitem('��ħ ����', '', 2, 4)]
[Attitem('������', '', 4, 2)]
[Attitem('����� ȣ�� �̵�', '', 4, 1)]
[Attitem('����', '', 4, 3)]
[Attitem('���� �б�', '', 4, 3)]
[Attitem('�߰����', '', 6, 2)]
[Attitem('�⸻���', '', 6, 4)]
[Attitem('���� ����', '', 2, 3)]
[Attitem('A���ϴ�', '', 1, 5)]
[Attitem('B������', '', 3, 3)]
[Attitem('C�Ѹ���', '', 5, 2)]
[Attitem('D��Ʈ���̾�', '', 6, 4)]
[Attitem('F-ų��', '', 10, 2)]


class Defitem:
    def __init__(self, name, itemimage, defencepower, additionalhealth):
        self.name=name
        self.itemimg=itemimage
        self.defpower=defencepower
        self.addhealth=additionalhealth

[Defitem('��������', '', 2, 0)]
[Defitem('����', '', 2, 0)]
[Defitem('�߽�', '', 2, 0)]
[Defitem('Ʃ�͸�', '', 2, 0)]
[Defitem('����', '', 3, 0)]
[Defitem('����', '', 3, 0)]
[Defitem('���� ��Ƽ', '', 3, 0)]
[Defitem('����', '', 3, 0)]
[Defitem('������', '', 5, 0)]
[Defitem('���� öȸ', '', 5, 0)]
[Defitem('ī�� ����', '', 0, 3)]
[Defitem('ī�� ����', '', 0, 3)]
[Defitem('û����', '', 0, 1)]
[Defitem('ī�����', '', 0, 1)]
[Defitem('üũ����', '', 0, 1)]
[Defitem('ī�� �ĵ�Ƽ', '', 0, 2)]


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



















