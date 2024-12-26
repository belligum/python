print("The table of 17")
num=17
for i in range(1,11):
 mul=num*i
 print("17 *%d=%d"%(i,mul))

print("The table of 23")
num=23
for i in range(1,11):
 mul=num*i
 print("23 *%d=%d"%(i,mul))

num=1
sum=0
while(num <=10):
 sum=sum+num 
 num=num+1
 print(sum)

num=9876543567897654324567897654324567897654
flag=False
for i in range(2,num):
 if (num%i)==0:
  flag=True 
  break
if flag:
 print("it is not a prime number")
else:
 print("it is a prime number")