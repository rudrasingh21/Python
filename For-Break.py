Key_Location="chair"
locations=["garage","living Room","chair","garden"]
for i in locations:
    if i==Key_Location:
        print("Key Is Found in : ",i)
        break
    else:
        print("Key Is Not Fount in : ",i)