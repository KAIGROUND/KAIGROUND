#-*- coding: euc-kr -*-
from typing import List 
from sys import stdin

n_team = 5
n_node = 42

attack_dictionary = {'개강':{'attack':1, 'range':10}, '퀴즈':{'attack':2, 'range':6}, '무거운 전공책':{'attack':2, 'range':2}, '아침 수업':{'attack':2, 'range':4}, '연습반':{'attack':4, 'range':2}, '기숙사 호실 이동':{'attack':4, 'range':1}, '과제':{'attack':4, 'range':3}, '계절 학기':{'attack':4, 'range':3}, '중간고사':{'attack':6, 'range':2}, '기말고사':{'attack':8, 'range':4}, '실험 수업':{'attack':4, 'range':3}}
def_dictionary = {'예습복습':{'defense':1, 'armor':0}, '낮잠':{'defense':1, 'armor':0}, '야식':{'defense':1, 'armor':0}, '튜터링':{'defense':1, 'armor':0}, '족보':{'defense':3, 'armor':0}, '공강':{'defense':3, 'armor':0}, '딸기 파티':{'defense':3, 'armor':0}, '축제':{'defense':3, 'armor':0}, '라이프':{'defense':5, 'armor':0}, '수강 철회':{'defense':7, 'armor':0}, '카이 야잠':{'defense':0, 'armor':2}, '카이 돕바':{'defense':0, 'armor':2}, '청바지':{'defense':0, 'armor':1}, '카고바지':{'defense':0, 'armor':1}, '체크남방':{'defense':0, 'armor':2}, '카이 후드티':{'defense':0, 'armor':2}}

class Node:
    def __init__(self, nd_id, items, teams, adj):
        self.nd_id=nd_id
        self.items=items 
        self.teams=teams 
        self.adj=adj #adjacent node id

class graph:
    def __init__(self, n_node=n_node):
        self.g=[] #차례로 1번 노드부터~ ~!!!! 0번째 노드는 사용하지 않음
        self.d=[[1e10 for _ in range(n_node+1)] for i in range(n_node+1)]
        for i in range(n_node+1): self.d[i][i]=0
        adj=[[],[2,4,20],[1,3],[2,8],[1,5],[4,6],[5,7,10],[6,8],[3,7,9,17],[8,10],[6,9,11],[10,12],[11,13,32],[12,14],[15,27,13],[16,14],[17,15],[8,16,18],[17,19],[18,20,26],[1,19,21],[20,22],[21,23],[22,24],[23,25,42],[24,26,27],[19,25],[14,25,28],[27,29,40],[28,30],[29,31],[30,32],[12,31,33],[32,34],[33,35],[34,36],[35,37],[38,39,41,36],[37,42],[40,37],[28,39],[37,42],[41,38,24]] #직접 만들기
        item=[[], [[7, 6], [2, 12], [6, 4]], [[8, 3], [2, 24], [7, 5]], [[4, 4], [6, 15], [8, 14]], [[5, 24], [4, 21], [2, 3]], [[10, 26], [7, 19], [7, 20]], [[7, 17], [8, 17], [4, 3]], [[3, 16], [4, 27], [3, 14]], [[6, 4], [2, 22], [6, 12]], [[4, 2], [4, 13], [4, 15]], [[5, 6], [7, 13], [2, 25]], [[4, 9], [6, 16], [5, 11]], [[2, 13], [6, 26], [4, 4]], [[3, 3], [2, 22], [5, 5]], [[4, 22], [6, 27], [5, 7]], [[10, 27], [3, 10], [4, 15]], [[3, 2], [7, 19], [8, 2]], [[9, 6], [4, 18], [3, 12]], [[5, 20], [11, 13], [3, 2]], [[3, 7], [5, 18], [3, 9]], [[2, 15], [5, 27], [9, 20]], [[2, 25], [3, 7], [2, 2]], [[2, 15], [6, 3], [6, 2]], [[4, 6], [5, 8], [4, 12]], [[6, 13], [7, 5], [3, 4]], [[6, 13], [7, 23], [8, 13]], [[5, 6], [9, 16], [11, 12]], [[6, 16], [11, 14], [7, 14]], [[2, 19], [3, 5], [4, 18]], [[8, 23], [7, 14], [9, 22]], [[2, 17], [10, 23], [3, 24]], [[10, 12], [9, 7], [2, 14]], [[4, 23], [6, 13], [10, 3]], [[3, 18], [3, 2], [3, 14]], [[3, 22], [2, 26], [7, 15]], [[2, 4], [9, 10], [4, 6]], [[2, 12], [3, 4], [8, 26]], [[4, 2], [3, 19], [2, 8]], [[4, 12], [2, 7], [7, 16]], [[8, 7], [2, 15], [11, 5]], [[8, 23], [4, 8], [7, 3]], [[3, 4], [8, 27], [2, 3]], [[2, 17], [6, 26], [10, 8]]]
        team=[[i for i in range(1, n_team+1,1)]] + [[] for i in range(n_node)] #초기화시 모든 팀은 0에 있음 i를 team object로 바꾸자
        for i in range(n_node+1):
            self.g.append(Node(i,item[i],team[i],adj[i]))
        for i in range(n_node+1):
            for j in self.g[i].adj:
                self.d[i][j]=1
        for k in range(n_node+1):
            for i in range(n_node+1):
                for j in range(n_node+1):
                    self.d[i][j]=min(self.d[i][k]+self.d[k][j], self.d[i][j])

    def dis_node(self, a, b):
        return self.d[a][b]
        
    def move_g(self, nd_id, team_pos, team_id, init): #nd_id로 team 객체가 이동
        if not init and self.dis_node(team_pos, nd_id)>3:
            return 0
        self.g[team_pos].teams.remove(team_id)
        self.g[nd_id].teams.append(team_id)
        return 1

    def show_item_nd(self, nd_id):
        for i in self.g[nd_id].items:
            print(i.name)

    def show_teams(self):
        for i in range(n_node+1):
            if self.g[i].teams!=[]:
                print("At sector %d: teams"%(i),*self.g[i].teams,"are here")

    def show_items(self):
        for i in range(n_node+1):
            if self.g[i].teams!=[]:
                print("At sector %d: items"%(i),*self.g[i].items,"are here")

