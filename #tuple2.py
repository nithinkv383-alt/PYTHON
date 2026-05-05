#tuple

L1 = () #empty tuple 
L2 = (1,2,3,4,5,6)
L3 = ("c program" , "java ","python")
print(L1)
print(L2[2])
print(L3[1:3])

# tuple functions
t = (2,3,4,4,5,6)
print(max(t))
print(min(t))
print(sum(t))
print(len(t))
print(t.count(4))
print(t.index(3))

#list

L1 =[] or list()
L2 = [1,2,3,4,5,6] or list((1,2,3,4,5,6))
L3 = ["c " , "java" , "python"] or list(("c","java","python"))
L4 = [123,"python",3.7] or list((123 , "python", 3.7))
print(L1)
print(L2)
print(L3)
print(L4)

# list operations

num = [1,2,3,4,5]
lang = ["python ", "c" , "java" , "php"]
print(num+lang)
print(num * 2)
print(lang[2])
print(lang[1:4])
print("cpp " in lang)
print("6" not in num)

# iterating list

lang = ["python ", "c " , "java " , "php"]
print("the list item are \n")
for i in lang:
    print(i)

# list functions

a = [1,2,3,4,4,5]
a.append(6)
print(a)
a.reverse()
print(a)
a.count(4)
print(a)
a.extend("b")
print(a)
a.index(2)
print(a)
a.insert(2, 10)
print(a)
a.pop(1)
print(a)
a.remove(3)
print(a)
a.clear()
print(a)



#sets

days1 = {"mon" , "tue ", "wed"  , "sat"}
days2 = {"thu" , "fri" , "sat" , "sun" , "mon"}
print("days1 union days2 : ", days1 | days2)
print("days1 intersection days2 : ", days1 & days2)
print("days1 difference days2 : ", days1 - days2)