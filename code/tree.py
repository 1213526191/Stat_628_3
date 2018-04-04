import numpy as numpy

class decisionTreeNode:
    def __init__(self, Length=0, isLeaf=False, splitAtt=None, splitValue=None, children=None, isLeftChild=True, isRoot=True, Amount=0):
        self.Length = Length
        self.isLeaf = isLeaf
        self.splitAtt = splitAtt
        self.splitValue = splitValue
        self.children = []
        self.isLeftChild = isLeftChild
        self.isRoot = isRoot
        self.Amount = Amount
    
    def setLength(self, Length_):
        self.Length = Length_
    def setisLeaf(self):
        self.isLeaf = True
    def setsplitAtt(self, splitAtt_):
        self.splitAtt = splitAtt_
    def setsplitValue(self, splitValue_):
        self.splitValue = splitValue_
    def setChildren(self, _children):
        return(self.children.append(_children))
    def setisLeftChild(self, isLeftChild_):
        self.isLeftChild = isLeftChild_
    def setisRoot(self, isRoot_):
        self.isRoot = isRoot_
    def setAmount(self, Amount_):
        self.Amount = Amount_

    def getLength(self):
        return(self.Length)
    def getisLeaf(self):
        return(self.isLeaf)
    def getsplitAtt(self):
        return(self.splitAtt)
    def getsplitValue(self):
        return(self.splitValue)
    def getChildren(self):
        return(self.children)
    def getisLeftChild(self):
        return(self.isLeftChild)
    def getisRoot(self):
        return(self.isRoot)
    def getAmount(self):
        return(self.Amount)