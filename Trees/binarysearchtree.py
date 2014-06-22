class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current):
        if key < current.key:
            if current.hasleft():
                self._put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, parent=current)
        elif key == current.key:
            current.val = val
        else:
            if current.hasright():
                self._put(key, val, current.right)
            else:
                current.right = treeNode(key, val, parent=current)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.val
            else:
                return None

    def _get(self, key, current):
        if not current:
            return None
        elif current.key == key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        elif key > current.key:
            return self._get(key, current.right)


    def delete(self, key):
        if self.size > 1:
            toremove = self._get(key, self.root)
            if toremove:
                self.remove(toremove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size -1
        else:
            raise KeyError('Error, key not in tree')

    def remove(self, toremove):
        if toremove.isleaf():
            if toremove == toremove.parent.left:
                toremove.parent.left = None
            else:
                toremove.parent.right = None
        else:
            if toremove.hasleft():
                if toremove.isleft():
                    toremove.left.parent = toremove.parent
                    toremove.parent.left = toremove.left
                elif toremove.isright():
                    toremove.left.parent = toremove.parent
                    toremove.parent.right = toremove.left
                else:
                    toremove.replaceval(toremove.left.key,
                        toremove.left.val
                        toremove.left.left
                        toremove.left.right)

            else:
                if toremove.isleft():
                    toremove.right.parent = toremove.parent
                    toremove.parent.left = toremove.right
                elif toremove.isright():
                    toremove.right.parent = toremove.parent
                    toremove.parent.right = toremove.right
                else:
                    toremove.replaceval(toremove.right.key,
                        toremove.right.val
                        toremove.right.left
                        toremove.right.right)


    def __delitem__(self, key):
        self.delete(key)



    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, k, v):
        self.put(k, v)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.balancefac = 0

    def hasleft(self):
        return self.left

    def hasright(self):
        return self.right

    def isleft(self):
        return self.parent and self.parent.left == self

    def isright(self):
        return self.parent and self.parent.right == self

    def isroot(self):
        return not self.parent

    def isleaf(self):
        return not (self.left or self.right)

    def haschildren(self):
        return self.right or self.left

    def hasbothchild(self):
        return self.right and self.left

    def replaceval(self, key, val, lc=None, rc=None):
        self.key = key
        self.val = val
        self.left = lc
        self.right = right
        if self.hasleft():
            self.left.parent = self
        if self.hasright():
            self.right.parent = self

    def findsuccessor(self):
        succ = None
        if self.hasright():
            succ = self.right.findmin()
        else:
            if self.parent:
                if self.isleft():
                    succ = self.parent
                else:
                    self.parent.right = None
                    succ = self.parent.findsuccessor()
                    self.parent.right = self
        return succ

    def findmin(self):
        current = self
        while current.hasleft():
            current = current.left
        return current

    def spliceout(self):
        if self.isleaf():
            if self.isleft():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.haschildren():
            if self.hasleft():
                if self.isleft():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isleft():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasleft():
                for elem in self.left:
                    yield elem
            yield self.key
            if self.hasright():
                for elem in self.right:
                    yield elem

class AVLT(BST):
    def _put(self, key, val, current):
        if key < current.key:
            if current.hasleft():
                self._put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, parent=current)
                self.updatebalance(current.left)
        else:
            if current.hasright():
                self._put(key, val, current.right)
            else:
                current.right = TreeNode(key, val, parent=current)
                self.updatebalance(current.right)

    def updatebalance(self, node):
        if node.balancefac > 1 or node.balancefac < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isleft():
                node.parent.balancefac += 1
            elif node.isright():
                node.parent.balancefac -= 1

            if node.parent.balancefac != 0:
                self.updatebalance(node.parent)

    def rotateleft(self, rotroot):
        newroot = rotroot.right
        rotroot.right = newroot.left
        if newroot.left != None:
            newroot.left.parent = rotroot
        newroot.parent = rotroot.parent
        if rotroot.isroot():
            self.root = newroot
        else:
            if rotroot.isleft():
                rotroot.parent.left = newroot
            else:
                rotroot.parent.right = newroot
        newroot.left = rotroot
        rotroot.parent = newroot
        rotroot.balancefac = rotroot.balancfac +1 - min(newroot.balancefac, 0)
        newroot.balancefac = newroot.balancfac +1 + mac(rotroot.balancefac, 0)

    def rotateleft(self, rotroot):
        newroot = rotroot.left
        rotroot.left = newroot.right
        if newroot.left != None:
            newroot.left.parent = rotroot
        newroot.parent = rotroot.parent
        if rotroot.isroot():
            self.root = newroot
        else:
            if rotroot.isleft():
                rotroot.parent.left = newroot
            else:
                rotroot.parent.right = newroot
        newroot.right = rotroot
        rotroot.parent = newroot
        rotroot.balancefac = rotroot.balancfac +1 - min(newroot.balancefac, 0)
        newroot.balancefac = newroot.balancfac +1 + mac(rotroot.balancefac, 0)

    def rebalance(self, node):
        if node.balancefac < 0:
            if node.right.balancefac > 0:
                self.rotateright(node.right)
                self.rotateleft(node)
            else:
                self.rotateleft(node)
        elif node.balancefac > 0:
            if node.left.balancefac < 0:
                self.rotateleft(node.left)
                self.rotateright(node)
            else:
                self.rotateright(node)