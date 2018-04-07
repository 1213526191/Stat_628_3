import numpy as np
import pandas as pd
from tree import decisionTreeNode
import random

# read data
dat = pd.read_csv('../data/dat1.csv')

# split train and test data
X = dat.drop('Class', axis=1)
e=0
l=np.log2(len(X.index))


def myc(x=0):
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
        
# def printTree(node, depth = 0):
#     if not node.getisRoot():
#         x = node.getsplitAtt()
#         if node.getisLeftChild():
#             equality = "<="
#         else:
#             equality = ">"
#         threshold = "%.6f" % node.getsplitValue() # Six decimal
#         if node.getisLeaf():
#             print(depth * "|\t" + "%s %s %s [%d]: %s" \
#                                   % (node.getsplitAtt(), equality, threshold,
#                                      node.getAmount(), node.getLength()))
#         else:
#             print(depth * "|\t" + "%s %s %s [%d]" \
#                                   % (node.getsplitAtt(), equality, threshold,
#                                      node.getAmount()))
#         depth +=1
#     for child in node.getChildren():
#         printTree(child, depth)

def classify(X, decisionTree, l):
    prediction = None
    if decisionTree.getisLeaf():
        if decisionTree.getAmount()>1:
            return(2**(-(decisionTree.getLength() + myc(decisionTree.getAmount()))/myc(l)))
        else:
            return(2**(-(decisionTree.getLength())/myc(l)))
    for child in decisionTree.getChildren():
        splitAtt = child.getsplitAtt()
        splitValue = child.getsplitValue()
        if child.getisLeftChild():
            if X[splitAtt] <= splitValue:
                prediction = classify(X, child, l)
        else:
            if X[splitAtt] > splitValue:
                prediction = classify(X, child, l)
    return(prediction)
        
# def predict(train, test, decisionTree):
#     numData = len(train.index)
#     prediction = np.zeros(numData)
#     for i in range(numData):
#         instance = train.loc[i, :]
#         prediction[i] = classify(instance, decisionTree)
#     pred_y = classify(test, decisionTree)
#     return prediction, pred_y


mytree = iTree(X,e,l) 
prediction, pred_y = predict(dat_train, dat_test, mytree)       
sum(prediction <= pred_y)/len(prediction)
sum(dat_train.Class)/len(dat_train.index)

