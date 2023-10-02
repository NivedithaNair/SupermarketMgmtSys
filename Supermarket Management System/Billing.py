# Billing Module: Generates a bill

import mysql.connector

def Billing():
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
    cursor = mycon.cursor()
    cursor.execute("select pcode from inventory")
    items = cursor.fetchall()
    avlb_pcodes = []
    for i in items:
        for j in i:
            avlb_pcodes += [j]

    # Start Billing
    print("\nS.No.\t\t[Product Code, Quantity]\n")

    # Enter [product code, quantity], type "STOP" to end and print the bill
    p_codes_total = []
    prod_entry = [None, None]
    S_No = 1
    while (prod_entry[0] != "STOP"):
        print(S_No, "\t\t", end="")
        prod_entry = eval(input())
        if prod_entry[0].upper() in avlb_pcodes:
            p_codes_total += [prod_entry]
        else:
            if (prod_entry[0] == "STOP"):
                pass
            else:
                print(prod_entry[0], "unavailable")
        S_No += 1

    # Printing the bill
    print("\n\t\t\t\t\t\t\t***** XYZ SUPERMARKET *****\n\n\n\n")
    print("\nS.No.\tProduct Code\t  Product Name\t\tMRP\tDiscount %\tHSN_Code\tTax %\tQuantity\t NetAmt\t  SGST\tCGST\n\n")
    S_No = 1
    Gross_amt = 0
    for i in range(len(p_codes_total)):
        pcode = p_codes_total[i][0]
        qty_bought = p_codes_total[i][1]
        cursor.execute("select * from inventory where PCode='{}'".format(pcode,))
        prod = cursor.fetchone()
        pname = prod[1]
        while (len(pname) < 20):
            pname += " "
        mrp = prod[3]
        discount_percent = prod[4]
        hsn_code = prod[5]
        discounted_price = mrp * (1 - 0.01 * discount_percent)
        net_amt = discounted_price * qty_bought
        cursor.execute("select Tax_Percent from HSN_Code_List where HSN_Code='{}'".format(hsn_code,))
        tax_percent = cursor.fetchone()[0]
        base_price = mrp / (1 + 0.01 * tax_percent)
        tax_per_unit = base_price * 0.01 * tax_percent
        net_tax = tax_per_unit * qty_bought
        sgst = net_tax / 2
        cgst = net_tax / 2
        new_qty = prod[2] - qty_bought
        cursor.execute("update inventory set Quantity={} where PCode='{}'".format(new_qty, pcode))
        mycon.commit()
        print(S_No, "\t", pcode, "\t\t", pname, "\t", mrp, "\t", discount_percent, "\t\t", hsn_code, "\t", "\t",
              tax_percent, "\t", qty_bought, "\t\t", round(net_amt, 2), "\t", round(sgst, 2), "\t", round(cgst, 2))
        Gross_amt += net_amt
        S_No += 1

    Gross_amt = round(Gross_amt, 2)
    print("\n\nGross Amount:", Gross_amt)
    pymt = input("\n\nMode of Payment(Cash/Debit Card/Credit Card/UPI):")
    if (pymt.lower() == "cash"):
        recd = float(input("\nAmount Received: Rs."))
        bal = round(recd - Gross_amt, 2)
        print("Balance paid in cash: Rs.", bal)
    print("\n\t\t\t\t\t\t\t ***** Have a nice day! *****")
