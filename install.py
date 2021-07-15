import os
from platform import system

if system() == "Linux":
    pass
else:
    print("This script is made for linux only")

try:
    from rich.console import Console
    from rich import print

except:
    os.system("sudo apt install python3-rich")

    from rich import print

    print("\n[bold red]Please run this script again[/bold red]\n")
    exit()

console = Console()


if not 'SUDO_UID' in os.environ.keys():
    console.print("\nTry running this program with sudo.\n",style="bold red")
    exit()

class Alerts():
    def __init__(self, color):
        self.color = color
        self.warning_text = ""

    def warning(self, text):
        self.warning_text = f"[bold {self.color}]{text}[/bold {self.color}]"
        print(self.warning_text)

        return self.warning_text


class Menu():
    def __init__(self, options=[], color_scheme=["red", "green", "blue"]):
        self.colors = color_scheme
        self.options = options

    def menu(self):
        print(
            f"\n[bold {self.colors[0]}]            MENU            [/bold {self.colors[0]}]")
        print(
            f"[bold {self.colors[0]}]----------------------------[/bold {self.colors[0]}]")
        for i in range(0, len(self.options)):
            print(
                f"[bold {self.colors[1]}]{str(i+1)}.[/bold {self.colors[1]}]" + f"[bold {self.colors[2]}]{self.options[i]}[/bold {self.colors[2]}]")


class Prompt():
    def __init__(self, color):
        self.color = color

    def input(self, text):

        print(f"[bold {self.color}]{text} : [/bold {self.color}]", end="")
        self.inp = input()

        return self.inp

def welcome():
    print()
    console.print("==========================", style="bold red", justify="center", )
    console.print("Welcome To Brave Installer", style="bold green", justify="center", )
    console.print("==========================\n", style="bold red", justify="center", )

    console.print("Developer", style="bold red", justify="center")
    console.print("Zayed Malick (DevXurde)", style="bold yellow", justify="center")

    print()

class App():
    def __init__(self):
        menu_theme = ["red","green","yellow"]
        menu_options = ["Arch Based Distributions", "Debian 9+, Ubuntu 16.04+ and Mint 18+", "Fedora 28+, CentOS/RHEL 8+", "OpenSUSE 15+", "Exit"]
        self.menu = Menu(options=menu_options, color_scheme=menu_theme)
        self.prompt = Prompt(color="red")
        self.alert = Alerts(color="red")

        self.distro = None

    def installer(self, distro):
        try:
            os.system(f"chmod a+x brave-{distro}.sh")
            os.system(f"sudo ./brave-{distro}.sh")
        
            return True

        except:
            self.alert.warning("\nSomething Went Wrong, Please Try Again")
        
            return False

    def run(self):
        self.menu.menu()
        self.distro_opt = self.prompt.input("\nEnter Your Distribution (Ex: 1)")
        print()

        opts = ["1", "2", "3", "4", "5"]

        if self.distro_opt in opts:
            if self.distro_opt == "1":
                self.distro = "arch"

            elif self.distro_opt == "2":
                self.distro = "debian"

            elif self.distro_opt == "3":
                self.distro = "fedora"

            elif self.distro_opt == "4":
                self.distro = "opensuse"

            elif self.distro_opt == "5":
                console.print("Thank You For Using\n", style="bold green")
                exit()

            self.installer(distro=self.distro)

        else:
            self.alert.warning("Invalid Choice")
            


if __name__ == "__main__":
    welcome()

    app = App()
    app.run()
