# Add HSN Code Module: Adds HSN Code, Tax Percent to SQL Table

import mysql.connector

def Add_Code():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()

        cursor.execute("select HSN_Code from HSN_Code_List")
        items = cursor.fetchall()
        no_of_items = cursor.rowcount
        avlb_hsn_codes = []

        for i in items:
            for j in i:
                avlb_hsn_codes += [j]

        hsn_code = input("\nEnter HSN Code to be added:")

        if hsn_code in avlb_hsn_codes:
            print("\nHSN Code", hsn_code, "already exists. Cannot be added")
        else:
            tax_percent = float(input("\nEnter the tax percent:"))
            cursor.execute("insert into HSN_Code_List values('{}',{})".format(hsn_code, tax_percent))
            mycon.commit()
            print("\nHSN Code", hsn_code, "with tax percent", tax_percent, "added successfully")

        cnt = input("\nDo you wish to add another code?(y/n):")
        if cnt in "yY":
            pass
        else:
            break
