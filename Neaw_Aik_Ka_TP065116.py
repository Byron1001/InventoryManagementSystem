#Neaw Aik Ka
#TP065116

def initial_item_list_input():
        items = [
        ["Head cover", "HC","KAP", 0],
        ["Face shield", "FS", "MOD", 0],
        ["Mask", "MS", "MOD", 0],
        ["Gloves", "GL", "BES", 0],
        ["Gown", "GW", "MOD", 0],
        ["Shoe covers", "SC", "SFL", 0],
         ]
        print("System first start input:")
        print()
        for item in items:
                item_index = items.index(item)#store the index in variable
                supplier = open("suppliers.txt", "r")
                print(supplier.read())#read the file and print
                supplier.close()#close file
                while True:
                        print("Item: " + items[item_index][0])
                        supplier_code = input("Please enter item supplier code: ")#ask input of supplier code
                        supplier_code = supplier_code.strip(" ")#check the input
                        ans = check_supplier_code_input(supplier_code.upper())
                        if ans == True:
                                items[item_index][2] = supplier_code.upper()
                                break
                        else:
                                print("Please enter the valid supplier code.")#invalid supplier code leads to reentering
                                continue
                print("Item: " + items[item_index][0])
                while True:
                        try:
                                stock = int(input("Please enter the stock of item [in boxes]: "))#ask input of stock
                                if stock < 0:#check input
                                        print("Number of item stock can not less than 0.")#invalid stock leads to reentering
                                        continue
                        except:
                                print("Please enter number.")#invalid input leads to reentering
                                continue
                        break
                items[item_index][3] = stock #store the stock in variable
        print("Input successful!")
        item_write(items)#write the correction into file
        item = open("ppe.txt", "r")#open file
        print(item.read())#read the file
        return items

def check_supplier_code_input(supplier_code):
    supplier = open("suppliers.txt", "r")
    supplier_list = supplier.readlines()#append all lines into list
    supplier.close()#close the file
    supplier = []
    for line in supplier_list:
        if line.startswith("Supplier code: "):#append supplier code into a list
            a = line.split(":")
            a = a[1].strip()
            supplier.append(a)
    if supplier_code.upper() in supplier:#check the supplier code given at the start of function
            return True
    else:
            return False

def item_write(items_list):
    ppe_file = open("ppe.txt", "w")
    for item in items_list:#write the txt file with items list
        ppe_file.write("Item: " + item[0] + "\n")
        ppe_file.write("Item code: " + item[1] + "\n")
        ppe_file.write("Supplier code: " + item[2] + "\n")
        ppe_file.write("Stock: " + str(item[3]) + " boxes\n\n")
    ppe_file.close()

def initial_supplier_detail():
    suppliers = [#store initial data in this function
        ["KAP Safety Supplies(M)Sdn Bhd", "KAP", "03-80621760", "11,Jalan TPP 1/1,Taman Perindustrian Puchong,47100 Puchong,Selangor."],
        ["MODESCO Sdn Bhd", "MOD", "03-3332333", "25-2,Jalan Simfoni 1 Balakong,43300 Seri Kembangan,Selangor."],
        ["Safetylab Sdn Bhd", "SFL", "03-89254088", "26 GF,Jalan 15/1f,Seksyen 15,43650 Bandar Baru Bangi,Selangor."],
        ["Blue Eagle Safety International Sdn Bhd", "BES", "03-38853237", "No.19,Jalan Bayi Tinggi 2,KS6,Batu Unjur,41200 Klang Selangor."],
                        ]
    return suppliers

def supplier_write(suppliers_list):
    supplier_file = open("suppliers.txt", "w")
    for supplier in suppliers_list:#write txt file with supplier list given
        supplier_file.write("Supplier name: " + supplier[0] + "\n")
        supplier_file.write("Supplier code: " + supplier[1] + "\n")
        supplier_file.write("Tel.No: " + supplier[2] + "\n")
        supplier_file.write("Address: " + supplier[3] + "\n\n")
    supplier_file.close()

def check_item_code_input(item_code):
    item = open("ppe.txt", "r")
    item_list = item.readlines()#append all lines to a list
    item.close()
    item = []
    for line in item_list:
        if line.startswith("Item code: "):
            b = line.split(":")
            b = b[1].strip()
            item.append(b)#append all item code into a list
    if item_code.upper() in item:#check the item code
            return True
    else:
            return False

