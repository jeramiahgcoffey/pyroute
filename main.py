from controller import Controller


def clear():
    print('\n' * 100)


def quit_app():
    raise SystemExit(0)


def start_app():
    should_start_day = input('WELCOME TO THE WGUPS ROUTING PROGRAM\n'
                             'ENTER Q TO QUIT, ENTER ANY OTHER KEY TO START DAY: ').lower() != 'q'

    if should_start_day:
        handler.start_day()
    else:
        quit_app()

    user_selection = None

    while user_selection != 'q':
        user_selection = input('\nWhat would you like to do?\n'
                               ' 1. Get all package statuses at a specific time\n'
                               ' 2. Lookup a package by ID number\n'
                               ' 3. Lookup a truck by ID number\n'
                               ' 4. Get total distance traveled by all trucks\n'
                               ' 5. Get total time taken to deliver all packages\n'
                               ' Q. Quit the application\n'
                               'Enter option: ').lower()

        next_function = ui_options(user_selection)

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


def ui_options(case):
    return {
        '1': handler.print_all_statuses,
        '2': handler.print_package,
        '3': handler.print_truck,
        '4': handler.print_total_distance,
        '5': handler.print_total_time,
        'q': quit_app
    }[case] or quit_app


handler = Controller()
start_app()
