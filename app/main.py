from house import House
from logger import log_action


houses = []


def add_house():
    name = input("Enter house name: ")
    location = input("Enter location: ")
    price = float(input("Enter price: "))

    house = House(name, location, price)
    houses.append(house)
    log_action(f"Added house: {house.name}, {house.location}, {house.price}")

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
            log_action(f"Rented house: {house.name}, {house.location}, {house.price}")

    except (IndexError, ValueError):
        print("Invalid selection.")


def release_house():
    if not houses:
        print("No houses available.")
        return

    view_houses()
    try:
        choice = int(input("Enter house number to release: "))
        house = houses[choice - 1]
        if not house.is_rented:
            print("This house is already available.")
        else:
            house.release()
            print(f"{house.name} has been released successfully!")
            log_action(f"Relealed house: {house.name}, {house.location}, {house.price}")

    except (IndexError, ValueError):
        print("Invalid selection.")


def search_houses():
    location = input("Enter location to search (leave blank to skip): ")
    max_price = input("Enter max price (leave blank to skip): ")

    results = houses
    if location:
        results = [h for h in results if h.location.lower() == location.lower()]
    if max_price:
        try:
            max_price_val = float(max_price)
            results = [h for h in results if h.price <= max_price_val]
        except ValueError:
            print("Invalid price input")
            return

    if not results:
        print("No houses found.")
        return

    for i, house in enumerate(results):
        status = "Rented" if house.is_rented else "Available"
        print(f"{i+1}. {house.name} | {house.location} | {house.price} | {status}")


def show_available_houses():
    available = [h for h in houses if not h.is_rented]
    if not available:
        print("No available houses.")
        return

    for i, house in enumerate(available):
        print(f"{i+1}. {house.name} | {house.location} | {house.price}")


def main():
    while True:
        print("\n1. Add house")
        print("2. View houses")
        print("3. Rent house")
        print("4. Release house")
        print("5. Search houses")
        print("6. Show available houses")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_house()
        elif choice == "2":
            view_houses()
        elif choice == "3":
            rent_house()
        elif choice == "4":
            release_house()
        elif choice == "5":
            search_houses()
        elif choice == "6":
            show_available_houses()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