def latest_items_list():
        item_details = []
        ppe = open("ppe.txt", "r")
        ppe_list = ppe.readlines()#append all lines in txt file into a list
        for line in ppe_list:
            if line != "\n":#append all data into a list
                if line.startswith("Stock: "):# clear the prefix and surfix written in txt file
                    line = line.strip(" boxes\n")
                info = line.split(":")
                info = info[1].strip()
                info = info.strip("\n")
                if info.isdigit() == True:
                        info = int(info)
                item_details.append(info)
                index = 0
                item = []
        for x in item_details:#append data of each item into a list
                if index < len(item_details):
                        item.append(item_details[index:index+4])
                        index += 4
        return item

def item_print(index, items_list):# print the item details
        print("Item: " + items_list[index][0])
        print("Item code: " + items_list[index][1])
        print("Supplier code: " + items_list[index][2])
        print("Stock: " + str(items_list[index][3]) + " boxes")

def add_item_stock(items_list, add, hospitals_list):
        while True:
                item_code = input("Please enter the item code [-1 to cancel]: ")
                item_code = item_code.strip(" ")
                if item_code == "-1":
                        item_menu()#go back to main menu if user wish to do it
                b = check_item_code_input(item_code.upper())#check the item code
                if b == False:
                        print("Please enter valid item code.")#invalid input leads to reentering
                        continue
                else:
                        break
        for item in items_list:
                if item_code.upper() == item[1]:
                    item_index = items_list.index(item)#store item index
                    supplier_code = items_list[item_index][2]#store supplier code
                    print("Current item stock: " + str(item[3]) + " Boxes")
                    print("Only stock in boxes is accepted.")
                    if add == "add":#identify the request of add stock
                            while True:
                                    try:
                                            add_stock = int(input("Please enter the receiving item stock [in boxes] [-1 to cancel]: "))
                                            if add_stock == -1:
                                                    item_menu()
                                            elif add_stock <= 0:
                                                    print("Receiving stock can not be 0 or less than 0.")#invalid input leads to reentering
                                                    continue
                                    except:
                                            print("Only number is accepted.")#invalid input leads to reentering
                                            continue
                                    break
                            for item in items_list:
                                    if item_code.upper() == item[1]:
                                            item_index = items_list.index(item)#store the item index
                                            stock = int(items_list[item_index][3]) + int(add_stock)#count for new stock
                                            items_list[item_index][3] = stock#store the new stock
                            print("Stock adding successful!")
                            record_append(item_code.upper(), None, supplier_code.upper(), add_stock)#record the adding
                            amount_check(item_code.upper(), supplier_code.upper(), "receive from", add_stock)#merge the same amount of adding
                    elif add == "distribute":#identify the request of distribute stock
                                while True:
                                        hospital_code = input("Please enter the hospital code [-1 to cancel]: ")#ask for the hospital code
                                        hospital_code = hospital_code.strip(" ")
                                        if hospital_code == "-1":
                                                item_menu()#go back if user wish to do it
                                        d = check_hospital_code_input(hospital_code.upper())#check the hospital code
                                        if d == False:
                                            print("Please enter the existing hospital code.")#invalid input leads to reentering
                                            continue
                                        else:
                                            break
                                for hospital in hospitals_list:
                                        if hospital_code.upper() == hospital[1]:
                                                hospital_get = hospital[1]#store the hospital get stock
                                print("Item: " + items_list[item_index][0])#print item's details
                                print("Item code: " + items_list[item_index][1])
                                print("Supplier code: " + items_list[item_index][2])
                                print("Current stock: " + str(items_list[item_index][3]) + " boxes")
                                stock = int(items_list[item_index][3])#store the stock of item in variable
                                while True:
                                    try:# ask distribute amount from user
                                        distribute = int(input("Please enter the distribute item amount [in boxes][-1 to cancel]: "))
                                        if distribute == -1:
                                                item_menu()#go back if user wish to do so
                                        elif distribute <= 0:#check the stock amount whether it is enough
                                                    print("Distribute stock can not be 0 or less than 0.")
                                                    continue
                                        elif distribute > stock:
                                                print("Stock insufficient for distribution.")
                                                print("""
Please choose your action:
Reenter amount distributed\tPress 1
Back to main menu\t\tPress 2
""")
                                                while True:#if not enough stock, consider to reenter amount or go back
                                                        try:
                                                                choice = int(input("Please enter your choice: "))
                                                                if choice != 1 and choice != 2:
                                                                        print("Please enter the given number.")
                                                                        continue
                                                        except:
                                                                print("Please enter the given number.")
                                                                continue
                                                        break
                                                if choice == 1:
                                                        continue
                                                elif choice == 2:
                                                        main_menu()
                                    except:
                                            print("Only number is accepted.")
                                            continue
                                    break
                                for item in items_list:
                                    if item_code.upper() == item[1]:
                                            item_index = items_list.index(item)#store the item index
                                            stock = int(items_list[item_index][3]) - int(distribute)#store the item stock after ditribution
                                items_list[item_index][3] = stock
                                print("Distribution processed successful!")
                                record_append(item_code.upper(), hospital_code.upper(), None, distribute)#record the distribution
                                amount_check(item_code.upper(), hospital_code.upper(), "distribute to", distribute)#check and merge for the same amount of distribution
                    elif add == "change":
                            while True:
                                    try:#ask the new stock from user
                                        change = int(input("Please enter the right item stocks [in boxes] [-1 to cancel]: "))
                                        if change == -1:#go back if user wish to do so
                                                main_menu()
                                        elif change < 0:
                                                    print("Stock can not less than 0.")#invalid input leads to reentering
                                                    continue
                                    except:
                                            print("Only number is accepted.")
                                            continue
                                    break
                            for item in items_list:
                                    if item_code.upper() == item[1]:
                                            item_index = items_list.index(item)#store item index
                                            items_list[item_index][3] = change#change item stock
                            print("Stock changed successful!")
        item_write(items_list)#rewrite the txt file
        print()
        item_print(item_index, items_list)#print item's new details
        item_menu()#back to item menu

