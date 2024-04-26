# Print Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
def fibo(stop):
    q=0
    w=1
    print(q, end="\n")

    while w<stop:
        print(w, end="\n")
        q, w = w, q + w
    print()
fibo(150)