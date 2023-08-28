'''b) Write a python program to multiply two matrices using nested loops'''

m1=[[1,2,3],[2,3,4],[3,4,5]]
m2=[[1,0,1,0],[1,1,2,2],[3,4,1,5]]

mul=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            mul[i][j]+=m1[i][k]*m2[k][j]

for i in mul:
    print(i)