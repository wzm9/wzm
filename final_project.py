#encoding:utf-8
"""
程序目标：通过自定义函数的方式，实现在屏幕上任意输入一串英文字符，根据字典中的配对，
在屏幕上输出其对应的加密字符。（如输入python，则输出037n67）
作者：文正梅
"""
import os,sys
import jieba,codecs,math
import jieba.posseg as pg
character={}  # 姓名字典
relationships={} # 关系字典
lineNames=[] # 每段内人物关系
jieba.load_userdict('dict.txt')
with codecs.open("黎明破晓的街道.txt",'r') as file1:
	for x in file1.readlines():
		ps=pg.cut(x) #分词并返回该词词性
		lineNames.append([])#为新读入的一段添加人物名称列表
		for w in ps:   
			if w.flag != "nr" or len(w.word) < 2:
				continue  #当分词长度小于2或该词词性不为nr时认为该词不为人名
			lineNames[-1].insert(-1,w.word) #为当前段的环境增加一个人物
			if character.get(w.word) is None:
				character[w.word]=0
				relationships[w.word]={}
			character[w.word]+=1#该人物出现次数加 1
	for name,times in character.items():
		print (name,times)
for x in lineNames:
	for name1 in x:
		for name2 in x: 
			if name1==name2:
				continue
			if relationships[name1].get(name2) is None:
				relationships[name1][name2]=1
			else:
				relationships[name1][name2]+=1
#过滤冗余的边并输出结果，将已经建立好的character和relationships输出到文本
with codecs.open('黎明破晓的街道_node.csv','w') as file1:
	file1.write("id lable weight\r\n")
	for name,times in character.items():
		file1.write(name+" "+name+" "+str(times)+"\r\n")
#节点集合保存在busan_node.csv
with codecs.open('黎明破晓的街道_edge.csv','w') as file1:
	file1.write("source target weight\r\n")
	for name,edges in relationships.items():
		for v, w in edges.items():
			if w>3:
				file1.write(name+ " "+v+" "+str(w)+"\r\n")
#边集合保存在busan_edge.node.csv
