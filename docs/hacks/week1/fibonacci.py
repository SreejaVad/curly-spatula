#basic recursion and implimentation of fibonacci pattern
def recur_fibo(n):
  if n<=1:
    return n
  else:
    return(recur_fibo(n-1) + recur_fibo(n-2))

# take input from the user in tester function
def tester():
  try:
    nterms = int(input("How many terms?"))
    if nterms <= 0:
      print("please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(nterms):
          print(recur_fibo(i))
  except ValueError:
    print(f"Not a number:{nterms}")