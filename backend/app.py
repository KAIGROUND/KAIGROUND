#-*- coding: utf-8 -*-
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from json import dumps
from typing import List 
from firebase_admin import credentials, db
from threading import Thread, Timer
import firebase_admin, random, time
from waitress import serve

app = Flask(__name__)
CORS(app)
cred = credentials.Certificate("./kaistground-firebase-adminsdk-gmdug-6d30cf4f0d.json")
admin = firebase_admin.initialize_app(cred, {'databaseURL':'https://kaistground-default-rtdb.firebaseio.com'})
game_thread = None
status = db.reference('status')

stop_sig = False
 
time_idx=None
T = db.reference('time_conf').get()
n_team = 26
n_node = 42
n_round = 11

attack_dictionary = {'개강':{'attack':2, 'range':3}, '퀴즈':{'attack':4, 'range':4}, '무거운 전공책':{'attack':4, 'range':2}, '아침 수업':{'attack':4, 'range':3}, '연습반':{'attack':8, 'range':2}, '기숙사 호실 이동':{'attack':8, 'range':1}, '실험 수업':{'attack':8, 'range':3}, '과제':{'attack':8, 'range':3}, '계절 학기':{'attack':12, 'range':3}, '중간고사':{'attack':12, 'range':2}, '기말고사':{'attack':16, 'range':2}}
def_dictionary = {'예습복습':{'defense':3, 'armor':0}, '낮잠':{'defense':4, 'armor':0}, '야식':{'defense':3, 'armor':0}, '튜터링':{'defense':2, 'armor':0}, '족보':{'defense':6, 'armor':0}, '공강':{'defense':7, 'armor':0}, '딸기 파티':{'defense':5, 'armor':0}, '축제':{'defense':5, 'armor':0}, '라이프':{'defense':10, 'armor':0}, '수강 철회':{'defense':14, 'armor':0}}
up_armor_dictionary = {'카이 야잠':2, '카이 돕바':2, '체크남방':2, '카이 후드티':2, '':0} #22, 23, 26, 27
down_armor_dictionary = {'청바지':1, '카고바지':1, '':0} #24, 25

id_to_item=['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실 이동','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티']
item_to_id={'': 0, '개강': 1, '퀴즈': 2, '무거운 전공책': 3, '아침 수업': 4, '기숙사 호실 이동': 5, '연습반': 6, '과제': 7, '실험 수업': 8, '계절 학기': 9, '중간고사': 10, '기말고사': 11, '예습복습': 12, '낮잠': 13, '야식': 14, '튜터링': 15, '족보': 16, '공강': 17, '딸기 파티': 18, '축제': 19, '라이프': 20, '수강 철회': 21, '카이 야잠': 22, '카이 돕바': 23, '청바지': 24, '카고바지': 25, '체크남방': 26, '카이 후드티': 27}
item_set_left=[[], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]]
minigame_ppt_idx=[]
f=[8,21,32,44,87,99,102,133,140,155,174,183,386,401,426,444,458,463,502,525,589,592]
idx=[10,8,9,2,3,6,4,2,4,4,1,20,2,20,3,2,2,4,2,5,11,2]
nw=[]
for i in range(len(f)):
    for j in range(idx[i]):
        nw.append([f[i],j+1])
for i in range(10):
    random.shuffle(nw)
for i in range(n_node):
    minigame_ppt_idx.append([])
    for j in range(3):
        minigame_ppt_idx[i].append(nw[-1])
        nw.pop()
        for _ in range(5):
            random.shuffle(nw)
minigame_ppt_idx.insert(0,[])
pass_list = ["5a6d935", "b0c8260", "d3454b3", "23afb7b", "5f2dd02", "0cfdee4", "bb33c82", "bd75bed", "8506f42", "2f2fdd7", "38d9924", "8c587a1", "1c90a1f", "5d573b6", "bcc3d15", "e2aede3", "c8598e5", "75311b4", "d35dad6", "dfcf865", "e3e14ed", "5c53d72", "20d48be", "2f3174b", "8f282ae", "ae7d478"]
item_set_av=[]
moved_dis=[0 for i in range(n_team+1)]
sleeped_his=[0 for i in range(n_team+1)]
kill_his=[0 for i in range(n_team+1)]
rank_history = []
moved = [0 for i in range(n_team+1)]
attacked = [0 for i in range(n_team+1)]
minigame_tried= [0 for i in range(n_team+1)]

