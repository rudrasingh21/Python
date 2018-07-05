exp = [1000, 2000, 3000, 4000, 5000]
total=0
for i in range(len(exp)):
    print('Month: ', (i+1), 'Expences:',exp[i])
    total = total + exp[i]
print('Total Exp is : ',total)