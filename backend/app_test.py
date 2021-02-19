#-*- coding: utf-8 -*-
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from json import dumps
from typing import List 
from firebase_admin import credentials, db
from threading import Thread, Timer
import sys, time, firebase_admin, random

app = Flask(__name__)
CORS(app)
cred = credentials.Certificate("./kaistground-firebase-adminsdk-gmdug-6d30cf4f0d.json")
admin = firebase_admin.initialize_app(cred, {'databaseURL':'https://kaistground-default-rtdb.firebaseio.com'})
game_thread = None
status = db.reference('status')
stop_sig = False

time_idx=None
T=[120,5,300,5]
n_team = 26
n_node = 42

attack_dictionary = {'개강':{'attack':1, 'range':10}, '퀴즈':{'attack':2, 'range':6}, '무거운 전공책':{'attack':2, 'range':2}, '아침 수업':{'attack':2, 'range':4}, '연습반':{'attack':4, 'range':2}, '기숙사 호실 이동':{'attack':4, 'range':1}, '과제':{'attack':4, 'range':3}, '계절 학기':{'attack':4, 'range':3}, '중간고사':{'attack':6, 'range':2}, '기말고사':{'attack':8, 'range':4}, '실험 수업':{'attack':4, 'range':3}}
def_dictionary = {'예습복습':{'defense':1, 'armor':0}, '낮잠':{'defense':1, 'armor':0}, '야식':{'defense':1, 'armor':0}, '튜터링':{'defense':1, 'armor':0}, '족보':{'defense':3, 'armor':0}, '공강':{'defense':3, 'armor':0}, '딸기 파티':{'defense':3, 'armor':0}, '축제':{'defense':3, 'armor':0}, '라이프':{'defense':5, 'armor':0}, '수강 철회':{'defense':7, 'armor':0}}
up_armor_dictionary = {'카이 야잠':2, '카이 돕바':2, '체크남방':2, '카이 후드티':2, '':0} #22, 23, 26, 27
down_armor_dictionary = {'청바지':1, '카고바지':1, '':0} #24, 25

id_to_item=['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실 이동','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티']
item_to_id={'': 0, '개강': 1, '퀴즈': 2, '무거운 전공책': 3, '아침 수업': 4, '기숙사 호실 이동': 5, '연습반': 6, '과제': 7, '실험 수업': 8, '계절 학기': 9, '중간고사': 10, '기말고사': 11, '예습복습': 12, '낮잠': 13, '야식': 14, '튜터링': 15, '족보': 16, '공강': 17, '딸기 파티': 18, '축제': 19, '라이 프': 20, '수강 철회': 21, '카이 야잠': 22, '카이 돕바': 23, '청바지': 24, '카고바지': 25, '체크남방': 26, '카이 후드티': 27}
item_set_left=[[], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]]
minigame_ppt_idx=[[], [[129, 2], [400, 17], [94, 1]], [[8, 2], [20, 5], [177, 3]], [[177, 13], [137, 1], [529, 8]], [[99, 2], [8, 1], [400, 20]], [[177, 14], [99, 1], [539, 5]], [[20, 3], [20, 2], [531, 2]], [[137, 2], [94, 3], [177, 2]], [[177, 8], [177, 5], [529, 9]], [[539, 3], [177, 10], [383, 1]], [[177, 6], [400, 7], [8, 4]], [[531, 4], [129, 1], [41, 1]], [[99, 3], [177, 5], [529, 10]], [[30, 4], [531, 3], [177, 9]], [[400, 10], [30, 7], [485, 2]], [[151, 2], [400, 11], [151, 1]], [[20, 4], [177, 19], [400, 2]], [[451, 1], [529, 4], [137, 4]], [[451, 2], [529, 7], [8, 9]], [[169, 1], [529, 3], [20, 1]], [[30, 3], [30, 1], [531, 5]], [[83, 2], [8, 6], [94, 5]], [[400, 16], [464, 1], [400, 18]], [[83, 1], [20, 7], [539, 9]], [[400, 15], [539, 4], [20, 6]], [[539, 7], [529, 6], [177, 7]], [[8, 3], [531, 1], [539, 1]], [[529, 2], [177, 11], [539, 2]], [[400, 12], [400, 4], [425, 2]], [[529, 5], [177, 20], [400, 9]], [[400, 14], [94, 4], [8, 10]], [[177, 12], [539, 10], [400, 1]], [[177, 8], [30, 5], [30, 2]], [[30, 6], [177, 16], [177, 18]], [[539, 8], [30, 8], [83, 3]], [[177, 15], [539, 6], [468, 1]], [[400, 6], [20, 8], [425, 1]], [[8, 5], [529, 1], [508, 1]], [[94, 6], [400, 13], [94, 2]], [[8, 7], [137, 3], [485, 1]], [[177, 1], [30, 9], [177, 4]], [[177, 17], [41, 2], [400, 3]], [[99, 4], [400, 19], [8, 8]]]
item_set_av=[]
moved = [0 for i in range(n_team+1)]
attacked = [0 for i in range(n_team+1)]
defended = dict()
check_update_point=1

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

