# Delete Product Module: Accepts Product Code and deletes corresponding product from inventory

import mysql.connector

def Del_Prod():
    while True:
        mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")
        cursor = mycon.cursor()
        cursor.execute("select pcode from inventory")
        items = cursor.fetchall()
        avlb_pcodes = []
        for i in items:
            for j in i:
                avlb_pcodes += [j]

        pcode = input("\n\nEnter the product code of the product to be deleted:")

        if pcode.upper() in avlb_pcodes:
            cursor.execute("select * from inventory where PCode='{}'".format(pcode,))
            prod = cursor.fetchone()
            print("\nCurrent values:\tPCode:", prod[0], "\tPName:", prod[1], "Quantity:", prod[2], "\tPrice:", prod[3], "\tDiscount%:", prod[4], "HSN Code:", prod[5], "\n")
            confirm = input("\nAre you sure you want to delete this product? (y/n):")
            if confirm in "yY":
                cursor.execute("delete from inventory where PCode='{}'".format(pcode,))
                mycon.commit()
                print("\nProduct", pcode, "deleted successfully")
            else:
                print("\nOkay. Product", pcode, "not deleted.")
        else:
            print("\nProduct", pcode, "not in inventory.")
        cnt = input("\nDo you wish to delete any other product? (y/n):")
        if cnt in "yY":
            pass
        else:
            print("Okay")
            break
