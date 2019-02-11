account = 1000
rate = int(input("Enter rate (0, 25): "))/100
month = 0

while account < 1100:
    month +=1
    account += account*rate

print(month)
