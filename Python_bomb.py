import os
d = 0
s = 0
while d == 0:
    s = s + 1
    os.mkdir("create")
    os.mkdir("create/" + str(s))
