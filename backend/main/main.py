#-*- coding: euc-kr -*-
n_team = 26
n_node = 42

class Node:
    def __init__(self, nd_id, items, teams, adj):
        self.nd_id=nd_id
        self.items=items #items dictionary list
        self.teams=teams #deployed teams
        self.adj=adj #adjacent node id

class graph:
    def __init__(self, n_node=n_node):
        self.g=[] #차례로 1번 노드부터~ ~!!!! 0번째 노드는 사용하지 않음
        self.d=[[1e10 for _ in range(n_node+1)] for i in range(n_node+1)]
        for i in range(n_node+1): self.d[i][i]=0
        adj=[[],[2,4,20],[1,3],[2,8],[1,5],[4,6],[5,7,10],[6,8],[3,7,9,17],[8,10],[6,9,11],[10,12],[11,13,32],[12,14],[15,27,13],[16,14],[17,15],[8,16,18],[17,19],[18,20,26],[1,19,21],[20,22],[21,23],[22,24],[23,25,42],[24,26,27],[19,25],[14,25,28],[27,29,40],[28,30],[29,31],[30,32],[12,31,33],[32,34],[33,35],[34,36],[35,37],[38,39,41,36],[37,42],[40,37],[28,39],[37,42],[41,38,24]] #직접 만들기
        item=[[] for i in range(n_node+1)]
        team=[[i for i in range(1, n_team+1,1)]] + [[] for i in range(n_node)] #초기화시 모든 팀은 0에 있음
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
        
    def move(self, nd_id, team): #team class
        if self.dis_node(team.node_id, team)>3:
            print("멀어서 이동이 불가능 합니다.!")
            return
        self.g[team.node_id].teams.remove(team.id)
        self.g[nd_id].teams.append(team.id)

    def add_item(self, nd_id, item):
        self.g[nd_id].items.append(item)

map=graph()
print(map.dis_node(1,4))