def change_item_supplier(items_list,suppliers_list):
    while True:#ask the item code from user
        item_code = input("Please enter the item code [-1 to cancel]: ")
        item_code = item_code.strip(" ")
        if item_code == "-1":
                item_menu()#go back if user wish to do so
        b = check_item_code_input(item_code.upper())#check the input
        if b == False:
            print("Please enter valid item code.")#invalid input leads to reentering
            continue
        else:
            break
    for item in items_list:
        if item_code.upper() == item[1]:
            item_index = items_list.index(item)#store the item index
            while True:
                    print("Current supplier: " + item[2])
                    print("Only existing suppliers is accepted.")
                    while True:#ask new supplier of item from user
                        new_supplier = input("Please enter the new supplier code [-1 to cancel]: ")
                        new_supplier = new_supplier.strip(" ")
                        if new_supplier == "-1":
                                item_menu()#go back if user wish to do so
                        c = check_supplier_code_input(new_supplier.upper())#check the input
                        if c == False:
                            print("Please enter existing supplier code.")#invalid input leads to reentering
                            continue
                        else:
                                break
                    for supplier in suppliers_list:
                            if new_supplier.upper() == supplier[1]:
                                    items_list[item_index][2] = new_supplier.upper()#change to new supplier
                    break
            item_write(items_list)#rewrite the txt file
            print("Supplier changed succesfully.")
            print()
            item_print(item_index, items_list)#print new details of item
            item_menu()#back to item menu

def latest_suppliers_list():
    supplier_details = []
    supplier = open("suppliers.txt", "r")
    detail_list = supplier.readlines()#append all lines into a list
    for detail in detail_list:
        if detail != "\n":#get data of supplier and append into a list
            element = detail.split(":")
            element = element[1].strip()
            element = element.strip("\n")
            supplier_details.append(element)
            num = 0
            supplier = []
    for x in supplier_details:
        if num < len(supplier_details):#append data of each supplier into another list
            supplier.append(supplier_details[num:num+4])
            num += 4
    return supplier

def ascending_item_code(items_list):
        asc = []
        for item in items_list:#append the item's name into a list
                asc.append(item[1])
        asc.sort()#sort the list according to item name
        for x in range(len(asc)):
            item_code = asc[x]
            print()
            index = 0
            while True:#print item's details according to ascending item name
                if item_code == items_list[index][1]:
                        print("Item: " + items_list[index][0])
                        print("Item code: " + items_list[index][1])
                        print("Supplier code: " + items_list[index][2])
                        print("Stock: " + str(items_list[index][3]) + " boxes")
                else:
                        index += 1
                        continue
                break
        item_menu()#back to item menu

