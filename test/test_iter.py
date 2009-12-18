import libpry
from xcb import iter, common

class uIter(libpry.AutoTree):
    def test_simple(self):
        i = iter.Iterator([1, 2, 3, 4], 2, "test", True)
        assert list(i) == [(1, 2), (3, 4)]

        i = iter.Iterator([1, 2, 3, 4], 2, "test", False)
        assert list(i) == [(1, 2), (3, 4)]

        i = iter.Iterator([], 2, "test", True)
        assert list(i) == []

        i = iter.Iterator([1], 2, "test", True)
        libpry.raises("extra items", list, i)

        i = iter.Iterator([1], 2, "test", False)
        libpry.raises("too few items", list, i)

        i = iter.Iterator([1, 2, 3, 4], 3, "test", True)
        libpry.raises("extra items", list, i)

        i = iter.Iterator([1, 2, 3, 4], 3, "test", False)
        libpry.raises("too few items", list, i)


class uFlatten(libpry.AutoTree):
    def test_simple(self):
        l = [1, 2, 3]
        assert list(iter.flatten(l)) == l

        l = [[1, 2], 3]
        assert list(iter.flatten(l)) == [1, 2, 3]

        l = [[1, [2]], 3]
        assert list(iter.flatten(l)) == [1, 2, 3]

        l = [["one", [2]], 3]
        assert list(iter.flatten(l)) == ["one", 2, 3]




tests = [
    uFlatten(),
    uIter(),
]
