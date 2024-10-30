import tools

while True:

    tools.show_menu()
    action_str = input("please enter cmd:")
    print("the cmd is [%s]" % action_str)

    if action_str in ["1", "2", "3"]:
        # Add business cards
        if action_str == "1":
            tools.add_business_cards()
        # Show all business cards
        elif action_str == "2":
            tools.show_all_business_cards()
        # Inquire business card
        elif action_str == "3":
            tools.inquire_business_card()
    # exit the system
    elif action_str == "0":
        print("Welcome again")
        break

    else:
        print("Input err")
        print("Please enter again")


