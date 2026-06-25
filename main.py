from system import RestaurantSystem

def main():
    system = RestaurantSystem()

    # Load menu from file
    system.load_menu_from_file()

    # Start interactive menu
    system.show_main_menu()

    # Save menu before exit
    system.save_menu_to_file()

if __name__ == "__main__":
    main()
