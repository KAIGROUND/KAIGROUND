#-*- coding: utf-8 -*-
import random

minigame_ppt_idx=[]
n_node=42

f=[8,21,32,44,87,99,104,135,144,159,178,186,389,406,431,454,468,472,489,513,534,537,546]
idx=[10,8,9,2,3,6,4,2,4,2,1,20,1,20,2,2,1,1,2,1,10,5,10]
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