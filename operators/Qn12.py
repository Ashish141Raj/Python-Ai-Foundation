# 12.Take principle,rate, and time calculate simple interset.

principle = float(input("Enter Principle Amount: "))
rate  =  float(input("Enter rate of interest: "))
time = float(input("Enter Time period of Interest: "))

simpleInterest = (principle*rate*time)/100

print(f"Simple interest of {principle} for {rate} on {time} is {simpleInterest}")