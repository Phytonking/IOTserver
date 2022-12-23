from commands import *


def command_center(command):
    if "send_global" in command:
        stat = input("Set status: ")
        update_global(command, stat)
    elif "delete" in command:
        delete_variable_or_status(command)
    elif "add" in command:
        add_variable_or_status(command)
    elif "update" in command:
        variable = input("Variable: ")
        value = input("Value: ")
        update_variable(variable, value)
    elif "exit" in command:
        sys.exit() 
    else:
        print("Command Not Found")