defended = dict()
check_update_point=1;end_of_game=1

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
        item=[]
        a=[0,0,14,18,16,20,16,12,12,6,6,6]
        b=[12,12,12,12,11,11,9,9,6,6,3,3,7,7,3,3] #12
        at=[];df=[]
        for i in range(len(a)):
            for j in range(a[i]):
                at.append(i)
        for i in range(10):
            random.shuffle(at)
        for i in range(len(b)):
            for j in range(b[i]):
                df.append(12+i)
        for i in range(10):
            random.shuffle(df)
        for i in range(n_node):
            item.append([])
            for j in range(3):
                item[i].append([at[i*3+j],df[i*3+j]])
        for i in range(10):
            random.shuffle(item)
        item.insert(0,[])  
        #[[[6, 13], [7, 23], [8, 13]], [[6, 13], [7, 5], [3, 4]], [[2, 13], [6, 26], [4, 4]], [[3, 22], [2, 26], [7, 15]], [[10, 12], [9, 7], [2, 14]], [[4, 4], [6, 15], [8, 14]], [], [[9, 6], [4, 18], [3, 12]], [[3, 16], [4, 27], [3, 14]], [[3, 7], [5, 18], [3, 9]], [[3, 2], [7, 19], [8, 2]], [[2, 15], [6, 3], [6, 2]], [[4, 23], [6, 13], [10, 3]], [[2, 19], [3, 5], [4, 18]], [[4, 22], [6, 27], [5, 7]], [[5, 6], [7, 13], [2, 25]], [[3, 4], [8, 27], [2, 3]], [[8, 7], [2, 15], [11, 5]], [[5, 6], [9, 16], [11, 12]], [[4, 9], [6, 16], [5, 11]], [[2, 4], [9, 10], [4, 6]], [[3, 18], [3, 2], [3, 14]], [[4, 12], [2, 7], [7, 16]], [[8, 23], [7, 14], [9, 22]], [[3, 3], [2, 22], [5, 5]], [[2, 25], [3, 7], [2, 2]], [[4, 6], [5, 8], [4, 12]], [[6, 16], [11, 14], [7, 14]], [[6, 4], [2, 22], [6, 12]], [[2, 17], [6, 26], [10, 8]], [[4, 2], [4, 13], [4, 15]], [[7, 6], [2, 12], [6, 4]], [[5, 20], [11, 13], [3, 2]], [[2, 12], [3, 4], [8, 26]], [[5, 24], [4, 21], [2, 3]], [[7, 17], [8, 17], [4, 3]], [[8, 23], [4, 8], [7, 3]], [[2, 17], [10, 23], [3, 24]], [[8, 3], [2, 24], [7, 5]], [[4, 2], [3, 19], [2, 8]], [[10, 27], [3, 10], [4, 15]], [[10, 26], [7, 19], [7, 20]], [[2, 15], [5, 27], [9, 20]]]        
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
        global moved_dis
        if not init and self.dis_node(team_pos, nd_id)>3:
            return 0
        if not init:
            moved_dis[team_id]+=self.dis_node(team_pos, nd_id)
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

Team_list = [Team(0,0,0,[],[],0)]+[Team(i+1,20,0,['개강'],[],0) for i in range(n_team)]
last_attack_list=[[] for i in range(n_team+1)] #last_attack_list[a][b] 뜻 a 팀이 last_attack_list[a][b]한테 공격 받음

def attack(a:Team, b:Team, attack_item:str): #a attack b with attack_item
    global last_attack_list, Team_list, mp
    if attack_item not in a.attack_itemlist:
        return
    last_attack_list[b.id].append([a.id,attack_dictionary[attack_item]['attack'],attack_item])

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Wrong Access</h1>", 404

