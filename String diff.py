
drr = []
arr = input()
brr = input()
i = 0
j = 0
r = -1
q = -1
length = len(brr)
length1 = len(arr)
def checker():
    global i
    global j
    global r
    count = 1
    counter = 1
    global length
    global length1
    print(arr[i],brr[j],i,j)
    while(counter>0):
        r = i
        q=j
        
        i+=1
        j+=1

        if((i>=length1 or j >= length)):
            counter = 0
            break

        if(arr[i]==brr[j]):

            temp1 = i
            temp2 = j

            count+=1
        if(arr[i]!=brr[j]):

            counter=0
            break
            

    print(count,'count')
    return(count)
def validate(p):
    global length
    global j
    f = 0
    for j in range(0,length):
        if(j>q):
            if(p==brr[j]):
                f = checker()
                print(f,'f')
                return(f)
                
    return(f)       
    

for i in range(0,len(arr)):
    if(i>r):

        b = validate(arr[i])
        print(b,'b')

        if(b==1 and i!=j):
            drr.append(0)
        if((b==1 and i==j) or b>1):                    
            drr.append(b)

tempor = sum(drr)
print(drr)
if(len(brr)>len(arr)):
    
    diff = len(brr) - tempor
else:
    diff = len(arr)- tempor
print(diff)