def low_stock_item(items_list):
        print("Item stock less than 25 boxes: ")
        print()
        flag = 0
        for item in items_list:
                stock = int(item[3])#identify the stock of items
                if stock < 25:#print the low stock items
                        print("Item: " + item[0])
                        print("Item code: " + item[1])
                        print("Supplier code: " + item[2])
                        print("Stock: " + str(item[3]) + " boxes")
                        print()
                        flag = 1
        if flag == 0:#print when there is no low stock items
            print("No item less than 25 boxes.")
        item_menu()# back to item menu
            
def item_menu():
        print("""
What you wish to do next?
Edit wrong item stock\t\t\tPress 1
Change item supplier\t\t\tPress 2
Check item stock(ascending by item code)\tPress 3
Check low stock items\t\t\tPress 4
Receive items\t\t\t\tPress 5
Distribute items\t\t\t\tPress 6
Check item distribution and receive record\tPress 7
Clear record\t\t\t\tPress 8
Back to main menu\t\t\t\tPress 9
""")
        while True:
                try:#ask for the user's choice
                        choice = int(input("Please enter the given number: "))
                        if choice > 9 or choice < 1:#check the input
                                print("Please enter valid number.")#invalid input leads to reentering
                                continue
                except:
                        print("Please enter valid number.")
                        continue
                break
        if choice == 1:#goes to particular function based on user's choice
                add_item_stock(latest_items_list(),"change", latest_hospital_list())
        elif choice == 2:
                change_item_supplier(latest_items_list(), latest_suppliers_list())
        elif choice == 3:
                ascending_item_code(latest_items_list())
        elif choice == 4:
                low_stock_item(latest_items_list())
        elif choice == 5:
                add_item_stock(latest_items_list(),"add", latest_hospital_list())
        elif choice == 6:
                add_item_stock(latest_items_list(),"distribute", latest_hospital_list())
        elif choice == 7:
                while True:#check the record based on item code
                        item_code = input("Please enter the item code [-1 to cancel]: ")
                        item_code = item_code.strip(" ")
                        if item_code == "-1":
                                item_menu()#go back if user wish to do so
                        b = check_item_code_input(item_code.upper())
                        if b == False:
                                print("Please enter valid item code.")#invalid input leads to reentering
                                continue
                        else:
                                break
                item_record_check(item_code.upper())
        elif choice == 8:#overwrite the txt file with nothing
                dis = open("distribution.txt", "w")
                dis.close()
                print("Record clear successfully.")
                item_menu()#back to item menu
        elif choice == 9:
                main_menu()#back to main menu

def initial_hospital_detail():
    hospitals = [#store the initial hospital details
        ["General hospital Kuala Lumpur", "GHK", "03-26155555","Jalan Pahang,50586 Kuala Lumpur,Wilayah Persekutuan Kuala Lumpur."],
        ["Pantai hospital Kuala Lumpur", "PHK", "03-91452888", "1,Jalan 1/96a,Taman Cheras Mahmur,56100 Kuala Lumpur,Wilayah Persekutuan Kuala Lumpur."],
        ["Columbia Asia hospital", "CAH", "03-79499999", "Lot 69,13 Jalan 13/6,Seksyen 13,46200 Petaling Jaya,Selangor."],
        ["Ampang specialist hospital", "ASH", "03-42895000", "1,Jalan Mamanda 9,Taman Dato Ahmad Razali,68000 Ampang,Selangor."],
        ]
    return hospitals

def hospital_print(index, hospitals_list):#print the details of hospitals
        print("Hospital name: " + hospitals_list[index][0])
        print("Hospital code: " + hospitals_list[index][1])
        print("Tel.No: " + hospitals_list[index][2])
        print("Address: " + hospitals_list[index][3])

def hospital_write(hospitals_list):#rewrite the hospital detials
    hospital_file = open("hospitals.txt", "w")
    for detail in hospitals_list:
        hospital_file.write("Hospital name: " + detail[0] + "\n")
        hospital_file.write("Hospital code: " + detail[1] + "\n")
        hospital_file.write("Tel.No: " + detail[2] + "\n")
        hospital_file.write("Address: " + detail[3] + "\n\n")
    hospital_file.close()