@app.route("/login", methods=['POST'])
def res_login():
    global pass_list
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    team_id=int(data['me']);ps=data['pw']
    if pass_list[team_id-1]==ps:
        return jsonify({'result':0,'suc_msg':'%d반 안녕하세요'%(team_id)})
    else:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
    
@app.route("/move", methods=['POST'])
def res_move(): 
    global last_attack_list, Team_list, mp, moved, pass_list
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    if data['pw'] not in pass_list:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
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
        return jsonify({'result':0,'area':area,'suc_msg':'구역 %d로 이동했습니다.'%(area)})
    if Team_list[team_id].sleep:
        moved[team_id]=0
        return jsonify({'result':2,'err_msg':'수면상태에 빠져 있으므로 이동할 수 없습니다.'})
    av_sec=Team_list[team_id].moveable_sections()
    if area in av_sec:
        Team_list[team_id].move_team(area)
        return jsonify({'result':0,'area':area,'suc_msg':'구역 %d로 이동했습니다.'%(area)})
    else: 
        moved[team_id]=0
        return jsonify({'result':1,'err_msg':'해당 지역과의 거리가 너무 멀어서 이동할 수 없습니다.'})

@app.route("/attack", methods=['POST'])
def res_attack():
    global last_attack_list, Team_list, mp, attacked, pass_list
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    if data['pw'] not in pass_list:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
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
        attacked[team_id]=0
        return jsonify({'result':1,'err_msg':'인벤토리에 해당 아이템이 없습니다.'})
    av_attk=Team_list[team_id].attackable_teams(attack_item)
    if team_to_attack==team_id:
        attacked[team_id]=0
        return jsonify({'result':1,'err_msg':'자신의 팀을 공격할 수 없습니다.'})
    if team_to_attack not in av_attk:
        attacked[team_id]=0
        return jsonify({'result':1,'err_msg':'해당 팀을 공격하기에는 너무 멀리 있습니다.'})
    attack(Team_list[team_id],Team_list[team_to_attack],attack_item)
    if attack_item!='개강':
        Team_list[team_id].remove_attitem(attack_item)
    dic=dict()
    for i in Team_list[team_id].attack_itemlist:
        if item_to_id[i] not in dic.keys():
            dic[item_to_id[i]]=1
        else: dic[item_to_id[i]]+=1
    return jsonify({'result':0,'attack_list':dumps(dic),'suc_msg':'팀 %d에게 공격력이 %d인 %s으로 공격 했습니다!'%(team_to_attack,attack_dictionary[attack_item]['attack'],attack_item)})
    
@app.route("/defense", methods=['POST'])
def res_defense():
    global last_attack_list, Team_list, mp, defended, pass_list
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    if data['pw'] not in pass_list:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
    team_id=int(data['me']);team_to_defend=int(data['classroom']);item_id=int(data['item'])
    if (team_id,team_to_defend) in defended.keys() and defended[(team_id,team_to_defend)]:
        return jsonify({'result':1,'err_msg':'해당 공격에 대해서는 이미 방어 아이템을 사용 했습니다.'})
    defended[(team_id,team_to_defend)]=1
    def_item=id_to_item[item_id]
    if def_item not in Team_list[team_id].def_itemlist:
        defended[(team_id,team_to_defend)]=0
        return jsonify({'result':1,'err_msg':'인벤토리에 해당 아이템이 없습니다.'})
    fl=0;attack_item=''
    for i in range(len(last_attack_list[team_id])):
        if last_attack_list[team_id][i][0]==team_to_defend: 
            last_attack_list[team_id][i][1]-=def_dictionary[def_item]['defense'] #lastattacklist[id][i][1] can be minus!!!!
            attack_item=last_attack_list[team_id][i][2];fl=1
    if not fl:
        defended[(team_id,team_to_defend)]=0
        return jsonify({'result':1,'err_msg':'해당 팀은 본 팀을 공격하지 않았습니다.'})
    Team_list[team_id].remove_defitem(def_item)
    dic=dict()
    for i in Team_list[team_id].def_itemlist:
        if item_to_id[i] not in dic.keys():
            dic[item_to_id[i]]=1
        else: dic[item_to_id[i]]+=1
    return jsonify({'result':0,'defense_list':dumps(dic),'suc_msg':'%s 아이템으로 팀 %d의 %s 공격의 피해를 %d만큼 감소시킵니다.'%(def_item,team_to_defend,attack_item,def_dictionary[def_item]['defense'])})

