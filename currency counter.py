curren=[100,50,20,10,5,2,1]
count=[]
amount=int(input('Enter the amount'))
for value in curren:
    if value<= amount:
        Q=amount//value
        count=count+[Q]
        print(f'{Q} notes of {value}')
        amount=amount%value
        if Q==0:
            break