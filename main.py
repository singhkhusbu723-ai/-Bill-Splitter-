print("==== Bill Splitter ====")
running_total = 0

num_of_friends = 5

starters = 1200
snacks = 350
lunch = 1300
drinks = 2500


running_total  += starters + snacks + lunch + drinks
print('Total bill so far:' , running_total) 

tip = running_total * 0.15
print(f"Tip amount: {tip}")

running_total += tip
print('Total with tip:' , running_total)

final_bill = running_total / num_of_friends
print('Bill per person:' , final_bill)

each_pays = round(final_bill, 2)
print(f"Each person pays (rounded): {each_pays}")