mp=graph(n_node)

class Team:
    def __init__(self, id:int, health, points, attack_itemlist:list, def_itemlist:list, sleep):
        self.id=id
        self.pos=0 #section no.
        self.hp=health
        self.points=points
        self.attack_itemlist=attack_itemlist
        self.def_itemlist=def_itemlist
        self.up_armor=''
        self.down_armor=''
        self.sleep=sleep

    def update_health(self, health):
        if self.sleep: return
        self.hp+=health
        if self.hp<=0:
            self.sleep=1;self.hp=0
            self.update_point(-5)

    def update_point(self, point):
        self.points+=point

    def add_item_by_index(self, item_id):
        if 1<=item_id<=11:
            self.attack_itemlist.append(id_to_item[item_id])
        elif 12<=item_id<=21:
            self.def_itemlist.append(id_to_item[item_id])
        elif 24<=item_id<=25:
            self.down_armor=id_to_item[item_id]
        else:
            self.up_armor=id_to_item[item_id]

    def remove_attitem(self, attitem):
        del self.attack_itemlist[self.attack_itemlist.index(attitem)]

    def remove_defitem(self, defitem):
        del self.def_itemlist[self.def_itemlist.index(defitem)]

    def move_team(self, nd_id, init=0, mp:graph=mp):
        if not mp.move_g(nd_id, self.pos, self.id, init):
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
                rt+=[i]
        return rt

Team_list = [Team(0,0,0,[],[],0)]+[Team(i+1,10,0,['개강'],[],0) for i in range(n_team)]
attack_list=[[] for i in range(n_team+1)] #attack_list[a][b] 뜻 a 팀이 attack_list[a][b]한테 공격 받음
last_attack_list=[[] for i in range(n_team+1)]

def attack(a:Team, b:Team, attack_item:str): #a attack b with attack_item
    global attack_list, last_attack_list, Team_list, mp
    if attack_item not in a.attack_itemlist:
        return
    attack_list[b.id].append([a.id,attack_dictionary[attack_item]['attack'],attack_item])

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Wrong Access</h1>", 404

@app.route("/move", methods=['POST'])
def res_move(): 
    global attack_list, last_attack_list, Team_list, mp, moved
    data = request.get_json()
    if not data['area'].isdigit():
        return jsonify({'result':1,'err_msg':'이동할 구역은 숫자이여야 합니다.'})
    team_id=int(data['me']);area=int(data['area']);init=int(data['initial'])
    if not (1<=area<=n_node):
        return jsonify({'result':1,'err_msg':'이동할 구역은 1~42 사이의 숫자이여야 합니다.'})
    if moved[team_id]:
        return jsonify({'result':1,'err_msg':'한 턴에는 한번만 이동할 수 있습니다.'})
    moved[team_id]=1
    if not init:
        Team_list[team_id].move_team(area,init=1)
        return jsonify({'result':0,'area':area})
    if Team_list[team_id].sleep:
        return jsonify({'result':2,'err_msg':'수면상태에 빠져 있으므로 이동할 수 없습니다.'})
    av_sec=Team_list[team_id].moveable_sections()
    if area in av_sec:
        Team_list[team_id].move_team(area)
        return jsonify({'result':0,'area':area})
    else: 
        return jsonify({'result':1,'err_msg':'해당 지역과의 거리가 너무 멀어서 이동할 수 없습니다.'})

@app.route("/attack", methods=['POST'])
def res_attack():
    global attack_list, last_attack_list, Team_list, mp, attacked
    data = request.get_json()
    if not data['classroom'].isdigit():
        return jsonify({'result':1,'err_msg':'공격할 반은 숫자이여야 합니다.'})
    team_id=int(data['me']);team_to_attack=int(data['classroom']);item_id=int(data['item'])
    if not (1<=team_to_attack<=n_team):
        return jsonify({'result':1,'err_msg':'공격할 반은 1~26 사이의 숫자이여야 합니다.'})
    if attacked[team_id]:
        return jsonify({'result':1,'err_msg':'한 턴에 두번 공격할 수 없습니다.'})
    attacked[team_id]=1
    attack_item=id_to_item[item_id]
    if attack_item not in Team_list[team_id].attack_itemlist:
        return jsonify({'result':1,'err_msg':'인벤토리에 해당 아이템이 없습니다.'})
    av_attk=Team_list[team_id].attackable_teams(attack_item)
    if team_to_attack==team_id:
        return jsonify({'result':1,'err_msg':'자신의 팀을 공격할 수 없습니다.'})
    if team_to_attack not in av_attk:
        return jsonify({'result':1,'err_msg':'해당 팀을 공격하기에는 너무 멀리 있습니다.'})
    attack(Team_list[team_id],Team_list[team_to_attack],attack_item)
    if attack_item!='개강':
        Team_list[team_id].remove_attitem(attack_item)
    dic=dict()
    for i in Team_list[team_id].attack_itemlist:
        if item_to_id[i] not in dic.keys():
            dic[item_to_id[i]]=1
        else: dic[item_to_id[i]]+=1
    return jsonify({'result':0,'attack_list':dumps(dic)})
    
