# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:29:55 2019

@author: ROBIN
"""
import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()

import random
#generate a primary culture
query='MLSRAVCGTSRQLAPVLAYLGSRQKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNVTEEKYQEALAKGDVTAQIALQPALKFNGGGHINHSIFWTNLSPNGGGEPKGELLEAIKRDFGSFDKFKEKLTAASVGVQGSGWGWLGFNKERGHLQIAACPNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYMACKK'
a1='GGRSRHLAAVLTQAGRRQQGRSFRAQVAGSEGPWLQHSSDQQQGRVFPDAGRRLAPAATAAGSRHKHSLPDLPYDYGALEPHINAQIMQLHHSKHHAAYVNNLNATEEKYREALAKGELLEAIKRDFGSFEKFKEKLTAVSAGVQGSGWGWLGFNKEQGRLQIAACSNQDPLQGTTGLIPLLGIDVWEHAYYLQYKNVRPDYLKAIWNVINWENVTERYTAC'
a2='MQAALAAMAVHTVFAAAAAAPTAHYSLFFPAVSSAPSASFSLHSSFSGLALKASTRPFLSLSAAAAPKPLSVVAATKKAVAVLKGTSSVEGVVTLTQEDDGPTTVKVRVTGLTPGKHGFHLHEYGDTTNGCISTGPHFNPKGLTHGAPEDEVRHAGDLGNIVANAEGVAEVTIVDNQIPLSGPNSVVGRAFVVHELEDDLGKGGHELSLSTGNAGGRLACGV'
a3='MFAKTAAANLTKKGGLSLLSTTARRTKVTLPDLKWDFGALEPYISGQINELHYTKHHQTYVNGFNTAVDQFQELSDLLAKEPSPANARKMIAIQQNIKFHGGGFTNHCLFWENLAPESQGGGEPPTGALAKAIDEQFGSLDELIKLTNTKLAGVQGSGWAFIVKNLSNGGKLDVVQTYNQDTVTGPLVPLVAIDAWEHAYYLQYQNKKADYFKAIWNVVNWK'
a4='MSVDRISSVVKKDSSSTLREKRKVSLPKLDWELNALEPYISAQINELHYAKHHQTYVNGFNAAVDQLENLTFQLASNPSPTIAEKIVCVQQNLKFHGGGFINHCLFWKSLAPKSQGGGRPPTGALAESIDKQFGSLGNLIDKVNSSLAALQGSGWVFIVKNLEIGGDLDIVQTLNQDTVAGSLVPLLAIDAWEHAYYLQYQNRKMDYFQSIWNIINWAEASK'
a5='WNGFSEWWTHEVDYNQKLTIENNQRPKIHEHEQWGLRQSPPPPKLCCPTCQMCERMRHQNRFAPLMEVGCRCMCWFHDWWVISVGTWLHTVIMYMMWPKRFHHNECPKACFRTTYTRKNHHALYWMLFEMCCYDQDVVWSKTHIFTTVRDIEVYVEQVFFIWGPLCHVAIACYEPVKTIRRRIPMYLCRHCIRGDNSYLLACCSIIYYFYHHMSYYGVLDIL'
prot=['Q','W','E','R','T','Y','I','P','A','S','D','F','G','H','K','L','C','V','N','M']#omitOZJUZB
dd={}
dots=[]

for num in range(0,20):
    dd[num]=prot[num]
# generate 10 random sequences and 1 query
species=[a1,a2,a3,a4,a5]
primaryculture=[]
for i in range(500):
    primaryculture+=species
# def process
#create a dictionary for biosum62 
dic={}
#import the matrix
text=open('biosum62.txt').read()
lines=text.splitlines()
#get each idnex for the dic

index1=lines[0].split()
for line in lines[1:]:
    splitted=line.split()
    dic_for_each={}
    for i in index1:
        value=splitted[index1.index(i)+1]
        dic_for_each[i]=value
    dic[line[0]]=dic_for_each
def score(x1,x2):#x1,x2 are sequences
    p=0
    list1=list(x1)   
    list2=list(x2)
    for num in range(len(list1)):#x1,x2 are of the same length
       nu_acid1=list1[num]
       nu_acid2=list2[num]
       single_score=int(dic[nu_acid1][nu_acid2])
       p+=single_score
    return p 
def selection (primary):#process one generation
    global query
    g=1
    while g <=200:
        score_list=[]
        for i in primary:
            score_list.append(score(i,query))
       # print(len(score_list))   
# selection: compare other sequences to query by blosum62, store the scores
# in score range, randomly generate a number (threshold), omit sequences with scores under threshold.
        r1=random.randint(-1000,max(score_list))
        new=[]
        for j in score_list:
            if j >=r1:#sequences over the threshold
                index=score_list.index(j)     
                survive=primary[index]
                sl=list(survive)
                r2=random.randint(0,len(sl)-1)
                r3=random.randint(0,19)
                ##mind!!!randint give number [0,20]~
                sl[r2]=dd[r3]
                survive=''.join(sl)    
                new.append(survive)
    
            
        dots.append(score_list)
        g+=1
        primary=new
   
    
    return


selection(primaryculture)
#print(primaryculture)
# cross: it is remain to be solved...or it is not suitable ofr protein.
# mutation: how many genes mutated (this time only 1);  to which gene(firstly 
# store the result (x—score; y—number)
# run process for 10 times and animation
#variables: g, survive_num, survive_score 
#make a movie
import matplotlib.pyplot as plt
for i in dots:
    y1=[]
    for j in range(len(i)):
        y1.append(j)
    ax.cla()
    ax.scatter(y1,i)
    ax.legend()
    plt.yticks(np.linspace(-300, 5, 5))
    plt.pause(0.1)
