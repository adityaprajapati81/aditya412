total_debit = float(input("Enter total Debit amount: "))
opening_balance = float(input("Enter opening balance amount: "))
answer = total_debit - opening_balance
average = float(input("Enter your average: "))
avg = average / 100
k = answer / avg
tds_type = float(input("Enter TDS: "))
t = tds_type / 100
tds = answer / avg * t
print(tds)