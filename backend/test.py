#-*- coding: utf-8 -*-
import random

id_to_item=['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실 이동','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티']
item_to_id={'': 0, '개강': 1, '퀴즈': 2, '무거운 전공책': 3, '아침 수업': 4, '기숙사 호실 이동': 5, '연습반': 6, '과제': 7, '실험 수업': 8, '계절 학기': 9, '중간고사': 10, '기말고사': 11, '예습복습': 12, '낮잠': 13, '야식': 14, '튜터링': 15, '족보': 16, '공강': 17, '딸기 파티': 18, '축제': 19, '라이프': 20, '수강 철회': 21, '카이 야잠': 22, '카이 돕바': 23, '청바지': 24, '카고바지': 25, '체크남방': 26, '카이 후드티': 27}

a=[0,0,22,20,20,10,14,14,10,6,6,4]
b=[14,14,14,14,9,9,8,8,5,5,4,4,5,5,4,4] #12
item=[]
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
for i in range(42):
    item.append([])
    for j in range(3):
        item[i].append([at[i*3+j],df[i*3+j]])
for i in range(10):
    random.shuffle(item)
item.insert(0,[])
print(item)