@app.route("/inventory", methods=['GET'])
def res_inventory():
    global last_attack_list, Team_list, mp
    if not request.args.get('me').isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
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
    dic_attk[1]='∞'
    return jsonify({'attack_list':dumps(dic_attk),'defense_list':dumps(dic_def),'top':item_to_id[Team_list[team_id].up_armor],'bottom':item_to_id[Team_list[team_id].down_armor]})

@app.route("/get_attack", methods=['GET'])
def res_get_attack():
    global last_attack_list, Team_list, mp
    if not request.args.get('me').isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    team_id:int = int(request.args.get('me'))
    dic=dict()
    for i in last_attack_list[team_id]:
        dic[i[0]]=item_to_id[i[2]]
    return jsonify({'team_list':dumps(dic)})

@app.route("/minigame", methods=['GET'])
def res_minigame():
    global last_attack_list, Team_list, mp, item_set_left
    if not request.args.get('me').isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
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
    global last_attack_list, Team_list, mp, item_set_left, item_set_av, minigame_ppt_idx,pass_list, minigame_tried
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    if data['pw'] not in pass_list:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
    team_id=int(data['me']);sel=int(data['select']);sec=Team_list[team_id].pos
    if not (0<=sel<=2):
        return jsonify({'result':1,'err_msg':'select 숫자가 0~2가 아닙니다.'})
    if item_set_left[sec][sel]==0:
        return jsonify({'result':1,'err_msg':'해당 아이템 세트 수량이 부족해 도전할 수 없습니다.'})
    if item_set_av[team_id][sec][sel]:
        return jsonify({'result':2,'err_msg':'해당 아이템 세트는 이미 도전한 아이템 세트 입니다.'})
    if minigame_tried[team_id]:
        return jsonify({'result':3,'err_msg':'한턴에 두번 아이템 세트에 도전하는건 좀 너무하지 않나요?'})
    minigame_tried[team_id]=1;item_set_av[team_id][Team_list[team_id].pos][sel]=1
    item_set_left[sec][sel]-=1
    if minigame_ppt_idx[sec][sel][0] in [174,589,99]:
        return jsonify({'result':0,'msg':'<b>%d번째</b> 슬라이드로 이동하여 게임 규칙을 확인하고 해당 게임을 시작해 주세요!'%(minigame_ppt_idx[sec][sel][0])}) 
    return jsonify({'result':0,'msg':'<b>%d번째</b> 슬라이드로 이동하여 게임 규칙을 확인하고 해당 게임의 <b>%d번째</b> 게임을 시작해 주세요!'%(minigame_ppt_idx[sec][sel][0],minigame_ppt_idx[sec][sel][1])})

