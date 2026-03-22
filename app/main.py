from house import House

houses = []


def add_house():
    name = input("Enter house name: ")
    location = input("Enter location: ")
    price = float(input("Enter price: "))

    house = House(name, location, price)
    houses.append(house)

    print("House added successfully!")


def view_houses():
    if not houses:
        print("No houses available.")
        return

    for i, house in enumerate(houses):
        status = "Rented" if house.is_rented else "Available"
        print(f"{i + 1}. {house.name} | {house.location} | {house.price} | {status}")


def rent_house():
    if not houses:
        print("No houses available.")
        return

    view_houses()
    try:
        choice = int(input("Enter house number to rent: "))
        house = houses[choice - 1]
        if house.is_rented:
            print("This house is already rented.")
        else:
            house.rent()
            print(f"{house.name} has been rented successfully!")
    except (IndexError, ValueError):
        print("Invalid selection.")


def main():
    while True:
        print("\n1. Add house")
        print("2. View houses")
        print("3. Rent house")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_house()
        elif choice == "2":
            view_houses()
        elif choice == "3":
            rent_house()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
