# 24.Take a 3-digit number and find sum of digits using % and //.

num = int(input("Entetr a 3-digit number: "))

firstDigit = (num // 100)
midDigit = (num // 10) % 10
lastDigit = (num % 10)

sum = firstDigit+midDigit+lastDigit

print(f"{firstDigit}+{midDigit}+{lastDigit} = {sum}")