def calculate_gst(amount, gst_rate):
    gst = amount * gst_rate / 100
    total_amount = amount + gst
    return total_amount

amount = float(input("Enter amount: "))
gst_rate = float(input("Enter GST rate (%): "))

total = calculate_gst(amount, gst_rate)

print("Total amount including GST =", total)