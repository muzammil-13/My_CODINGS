# handling the list index out of range(IndexError)
try:
    a=[12,34,56,78]
    print(a[4])
except:
    print("there is an index error!!")
finally:
    print("am friendly")