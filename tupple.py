#for making a tupple
tup=("mango","litchi","apple","banana","apple")
print(tup)

#length of the touple
print(len(tup))

#type of the touple
print(type(tup))

#indexing
print(tup[4])

#negetive indexing
print(tup[-2])

#range of indexing
print(tup[3:6])

#range of negative indexing
print(tup[-4:5])

#check item is exists or not
if "orange" in tup:
    print("item exists.")
else:
    print("item does not exist!!")

#update values:adding the values
y=("litchi" ,)
tup+=y
print(tup)


#remove the values
y=list(tup)
y.remove("apple")
print(tup)
tup= tuple(y)

#unpacking a touple(we normally assign values is call packing of touple)
(yellow,red,purple,pink, blue)=tup
print(yellow)
print(purple)
print(red)
print(blue)
print(pink)


    #using astrick 
(green,black,*white)=tup
print(green)
print(white)
print(black) 


#loop  touple
for double in  tup:
 print(double)

 #loop through indexing touple
 for i in  range(len(tup)):
    print(tup[i])

#using a while numbers
i=0
while(i<len(tup)):
   print(tup[i])
   i=i+1

#join two touples 
tup2=(2,3,4,6,7)
newTup=tup+tup2
print(newTup)

#multiply touples
newTup2=tup*2
print(newTup2)

#touple mehtods->
tup.count()
print(tup)
