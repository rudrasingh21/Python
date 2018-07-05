indian=["samosa","daal","naan"]
chinese=["momos","egg roll","fried rice"]
italian=["pizza","pasta","risotto"]

dish=input("Enter a dish Name: ")
if dish in indian:
    print("Indian Cuision")
elif dish in chinese:
    print("Chinese Cuision")
elif dish in italian:
    print("Italian Cuision")
else:
    print("I don't have enough data for:",dish)
