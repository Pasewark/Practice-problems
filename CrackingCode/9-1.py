def solve(n):
    solutions=[0 for i in range(n)]
    solutions[0]=1
    solutions[1]=2
    solutions[2]=4
    for i in range(3,n):
        solutions[i]=solutions[i-1]+solutions[i-2]+solutions[i-3]
    print solutions[-1]