def change_hospital_name(hospitals_list):
    while True:#ask hospital code from user
        hospital_code = input("Please enter the hospital code [-1 to cancel]: ")
        hospital_code = hospital_code.strip(" ")
        if hospital_code == "-1":
                hospital_menu()#go back if user wish to do so
        d = check_hospital_code_input(hospital_code)#check the input
        if d == False:
            print("Please enter the existing hospital code.")#invalid input leads to reentering
            continue
        else:
            break
    for hospital in hospitals_list:
        if hospital_code.upper() == hospital[1]:
            hospital_index = hospitals_list.index(hospital)#store the data index
            print("Current hospital name: " + hospital[0])
            while True:#ask the new hospital name from user
                    new_hospital_name = input("Please enter the new hospital name [colon is not accepted] [-1 to cancel]: ")
                    new_hospital_name = new_hospital_name.strip(" ")
                    import string
                    new_hospital_name = new_hospital_name.strip(string.punctuation)
                    if new_hospital_name == "-1":
                            hospital_menu()#go back if user wish to do so
                    elif new_hospital_name == "" or new_hospital_name.isdigit() == True:#invalid input leads to reentering
                            print("New hospital name can not be space and number only or nothing.")
                            continue
                    check = check_colon(new_hospital_name)#check for colon in input
                    if check == True:
                            print("Colon is not accepted.")#invalid input leads to reentering
                            continue
                    else:
                            break
            hospitals_list[hospital_index][0] = new_hospital_name
            hospital_write(hospitals_list)#rewrite the new hospital details
            print("Hospital name changed succesfully.")
            print()
            hospital_print(hospital_index, hospitals_list)#print the new hospital details
            hospital_menu()#back to hospital menu

def change_hospital_tel(hospitals_list):
    while True:#ask hospital code from user
        hospital_code = input("Please enter the hospital code [-1 to cancel]: ")
        hospital_code = hospital_code.strip(" ")
        if hospital_code == "-1":
                hospital_menu()#go back if user wish to do so
        d = check_hospital_code_input(hospital_code)#check the input
        if d == False:
            print("Please enter the existing hospital code.")#invalid input leads to reentering
            continue
        else:
            break
    for hospital in hospitals_list:
        if hospital_code.upper() == hospital[1]:
            hospital_index = hospitals_list.index(hospital)#store the data index
            print("Current Tel.No: " + hospital[2])
            print("Only number is accepted.")
            while True:
                try:#ask new hospital tel.no from user
                        new_hospital_tel = int(input("Please enter the new hospital tel.no [not less than 4 digits] [-1 to cancel]: "))
                        if new_hospital_tel == -1:
                                hospital_menu()#go back if user wish to do so
                        elif len(str(new_hospital_tel)) < 4:#check the input of user
                                print("Tel.No cannot less than 4 digits.")#invalid input leads to reentering
                                continue
                except:
                        print("Only number is accepted.")
                        continue
                break
            new_hospital_tel = str(new_hospital_tel)
            hospitals_list[hospital_index][2] = str(new_hospital_tel[:2]) + "-" + str(new_hospital_tel[2:])
            new_hospitals_list = hospitals_list
            hospital_write(new_hospitals_list)#change details with new data
            print("Hospital tel changed succesfully.")
            print()
            hospital_print(hospital_index, new_hospitals_list)#print the new details of hospital
            hospital_menu()#back to hospital menu

def change_hospital_address(hospitals_list):
    while True:#ask hospital code from user
        hospital_code = input("Please enter the hospital code [-1 to cancel]: ")
        hospital_code = hospital_code.strip(" ")
        if hospital_code == "-1":
                hospital_menu()#go back if user wish to do so
        d = check_hospital_code_input(hospital_code)#check the input
        if d == False:#invalid input leads to reentering
            print("Please enter the existing hospital code.")
            continue
        else:
            break
    for hospital in hospitals_list:
        if hospital_code.upper() == hospital[1]:
            hospital_index = hospitals_list.index(hospital)#store the data index
            print("Current hospital address: " + hospital[3])
            while True:#ask new hospital address from user
                    new_hospital_address = input("Please enter the new hospital address [colon is not accepted] [-1 to cancel]: ")
                    new_hospital_address = new_hospital_address.strip(" ")
                    import string
                    new_hospital_address = new_hospital_address.strip(string.punctuation)
                    if new_hospital_address == "-1":
                            hospital_menu()#go back if user wish to do so
                    elif new_hospital_address == "" or new_hospital_address.isdigit() == True:#check the input
                            print("New hospital address can not be space and number only or nothing.")
                            continue #invalid input leads to reentering
                    check = check_colon(new_hospital_address)
                    if check == True:
                            print("Colon is not accepted.")
                            continue
                    else:
                            break
            hospitals_list[hospital_index][3] = new_hospital_address
            hospital_write(hospitals_list)#write the new data into the list
            print("Hospital address changed succesfully.")
            print()
            hospital_print(hospital_index, hospitals_list)#print the new hospital details
            hospital_menu()#back to hospital menu


