# Display HSN Codes Module: Displays HSN Codes with corresponding tax percent

import mysql.connector

def Disp_Code():
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="supermarket")
    cursor = mycon.cursor()
    
    cursor.execute("select * from HSN_Code_List")
    codes = cursor.fetchall()

    print("\n\nHSN Code\tTax %")

    for i in codes:
        for j in i:
            print(j, end="\t\t")
        print()
