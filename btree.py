class BTree():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        leftStr, rightStr = "", ""
        if self.left is not None:
            leftStr = str(self.left)
        if self.right is not None:
            rightStr = str(self.right)

        return "(" + str(self.value) + "=>" + leftStr + "=>" + rightStr + ")"

    def setRight(self, tree):
        self.right = tree

    def setLeft(self, tree):
        self.left = tree

    def insert(self, key, val):
        if key <= self.key:
            if self.left is None:
                self.left = BTree(key, val)
            else:
                self.left.insert(key, val)
        else:
            if self.right is None:
                self.right = BTree(key, val)
            else:
                self.right.insert(key, val)

    def insertList(self, keyValPairs):
        for k, v in keyValPairs:
            self.insert(k, v)

    def contains(self, key):
        if key == self.key:
            return True
        if key <= self.key:
            return self.left is None or self.left.contains(key)  # short-circ
        return self.right is None or self.right.contains(key)

    def height(self):
        leftHeight, rightHeight = 0, 0
        if self.left is not None:
            leftHeight = self.left.height()
        if self.right is not None:
            rightHeight = self.right.height()
        return 1 + max(leftHeight, rightHeight)

    def inorder(self):
        if self.left is not None:
            yield from self.left.inorder()

        yield self.value

        if self.right is not None:
            yield from self.right.inorder()

    def preorder(self):
        yield self.value
        if self.left is not None:
            yield from self.left.preorder()
        if self.right is not None:
            yield from self.right.preorder()

    def postorder(self):
        if self.left is not None:
            yield from self.left.postorder()
        if self.right is not None:
            yield from self.right.postorder()
        yield self.value

    def invert(self):
        if self.left is not None:
            self.left.invert()
        if self.right is not None:
            self.right.invert()
        r = self.right
        self.setRight(self.left)
        self.setLeft(r)


class AVLTree(BTree):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, key, val):
        if key <= self.key:
            if self.left is None:
                self.left = AVLTree(key, val, parent=self)
            else:
                self.left.insert(key, val)
        else:
            if self.right is None:
                self.right = AVLTree(key, val, parent=self)
            else:
                self.right.insert(key, val)

        self.balance()
        # returns root because this subtree might not be root after rotating
        return self.root()

    def insertList(self, keyValPairs):
        return NotImplemented
        # for k, v in keyValPairs:
        #     self.root().insert(k, v)
        # return self.root()

    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()

    def setParent(self, parent):
        self.parent = parent

    def isRightChild(self):
        return self.parent.right == self

    def balance(self):
        if self.bal() == -2:
            if self.left.bal() == 1:
                self.rotate_left_right()
            else:
                self.rotate_right()
        elif self.bal() == 2:
            if self.right.bal() == -1:
                self.rotate_right_left()
            else:
                self.rotate_left()
        else:
            pass

    def bal(self):
        leftHeight, rightHeight = 0, 0
        if self.left is not None:
            leftHeight = self.left.height()
        if self.right is not None:
            rightHeight = self.right.height()
        return rightHeight - leftHeight

    def rotate_right(self):
        print(f"{self.key}: right")
        z = self.parent
        if z is not None:
            if self.isRightChild():
                z.setRight(self.left)
            else:
                z.setLeft(self.left)
        v = self.left
        self.setLeft(v.right)
        if v.right:
            v.right.setParent(self)
        v.setRight(self)
        v.setParent(z)
        self.setParent(v)

    def rotate_left(self):
        print(f"{self.key}: left")
        z = self.parent
        if z is not None:
            if self.isRightChild():
                z.setRight(self.right)
            else:
                z.setLeft(self.right)
        v = self.right
        self.setRight(v.left)
        if v.left:
            v.left.setParent(self)
        v.setLeft(self)
        v.setParent(z)
        self.setParent(v)

    def rotate_left_right(self):
        self.left.rotate_left()
        self.rotate_right()

    def rotate_right_left(self):
        self.right.rotate_right()
        self.rotate_left()


def sampleTree():
    a = AVLTree(10, 10)
    for k, v in [(11, 11), (5, 5), (6, 6), (4, 4), (3, 3), (2, 2), (7, 7)]:
        a = a.insert(k, v)
    return a