@app.route("/minisuccess", methods=['POST'])
def res_minisuccess ():
    global last_attack_list, Team_list, mp, item_set_left, pass_list, minigame_tried, item_set_av
    data = request.get_json()
    if not data['me'].isdigit():
        return jsonify({'result':1,'err_msg':'Wrong Reuest'})
    if data['pw'] not in pass_list:
        return jsonify({'result':1,'err_msg':'권한이 없습니다.'})
    team_id=int(data['me']);sel=int(data['select']);suc=int(data['success'])
    if not (0<=sel<=2):
        return jsonify({'result':1,'err_msg':'select 숫자가 0~2가 아닙니다.'})
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
    global time_idx, last_attack_list, Team_list, mp, item_set_left, item_set_av
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
    global time_idx, last_attack_list, Team_list, mp, item_set_left, item_set_av, moved, attacked, check_update_point, defended, end_of_game, stop_sig, minigame_tried, moved_dis, rank_history, sleeped_his, kill_his, n_round
    #mode 0 : move, 1 : attack,game, 2 : def , 3 : wait
    #2분 시작할 때
    t_sum = T[0] + T[1] + T[2] + T[3] + T[4] + T[5]
    if time_idx%t_sum == 0:
        turn = (time_idx // t_sum) + 1
        if turn > n_round and end_of_game:
            end_of_game=0
            #Game end
            for i in range(n_team):
                if Team_list[i+1].sleep:
                    sleeped_his[i+1]+=1
                    Team_list[i+1].sleep=0
                    Team_list[i+1].hp=20+up_armor_dictionary[Team_list[i+1].up_armor]+down_armor_dictionary[Team_list[i+1].down_armor]
                    Team_list[i+1].up_armor='';Team_list[i+1].down_armor=''
                    Team_list[i+1].move_team(random.randint(1,n_node),init=1)
            update_database()
            defended=dict()
            #rank selction
            final_rank=[0 for _ in range(n_team+1)]
            sum_rank=[[0,i] for i in range(n_team+1)]
            rk=0 
            for j in range(len(sum_rank)):
                sum_rank[j][0]+=rank_history[-1][sum_rank[j][1]]
            sum_rank.sort()
            i=0
            while i<len(sum_rank):
                if i==len(sum_rank)-1 or (i<len(sum_rank)-1 and sum_rank[i][0]!=sum_rank[i+1][0]):
                    final_rank[sum_rank[i][1]]=rk;rk+=1
                else:
                    j=1;a=sum_rank[i][0];b=sum_rank[i+1][0]
                    while j<len(rank_history)-1 and a==b:
                        a+=rank_history[-1-j][sum_rank[i][1]]
                        b+=rank_history[-1-j][sum_rank[i+1][1]]
                        j+=1
                    if a>b:
                        final_rank[sum_rank[i+1][1]]=rk;rk+=1
                        final_rank[sum_rank[i][1]]=rk;rk+=1
                    else:
                        final_rank[sum_rank[i][1]]=rk;rk+=1
                        final_rank[sum_rank[i+1][1]]=rk;rk+=1
                    i+=1
                i+=1
            get_special=[];s1=0;s2=0
            for i in range(n_team):
                if final_rank[i+1]==21:
                    s2=i+1
            for i in range(n_team):
                get_special.append((moved_dis[i+1],-Team_list[i+1].points,i+1))
            get_special.sort(reverse=1)
            for i in range(len(get_special)):
                if 0<=final_rank[get_special[i][2]]<=3 or final_rank[get_special[i][2]]==21:
                    continue
                s1=get_special[i][2]
                break
            
            #set statistics
            all_dic=dict()
            for i in range(n_team):
                dic=dict()
                dic['move_cnt']=moved_dis[i+1]
                dic['sleep_cnt']=sleeped_his[i+1]
                dic['kill_cnt']=kill_his[i+1]
                dic['rank']=final_rank[i+1] #rank
                if s1==i+1:
                    dic['s1']=1
                if s2==i+1:
                    dic['s2']=1
                all_dic[i+1]=dic
            db.reference("winner").set(all_dic)
            stop_sig = True
            set_value("status", "mode", 3)
            set_value("status", "turn", 0)

        set_value("status", "turn", turn)
        set_value("status", "mode", 0)
    #2분 끝나고 3초
    if time_idx%t_sum == (T[0] + 3):
        for i in range(n_team):
            if Team_list[i+1].sleep:
                sleeped_his[i+1]+=1
                Team_list[i+1].sleep=0
                Team_list[i+1].hp=20+up_armor_dictionary[Team_list[i+1].up_armor]+down_armor_dictionary[Team_list[i+1].down_armor]
                Team_list[i+1].up_armor='';Team_list[i+1].down_armor=''
                Team_list[i+1].move_team(random.randint(1,n_node),init=1)
        turn = (time_idx // t_sum) + 1
        if turn==1:
            for i in range(n_team):
                if not Team_list[i+1].pos:
                    Team_list[i+1].move_team(random.randint(1,n_node),init=1)
        update_database()
        defended=dict()
    #7분 시작할 때
    if time_idx%t_sum == (T[0] + T[1]):
        set_value("status", "mode", 1)
    #7분 끝나고 3초
    if time_idx%t_sum == (T[0] + T[1] + T[2] + 3):
        moved = [0 for i in range(n_team+1)];check_update_point=1
    #9분 시작할 때
    if time_idx%t_sum == (T[0] + T[1] + T[2] + T[3]):
        set_value("status", "mode", 2)
    #9분 끝나고 3초
    if time_idx%t_sum == (T[0] + T[1] + T[2] + T[3] + T[4] + 3) and check_update_point:
        check_update_point=0
        for i in range(n_team):
            update_pt=[]
            for j in last_attack_list[i+1]:
                if j[1]>0:
                    Team_list[i+1].update_health(-j[1])
                update_pt.append([j[1],j[0]])
            if Team_list[i+1].sleep:
                for j in update_pt: 
                    j[0]=10
                    kill_his[j[1]]+=1
            for j in update_pt:
                if j[0]>0: Team_list[j[1]].update_point(j[0])
        for i in range(n_team):
            if Team_list[i+1].sleep:
                Team_list[i+1].move_team(0,init=1)
        update_database()
        last_attack_list=[[] for i in range(n_team+1)]
        rank_nw=[0 for i in range(n_team+1)] #input the rank of each class
        nw=[];mx=1e9;rank=0
        for i in range(n_team):
            nw.append((Team_list[i+1].points,i+1))
        nw.sort(reverse=1)
        for i in nw:
            if i[0]<mx:
                rank+=1;mx=i[0]
            rank_nw[i[1]]=rank
        rank_history.append(rank_nw)
        minigame_tried = [0 for i in range(n_team+1)]
        attacked = [0 for i in range(n_team+1)]

    time_idx += 1
    set_value("status", "time_idx", time_idx)

def run_game():
    global time_idx
    time_idx = status.child('time_idx').get()
    set_value("status", "turn", time_idx // (T[0] + T[1] + T[2] + T[3] + T[4] + T[5]) + 1)
    if time_idx % (T[0] + T[1] + T[2] + T[3] + T[4] + T[5]) < T[0]:
        set_value("status", "mode", 0)
    elif (T[0] + T[1]) < time_idx % (T[0] + T[1] + T[2] + T[3] + T[4] + T[5]) < (T[0] + T[1] + T[2]):
        set_value("status", "mode", 1)
    elif (T[0] + T[1] + T[2] + T[3]) < time_idx % (T[0] + T[1] + T[2] + T[3]) < (T[0] + T[1] + T[2] + T[3] + T[4]):
        set_value("status", "mode", 2)
    set_interval(every_second, 1)

@app.route('/init', methods=['GET'])
def res_init():
    global stop_sig
    stop_sig = False
    if request.args.get('ps')!="3141592":
        return 'Not admin'
    idx = request.args.get('time_idx')
    if (idx is not None) and int(idx)!=0:
        set_value("status", "time_idx", int(idx))
    else:
        set_value("status", "mode", 4)
        time.sleep(10)
        set_value("status", "time_idx", 0)
    update_database()
    game_thread = Thread(target=run_game)
    game_thread.start()
    return 'Start to run'

@app.route('/stop')
def res_stop():
    if request.args.get('ps')!="3141592":
        return 'Not admin'
    global stop_sig
    stop_sig = True
    set_value("status", "mode", 3)
    set_value("status", "turn", 0)
    return 'Stopped'

@app.route('/')
def mainpage():
    return 'Go to init'

for i in range(n_team+1):
    item_set_av.append([])
    for j in range(n_node+1):
        item_set_av[i].append([])
        for k in range(3):
            item_set_av[i][j].append(0)

db.reference("winner").delete()
set_value("status", "mode", 3)
set_value("status", "turn", 0)
for i in range(n_node):
    for j in range(3):
        if (mp.g[i+1].items[j][0] in [9, 10, 11]) or (mp.g[i+1].items[j][1] in [20, 21]):
            item_set_left[i+1][j]=3
update_database()
if __name__=="__main__":
    serve(app, host='0.0.0.0', port=5555, threads=26)