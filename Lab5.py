# Lab 5
# Programmed by Anthony Herrera
# Last modified May 8, 2019
import math

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def Insert(T,word,numbers,ind = 0):
    if T == None:
        T =  BST([word,numbers])
    elif T.item[0][ind] > word[ind]:
        T.left = Insert(T.left,word,numbers,ind)
    else:
        T.right = Insert(T.right,word,numbers,ind)
    return T
def Find(T,word):
    if T is None or T.item == k:
        return T.item[1]
    if T.item[0][0] > word[0]:
        return Find(T.left,word)
    else:
        return Find(T.right,word)



class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):
        self.item = []
        self.count = 0
        for i in range(size):
            self.item.append([])

def IncreaseC(H):
    if H.count // len(H.item) > 1:
        temp = HashTableC(len(H.item)*2 +1)
        for x in range(len(H.item)):
            for y in H.item[x]:
                temp.item[x].append(y)
        return temp
    return H



def InsertC(H,W,N):
    b = h(W,len(H.item))
    H.item[b].append([W,N])
    H.count += 1

def h(W,n):
    r = 0
    for c in W:
        r = (r*255 + ord(c)) % n
    return r

def FindC(H,k):
    # Returns bucket (b) and index (i)
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return [b][i][1]
    return False


def Similarity(T,word1,word2):
    e0 = Find(T, word1)
    e1 = Find(T, word2)
    if e0 == False or None and e1 == False or None:
        return 'Word not Found'
    mult = 0
    for x in e0:
        for y in e1:
            mult += x * y
    absolutV = 0
    for x in e0:
        for y in e1:
            absolutV += x + y
    return mult / math.sqrt(absolutV)

def SimilarityC(H,word1,word2):
    e0 = FindC(H,word1)
    e1 = FindC(H,word2)
    mult = 0
    if e0 == False or None and e1 == False or None:
        return 'Word not Found'
    for x in e0:
        for y in e1:
            mult += x*y
    absolutV = 0
    for x in e0:
        for y in e1:
            absolutV += x+y
    return mult / math.sqrt(absolutV)


option = input('Choose a table implementation binary search tree(1) or hash table chaining(2)\n')
if option == '1':
    T = None
    counter = 0
    file = open('glove.6B.50d.txt','r',encoding='utf-8')
    contents = file.readlines()
    for x in contents:
        line = x
        line_split = line.split()
        T = Insert(T,line_split[0],line_split[1:])
        counter += 1
    file.close()
    print('Number of Nodes: ', counter)
    print('Similarity [bear,bear]', Similarity(T,'bear', 'bear'))
    print('Similarity [barley,shrimp]', Similarity(T,'barley', 'shrimp'))
    print('Similarity [barley,oat]', Similarity(T,'barley', 'oat'))
    print('Similarity [federer,baseball]', Similarity(T,'federer', 'baseball'))
    print('Similarity [federer,tennis]', Similarity(T,'federer', 'tennis'))
    print('Similarity [harvard,stanford]', Similarity(T,'harvard', 'stanford'))
    print('Similarity [harvard,utep]', Similarity(T,'harvard', 'utep'))
    print('Similarity [harvard,ant]', Similarity(T,'harvard', 'ant'))
    print('Similarity [raven,crow]', Similarity(T,'raven', 'crow'))
    print('Similarity [raven,whale]', Similarity(T,'raven', 'whale'))
    print('Similarity [spain,france]', Similarity(T,'spain', 'france'))
    print('Similarity [spain,mexico]', Similarity(T,'spain', 'mexico'))
    print('Similarity [mexico,france]', Similarity(T,'mexico', 'france'))
    print('Similarity [mexico,guatemala]', Similarity(T,'mexico', 'guatemala'))
    print('Similarity [computer,platypus]', Similarity(T,'computer', 'platypus'))
else:
    H = HashTableC(11)
    file = open('glove.6B.50d.txt', 'r', encoding='utf-8')
    contents = file.readlines()
    for x in contents:
        line = x
        line_split = line.split()
        H = IncreaseC(H)
        InsertC(H,line_split[0],line_split[1:])
    file.close()
    print('Initial table size:', 11)
    print('Final table size:',len(H.item))
    print('Similarity [bear,bear]', SimilarityC(H,'bear', 'bear'))
    print('Similarity [barley,shrimp]', SimilarityC(H,'barley', 'shrimp'))
    print('Similarity [barley,oat]', SimilarityC(H,'barley', 'oat'))
    print('Similarity [federer,baseball]', SimilarityC(H,'federer', 'baseball'))
    print('Similarity [federer,tennis]', SimilarityC(H,'federer', 'tennis'))
    print('Similarity [harvard,stanford]', SimilarityC(H,'harvard', 'stanford'))
    print('Similarity [harvard,utep]', SimilarityC(H,'harvard', 'utep'))
    print('Similarity [harvard,ant]', SimilarityC(H,'harvard', 'ant'))
    print('Similarity [raven,crow]', SimilarityC(H,'raven', 'crow'))
    print('Similarity [raven,whale]', SimilarityC(H,'raven', 'whale'))
    print('Similarity [spain,france]', SimilarityC(H,'spain', 'france'))
    print('Similarity [spain,mexico]', SimilarityC(H,'spain', 'mexico'))
    print('Similarity [mexico,france]', SimilarityC(H,'mexico', 'france'))
    print('Similarity [mexico,guatemala]', SimilarityC(H,'mexico', 'guatemala'))
    print('Similarity [computer,platypus]', SimilarityC(H,'computer', 'platypus'))