def latest_hospital_list():
    hospital_details = []
    hospital = open("hospitals.txt", "r")
    line_list = hospital.readlines()#append all lines into a list
    for line in line_list:
        if line != "\n":
            index_num = line_list.index(line)#store the index of data
            element = line.split(":")
            element = element[1].strip()
            element = element.strip("\n")
            hospital_details.append(element)#append the data into a list
            num = 0
            hospital = []
    for x in hospital_details:
        if num < len(hospital_details):#append data of each hospital to a list
            hospital.append(hospital_details[num:num+4])
            num += 4
    return hospital

def check_hospital_code_input(hospital_code):
    hospital = open("hospitals.txt", "r")
    hospital_list = hospital.readlines()#append all lines into a list
    hospital.close()
    hospital = []
    for line in hospital_list:
        if line.startswith("Hospital code: "):
            d = line.split(":")
            d = d[1].strip()
            hospital.append(d)#append target data into a list
    if hospital_code.upper() in hospital:#check the validation of given hospital code
            return True
    else:
            return False

def hospital_menu():
    print("""
What you wish to do next?
Edit hospital name\t\tPress 1
Edit hospital Tel.No\t\tPress 2
Edit hospital address\tPress 3
Check hospital list\t\tPress 4
Back to main menu\t\tPress 5
""")
    while True:
        try:#ask the choice of user
            choice = int(input("Please enter the given number: "))
            if choice != 1 and choice != 2 and choice != 3 and choice !=4 and choice != 5:#check the input
                print("Please enter valid number.")#invalid input leads to reentering
                continue
        except:
            print("Please enter valid number.")
            continue
        break
    if choice == 1:#go to particular function based on user's choice
        change_hospital_name(latest_hospital_list())
    elif choice == 2:
        change_hospital_tel(latest_hospital_list())
    elif choice == 3:
        change_hospital_address(latest_hospital_list())
    elif choice == 4:
        hospital = open("hospitals.txt", "r")
        print(hospital.read())#print all details of hospitals
        hospital_menu()
    elif choice == 5:
        main_menu()#back to main menu

def supplier_print(index, suppliers_list):#print the details of supplier
        print("Supplier name: " + suppliers_list[index][0])
        print("Supplier code: " + suppliers_list[index][1])
        print("Tel.No: " + suppliers_list[index][2])
        print("Address: " + suppliers_list[index][3])

def change_supplier_name(suppliers_list):
    while True:#ask supplier code from user
        supplier_code = input("Please enter the supplier code [-1 to cancel]: ")
        supplier_code = supplier_code.strip(" ")
        if supplier_code == "-1":
                supplier_menu()#go back if the user wish to do so
        d = check_supplier_code_input(supplier_code)#check the input
        if d == False:
            print("Please enter the existing supplier code.")
            continue#invalid input leads to reentering
        else:
            break
    for supplier in suppliers_list:
        if supplier_code.upper() == supplier[1]:
            supplier_index = suppliers_list.index(supplier)#store the supplier index
            print("Current supplier name: " + supplier[0])
            while True:#ask the user for new supplier name
                    new_supplier_name = input("Please enter the new supplier name [colon is not accepted] [-1 to cancel]: ")
                    new_supplier_name = new_supplier_name.strip(" ")
                    import string
                    new_supplier_name = new_supplier_name.strip(string.punctuation)
                    if new_supplier_name == "-1":
                            supplier_menu()#go back if user wish to do so
                    elif new_supplier_name == "" or new_supplier_name.isdigit() == True:
                            print("New supplier name can not be space and number only or nothing.")
                            continue #invalid input leads to reentering
                    check = check_colon(new_supplier_name)
                    if check == True:
                            print("Colon is not accepted.")
                            continue
                    else:
                            break
            suppliers_list[supplier_index][0] = new_supplier_name#overwrite the detail changed
            supplier_write(suppliers_list)#overwrite the txt file
            print("Supplier name changed succesfully.")
            print()
            supplier_print(supplier_index, suppliers_list)#print the new supplier detail
            supplier_menu()#go back to supplier menu

