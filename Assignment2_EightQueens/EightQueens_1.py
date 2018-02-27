# -*- coding: utf-8 -*-
"""
Crequeented on Squeent queenpr 01 14:21:29 2017

@queenuthor: Junlin Wu
"""

"""
定义求解八皇后函数
queen为1*8的向量，位置表示行，值表示列
current的值表示已经放好的皇后个数
"""
import numpy 
import random
#清空数据
output = open('data.txt', 'w')
output.close()
output = open('data.txt', 'w+')
def eight_queen(queen, current=0):
    #当current的值等于queen的长度时，说明皇后位置已经放好
    if current==len(queen):
        print queen
        #展示结果
        paint(queen)
    else:
        for col in range(len(queen)):
            #将第current行的皇后放在col列上
            queen[current] = col
            #判断是否跟前面的皇后冲突
            if all(queen[r]!=queen[current] and r-queen[r]!=current-queen[current] and r+queen[r]!=current+queen[current] for r in range(current)):
                #进行递归调用
                eight_queen(queen, current+1)

#用X表示每个皇后的位置，将结果展示出来
def paint(result):
    #画出一行结果
    def paint_line(pos, length=len(result)):
        return '. ' * (pos) + '* ' + '. '*(length-pos-1)
    #记录结果
    temp=""
    #一行一行的画出结果
    for pos in result:
        print paint_line(pos)
    for i in range(len(result)):
        temp=temp+str(result[i])
    str_convert = ''.join(temp)
    output.write(str_convert)
    output.write("\n")
    
#找到与当前位置距离最小的合法状态
def Cal_Distance(state):
    minD=20000
    index=[]
    indexR=[]
    #用来计算结果
    results=[]
    file_obj=open('data.txt','r')
    for line in file_obj:
        line=line.split('\n')[0]
        results.append(list(line))
    for result in results:
        dis=0
        for i in range(len(state)):
            dis=dis+abs(state[i]-int(result[i]))
        if minD>dis:
            minD=dis
            indexR=result
    dis,index=Distance(state,indexR)
    if dis<minD:
        minD=dis
    return minD,indexR,index

#遍历所有可能的移动方法
def Distance(vec1,vec2):
    mindis=20000
    index = [0,0, 0, 0, 0, 0, 0,0]
    dis = [0,0, 0, 0, 0, 0, 0,0]
    for i in range(len(vec1)):
        dis[0]=max(i,abs(vec1[0]-int(vec2[i])))
        for ii in range(len(vec1)):
            if(ii!=i):
                dis[1]=max(abs(ii-1),abs(vec1[1]-int(vec2[ii])))
            else:
                dis[1]=10000
            for iii in range(len(vec1)):
                if(iii!=i and iii!=ii):
                    dis[2]=max(abs(iii-2),abs(vec1[2]-int(vec2[iii])))
                else:
                    dis[2]=10000
                for iiii in range(len(vec1)):
                    if(iiii!=i and iiii!=ii and iiii!=iii):
                        dis[3]=max(abs(iiii-3),abs(vec1[3]-int(vec2[iiii])))
                    else:
                        dis[3]=10000
                    for iiiii in range(len(vec1)):
                        if(iiiii!=i and iiiii!=ii and iiiii!=iii and iiiii!=iiii):
                            dis[4]=max(abs(iiiii-4),abs(vec1[4]-int(vec2[iiiii])))
                        else:
                            dis[4]=10000
                        for iiiiii in range(len(vec1)):
                            if(iiiiii!=i and iiiiii!=ii and iiiiii!=iii and iiiiii!=iiii and iiiiii!=iiiii):
                                dis[5]=max(abs(iiiiii-5),abs(vec1[5]-int(vec2[iiiiii])))
                            else:
                                dis[5]=10000
                            for iiiiiii in range(len(vec1)):
                                if(iiiiiii!=i and iiiiiii!=ii and iiiiiii!=iii and iiiiiii!=iiii and iiiiiii!=iiiii and iiiiiii!=iiiiii):
                                    dis[6]=max(abs(iiiiiii-6),abs(vec1[6]-int(vec2[iiiiiii])))
                                else:
                                    dis[6]=10000
                                for iiiiiiii in range(len(vec1)):
                                    if(iiiiiiii!=i and iiiiiiii!=ii and iiiiiii!=iii and iiiiiiii!=iiii and iiiiiiii!=iiiii and iiiiiiii!=iiiiii and iiiiiiii!=iiiiiii):
                                        dis[7]=max(abs(iiiiiiii-7),abs(vec1[7]-int(vec2[iiiiiiii])))
                                    else:
                                        dis[7]=10000
                                    if mindis>sum(dis):
                                        mindis=sum(dis)
                                        #index=[vec2[i],vec2[ii],vec2[iii],vec2[iiii],vec2[iiiii],vec2[iiiiii],vec2[iiiiiii],vec2[iiiiiiii]]
                                        index=vec2
    return mindis,index
#调用生成八皇后的位置
eight_queen([0]*8)
output.close()
#随机生成八皇后位置
state = [0,1, 2, 3, 4, 5, 6,7]
random.shuffle(state)
print "计算中..."
[dis,result,index]=Cal_Distance(state)
print "计算完成!"
print "当前状态为：",state
print "变成合法状态最少步数为：",dis
print "合法状态为：",result



