"""
Disjoint Set or Union-Find

This is a forest based disjoint set implementation so we have to consider that
- each set is represented as a tree
- the representative element is the root of the tree
- there are two methods used in the implementation of union-find methods:
    - union by rank : "if i always choose he root of the deeper tree to be the new root, then the tree will not grow
    deeper!"
    - path compression: "During find operation all traversed nodes are made direct sons of the root."

better explanation in:
* http://quegrande.org/apuntes/EI/2/Alg/teoria/08-09/tema_7_-_conjuntos_disjuntos.pdf
* http://hjemmesider.diku.dk/~pawel/ad/ds.pdf

O(mlog(n) + n)
"""


class DisjointSet:
    def __init__(self, n):
        self.parent_of = [x for x in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent_of[x] != x:
            # here we apply path compression
            self.parent_of[x] = self.find(self.parent_of[x])
        return self.parent_of[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # here we apply union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent_of[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent_of[y_root] = x_root
        else:
            self.parent_of[y_root] = x_root
            self.rank[x_root] += 1


if __name__ == '__main__':
    ds = DisjointSet(8)

    ds.union(0, 1)
    ds.union(2, 3)

    ds.union(0, 5)

    ds.union(1, 2)
    ds.union(1, 5)
    ds.union(1, 6)
    ds.union(1, 7)

    ds.union(2, 4)
    ds.union(2, 5)
    ds.union(2, 6)
    ds.union(2, 7)

    ds.union(3, 6)

    ds.union(4, 5)

    ds.union(5, 6)
    ds.union(5, 7)

    ds.union(6, 7)

    print(ds.parent_of)
