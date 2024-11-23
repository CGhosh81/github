def plusOne(digits):
       x=0
       for i in range(len(digits)):
          x=x*10+digits[i]

  
       
       result=[int(digit) for digit in str(x+1)]
       return result

digits = [9]
print(plusOne(digits))