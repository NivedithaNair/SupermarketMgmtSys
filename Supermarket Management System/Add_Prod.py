# Add Products Module: Adds a product to SQL Table

import mysql.connector

def Add_Prod():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()
        cursor.execute("select pcode from inventory")
        items = cursor.fetchall()
        avlb_pcodes = []
        for i in items:
            for j in i:
                avlb_pcodes += [j]

        cursor.execute("select HSN_Code from HSN_Code_List")
        items = cursor.fetchall()
        no_of_items = cursor.rowcount
        avlb_hsn_codes = []
        for i in items:
            for j in i:
                avlb_hsn_codes += [j]

        print("\nEnter the details of the product:")
        pcode = input("\nProduct Code:")
        if pcode.upper() in avlb_pcodes:
            print("\nA product with the same PCode already exists. New product with the same code cannot be added")
        else:
            pname = input("Product Name:")
            qty = float(input("Quantity:"))
            price = float(input("Price:"))
            dcnt = float(input("Discount %:"))
            hsn_code = input("HSN_Code:")

            if hsn_code in avlb_hsn_codes:
                prod = (pcode, pname, qty, price, dcnt, hsn_code)
                cursor.execute("insert into inventory values('{}','{}',{},{},{},'{}')".format(pcode, pname, qty, price, dcnt, hsn_code))
                mycon.commit()
                print("\n\nProduct", prod, "added successfully")
            else:
                hsn_choice = input(("HSN_Code does not exist in the table. Do you wish to add it? (y/n):"))
                if hsn_choice in "yY":
                    tax_percent = float(input("Enter the tax% for the HSN Code"))
                    cursor.execute("insert into HSN_Code_List values ('{}',{})".format(hsn_code, tax_percent))
                    mycon.commit()
                    print("HSN Code", hsn_code, "with tax%", tax_percent, "successfully added")

                    prod = (pcode, pname, qty, price, dcnt, hsn_code)
                    cursor.execute("insert into inventory values('{}','{}',{},{},{},'{}')".format(pcode, pname, qty, price, dcnt, hsn_code))
                    mycon.commit()
                    print("\n\nProduct", prod, "added successfully")
                else:
                    print("Product cannot be added without an existing HSN_Code")

        ch = input("\n\nDo you wish to add more products? (y/n):")
        if ch in "yY":
            pass
        else:
            print("\n\nOkay!")
            break
