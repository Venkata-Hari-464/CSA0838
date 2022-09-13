sub1=int(input("enter marks of sub1"))
sub2=int(input("enter marks of sub2"))
sub3=int(input("enter marks of sub3"))
sub4=int(input("enter marks of sub4"))
sub5=int(input("enter marks of sub5"))
average=sub1+sub2+sub3+sub4+sub5/5
if average>90:
 print("grade S")
elif average<90 and average>80:
 print("grade A")
elif average<80 and average>70:
 print("grade B")
elif average<70 and average>60:
 print("grade C")
else:
 print("fail")
