


from tkinter import PIESLICE


class Node:
    def __init__(self):
        self.data=None
        #self.root=None
        self.rightChild=None
        self.leftChild=None

    def setData(self,data):
        self.data=data
        
    def addNode(self,newNode,treeDepth,depth):
        
        if treeDepth-1 == depth:
            if self.leftChild is None:
                #print("depth: ",depth+1,"current node: ",self.data,"left","value: ",newNode.data)
                self.leftChild=newNode
                newNode.root=self
                return True
            if self.rightChild is None:
                #print("depth: ",depth+1,"current node: ",self.data,"right","value: ",newNode.data)
                self.rightChild=newNode
                newNode.root=self
                return True
            
            return False
        else:
            isTaskDone = self.leftChild.addNode(newNode,treeDepth,depth+1)
            if not isTaskDone:
               isTaskDone=self.rightChild.addNode(newNode,treeDepth,depth+1)
            
            return isTaskDone
        
    def showPerOrder(self):
        if self.data is None:
            print("Empty set")
            return

        print(self.data,end=" ")
        if self.leftChild is None:
            return
        self.leftChild.showPerOrder()
        if self.rightChild is None:
            return
        self.rightChild.showPerOrder()
        
    
    def showPostOrder(self):
        if self.data is None:
            print("Empty set")
            return

        if self.leftChild is None:
            print(self.data,end=" ")
            return
        self.leftChild.showPostOrder()
        if self.rightChild is None:
            #print(self.data,end=" ")
            return
        self.rightChild.showPostOrder()
        print(self.data,end=" ")
        

    def showInOrder(self):
        if self.data is None:
            print("Empty set")
            return

        if self.leftChild is None:
            print(self.data,end=" ")
            return
        self.leftChild.showInOrder()
        
        print(self.data,end=" ")
        

        if self.rightChild is None:
            return
        self.rightChild.showInOrder()
            

        
       
class Tree:

    def __init__(self):
        self.depth=0
        self.node=Node()
    

    def add (self,data):
        tempNode=Node()
        tempNode.setData(data)
        if self.node.data is None:
            print("add first node")
            self.node.data = tempNode.data
            return

        isDone=self.node.addNode(tempNode,self.depth,-1)
        if not isDone:
            self.depth=self.depth+1
            self.node.addNode(tempNode,self.depth,-1)
    def perOrder(self):
        print("perOrder: ",end="")
        self.node.showPerOrder()
        print()
    def postOrder(self):
        print("postOrder: ",end="")
        self.node.showPostOrder()
        print()
    def inOrder(self):
        print("inorder: ",end="")
        self.node.showInOrder()
        print()



# testing project
if __name__== "__main__":
    tree = Tree()

    for i in range(11):
        tree.add(i)

    tree.perOrder()
    
    tree.postOrder()
    
    tree.inOrder()
    

