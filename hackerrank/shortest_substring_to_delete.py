"""

Shortest Substring To Delete

find the shortest substring that after deleting it, the string
only have unique characters

example:

abcbbk -> the shortest substring is bb
xabbcacpqr -> the shortest substring is bca
xyzqwerx -> x
xyzqwzerx -> zerx
xyzqwzerz -> zerz

================
xyzz
s=0
e=0
x
xy  <- y
xyz <- z
xyz !<- z  => s=3 e=3
return 1
================
xyzazbcy
s=0
e=0
x
xy  <- y
xyz <- z
xyza <- a
xyza !<- z  => s=4 e=4
xyzab <- b
xyzabc <- c
xyzabc !<- y => s=4 e=8
return 5
================
xabbcacpqr
s=0
e=0
x
xa  <- a
xab <- b
xab !<- b  => s=3 e=3
xabc <- c
xabc !<- a => s=3 e=5
xyzabc !<- y => s=4 e=8
return 5
================


"""

class Solution:

    def shortestSubString(self):
        pass

if __name__ == '__main__':
    pass