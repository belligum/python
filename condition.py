num1=int(input("enter the num1"))
if num1>0:
 print("it is a positive number")
elif num1<0:
 print("it is a negative number")
else:
 print("it is zero")

num1=int(input("enter the num1"))
if num1%2==0:
 print("it is an even number")
else:
 print("it is odd")

list=["football","cricket","basketball","hockey","baseball","coco"]

print("length",len(list))
print("first element",list[0])
print("last element",list[0])
list.append("vollyball")
print(list)