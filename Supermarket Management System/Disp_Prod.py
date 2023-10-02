# Display Products Module: Displays products from selected category in tabular form

import mysql.connector

def Disp_Prod():
    mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="supermarket")
    cursor = mycon.cursor()
    cursor.execute("select * from inventory order by PCode")
    items = list(cursor.fetchall())

    # Separate List:

    fruits, veg, groc, pers_gr = [], [], [], []

    for i in items:
        i = list(i)
        while (len(i[1]) < 20):
            i[1] += " "
        if (i[0][:2] == "FR"):
            fruits.append(i)
        elif (i[0][:2] == "VG"):
            veg.append(i)
        elif (i[0][:2] == "GR"):
            groc.append(i)
        elif (i[0][:2] == "PG"):
            pers_gr.append(i)

    # Asking for choice

    def Category_Disp():
        print("\n\nMenu:\n1. Fruits\n2. Vegetables\n3. Groceries\n4. Personal Grooming")
        choice3 = input("\nEnter category no. from above menu:")
        S_No = 1

        if choice3 == '1':
            print("\nS.No\t\tProduct Code\t\tProduct Name\t\tQuantity\t\tPrice\t\tDiscount\tHSN Code\n\n")
            for i in fruits:
                print(S_No, "\t\t", i[0], "\t\t\t", i[1], "\t", i[2], "\t\t\t", i[3], "\t\t", i[4], "\t\t", i[5])
                S_No += 1

        elif choice3 == '2':
            print("\nS.No\t\tProduct Code\t\tProduct Name\t\tQuantity\t\tPrice\t\tDiscount\tHSN Code\n\n")
            for i in veg:
                print(S_No, "\t\t", i[0], "\t\t\t", i[1], "\t", i[2], "\t\t\t", i[3], "\t\t", i[4], "\t\t", i[5])
                S_No += 1

        elif choice3 == '3':
            print("\nS.No\t\tProduct Code\t\tProduct Name\t\tQuantity\t\tPrice\t\tDiscount\tHSN Code\n\n")
            for i in groc:
                print(S_No, "\t\t", i[0], "\t\t\t", i[1], "\t", i[2], "\t\t\t", i[3], "\t\t", i[4], "\t\t", i[5])
                S_No += 1

        elif choice3 == '4':
            print("\nS.No\t\tProduct Code\t\tProduct Name\t\tQuantity\t\tPrice\t\tDiscount\tHSN Code\n\n")
            for i in pers_gr:
                print(S_No, "\t\t", i[0], "\t\t\t", i[1], "\t", i[2], "\t\t\t", i[3], "\t\t", i[4], "\t\t", i[5])
                S_No += 1

        else:
            print("\n\nInvalid choice")

    Category_Disp()

    while True:
        cnt = input("\n\nDo you wish to check other categories? (y/n):")
        if cnt in "yY":
            Category_Disp()
        else:
            print("\nOkay!")
            break
