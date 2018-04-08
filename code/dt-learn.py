import numpy as np
import pandas as pd
from tree import decisionTreeNode
import random
import time

def myc(x=0): # c function
    y = 2*(np.log(x-1) + 0.5772156649) -2*(x-1)/x
    return(y)

def nodeInfo(X, Length=0, isLeaf=False, splitAtt=None, splitValue=None, isLeftChild=None, isRoot=True, Amount=0):
    node = decisionTreeNode()
    node.setLength(Length)
    node.setsplitAtt(splitAtt)
    node.setsplitValue(splitValue)
    node.setisLeftChild(isLeftChild)
    node.setisRoot(isRoot)
    node.setAmount(Amount)
    if(isLeaf):
        node.setisLeaf()
    return(node)

def iTree(X, e, l, Length=0, isLeaf=False, splitAtt=None, splitValue=None, isLeftChild=None, isRoot=True, Amount=0):
    if(e < l and len(X.index) > 1):
        node = nodeInfo(X, Length, isLeaf, splitAtt, splitValue, isLeftChild, isRoot, Amount)
        splitAtt = X.columns[random.randint(0, (len(X.columns)-1))]
        minimum = min(X[splitAtt])
        maximum = max(X[splitAtt])
        while(minimum == maximum):
            splitAtt = X.columns[random.randint(0, (len(X.columns)-1))]
            minimum = min(X[splitAtt])
            maximum = max(X[splitAtt])
        splitValue = np.random.uniform(low=minimum, high=maximum)
        Xl = X.loc[X[splitAtt]<=splitValue, :]
        Xr = X.loc[X[splitAtt]>splitValue, :]
        ee = e + 1
        Amountl = len(Xl.index)
        Child_left = iTree(X=Xl, e=ee, l=l, Length=ee, splitAtt=splitAtt, splitValue=splitValue, 
                           isLeftChild=True, isRoot=False, Amount=Amountl)
        node.setChildren(Child_left)
        Amountr = len(Xr.index)
        Child_right = iTree(X=Xr, e=ee, l=l, Length=ee, splitAtt=splitAtt, splitValue=splitValue, 
                            isLeftChild=False, isRoot=False, Amount=Amountr)
        node.setChildren(Child_right)
    else:
        Amount = len(X.index)
        node = nodeInfo(X, Length, isLeaf=True, splitAtt=splitAtt, splitValue=splitValue, 
                        isLeftChild=isLeftChild, isRoot=isRoot, Amount=Amount)
    return(node)
        
def printTree(node, depth = 0):
    if not node.getisRoot():
        x = node.getsplitAtt()
        if node.getisLeftChild():
            equality = "<="
        else:
            equality = ">"
        threshold = "%.6f" % node.getsplitValue() # Six decimal
        if node.getisLeaf():
            print(depth * "|\t" + "%s %s %s [%d]: %s" \
                                  % (node.getsplitAtt(), equality, threshold,
                                     node.getAmount(), node.getLength()))
        else:
            print(depth * "|\t" + "%s %s %s [%d]" \
                                  % (node.getsplitAtt(), equality, threshold,
                                     node.getAmount()))
        depth +=1
    for child in node.getChildren():
        printTree(child, depth)

def PathLength(X, decisionTree, l):
    prediction = None
    if decisionTree.getisLeaf():
        if decisionTree.getAmount()>1:
            return(decisionTree.getLength() + myc(decisionTree.getAmount()))
        else:
            return(decisionTree.getLength())
    for child in decisionTree.getChildren():
        splitAtt = child.getsplitAtt()
        splitValue = child.getsplitValue()
        if child.getisLeftChild():
            if X[splitAtt] <= splitValue:
                prediction = PathLength(X, child, l)
        else:
            if X[splitAtt] > splitValue:
                prediction = PathLength(X, child, l)
    return(prediction)

def AnomalyScore(x, n):
    return(2**(-x/myc(n)))
        
def predict(dat, decisionTree, l):
    numData = len(dat.index)
    prediction = np.zeros(numData)
    for i in range(numData):
        instance = dat.iloc[i, :]
        prediction[i] = PathLength(instance, decisionTree, l)
    return prediction

def mymse(pred, true):
    diff = pred-true
    y = [1 if a==1 else 400 if a==-1 else 0 for a in diff]
    return(sum(y)/len(diff))


## start -------------------------------------------------

dat = pd.read_csv('../data/dat1.csv')

t1 = time.time()
phi = 256
N = 20000
dat_use = dat.iloc[range(N), ]
the_list = range(N)
random.seed(1234)
cishu = 100
prediction = np.zeros(N)
for i in range(cishu):
    print(i, end="")
    train_index = random.sample(the_list, phi)
    dat_train = dat_use.iloc[train_index, ]
    X = dat_train.drop('Class', axis=1)
    y = dat_train.Class
    e=0
    l=np.log2(len(X.index))
    myTree = iTree(X, e, l)
    prediction += predict(dat_use, myTree, l)
    
prediction_final = prediction/cishu

t2 = time.time() 
print(t2 - t1)

sh = 0.7
result = AnomalyScore(prediction_final, phi)
prediction_final2 = np.zeros(N)
prediction_final2[np.where(result>sh)] = 1
true_value = dat_use.Class
MSE = mymse(prediction_final2, dat_use.Class)

print(MSE)