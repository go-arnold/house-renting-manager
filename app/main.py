from house import House

houses = []


def add_house():
    name = input("Enter house name: ")
    location = input("Enter location: ")
    price = float(input("Enter price: "))

    house = House(name, location, price)
    houses.append(house)

    print("House added successfully!")


def main():
    while True:
        print("\n1. Add house")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_house()
        elif choice == "2":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
