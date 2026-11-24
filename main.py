
def main():
    """
    The main function houses the other functions that will be called throughout the program.
    :return: -
    """

    package, km_price = choose_package()
    trip_price, distance = calculate_price(package, km_price)
    trip_overview(trip_price, distance, package)

def choose_package():
    """
    The choose_package function visualizes the different packages and the price per kilometer per package.
    It will then request the user to choose a package.
    :return: Returns both the name of the chosen package and also the price per km that's associated with the chosen package.
    """

    # Price per km per package
    uber_black = 2
    uber_van = 3.50
    uber_x = 1.50

    while True:
        print("-----------------------------------------------------")
        print("Welcome by Uber, choose your package")
        print(f"1. Uber Black                         €{uber_black:.2f} per km.")
        print(f"2. Uber Van                           €{uber_van:.2f} per km.")
        print(f"3. Uber X                             €{uber_x:.2f} per km.")
        print("-----------------------------------------------------")
        program_choice = input("[1, 2, or 3]: ")
        if program_choice == "1":
            return "Uber Black", uber_black
        elif program_choice == "2":
            return "Uber Van", uber_van
        elif program_choice == "3":
            return "Uber X", uber_x
        else:
            print("Error (Invalid user input),")

def calculate_price(package, km_price):
    """
    The calculate_price function requests the distance that the user wishes to travel.
    It will then calculate the price of the trip based on the package the user has chosen.
    :param package: The package the user has chosen.
    :param km_price: The price per kilometer associated with the chosen package.
    :return: Returns the distance the user wishes to travel and the price of the trip based on the distance and chosen package.
    """

    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(f"You have chosen the {package} package.")
    print(f"The price per kilometer is €{km_price:.2f}.")
    while True:
        print("-----------------------------------------------------")
        print("The maximum distance is 250 kilometers.")
        distance = input("How many kilometers do you wish to travel: ")
        is_digit = False
        while is_digit == False:
            if distance.isdigit():
                distance = float(distance)
                is_digit = True
            else:
                print("Error (Invalid user input),")
                print("-----------------------------------------------------")
                distance = input("How many kilometers do you wish to travel: ")

        if distance < 1:
            print("Error [Invalid user input],")
        elif distance > 250:
            print("Error [Too great of a distance],")
        elif distance < 251:
            trip_price = distance * km_price
            return trip_price, distance

def trip_overview(trip_price, distance, package):
    """
    trip_overview shows the full overview of the trip, distance, cost and chosen package.
    It will then ask for a confirmation and close the program with an appropriate message.
    :param trip_price: Price of the distance based on the chosen package + distance the user has put in.
    :param distance: The distance the user wishes to travel.
    :param package: The package the user has chosen.
    :return: Exits the function so the program can end.
    """
        
    print(" ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------")
    print(f"A trip of {distance:.1f} km with the {package} package will cost €{trip_price:.2f}.")
    print("Do you wish to continue?")
    print("-----------------------------------------------------")
    valid_input = False
    while valid_input == False:
        trip_confirmation = input("[Type 'y' for Yes] & [Type 'n' for no]: ")
        trip_confirmation = trip_confirmation.lower()
        if trip_confirmation == "yes" or trip_confirmation == "y":
            print(" ")
            print(" ")
            print(" ")
            print("-----------------------------------------------------")
            print("You will arrive at your destination shortly.")
            print("Have a nice trip.")
            return
        elif trip_confirmation == "no" or trip_confirmation == "n":
            print(" ")
            print(" ")
            print(" ")
            print("-----------------------------------------------------")
            print("Uber ride cancelled.")
            print("Have a nice day.")
            return
        else:
            print("-----------------------------------------------------")
            print("Error [Invalid user input],")
            print("-----------------------------------------------------")

main()

# TODO Improve user experience.
# TODO Add comments to code + improve visualization.