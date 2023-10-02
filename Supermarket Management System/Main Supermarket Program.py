# SUPERMARKET MAIN MODULE: Provides menu at different stages, allowing a wide variety of operations

import mysql.connector
import Billing, Add_Prod, Update_Prod, Del_Prod, Disp_Prod, Add_HSN_Code, Update_HSN_Code, Del_HSN_Code, Disp_HSN_Code

mycon = mysql.connector.connect(host="localhost", user="root", passwd="sqlpaswd", database="Supermarket")

password = "securepaswd"

if mycon.is_connected():
    print("Successfully connected to Supermarket Database\n")

    sysadmin_main_menu = "\n1. Product Manipulation\n2. HSN Code Manipulation\n3. Exit"
    sysadmin_menu_1 = "\n1. Billing\n2. Add Product\n3. Update Product\n4. Delete Product\n5. Display Products\n6. Exit"
    sysadmin_menu_2 = "\n1. Add HSN Code\n2. Update HSN Code\n3. Delete HSN Code\n4. Display HSN Code List\n5. Exit"

    authority = input("sysadmin/admin:")

    if authority.lower() == "sysadmin":
        gate_pass = input("\nEnter password:")

        if gate_pass == password:

            while True:
                print(sysadmin_main_menu)
                choice_main = input("\nEnter choice number from the above menu:")

                if choice_main == '1':
                    while True:
                        print(sysadmin_menu_1)
                        choice1 = input("\nEnter operation number from the menu")

                        if choice1 == "1":
                            Billing.Billing()
                        elif choice1 == "2":
                            Add_Prod.Add_Prod()
                        elif choice1 == "3":
                            Update_Prod.Update_Prod()
                        elif choice1 == "4":
                            Del_Prod.Del_Prod()
                        elif choice1 == "5":
                            Disp_Prod.Disp_Prod()
                        elif choice1 == "6":
                            break
                        else:
                            print("\nInvalid Choice")

                        proceed1 = input("\n\nDo you wish to proceed with another operation?(y/n):")

                        if proceed1 in "yY":
                            pass
                        else:
                            break

                elif choice_main == '2':
                    while True:
                        print(sysadmin_menu_2)
                        choice2 = input("\nEnter operation number from the menu")

                        if choice2 == "1":
                            Add_HSN_Code.Add_Code()
                        elif choice2 == "2":
                            Update_HSN_Code.Update_Code()
                        elif choice2 == "3":
                            Del_HSN_Code.Del_Code()
                        elif choice2 == "4":
                            Disp_HSN_Code.Disp_Code()
                        elif choice2 == "5":
                            break
                        else:
                            print("\nInvalid Choice")

                        proceed1 = input("\n\nDo you wish to proceed with another operation?(y/n):")

                        if proceed1 in "yY":
                            pass
                        else:
                            break

                elif choice_main == '3':
                    print("\nGoodbye!")
                    break

                else:
                    print("\nInvalid choice!")

                main_menu_choice = input("\nDo you want to continue with the manipulation of any other table(y/n)?:")

                if main_menu_choice in "yY":
                    pass
                else:
                    print("\nOkay!")

                    break

        else:
            print("\nIncorrect password")

    elif authority.lower() == "admin":
        choice_billing = input("\n\nDo you wish to start billing(y/n):")

        if choice_billing in "yY":
            while True:
                Billing.Billing()
                Billing_cnt = input("Do you wish to bill another set of items?(y/n):")

                if Billing_cnt in "yY":
                    pass
                else:
                    break

    else:
        print("\n\n**--** Access Denied **--**")

else:
    print("\nConnecting....")
    print("\nDatabase connection failed\n\nTry again")
