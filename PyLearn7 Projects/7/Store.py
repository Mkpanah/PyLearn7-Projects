import qrcode

PRODUCTS = []


def read_from_database():
    file = open("database.txt", "r")

    for line in file:
        result = line.split(", ")

        my_dict = {"code": result[0], "name": result[1], "price": int(result[2]), "count": int(result[3].strip("\n"))}

        PRODUCTS.append(my_dict)

    file.close()


def write_to_database():
    print("Thanks For your Purchases. ")
    file = open("database.txt", "w")
    for i in range(len(PRODUCTS)):
        file.write(
            f"{PRODUCTS[i]['code']}, {PRODUCTS[i]['name']}, {PRODUCTS[i]['price']}, {PRODUCTS[i]['count']}\n")

    file.close()


def show_menu():
    print("__________________________________________")
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- Buy")
    print("7- QR Code Saving")
    print("8- Exit")
    print("__________________________________________")


def add():
    code = input("Enter code: ")
    name = input("Enter name: ")
    price = int(input("Enter price: "))
    count = int(input("Enter count: "))
    new_product = {
        "code": code,
        "name": name,
        "price": price,
        "count": count
    }
    PRODUCTS.append(new_product)


def edit():
    code = input("The code of the Desired Product: ")
    for product in PRODUCTS:
        if product["code"] == code:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            print("1 - Name of the Product")
            print("2 - Price of the Product")
            print("3 - Count of the Product")
            desired_field = int(input("Hold the Operation: "))

            if desired_field == 1:
                new_name = input("The Latest Name of the Product: ")
                product["name"] = new_name
                print("The Latest Information has been updated Successfully")
                break

            elif desired_field == 2:
                new_price = input("The Latest Price of the Product: ")
                product["price"] = new_price
                print("The Latest Information has been updated Successfully")
                break

            elif desired_field == 3:
                new_count = input("The Latest Count of the Product: ")
                product["count"] = new_count
                print("The Latest Information has been updated Successfully")
                break

    else:
        print("Not Found!!")


def remove():
    code = input("The code of the Desired Product: ")
    for i in range(len(PRODUCTS)):
        if code == PRODUCTS[i]["code"]:
            index = i
            del PRODUCTS[index]
            print("Removed Successfully.")
            break
    else:
        print("Unavailable Product")


def search():
    user_input = input("Type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("Not Found!!")


def show_list():
    print("Code\t\t Name\t\t Price \t\t Count")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"])


def buy():
    proceed = "y"
    purchased_value = 0
    purchased_objects = []
    purchased_quantity = []
    while proceed.lower() == "y":
        code = input("The Code of the Desired Product: ")
        for i in range(len(PRODUCTS)):
            if code == PRODUCTS[i]["code"]:
                quantity = int(input("How Much do you need? "))
                if quantity <= PRODUCTS[i]["count"]:
                    PRODUCTS[i]["count"] -= quantity
                    purchased_value = purchased_value + quantity * (PRODUCTS[i]["price"])
                    purchased_objects.append(PRODUCTS[i]["name"])
                    purchased_quantity.append(quantity)
                    print("Successfully Added to Purchase Basket.")
                    break
                print("Not Currently Available")
                break
        else:
            print("Not Available in Store")
            break
        proceed = input("Do you Want to Purchase More? (Y/N): ")
    for i in range(len(purchased_objects)):
        print(f"You have bought {purchased_quantity[i]} {purchased_objects[i]}.")
    print("The Total Expenditure is = ", purchased_value)


def qr_code_saver():
    code = input("The Code of the Desired Product: ")
    for i in range(len(PRODUCTS)):
        if code == PRODUCTS[i]["code"]:
            index = i
            img = qrcode.make(f"{PRODUCTS[index]['code']} | "
                              f"{PRODUCTS[index]['name']} | "
                              f"{PRODUCTS[index]['price']} | "
                              f"{PRODUCTS[index]['count']}")
            img.save("Product.jpg")
            print("Saved Successfully.")
            break
    else:
        print("Unavailable Product")


print("Welcome to Store")
print("Loading...")
read_from_database()
print("Data loaded.")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()

    elif choice == 2:
        edit()

    elif choice == 3:
        remove()

    elif choice == 4:
        search()

    elif choice == 5:
        show_list()

    elif choice == 6:
        buy()

    elif choice == 7:
        qr_code_saver()

    elif choice == 8:
        write_to_database()
        exit(0)

    else:
        print("Enter desired value")
