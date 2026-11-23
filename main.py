
def main():
    package, km_price = choose_package()
    trip_price = calculate_price(km_price)

def choose_package():
    uber_black = 2
    uber_van = 3.50
    uber_x = 1.50

    while True:
        print("-----------------------------------------------------")
        print("Welcome by Uber, choose your package")
        print(f"1. Uber Black                 €{uber_black:.2f}")
        print(f"2. Uber Van                   €{uber_van:.2f}")
        print(f"3. Uber X                     €{uber_x:.2f}")
        print("-----------------------------------------------------")
        program_choice = input("[1, 2, or 3]: ")
        if program_choice == "1":
            return "Uber Black", uber_black
        elif program_choice == "2":
            return "Uber Van", uber_van
        elif program_choice == "3":
            return "Uber X", uber_x
        else:
            print("Error (Invalid choice),")

def calculate_price(km_price):

    trip_price = km_price * distance
    print("-----------------------------------------------------")
    print(f"You have chosen the {program_choice} package.")
    print(f"The price per kilometer is €{km_price:.2f}.")
    distance = input("How many kilometers do you wish to travel: ")

    print("-----------------------------------------------------")
    print(f"")

def trip_price():
    None

main()
