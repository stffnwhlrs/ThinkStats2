t = [1,2,4,6,2,5,7,2,5,6,3]

hist = {}

for x in t:
    hist[x] = hist.get(x,0) + 1

# ---------

for val in sorted(t):
    print(val)