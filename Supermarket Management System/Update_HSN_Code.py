# Update HSN Codes Module: Updates details of an existing HSN Code

import mysql.connector

def Update_Code():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()

        cursor.execute("select HSN_Code from HSN_Code_List")
        items = cursor.fetchall()
        avlb_hsn_codes = []

        for i in items:
            for j in i:
                avlb_hsn_codes += [j]

        hsn_code = input("\nEnter the HSN Code to be updated:")

        if hsn_code in avlb_hsn_codes:
            cursor.execute("select tax_percent from HSN_Code_List where HSN_Code='{}'".format(hsn_code,))
            current_tax_percent = cursor.fetchone()[0]
            print("\nCurrent details: HSN Code:", hsn_code, "\tTax %:", current_tax_percent)
            new_tax_percent = float(input("\nEnter the new tax percent:"))
            cursor.execute("update hsn_code_list set Tax_Percent={} where HSN_Code='{}'".format(new_tax_percent, hsn_code))
            mycon.commit()
            print("\nUpdated successfully")
        else:
            print("\nHSN Code", hsn_code, "does not exist in table")

        cnt = input("\nDo you wish to update any other code?(y/n):")
        if cnt in "yY":
            pass
        else:
            break
