# Update Products Module: Updates details of an existing product

import mysql.connector

def Update_Prod():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()
        cursor.execute("select pcode from inventory")
        items = cursor.fetchall()
        avlb_pcodes = []
        for i in items:
            for j in i:
                avlb_pcodes += [j]

        pcode = input("\nEnter the product code of the product to be updated:")

        if pcode.upper() in avlb_pcodes:
            while True:
                cursor.execute("select * from inventory where PCode='{}'".format(pcode,))
                prod = cursor.fetchone()
                print("\nCurrent values:\tPCode:", prod[0], "\tPName:", prod[1], "Quantity:", prod[2], "\tPrice:", prod[3], "\tDiscount%:", prod[4], "\tHSN Code:", prod[5], "\n")
                print("\nMenu:\n1.Quantity\n2.Price\n3.Discount\n4.HSN Code")
                field = input("\nEnter field number to be updated from the menu:")
                if field == '1':
                    qty = int(input("\nEnter the new quantity:"))
                    cursor.execute("update inventory set Quantity={} where PCode='{}'".format(qty, pcode))
                    mycon.commit()
                    print("\nUpdated successfully")
                elif field == '2':
                    price = float(input("\nEnter the new price:"))
                    cursor.execute("update inventory set Price={} where PCode='{}'".format(price, pcode))
                    mycon.commit()
                    print("\nUpdated successfully")
                elif field == '3':
                    dcnt = float(input("\nEnter the new discount:"))
                    cursor.execute("update inventory set Discount_percent={} where PCode='{}'".format(dcnt, pcode))
                    mycon.commit()
                    print("\nUpdated successfully")
                elif field == '4':
                    cursor.execute("select HSN_Code from HSN_Code_List")
                    items = cursor.fetchall()
                    no_of_items = cursor.rowcount
                    avlb_hsn_codes = []
                    for i in items:
                        for j in i:
                            avlb_hsn_codes += [j]

                    hsn_code = input("\nEnter the new HSN Code:")
                    if hsn_code in avlb_hsn_codes:
                        cursor.execute("update inventory set HSN_Code='{}' where PCode='{}'".format(hsn_code, pcode))
                        mycon.commit()
                        print("\nUpdated successfully")
                    else:
                        hsn_choice = input(("\nHSN_Code does not exist in the table. Do you wish to add it? (y/n):"))
                        if hsn_choice in "yY":
                            tax_percent = float(input("\nEnter the tax% for the HSN Code"))
                            cursor.execute("insert into HSN_Code_List values ('{}',{})".format(hsn_code, tax_percent))
                            mycon.commit()
                            print("\nHSN Code", hsn_code, "with tax%", tax_percent, "successfully added")
                            cursor.execute("update inventory set HSN_Code='{}' where PCode='{}'".format(hsn_code, pcode))
                            mycon.commit()
                            print("\nUpdated successfully")
                        else:
                            print("\nCannot add an HSN Code that does not exist in the table")
                else:
                    print("\nInvalid choice")
                field_choice = input("\nDo you wish to update another field? (y/n):")
                if field_choice in "yY":
                    pass
                else:
                    print("\nOkay")
                    break
        else:
            print("\n", pcode, "not available. Try again")
        ch = input("\nDo you wish to update any other record? (y/n):")
        if ch in "yY":
            pass
        else:
            print("\nOkay!")
            break
