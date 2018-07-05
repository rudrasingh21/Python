#store monthly expences in a list and find out total expences for all months

exp = [2340, 2500, 6500, 4322, 2500]
#total = exp[0] + exp[1] + exp[2] + exp[3] + exp[4]
total = 0
for item in exp:
    total = total + item
print(total)