@app.route("/defense", methods=['POST'])
def res_defense():
    global attack_list, last_attack_list, Team_list, mp, defended
    data = request.get_json()
    team_id=int(data['me']);team_to_defend=int(data['classroom']);item_id=int(data['item'])
    if (team_id,team_to_defend) in defended.keys():
        return jsonify({'result':1,'err_msg':'해당 공격에 대해서는 이미 방어 아이템을 사용 했습니다.'})
    defended[(team_id,team_to_defend)]=1
    def_item=id_to_item[item_id]
    if def_item not in Team_list[team_id].def_itemlist:
        return jsonify({'result':1,'err_msg':'인벤토리에 해당 아이템이 없습니다.'})
    fl=0
    for i in last_attack_list[team_id]:
        if i[0]==team_to_defend: 
            last_attack_list[team_id][1]-=def_dictionary[def_item]['defense'] #lastattacklist[id][1] can be minus!!!!
            fl=1
    if not fl:
        return jsonify({'result':1,'err_msg':'해당 팀은 본 팀을 공격하지 않았습니다.'})
    Team_list[team_id].remove_defitem(def_item)
    dic=dict()
    for i in Team_list[team_id].def_itemlist:
        if item_to_id[i] not in dic.keys():
            dic[item_to_id[i]]=1
        else: dic[item_to_id[i]]+=1
    return jsonify({'result':0,'defense_list':dumps(dic)})

@app.route("/inventory", methods=['GET'])
def res_inventory():
    global attack_list, last_attack_list, Team_list, mp
    team_id:int = int(request.args.get('me'))
    dic_def=dict();dic_attk=dict()
    for i in Team_list[team_id].def_itemlist:
        if item_to_id[i] not in dic_def.keys():
            dic_def[item_to_id[i]]=1
        else: dic_def[item_to_id[i]]+=1

    for i in Team_list[team_id].attack_itemlist:
        if item_to_id[i] not in dic_attk.keys():
            dic_attk[item_to_id[i]]=1
        else: dic_attk[item_to_id[i]]+=1
    return jsonify({'attack_list':dumps(dic_attk),'defense_list':dumps(dic_def),'top':item_to_id[Team_list[team_id].up_armor],'bottom':item_to_id[Team_list[team_id].down_armor]})

@app.route("/get_attack", methods=['GET'])
def res_get_attack():
    global attack_list, last_attack_list, Team_list, mp
    team_id:int = int(request.args.get('me'))
    dic=dict()
    for i in last_attack_list[team_id]:
        dic[i[0]]=item_to_id[i[2]]
    return jsonify({'team_list':dumps(dic)})

@app.route("/minigame", methods=['GET'])
def res_minigame():
    global attack_list, last_attack_list, Team_list, mp, item_set_left
    team_id:int=int(request.args.get('me'))
    sec=Team_list[team_id].pos
    dic=dict()
    for i in range(len(mp.g[sec].items)):
        dic_item=dict()
        dic_item['item1']=mp.g[sec].items[i][0]
        dic_item['item2']=mp.g[sec].items[i][1]
        dic_item['cnt']=item_set_left[sec][i]
        dic[i]=dic_item
    return jsonify({'data':dumps(dic)})

@app.route("/miniselect", methods=['POST'])
def res_miniselect():
    global attack_list, last_attack_list, Team_list, mp, item_set_left, item_set_av, minigame_ppt_idx
    data = request.get_json()
    team_id=int(data['me']);sel=int(data['select']);sec=Team_list[team_id].pos
    if item_set_left[sec][sel]==0:
        return jsonify({'result':1,'err_msg':'해당 아이템 세트 수량이 부족해 도전할 수 없습니다.'})
    if item_set_av[team_id][sec][sel]:
        return jsonify({'result':2,'err_msg':'해당 아이템 세트는 이미 도전한 아이템 세트 입니다.'})
    item_set_left[sec][sel]-=1;item_set_av[team_id][sec][sel]=1
    return jsonify({'result':0,'msg':'%d번째 슬라이드로 이동하여 게임 규칙을 확인하고 해당 게임의 %d번째 게임을 해주세요!'%(minigame_ppt_idx[sec][sel][0],minigame_ppt_idx[sec][sel][1])}) #minigame_ppt_idx[sec][sel]

