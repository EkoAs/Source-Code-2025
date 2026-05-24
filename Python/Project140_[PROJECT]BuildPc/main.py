import DATA as DATA
from DATA.VIEW import UserMenu as Menu
import os
sistem = os.name

if __name__ == "__main__":
    while(True):
        match sistem:
            case "nt": os.system("cls")
            case "posix": os.system("clear")
        menu = Menu()
        menu.menu_User()
        done = input("\nIngin Exit? (y/n): ").lower()
        if done != 'n':
            match sistem:
                case "nt": os.system("cls")
                case "posix": os.system("clear")
            break

print(f"\nProgram Berakhir, Terimakasih Kaka!\n")