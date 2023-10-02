# Delete HSN Code Module: Accepts HSN Code and deletes corresponding record from HSN Code List

import mysql.connector

def Del_Code():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()

        cursor.execute("select hsn_code from HSN_Code_List")
        items = cursor.fetchall()
        avlb_hsn_codes = []

        for i in items:
            for j in i:
                avlb_hsn_codes += [j]

        cursor.execute("select HSN_Code from inventory")
        items = cursor.fetchall()
        prod_hsn_codes = []

        for i in items:
            for j in i:
                prod_hsn_codes += [j]

        hsn_code = input("\nEnter HSN Code to be deleted from HSN Code List:")

        if hsn_code in avlb_hsn_codes:
            if hsn_code in prod_hsn_codes:
                print("\nProduct with HSN Code", hsn_code, "exists in the inventory table.")
                print("HSN Code", hsn_code, "cannot be deleted from HSN_Code_List")
            else:
                confirm = input("\nAre you sure you want to delete the code?(y/n):")
                if confirm in "yY":
                    cursor.execute("delete from HSN_Code_List where HSN_Code='{}'".format(hsn_code,))
                    mycon.commit()
                    print("\nHSN Code", hsn_code, "successfully deleted")
                else:
                    print("\nOkay. HSN Code", hsn_code, "not deleted.")
        else:
            print("\nHSN Code", hsn_code, "does not exist in HSN_Code_List")

        cnt = input("\nDo you wish to delete any other code?(y/n):")
        if cnt in "yY":
            pass
        else:
            break
