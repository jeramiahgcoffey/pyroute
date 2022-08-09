from controller import Controller


def clear():
    """'Clear' console by printing 100 blank lines"""

    print('\n' * 100)


def quit_app():
    """Quit application with exit code 0"""

    raise SystemExit(0)


def main():
    """
    Start application and UI. Contains main loop which gets user selections and calls the respective methods.

    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    """

    # Initialize Controller
    controller = Controller()

    should_start_day = input('WELCOME TO THE WGUPS ROUTING PROGRAM\n'
                             'ENTER Q TO QUIT, ENTER ANY OTHER KEY TO START DAY: ').lower() != 'q'

    # Starts routing if user doesn't quit
    if should_start_day:
        controller.start_day()
    else:
        quit_app()

    user_selection = None

    # Main loop which waits for user selection and calls the respective method on the controller
    while user_selection != 'q':
        user_selection = input('\nWhat would you like to do?\n'
                               ' 1. Get all package statuses at a specific time\n'
                               ' 2. Lookup a package by ID number\n'
                               ' 3. Lookup a truck by ID number\n'
                               ' 4. Get total distance traveled by all trucks\n'
                               ' 5. Get total time taken to deliver all packages\n'
                               ' Q. Quit the application\n'
                               'Enter option: ').lower()

        if user_selection == 'q':
            quit_app()

        # The next Controller method to be called is the return value of ui_options when the user selection is passed in
        next_function = ui_options(user_selection, controller)

        # Selections 1 - 3 have specific formatting checks and exception handling
        if user_selection == '1':
            clear()
            timestamp = None
            while timestamp is None or timestamp == '':
                timestamp = input('Enter time (format HH:MM, 24 hour time): ')

            try:
                next_function(timestamp)
            except ValueError:
                print('\nInvalid input, returning to main menu.\n')
            except IndexError:
                print('\nInvalid input, returning to main menu.\n')

        elif user_selection == '3':
            clear()
            truck_id = None
            while truck_id is None or truck_id == '':
                try:
                    truck_id = int(input('Enter the truck ID: '))
                except ValueError:
                    print('\nInvalid ID, try again.\n')
            try:
                next_function(truck_id)
            except AttributeError:
                print('\nInvalid ID, returning to main menu.')

        elif user_selection == '2':
            clear()
            package_id = None
            while package_id is None or package_id == '':
                try:
                    package_id = int(input('Enter the package ID: '))
                except ValueError:
                    print('\nInvalid ID, try again.\n')
            try:
                next_function(package_id)
            except AttributeError:
                print('\nInvalid ID, returning to main menu.\n')
        else:
            clear()
            next_function()


def ui_options(case, controller):
    """
    Take in user selection and return a method from the Controller to be called inside the main loop in start_app

    Time Complexity: O(1)
    Space Complexity: O(1)

    :param case: String. User selection received inside the main loop in start_app.
    :param controller: The application Controller.
    :return: A Controller method to be called inside the main loop in start_app.
    """

    try:
        return {
            '1': controller.print_all_statuses,
            '2': controller.print_package,
            '3': controller.print_truck,
            '4': controller.print_total_distance,
            '5': controller.print_total_time,
        }[case]
    except KeyError:
        print('Invalid Entry, Exiting...')
        quit_app()


# Start application
main()
