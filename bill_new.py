import time

name_payer = []
amount_payer = []
amount_decr = []
amount_debit1 = []
amount_debit2 = []
amount_tempdecr1 = []
amount_tempdecr2 = []
num = int(input("\n Enter the total number of persons: "))
payer = int(input("\n Enter the number of persons paid: "))
if (payer<=num):
    
    for i in range(1 ,payer + 1):
        temp = input("\n Enter the name of payer: ")
        name_payer.append(temp)

        temp1 = int(input("\n Enter the paid amount: "))
        amount_payer.append(temp1)
    print("\n Enter names of other persons")
    time.sleep(1)
    for i in range(payer +1 , num+1):
        amount_payer.append(0)
        temp3 = input("\n Enter the name: ")
        name_payer.append(temp3)
        

amount_total = 0

for i in range(0,payer):
    amount_total = amount_total + amount_payer[i]

amount_each = amount_total//num

for i in range(0,num):
    temp2 = amount_payer[i] - amount_each
    amount_decr.append(temp2)
for p in range(0,payer):
    print("\n",name_payer[p],"will get a total amount of Rs.",amount_decr[p])
 

for i in range(0,payer):
    temp10 = amount_decr[i]
    amount_tempdecr1.append(temp10)
    for j in range(payer,num):
        temp11 = amount_decr[j]
        amount_tempdecr2.append(temp11)
        if(amount_decr[j]!=0):
            if((amount_tempdecr1[i]-(0-amount_decr[j]))==0):
                print("\n",name_payer[i],"will get Rs.",0-amount_decr[j],"from",name_payer[j])
                amount_tempdecr1[i] = 0
                amount_decr[j] = 0
                break
                
            if((amount_tempdecr1[i]-(0-amount_decr[j]))>0):
                                
                temp4 = 0-amount_decr[j]
                amount_debit1.append(temp4)
                print("\n",name_payer[i],"will get Rs.",temp4,"from",name_payer[j])
                amount_tempdecr1[i] = amount_tempdecr1[i] + amount_decr[j]
                amount_decr[j]=0
                
            if((amount_tempdecr1[i]-(0-amount_decr[j]))<0):
                
                temp5 = (amount_tempdecr1[i]+amount_decr[j])
                print("\n",name_payer[i],"will get Rs.",amount_tempdecr1[i],"from",name_payer[j])
                amount_debit2.append(amount_tempdecr1[i])
                amount_decr.pop(j)
                amount_decr.insert(j,temp5)
                amount_tempdecr1[i] = 0
                break
                
            
           
           



        

