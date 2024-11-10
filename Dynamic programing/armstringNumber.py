n =int(input("Enter a number:"))
n1=str(n)
temp=sum(int(i)**len(n1) for i in n1)

if n==temp:
    print(f"The given number {t} is a armstrong")
else:
      print(f"The given number {t} is not a armstrong")