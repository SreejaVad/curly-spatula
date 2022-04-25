from week0 import menu
from week1 import list, fibonacci
from week2 import factor, factorial

# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    #["Stringy", menu.stringy],
    # ["Numby", menu.numby],
    #["Listy", menu.listy],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
math_sub_menu = [["Matrix", menu.matrix], ["Fibonacci", fibonacci.tester],
                 ["Factors Test Data", factor.testdata],
                 ["Factors Test Input", factor.testinput],
                 ["Factorial", factorial.tester]]

patterns_sub_menu = [
    ["Animation", menu.ship],
    ["Christmas Tree", menu.grow_tree],
]
data_sub_menu = [
    ["For Loop", list.tester1],
    ["While Loop", list.tester2],
    ["Recursive Loop", list.tester3],
    ["Swap", menu.swapnumbers],
]
# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Mathamatics", math_submenu])
    menu_list.append(["Patterns", patterns_submenu])
    menu_list.append(["Data Types", data_submenu])

    buildMenu(title, menu_list)


# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_sub_menu)


def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)


def data_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, data_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