mp=graph(n_node)

class Team:
    def __init__(self, id:int, health, points, attack_itemlist:list, def_itemlist:list, sleep):
        self.id=id
        self.pos=0 #section no.
        self.hp=health
        self.points=points
        self.attack_itemlist=attack_itemlist
        self.def_itemlist=def_itemlist
        self.sleep=sleep

    def update_health(self, health):
        if self.sleep: return
        self.hp+=health
        if self.hp<=0:
            self.sleep=1
            print("Team %d는 수면상태에 빠집니다."%(self.id))
            self.update_point(-5)

    def update_point(self, point):
        self.points+=point

    def add_attitem(self, attitem):
        self.attack_itemlist.append(attitem)

    def remove_attitem(self, attitem):
        del self.attack_itemlist[attitem]

    def add_defitem(self, defitem):
        self.def_itemlist.append(defitem)

    def remove_defitem(self, defitem):
        del self.def_itemlist[defitem]

    def move_team(self, nd_id, init=0, mp:graph=mp):
        if not mp.move_g(nd_id, self.pos, self.id, init):
            raise Exception("Invalid Move")
            return
        self.pos = nd_id        

    def attackable_teams(self, attack_item:str, mp:graph=mp):
        rt=[]
        for i in range(1,n_node+1):
            if mp.dis_node(self.pos, i)<=attack_dictionary[attack_item]['range']:
                rt += mp.g[i].teams
        rt.remove(self.id)
        return rt
    
    def moveable_sections(self, mp:graph=mp):
        rt=[]
        for i in range(1,n_node+1):
            if mp.dis_node(self.pos, i)<=3:
                rt += [i]
        return rt

Team_list = [Team(0,0,0,[],[],0)]+[Team(i+1,10,0,['개강'],[],0) for i in range(n_team)]
attack_list=[[] for i in range(n_team+1)] #attack_list[a][b] 뜻 a 팀이 attack_list[a][b]한테 공격 받음
last_attack_list=[[] for i in range(n_team+1)]

def attack(a:Team, b:Team, attack_item:str): #a attack b with attack_item
    if attack_item not in a.attack_itemlist:
        raise Exception("Error attack_item not in the player")
    attack_list[b.id].append([a.id,attack_item])

