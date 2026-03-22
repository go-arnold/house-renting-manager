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


def main():
    while True:
        print("\n1. Add house")
        print("2. View houses")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_house()
        elif choice == "2":
            view_houses()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
