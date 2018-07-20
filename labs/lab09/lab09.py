# Mutable Trees

# Q2
def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return t
    else:
        for b in t.branches:
            cumulative_sum(b)
            t.label += sum([b.label])

# Q3
def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    "*** YOUR CODE HERE ***"
    results = []
    def helper(t):
        if t.is_leaf():
            results.append(t.label)
        else:
            for b in t.branches:
                helper(b)
        return results
    return helper(t)

# Q4
def insert(bst, v):
    """
    >>> bst = BST(5, BST(3, BST(1), BST(4)), BST(10, BST.empty, BST(11)))
    >>> insert(bst, 2)
    >>> 2 in bst
    True
    >>> insert(bst, 7)
    >>> insert(bst, 6)
    >>> bst
    BST(5, BST(3, BST(1, BST.empty, BST(2)), BST(4)), BST(10, BST(7, BST(6)), BST(11)))
    """
    "*** YOUR CODE HERE ***"
    if bst is None:
        return
    elif v < bst.label:
        if bst.left:
            insert(bst.left, v)
        else:
            bst.left = BST(v)
    else:
        if bst.right:
            insert(bst.right, v)
        else:
            bst.right = BST(v)

# Tree class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# BST class
class BST:
    """
    >>> bst1 = BST(4, BST(2, BST(1)))
    >>> bst1.max()
    4
    >>> bst1.min()
    1
    >>> bst2 = BST(6, BST(2, BST(1), BST(4)), BST(7, BST.empty, BST(9)))
    >>> bst2.max()
    9
    >>> bst2.min()
    1
    >>> 9 in bst2
    True
    >>> 10 in bst2
    False
    >>> bst3 = BST(6, BST(2, BST(1), BST(4)), BST(8, BST(7), BST(9)))
    >>> 7 in bst3
    True
    >>> 10 in bst3
    False
    """
    empty = ()

    def __init__(self, label, left=empty, right=empty):
        assert left is BST.empty or isinstance(left, BST)
        assert right is BST.empty or isinstance(right, BST)

        self.label = label
        self.left, self.right = left, right

        if left is not BST.empty:
            assert left.max() <= label
        if right is not BST.empty:
            assert label < right.min()

    def is_leaf(self):
        return self.left is BST.empty and self.right is BST.empty

    def __repr__(self):
        if self.is_leaf():
            return 'BST({0})'.format(self.label)
        elif self.right is BST.empty:
            left = repr(self.left)
            return 'BST({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BST.empty:
                left = 'BST.empty'
            template = 'BST({0}, {1}, {2})'
            return template.format(self.label, left, right)

    def max(self):
        """Returns max element in BST."""
        if self.right is BST.empty:
            return self.label
        return self.right.max()

    def min(self):
        """Returns min element in BST."""
        if self.left is BST.empty:
            return self.label
        return self.left.min()

    def __contains__(self, e):
        if self.label == e:
            return True
        elif e > self.label and self.right is not BST.empty:
            return e in self.right
        elif self.left is not BST.empty:
            return e in self.left
        return False
