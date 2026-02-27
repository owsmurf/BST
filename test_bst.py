from bst import BinarySearchTree

def _tree(*keys):
    t = BinarySearchTree()
    for k in keys: t.insert(k)
    return t

def test_insert_search():
    t = BinarySearchTree(); t.insert(5,"five"); t.insert(3,"three")
    assert t.search(5) == "five" and t.search(99) is None and t.size == 2

def test_update():
    t = _tree(1); t.insert(1,"new")
    assert t.search(1) == "new" and t.size == 1

def test_delete_leaf():
    t = _tree(5,3); assert t.delete(3) and t.search(3) is None and t.size == 1

def test_delete_two_children():
    t = _tree(5,3,7,2,4,6,8); t.delete(5)
    assert t.search(5) is None and [k for k,_ in t.inorder()] == [2,3,4,6,7,8]

def test_delete_miss():
    t = _tree(1); assert not t.delete(99) and t.size == 1

def test_height():
    assert BinarySearchTree().height() == -1 and _tree(1).height() == 0

def test_balanced():
    assert _tree(4,2,6,1,3,5,7).is_balanced()
    assert not _tree(1,2,3,4,5).is_balanced()

def test_inorder():
    assert [k for k,_ in _tree(5,1,8,3,9,2).inorder()] == [1,2,3,5,8,9]

def test_contains():
    t = _tree(10); assert 10 in t and 99 not in t

if __name__ == "__main__":
    import sys; ts = [v for k,v in globals().items() if k.startswith("test_")]
    fail = 0
    for f in ts:
        try: f(); print(f"  ✓ {f.__name__}")
        except AssertionError as e: print(f"  ✗ {f.__name__}: {e}"); fail += 1
    print("All passed!" if not fail else f"{fail} failed"); sys.exit(fail)