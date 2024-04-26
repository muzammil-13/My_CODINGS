"""
Additional Code Challenges

1.Create a new list from existing list (Use String Format)
2.Create a List with 8 elements
    1. Print second index to sixth index.
3.Create a tuple with 7 elements
    1. Use Insert, Append.
    2. Print the last second element.
"""

oldList=['hello','hi','good','nice']
newList=[]
for i in oldList:
    lists="wishing you {}".format(i)
    newList.append(lists)
print("Q1 = ",newList)

carList=['baleno','alto','thar','city','xuv500','ciaz','amaze','ritz']
print("car list= ",carList[2:7])

tuple1=(1,2,3,4,5,6,7)
x=list(tuple1)
x.insert(8,10)
x.append(12)
tuple1=tuple(x)
print("tuple items= ",tuple1)
print("last second element in tuple= ",tuple1[-2])
