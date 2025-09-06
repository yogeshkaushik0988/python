# list_manipulation.py

def display_menu():
    print("\nList Manipulation Menu:")
    print("1. Add item to list")
    print("2. Insert item at index")
    print("3. Remove item from list")
    print("4. Pop item at index")
    print("5. Sort list")
    print("6. Reverse list")
    print("7. Search for item")
    print("8. Display list")
    print("9. Exit")


def main():
    my_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            item = input("Enter item to add: ")
            my_list.append(item)
            print("Item added.")
        
        elif choice == '2':
            item = input("Enter item to insert: ")
            index = int(input("Enter index: "))
            if 0 <= index <= len(my_list):
                my_list.insert(index, item)
                print("Item inserted.")
            else:
                print("Invalid index.")

        elif choice == '3':
            item = input("Enter item to remove: ")
            if item in my_list:
                my_list.remove(item)
                print("Item removed.")
            else:
                print("Item not found in the list.")

        elif choice == '4':
            index = int(input("Enter index to pop: "))
            if 0 <= index < len(my_list):
                popped = my_list.pop(index)
                print(f"Popped item: {popped}")
            else:
                print("Invalid index.")

        elif choice == '5':
            my_list.sort()
            print("List sorted.")

        elif choice == '6':
            my_list.reverse()
            print("List reversed.")

        elif choice == '7':
            item = input("Enter item to search: ")
            if item in my_list:
                index = my_list.index(item)
                print(f"Item found at index {index}")
            else:
                print("Item not found.")

        elif choice == '8':
            print("Current List:", my_list)

        elif choice == '9':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
