from __future__ import annotations

class TreeNode:
    __slots__ = ("key", "val", "left", "right")
    def __init__(self, key, val=None):
        self.key, self.val, self.left, self.right = key, val if val is not None else key, None, None

class BinarySearchTree:
    def __init__(self):
        self._root = None; self._size = 0

    def insert(self, key, val=None):
        def _ins(n):
            if not n: self._size += 1; return TreeNode(key, val)
            if key < n.key: n.left = _ins(n.left)
            elif key > n.key: n.right = _ins(n.right)
            else: n.val = val if val is not None else key
            return n
        self._root = _ins(self._root)

    def search(self, key):
        n = self._root
        while n:
            if key == n.key: return n.val
            n = n.left if key < n.key else n.right

    def delete(self, key):
        found = [False]
        def _del(n, k):
            if not n: return None
            if k < n.key: n.left = _del(n.left, k)
            elif k > n.key: n.right = _del(n.right, k)
            else:
                found[0] = True
                if not n.left: self._size -= 1; return n.right
                if not n.right: self._size -= 1; return n.left
                s = n.right
                while s.left: s = s.left
                n.key, n.val = s.key, s.val
                n.right = _del(n.right, s.key)
            return n
        self._root = _del(self._root, key); return found[0]

    def height(self):
        def _h(n): return -1 if not n else 1 + max(_h(n.left), _h(n.right))
        return _h(self._root)

    def is_balanced(self):
        def _b(n):
            if not n: return True, -1
            lok, lh = _b(n.left); rok, rh = _b(n.right)
            return lok and rok and abs(lh - rh) <= 1, 1 + max(lh, rh)
        return _b(self._root)[0]

    def inorder(self):
        res = []
        def _go(n):
            if n: _go(n.left); res.append((n.key, n.val)); _go(n.right)
        _go(self._root); return res

    @property
    def size(self): return self._size
    def __len__(self): return self._size
    def __contains__(self, key): return self.search(key) is not None

if __name__ == "__main__":
    bst = BinarySearchTree()
    for k, v in [(8,"eight"),(3,"three"),(10,"ten"),(1,"one"),(6,"six"),(14,"fourteen"),(4,"four"),(7,"seven")]:
        bst.insert(k, v)
    print(f"size={bst.size}  height={bst.height()}  balanced={bst.is_balanced()}")
    print(f"inorder: {bst.inorder()}")
    print(f"search(6)={bst.search(6)}  search(99)={bst.search(99)}")
    bst.delete(3)
    print(f"after delete(3): {bst.inorder()}")