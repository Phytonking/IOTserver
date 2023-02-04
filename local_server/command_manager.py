from commands import *


def command_center(command):
    try:
        if "send_global" in command:
            stat = input("Set status: ")
            update_global(stat)
        elif "delete" in command:
            command = command.split(" ")
            delete_variable_or_status(command[1],command[2])
        elif "add" in command:
            command = command.split(" ")
            if command[1] == "-v":
                add_variable_or_status(command[1], command[2], command[3])
            elif command[1] == "-s":
                add_variable_or_status(command[1], command[2], None)
        elif "update" in command:
            variable = input("Variable: ")
            value = input("Value: ")
            update_variable(variable, value)
        elif "exit" in command:
            sys.exit() 
        else:
            print("Command Not Found")
    except TypeError:
        print(f"Could not run command \'{command}\'")
