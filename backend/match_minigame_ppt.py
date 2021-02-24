#-*- coding: utf-8 -*-
import random

minigame_ppt_idx=[]
n_node=42

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
print(minigame_ppt_idx)