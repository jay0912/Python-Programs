t = int(input())
for i in range(t):
    a=[]
    result=[]
    n,k = input().split()
    n,k = int(n),int(k)
    
    a = input().split()
    
    #main operation
  
    for j in range(n-1):
        #count=0
        if(n%2==0):
            count = 0
        if(n%2!=0) :
            count = 1 

        if (a[j] in result) or ((j+1) == a[j]):
            continue
        
        for l in range(j+1,n):
            if a[j] == a[l]:
                count=count+1
            if count == k:
                result.append(a[j])
                break
            
    #prints result
    print(len(result))