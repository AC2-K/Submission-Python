N=int(input())
A=list(map(int,input().split()))
ans=0
check=True
while check:
    exist=False
    for i in range(N):
        if A[i]%2==0:
            exist=true
    
    if exist:
        check=False
        continue
    ans+=1
    for i in range(N):
        A[i]//=2

print(ans)