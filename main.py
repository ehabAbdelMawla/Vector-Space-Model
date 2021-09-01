from random import randint
from flask import Flask
from flask import render_template, request
import os
import math
import numpy
import networkx as nx
import matplotlib.pyplot as plt


# New Project
def Normalize(arr):
    sum=0
    for item in arr:
        sum+=item**2

    for i in range(0,len(arr)):
        arr[i]/=math.sqrt(sum)

def getNodesList(Matrix=[]):
    list=[]
    for r in range(0,len(Matrix)):
        for c in range(0,len(Matrix[r])):
            if Matrix[r][c]>0:
                list.append((r+1,c+1))
            else :
                list.append((r + 1,r+1))

    return list






def craeteBasic2DArrray():
    FilesNames=getAllTextFilesinFolder()
    size=len(FilesNames)
    __2DArray__= numpy.zeros((size,size))
    print(__2DArray__)
    for file in FilesNames:
        data=open('Files/'+file+'.txt').read().split(' ')
        print(data)
        for item in data:
            try:
                int(item)
                n=int(file)-1
                m=int(item)-1
                if n!=m and n<size and m<size:
                    __2DArray__[n][m]=1
            except:
                continue
    print(__2DArray__)
    G = nx.Graph()

    plt.figure(figsize=(6, 6))
    G.add_edges_from(getNodesList(__2DArray__))

    nx.draw_networkx(nx.to_directed(G))

    plt.savefig('static/graph1.png', transparent=True)
    __2DArray__Transpose=__2DArray__.transpose()
    print('__2DArray__Transpose')
    print(__2DArray__Transpose)
    h= numpy.full(size, 1)
    print('H')
    print(h)
    print('Authority')
    # a=numpy.matmul(__2DArray__Transpose, h)

    print('Hup')
    # h = numpy.matmul(__2DArray__, a)
    for i in range(0,100):
        a = numpy.matmul(__2DArray__Transpose, h)
        h = numpy.matmul(__2DArray__, a)

        Normalize(a)
        Normalize(h)

    print(h)
    resultOfAuth={}
    for i in range(0,len(a)):
        resultOfAuth['D'+str(i+1)]=round(a[i],2)
    resultOfAuth = sort((sorted(resultOfAuth, key=resultOfAuth.__getitem__, reverse=True)), resultOfAuth)
    print(resultOfAuth)
    return resultOfAuth

















# Get All text Files From myFolder
def getAllTextFilesinFolder():
    files=[]
    for filename in os.listdir(os.getcwd() + "/Files"):
        if filename.endswith('.txt'):
            files.append(filename.strip('.txt'))
    return files


def RondomAction():
   files= getAllTextFilesinFolder()
   for file in files:
       appendRandomTextToFiles('Files/'+file+'.txt')


# Generate Random Text To Append To Files Later:
def getRandomText(num):
    randomString=''
    for i in range (0,num):
        if i%(num/2)==0:
            randomString += str(randint(1, 5)) + ' '

        else:
            randomString += chr(randint(65, 69)) + ' '
    return randomString
# ---------------------------------------------------------------

# Generate Files And Append The random text to it:
def appendRandomTextToFiles(fileName):
    file=open(fileName,'w')
    file.write(getRandomText(randint(5,15)))

# get All Data Of Files
def getAllDataFromFile(fileName):

    fileData = open("Files/"+fileName+".txt").read()
    return fileData


charsSet={}
charsSetIDF={}
documentsData={}
documentsTF={}


def getDistictChars(str=""):
    QueryChars=str.split(' ')
    for item in QueryChars:
        if item not in charsSet and item!='':
            try:
                int(item)
            except:
                charsSet[item]=0

def getMaxFerq(l=[]):
    max=1
    for item in l:

        if l.count(item)> max:
             max=l.count(item)
    return max


def generateWheights(TfList={},idfList={}):
    for doc in TfList:
        for charIDF in idfList:
            TfList[doc][charIDF]=round(TfList[doc][charIDF]*idfList[charIDF],2)

def generateDF(d=[]):
    for item in charsSet:
        if item in d:
            charsSet[item]+=1

def generateIDF(df,num):
    for char in df:
        charsSetIDF[char]=round(math.log((num/df[char]),2),2)

def simCos(d1={},d2={}):
    numOFUpperPart = 0
    leftSideLowerPart=0
    RightSideLowerPart = 0
    for char in d1:
        numOFUpperPart+=d1[char]*d2[char]
        leftSideLowerPart+=math.pow(d1[char],2)
        RightSideLowerPart+=math.pow(d2[char],2)
    return numOFUpperPart/(math.sqrt(leftSideLowerPart+RightSideLowerPart))


def sort(listOFKeys=[],mainDic={}):
    sortedDic={}
    for i in listOFKeys:
        sortedDic[i]=mainDic[i]
    return sortedDic


def getSimilarityWithQuery(IdfDic={}):
    result={}
    queryDic=IdfDic['Query']
    # print(queryDic)
    del IdfDic['Query']
    for doc in IdfDic:
        docscore=round(simCos(IdfDic[doc],queryDic),2)
        result[doc]=docscore
    result=sort((sorted(result, key=result.__getitem__, reverse=True)),result)
    return result


def generateTfForAllDocuments(docs={},chars={}):
    for doc in docs:
        # print(documentsTF)
        documentsTF[doc]={}
        data=docs[doc].split(' ')
        maxOFDoc=getMaxFerq(data)
        generateDF(data)
        for char in chars:
            if char in documentsTF[doc]:
                documentsTF[doc][char]+=data.count(char)
            else:
                documentsTF[doc][char] = data.count(char)

        for item in documentsTF[doc]:
            documentsTF[doc][item]=round(documentsTF[doc][item]/maxOFDoc,2)




# ['D1','D2','D3','D4','D5']
def takedataFrom(ss='',filesList=[]):
    if ss.strip(' ') == '':
        return "You Must Insert Query"
    charsSet.clear()
    documentsData.clear()
    documentsTF.clear()
    charsSetIDF.clear()

    getDistictChars(ss)
    documentsData['Query']=ss
    for file in filesList:
        getDistictChars(getAllDataFromFile(file))
        documentsData[file]=getAllDataFromFile(file)
    print("Documents",documentsData)
    print("Chars",charsSet)
    generateTfForAllDocuments(documentsData,charsSet)
    print("TF",documentsTF)
    generateIDF(charsSet,len(documentsData))
    print("IDF",charsSetIDF)
    # here we use documentsTF To Store Wheights
    generateWheights(documentsTF,charsSetIDF)
    print("Wheights", documentsTF)
    return getSimilarityWithQuery(documentsTF)




#Flask App
app = Flask(__name__)
title = "Vector Space"


@app.route('/', methods=['POST', 'GET', 'search'])
def index():
    if request.method == 'POST':
        if request.form['BTN'] == 'search':
            print("search Action")
            # ss=takedataFrom(request.form['queryString'],['D1','D2','D3','D4','D5'])
            ss = takedataFrom(request.form['queryString'],getAllTextFilesinFolder())
            print("Sim",ss)
            if isinstance(ss,str):
                return render_template("index.html", title=title,MSG=ss,QueryValid=1,display=0)
            else:
                return render_template("index.html", title=title, queryString=request.form['queryString'], display=1,result=ss,data=documentsData,Authority=craeteBasic2DArrray())
        elif request.form['BTN'] == 'Create Random Text':
            print("Random Action")
            RondomAction()


    return render_template("index.html", title=title)


if __name__ == '__main__':
    app.debug = True
    app.run()







