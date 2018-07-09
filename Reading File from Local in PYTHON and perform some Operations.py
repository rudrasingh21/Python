Reading File from Local and perform some Operations:-

>>> orderitemFILE = open("/root/data/retail_db/order_items/order_items.txt","r")

#(‘r’) : Open text file for reading.

>>> type(orderitemFILE)
<type 'file'>

>>> orderitemFILE
<open file '/root/data/retail_db/order_items/order_items.txt', mode 'r' at 0x7f46cc622c00>

>>> orderItemsREAD = orderitemFILE.read()

>>> type(orderItemsREAD)
<type 'str'>

>>> help(str)

>>> orderItemSPLIT = orderItemsREAD.splitlines()

>>> type(orderItemSPLIT)
<type 'list'>

----#preview data

#10 records from starting
>>> orderItemSPLIT[:10]
['1,1,957,1,299.98,299.98', '2,2,1073,1,199.99,199.99', '3,2,502,5,250.0,50.0', '4,2,403,1,129.99,129.99', '5,4,897,2,49.98,24.99', '6,4,365,5,299.95,59.99', '7,4,502,3,150.0,50.0', '8,4,1014,4,199.92,49.98', '9,5,957,1,299.98,299.98', '10,5,365,5,299.95,59.99']

>>> len(orderItemSPLIT)
172198

#10 records from last
>>> orderItemSPLIT[-10:]
['172189,68880,1014,3,149.94,49.98', '172190,68880,502,5,250.0,50.0', '172191,68880,1073,1,199.99,199.99', '172192,68880,1014,5,249.9,49.98', '172193,68880,1014,3,149.94,49.98', '172194,68881,403,1,129.99,129.99', '172195,68882,365,1,59.99,59.99', '172196,68882,502,1,50.0,50.0', '172197,68883,208,1,1999.99,1999.99', '172198,68883,502,3,150.0,50.0']

----

>>> orderItemFILTER = filter(lambda i: int(i.split(",")[1]) == 68880,orderItemSPLIT)

>>> orderItemFILTER
['172189,68880,1014,3,149.94,49.98', '172190,68880,502,5,250.0,50.0', '172191,68880,1073,1,199.99,199.99', '172192,68880,1014,5,249.9,49.98', '172193,68880,1014,3,149.94,49.98']

>>> orderItemMAP = map(lambda i : float(i.split(",")[4]), orderItemFILTER)
>>> orderItemMAP
[149.94, 250.0, 199.99000000000001, 249.90000000000001, 149.94]

>>> orderItemREDUCE = reduce(lambda total, element: total + element, orderItemMAP)

>>> orderItemREDUCE
999.76999999999998

----------------------------FYNAL STEPS:----------------------------


>>> orderitemFILE = open("/root/data/retail_db/order_items/order_items.txt","r")


>>> orderItemsREAD = orderitemFILE.read()


>>> orderItemSPLIT = orderItemsREAD.splitlines()


>>> orderItemFILTER = filter(lambda i: int(i.split(",")[1]) == 68880,orderItemSPLIT)


>>> orderItemMAP = map(lambda i : float(i.split(",")[4]), orderItemFILTER)

>>> orderItemREDUCE = reduce(lambda total, element: total + element, orderItemMAP)

>>> orderItemREDUCE
999.76999999999998
