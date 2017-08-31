c=int(input('Please enter the amount of change up to 99 cents and we\'ll split it up with the fewest coins possible:'))
print(c//25, "quarters")
c = c%25
print(c//10, "dimes")
c = c%10
print(c//5, "nickles")
c = c%5
print(c//1, "pennies")
