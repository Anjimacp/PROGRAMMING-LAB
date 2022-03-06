#code1
 list=[-1,0,1,2]
positive=[num for num in list if num>0]
print(positive)
#code2
n=int(input("enter the limit"))
square=[i*i for i in range(n)]
print(square)
#code3
word=input("enter the word")
vowels = [x for x in word if x== "a" or x=="e" or x=="i" or x=="o" or x=="u"]
print(vowels)
#code4
list1=["python"]
value=[ord(ele) for sub in list1 for ele in sub]
print(value)
