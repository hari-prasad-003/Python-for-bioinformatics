from datetime import datetime

# ---------- Price Data ----------
price ={"Maggie":20, "Biscuits":15, "Kitkat":20, "Coca cola":40, "Wine":1000, "Nuts":500}
item = {1:"Maggie", 2:"Biscuits", 3:"Kitkat", 4:"Coca cola", 5:"Wine", 6:"Nuts"}
orditems =[]

# ---------- Input Section ----------
print("List of items")
print("1.Maggie\n2.Biscuits\n3.Kitkat\n4.Coca cola\n5.Wine\n6.Nuts")
print()
print("Enter the numbers 1to 6 for your choice and enter 7 for exit")

# User input loop
t = int(input("Enter your choice: "))
while (t>=1) and (t<=6):
    n = int(input("No of quantity: "))    # No of quantity
    t1 = item[t]                          # Extract items
    t2 = price[t1]                        # Extract prices
    tc = n*t2                             # Total amount of one product
    orditems.append([t1, t2, n, tc])
    print("List of items")
    print("1.Maggie\n2.Biscuits\n3.Kitkat\n4.Coca cola\n5.Wine\n6.Nuts")
    print()
    print("Enter the numbers 1to 6 for your choice and enter 7 for exit")
    t = int(input("Enter your choice: "))

# ---------- FUNCTIONS ----------
def apply_discount(total):
    """Apply 10% discount if total > 500"""
    if total > 500:
        discount = total * 0.10
        new_total = total - discount
        return discount, new_total
    else:
        return 0, total

def apply_gst(total):
    """Apply 5% GST on total"""
    gst = total * 0.05
    final_total = gst + total
    return gst, final_total

# ---------- BILL PRINTING ----------
print()
print(f"{"Retail Bill System":^20}")
print("---------------------------------")

# ---------- Timestamp ----------
now = datetime.now()
bill_time = now.strftime("%d-%m-%Y %H:%M:%S")
print(bill_time)

print(f"{"Name":<10}{"Price":<7}{"Quanity":<8}{"Total"}")
print("---------------------------------")

grand_total = 0
for i in orditems:
    print(f"{i[0]:<10}{i[1]:<7}{i[2]:^8}{i[3]}")
    grand_total+=i[3]

print("---------------------------------")
print("Gross total amount: ",grand_total)

# Apply discount
print()
discount, new_total = apply_discount(grand_total)
if discount>0:
    print(f"Discount (10%) = -₹{discount:.2f}")
else:
    print("Discount is not applicable")

# Apply GST after discount
gst, final_total = apply_gst(new_total)
print(f"GST (5%) = +₹{gst:.2f}")
print("---------------------------------")
print(f"Total payable amount = ₹{final_total}")
print("---------------------------------")
print("Thank you for shopping")