def start_game():
    global attack_list, last_attack_list, Team_list
    print("Game start!")
    print("각각 시작할 구역을 선택하세요.")
    mv=list(map(int, stdin.readline().split()))
    assert len(mv)==n_team

    for i in range(len(mv)):
        Team_list[i+1].move_team(mv[i], 1)
    mp.show_teams()
    rd = 15
    for _ in range(rd):
        print("Round %d"%(_+1))
        print("이동 단계!")
        for i in range(n_team):
            av_sec=Team_list[i+1].moveable_sections()
            print("Team %d는 다음 구역들로 이동할 수 있습니다. "%(i+1), *av_sec)
            mv=int(input("어느 구역으로 이동하시겠습니까?"))
            if mv in av_sec:
                Team_list[i+1].move_team(mv)
            else: 
                print("이동할 수 없는 구역입니다. 움직이지 않습니다.")
        mp.show_teams()



        print("공격 선택 단계")  
        for i in range(n_team):
            print("Team %d"%(i+1))
            for j in range(len(Team_list[i+1].attack_itemlist)):
                print("%d : %s, 공격력: %d"%(j,Team_list[i+1].attack_itemlist[j],attack_dictionary[Team_list[i+1].attack_itemlist[j]]['attack']))
            sel=int(input("공격 아이템을 번호로 선택해 주세요: "))
            attack_item=Team_list[i+1].attack_itemlist[sel]
            av_attk=Team_list[i+1].attackable_teams(attack_item)
            if len(av_attk):
                print("Team %d는 %s로 다음 팀들을 공격할 수 있습니다. "%(i+1, attack_item), *av_attk)
                sel_t=int(input("어느 팀을 공격 하시겠습니까?"))
                if sel_t in av_attk:
                    attack(Team_list[i+1],Team_list[sel_t],attack_item)
                    if attack_item!='개강':
                        Team_list[i+1].remove_attitem(sel)
                else: 
                    print("공격 할 수 없는 팀 입니다. 공격하지 않습니다.")
            else:
                print("해당 아이템으로 공격할 수 있는 적이 없습니다.")
        

        print("방어 단계")

        for i in range(n_team):
            if last_attack_list[i+1]!=[]:
                print("Team %d"%(i+1))
                sm_attack=0
                for j in last_attack_list[i+1]:
                    sm_attack += attack_dictionary[j[1]]['attack']
                print("Team %d는 총 %d개의 팀으로 부터 총 %d의 공격을 받게 됩니다."%(i+1,len(last_attack_list[i+1]), sm_attack))
                update_pt=[]
                for j in range(len(last_attack_list[i+1])):
                    attack_team=last_attack_list[i+1][j][0];attack_item=last_attack_list[i+1][j][1];attack_damage=attack_dictionary[last_attack_list[i+1][j][1]]['attack']
                    print("당신은 team %d로부터 %s 무기로 공격력이 %d인 공격을 받게 됩니다."%(attack_team, attack_item, attack_damage))
                    defense=0
                    if len(Team_list[i+1].def_itemlist):
                        for j in range(len(Team_list[i+1].def_itemlist)):
                            print("%d : %s 방어력: %d"%(j,Team_list[i+1].def_itemlist[j],def_dictionary[Team_list[i+1].def_itemlist[j]]['defense']))
                        sel=int(input("방어 아이템을 번호로 선택해 주세요(사용하지 않을 경우 -1): "))
                        if sel!=-1 and sel<len(Team_list[i+1].def_itemlist):
                            def_item=Team_list[i+1].def_itemlist[sel]
                            Team_list[i+1].remove_defitem(sel)
                            print("Team %d는 %s로 방어력 %d 만큼 방어 합니다. "%(i+1, def_item,def_dictionary[def_item]['defense']))
                            defense=def_dictionary[def_item]['defense']
                    pt=attack_damage-defense
                    if pt>0:
                        Team_list[i+1].update_health(-pt)
                    update_pt.append([pt,attack_team])
                if Team_list[i+1].sleep:
                    for j in update_pt: j[0]=10
                for j in update_pt:
                    if j[0]>0: Team_list[j[1]].update_point(j[0])

        print("미니게임 아이템 획득 단계")            
        mp.show_items()
        print("기상")
        for i in range(n_team):
            if Team_list[i+1].sleep:
                print("Team %d가 캠폴에 의해 깨어나 무작위 구역에 배치됩니다."%(i+1))
                Team_list[i+1].sleep=0
                Team_list[i+1].hp=10
                for j in Team_list[i+1].def_itemlist:
                    Team_list[i+1].hp+=def_dictionary[j]['armor']
        print("라운드 종료... 통계 확인")
        for i in range(n_team):
            print("Team %d is at sector:%d, health:%d, point:%d, attack_items:"%(i+1, Team_list[i+1].pos, Team_list[i+1].hp, Team_list[i+1].points),*Team_list[i+1].attack_itemlist,", def_items:",*Team_list[i+1].def_itemlist)
        
        last_attack_list=attack_list
        attack_list=[[] for i in range(n_team+1)]
        input()
