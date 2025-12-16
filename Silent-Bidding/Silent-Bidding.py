from logo import logo
print(logo)
print("Welcome to Silent Bidding!")

people= {}
final_bidder= ""

final_bid=0
rerun = True
while rerun:
    status = input("'yes' to  bid, 'no' to see results\n").lower()

    if status == "yes":
        name = input("Type the name of the bidder\n")
        bid = int(input("Place your bid\n"))

        people[name]= bid
        print("\n"*200)

    elif status == "no":
        rerun = False

    else:
        print("Enter properly")

for key in people:
    if people[key]>=final_bid:
        final_bid=people[key]
        final_bidder= key

print(f"{final_bidder} wins the bid with {final_bid}\n")

print("Final results:\n")

for key in people:
    print(f"{key} : rs. {people[key]}")