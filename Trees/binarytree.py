#Binary tree implementation

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftC = None
        self.rightC = None

    def addleft(self, root):
        if self.leftC == None:
            self.leftC = BinaryTree(root)
        else:
            t = BinaryTree(root)
            t.leftC = self.leftC
            self.leftC = t
    def addright(self, root):
        if self.rightC == None:
            self.rightC = BinaryTree(root)
        else:
            t = BinaryTree(root)
            t.rightC = self.rightC
            self.rightC = t

    def getrightC(self):
        return self.rightC
    def getleftC(self):
        return self.leftC

    def setroot(self, root):
        self.root = root

    def getroot(self):
        return self.root

    def preorder(self):
        print(self.key)
        if self.leftC:
            self.left.preorder()
        if self.rightC:
            self.left.preorder()
    def postorder(self):
        if self.leftC:
            self.leftC.postorder()
        if self.rightC:
            self.rightC.postorder()
        print(tree.getroot())
    def inorder(self):
        if self.leftC:
            self.leftC.postorder()
        print(tree.getroot())
        if self.rightC:
            self.rightC.postorder()


