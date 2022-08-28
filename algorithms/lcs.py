"""
Classic LCS

Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Solution

Dynamic programming

X abb with x elements
Y ab with y elements

F(x, y)

F(0, 0) -> 0
F(0, 1) -> 0
F(1, 0) -> 0

... el maximo LCS será siempre 0

todos los que tiene a x=0 OR y=0 tienen un valor de 0, por ende inicializamos

M[x+1][y+1]
M[0][] = 0
M[][0] = 0

Quedando,

  - a b
- 0 0 0
a 0
b 0
c 0

analizando el caso aislado F(1, 0)

X a
Y -

  -
- 0
a 0

que pasa si tengo F(1, 1)

X a
Y a

X[0] = Y[0]

  - a
- 0 0
a 0 1

si luego agrego uno más F(1, 2)

  - a b
- 0 0 0
a 0 1 1

si luego agrego uno más F(2, 1)

  - a
- 0 0
a 0 1
b 0 1

si luego agrego uno más F(2, 2)

  - a b
- 0 0 0
a 0 1 1
b 0 1 2

si luego agrego uno más F(3, 1)

  - a
- 0 0
a 0 1
b 0 1
b 0 1

si luego agrego uno más F(3, 2)

  - a b
- 0 0 0
a 0 1 1
b 0 1 2
b 0 1 2

Luego,

i = 0, 1, 2 ... x
j = 0, 1, 2 ... y

F(i, j) = F(i-1,  j-1) + 1 si X[i] == Y[j] sino max(F(i-1,  j), F(i,  j-1))

"""


class LCS(object):

    @staticmethod
    def longest_common_subsequence(text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        X = text1
        x = len(text1)

        Y = text2
        y = len(text2)

        M = [[None] * (y + 1) for _ in range(x + 1)]

        for i in range(x + 1):
            for j in range(y + 1):
                if i == 0 or j == 0:
                    M[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    M[i][j] = M[i - 1][j - 1] + 1
                else:
                    M[i][j] = max(M[i - 1][j], M[i][j - 1])

        return M[x][y]


if __name__ == '__main__':
    print(LCS.longest_common_subsequence("abc", "ab"))