def change_supplier_tel(suppliers_list):
    while True:#ask the supplier code from user
        supplier_code = input("Please enter the supplier code [-1 to cancel]: ")
        supplier_code = supplier_code.strip(" ")
        if supplier_code == "-1":
                supplier_menu()#go back if user wish to do so
        d = check_supplier_code_input(supplier_code)#check the input
        if d == False:#invalid input leads to reentering
            print("Please enter the existing supplier code.")
            continue
        else:
            break
    for supplier in suppliers_list:
        if supplier_code.upper() == supplier[1]:
            supplier_index = suppliers_list.index(supplier)#store the index of supplier
            print("Current tel.no: " + supplier[2])
            print("Only number is accepted.")
            while True:
                try:#ask the new supplier tel from user
                    new_supplier_tel = int(input("Please enter the new supplier Tel.No [not less than 4 digits] [-1 to cancel]: "))
                    if new_supplier_tel == -1:
                            supplier_menu()#go back if user wish to do so
                    elif len(str(new_supplier_tel)) < 4:#check the input
                            print("Tel.No cannot less than 4 digits.")
                            continue #invalid input leads to reentering
                except:
                    print("Only number is accepted.")
                    continue
                break
            new_supplier_tel = str(new_supplier_tel)#store the new supplier tel in variable
            suppliers_list[supplier_index][2] = str(new_supplier_tel[:2]) + "-" + str(new_supplier_tel[2:])
            supplier_write(suppliers_list)#write the new data into txt file
            print("Supplier tel changed succesfully.")
            print()
            supplier_print(supplier_index, suppliers_list)#print the new data
            supplier_menu()#go back to supplier menu

def change_supplier_address(suppliers_list):
    while True:#ask supplier code from user
        supplier_code = input("Please enter the supplier code [-1 to cancel]: ")
        supplier_code = supplier_code.strip(" ")
        if supplier_code == "-1":
                supplier_menu()#go back if user wish to do so
        d = check_supplier_code_input(supplier_code)#check the input
        if d == False: #invalid input leads to reentering
            print("Please enter the existing supplier code.")
            continue
        else:
            break
    for supplier in suppliers_list:
        if supplier_code.upper() == supplier[1]:
            supplier_index = suppliers_list.index(supplier)#store the index of supplier
            print("Current supplier address: " + supplier[3])
            while True:#ask the new supplier address from user
                    new_supplier_address = input("Please enter the new supplier address [colon is not accepted] [-1 to cancel]: ")
                    new_supplier_address = new_supplier_address.strip(" ")
                    import string
                    new_supplier_address = new_supplier_address.strip(string.punctuation)
                    if new_supplier_address == "-1":
                            supplier_menu()#go back if user wish to do so
                    elif new_supplier_address == "" or new_supplier_address.isdigit() == True:
                            print("New supplier address can not be space and number only or nothing.")
                            continue  #invalid input leads to reentering
                    check = check_colon(new_supplier_address)
                    if check == True:
                            print("Colon is not accepted.")
                            continue
                    else:
                            break
            suppliers_list[supplier_index][3] = new_supplier_address#store the new data
            new_suppliers_list = suppliers_list
            supplier_write(new_suppliers_list)#overwrite txt file with new data
            print("Supplier address changed succesfully.")
            print()
            supplier_print(supplier_index, new_suppliers_list)#print new supplier details
            supplier_menu()#back to supplier menu

def supplier_menu():
    print("""
What you wish to do next?
Edit supplier name\t\tPress 1
Edit supplier Tel.No\t\tPress 2
Edit supplier address\tPress 3
Check supplier list\t\tPress 4
Back to main menu\t\tPress 5
""")
    while True:
        try:#get the choice from user
            choice = int(input("Please enter the given number: "))#check the input
            if choice != 1 and choice != 2 and choice != 3 and choice !=4 and choice != 5:
                print("Please enter valid number.")
                continue #invalid input leads to reentering
        except:
            print("Please enter valid number.")
            continue
        break
    if choice == 1:#go to particular function based on user's choice
        change_supplier_name(latest_suppliers_list())
    elif choice == 2:
        change_supplier_tel(latest_suppliers_list())
    elif choice == 3:
        change_supplier_address(latest_suppliers_list())
    elif choice == 4:
        supplier = open("suppliers.txt", "r")
        print(supplier.read())#print the supplier details
        supplier_menu()#go back to supplier menu
    elif choice == 5:
        main_menu()#go back to main menu