@app.route("/minisuccess", methods=['POST'])
def res_minisuccess ():
    global attack_list, last_attack_list, Team_list, mp, item_set_left
    data = request.get_json()
    team_id=int(data['me']);sel=int(data['select']);suc=int(data['success'])
    pos=Team_list[team_id].pos
    if not suc:
        for i in mp.g[pos].items[sel]:
            Team_list[team_id].add_item_by_index(i)
    else:
        item_set_left[pos][sel]+=1
    return jsonify({'result':0})

#firebase update
def set_value(ref, child, val):
    db.reference(ref).child(child).set(val)

def update_database():
    global time_idx, attack_list, last_attack_list, Team_list, mp, item_set_left, item_set_av
    dic=dict()
    for i in range(n_team):
        dic[i+1]=Team_list[i+1].pos
    db.reference("pos").set(dic)
    dic=dict()
    for i in range(n_team):
        dic[i+1]=Team_list[i+1].hp
    db.reference("stamina").set(dic)
    dic=dict()
    for i in range(n_team):
        dic[i+1]=Team_list[i+1].points
    db.reference("point").set(dic)

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = None
    if not stop_sig:
        t = Timer(sec, func_wrapper)
        t.start()
    return t

def every_second():
    global time_idx, attack_list, last_attack_list, Team_list, mp, item_set_left, item_set_av, moved, attacked, check_update_point, defended
    #mode 0 : move, 1: bg, 2: wait
    #2분 시작할 때
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == 0:
        turn = (time_idx // (T[0] + T[1] + T[2] + T[3])) + 1
        if turn > 15:
            sys.exit()
        set_value("status", "turn", turn)
        set_value("status", "mode", 0)
    #2분 끝나고 3초
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + 3):
        for i in range(n_team):
            if Team_list[i+1].sleep:
                Team_list[i+1].sleep=0
                Team_list[i+1].hp=10+up_armor_dictionary[Team_list[i+1].up_armor]+down_armor_dictionary[Team_list[i+1].down_armor]
                Team_list[i+1].move_team(random.randint(1,n_node),init=1)
        update_database()
        moved = [0 for i in range(n_team+1)];check_update_point=1
    #5분 시작할 때
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + T[1]):
        set_value("status", "mode", 1)
    #5분 끝나고 3초
    if time_idx%(T[0] + T[1] + T[2] + T[3]) == (T[0] + T[1] + T[2] + 3) and check_update_point:
        check_update_point=0
        for i in range(n_team):
            update_pt=[]
            for j in last_attack_list[i+1]:
                if j[1]>0:
                    Team_list[i+1].update_health(-j[1])
                update_pt.append([j[1],j[0]])
            if Team_list[i+1].sleep:
                for j in update_pt: j[0]=10
            for j in update_pt:
                if j[0]>0: Team_list[j[1]].update_point(j[0])
        for i in range(n_team):
            if Team_list[i+1].sleep:
                Team_list[i+1].move_team(0,init=1)
        update_database()
        last_attack_list=attack_list
        attack_list=[[] for i in range(n_team+1)]
        attacked = [0 for i in range(n_team+1)]
        defended=dict()
    time_idx += 1
    set_value("status", "time_idx", time_idx)

def run_game():
    global time_idx
    time_idx = status.child('time_idx').get()
    set_value("status", "turn", time_idx // (T[0] + T[1] + T[2] + T[3]) + 1)
    if time_idx % (T[0] + T[1] + T[2] + T[3]) < T[0]:
        set_value("status", "mode", 0)
    elif (T[0] + T[1]) < time_idx % (T[0] + T[1] + T[2] + T[3]) < (T[0] + T[1] + T[2]):
        set_value("status", "mode", 1)
    set_interval(every_second, 1)

@app.route('/init')
def res_init():
    global stop_sig
    stop_sig = False
    idx = request.args.get('time_idx')
    if idx is not None:
        set_value("status", "time_idx", int(idx))
    else:
        set_value("status", "time_idx", 0)
    game_thread = Thread(target=run_game)
    game_thread.start()
    return 'Start to run'

@app.route('/stop')
def res_stop():
    global stop_sig
    stop_sig = True
    set_value("status", "mode", 2)
    set_value("status", "turn", 0)

    return 'Stopped'

@app.route('/')
def admin_init():
    return "<h1>Go to init</h1>"
if __name__=="__main__":
    for i in range(n_team+1):
        item_set_av.append([])
        for j in range(n_node+1):
            item_set_av[i].append([])
            for k in range(3):
                item_set_av[i][j].append(0)
    app.run(host="127.0.0.1", port=5555, debug=0)