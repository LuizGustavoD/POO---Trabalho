from utils.menu_func import MenuFunc

menu = MenuFunc()
while True:
    menu.show_menu()
    decision = menu.get_decision()
    if decision == "0":
        break
    print("\n\n\n\n")
    menu.start_decision()