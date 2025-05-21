def pttab(m):
    for f in m:
        print(" ".join(str(c) for c in f))
    print()
def nxtgn(m):
    r, c = len(m), len(m[0])
    n = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            v = 0
            if j > 0 and m[i][j-1]: v += 1
            if j < c-1 and m[i][j+1]: v += 1
            if m[i][j] == 1:
                n[i][j] = 1 if v in [1, 2] else 0
            else:
                n[i][j] = 1 if v == 1 else 0
    return n
matriz = [ 
    [0,0,0,0,0,0,0,1,1,0], 
    [0,1,1,0,0,0,0,0,0,0], 
    [0,1,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,1,1,0,0,0], 
    [0,0,0,0,0,1,1,0,0,0], 
    [0,0,1,1,0,0,0,0,0,0], 
    [0,0,1,1,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,1,0], 
]
print("Gen 0:")
pttab(matriz)
g1 = nxtgn(matriz)
print("Gen 1:")
pttab(g1)
g2 = nxtgn(g1)
print("Gen 2:")
pttab(g2)
