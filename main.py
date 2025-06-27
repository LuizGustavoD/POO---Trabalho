from utils.menu_func import MenuFunc

menu = MenuFunc()

while True:
    menu.show_menu()
    menu.get_decision()
    if menu.options[int(menu.decision)][1] == "Encerrar programa":
        break
    menu.start_decision()