def record_append(item_code , hospital_code, supplier_code, num_dis):
    dis = open("distribution.txt", "a")
    import datetime
    now = str(datetime.datetime.now())#store the current time into variable
    if hospital_code == None:
        status = "receive from"#state the status of request and assign value to a
        a = str(now[:-7]) + "\t" + str(item_code) + "\t" + str(status) + "\t" + str(supplier_code) + "\t"+ str(num_dis) + " boxes\n"
    elif supplier_code == None:
        status = "distribute to"
        a = str(now[:-7]) + "\t" + str(item_code) + "\t" + str(status) + "\t" + str(hospital_code) + "\t"+ str(num_dis) + " boxes\n"
    dis.write(a)# append new data to txt file
    print(a)#print the new data
    dis.close()

def amount_check(item, hos_sup, status_input, num):
    dis = open("distribution.txt", "r")
    dis_list = dis.readlines()#append all lines into a list
    if dis_list != []:
        num_dis = dis_list[-1].split("\t")
        time = num_dis[0]# assign the time,status and status code into variable
        item_code = num_dis[1]
        status = num_dis[2]
        hos_sup_code = num_dis[3]
        num_dis = num_dis[4].split(" ")#identify the amount of distribution
        num_dis = int(num_dis[0].strip())
        if item == item_code and hos_sup == hos_sup_code and status_input == status:
            num_dis += num#calculate the total amount of two records
        dis_list[-1] = str(time) + "\t" + str(item_code) + "\t" + str(status) + "\t" + str(hos_sup_code) + "\t"+ str(num_dis) + " boxes\n"
        dis.close()
        dis = open("distribution.txt", "w")
        dis.writelines(dis_list)#overwrite txt file with new data
        dis.close()

def item_record_check(item_code):
    dis = open("distribution.txt", "r")
    dis_list = dis.readlines()#append all lines into a list
    for record in dis_list:
        info = record.split("\t")
        if info[1] == item_code:# check the record with item code
            print(record.strip("\n"))
    item_menu()#back to item menu

def check_colon(var):
        colon = False
        for x in var:#check if there is colon in the variable
                if x == ":":
                        colon = True
        return colon

def main_menu():
        print("""
>>>>>System Menu<<<<<

Edit items details(stock, info and record)\tPress 1
Edit supplier details\t\t\t\tPress 2
Edit about hospital details\t\t\tPress 3
Restart whole system\t\t\tPress 4
Exit system\t\t\t\tPress 5
""")
        while True:
                try:#ask choice from user
                        choice = int(input("Please enter your choice: "))
                        if choice < 1 or choice > 5:#check the input
                                print("Please enter the given number.")
                                continue #invalid input leads to reentering
                except:
                        print("Please enter the given number.")
                        continue
                break
        if choice == 1:# go to particular function based on user's choice
                item_menu()
        elif choice == 2:
                supplier_menu()
        elif choice == 3:
                hospital_menu()
        elif choice == 4:
                hospital_write(initial_hospital_detail())#overwrite the txt file
                supplier_write(initial_supplier_detail())
                dis = open("distribution.txt", "w")# clear the distribution file
                dis.close()
                initial_item_list_input()#input the initial settings
                main_menu()#go to main menu
        elif choice == 5:
                exit()#exit from system


def start_program():
        print("""
Do you want to reset the whole system?
Yes\t Press 1
No\t Press 2
        """)
        while True:
                try:# ask choice of user
                        choice = int(input("Please enter your choice: "))
                        if choice != 1 and choice != 2:# check the input
                                print("Please enter the given number.")
                                continue
                except:
                        print("Please enter the given number.")
                        continue
                break
        if choice == 1:# confirmation for restarting
                print("Restart system cannot cancel or redo.")
                print("Double confirm for restarting by enter 0.")
                while True:
                        try:#get confirmation from user
                                nd = int(input("Please confirm for restarting [-1 to cancel]:"))
                                if nd != -1 and nd != 0:#check the input
                                        print("Please enter given number.")
                                        continue
                        except:
                                print("Please enter given number.")
                                continue
                        break
                if nd == 0:#restarting confirmed
                        print("Initial settings start.")
                        hospital_write(initial_hospital_detail())
                        supplier_write(initial_supplier_detail())
                        dis = open("distribution.txt", "w")
                        dis.close()
                        initial_item_list_input()
                elif nd == -1:# restarting cancelled
                        print("Restarting cancelled.")
                        return start_program()# go back to the start of program
        else:
                pass
        main_menu()# go to main menu

start_program()
