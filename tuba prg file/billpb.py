unit=int(input("enter unit consumed:"))
if unit<=50:
    bill=unit*0.5
elif unit<=150:
    bill=25+(unit-50)*0.75
elif unit<=250:
    bill=100+(unit-150)*1.2
else:
    bill=220+(unit-250)*1.5
print("your bill is",bill)   
