errors: 

`-1` = Not enough information
`-2` = Account not found on the servers.
`0` = Not logged in



***Configuration and StartUp***

1. In the `/configuration` folder, you will find a file called `config.json`:
 - Put in your account and device accordingly. 
 - You may ignore the `nearest_server` part. 

2. In the `/configuration` folder, you will find `servers.txt`:
  - Delete all lines in the file, if any.
  - put in the global server url: `aaking.pythonanywhere.com`.
3. Run using `python3 local_server.py <command>` (for commands, refer to ***Methods of using the device***).  




***Methods of using the device***
*command line* - running a command prompt 
  - Using `--commands` or `-c` when running the device(`python3 local_server.py`) will begin the operation of the commmand prompt system, managed by function `command_center()` in `command_manager.py`. 
  - Commands are built within an conditional which checks for a special keyword in the command and processing that command based on the key_word's presence. 
  - Prebuilt commands in the command prompt are: `send_global` - sending data to global servers, `delete` - deleting variables and statuses, `add` - adding variables or statuses, `update` - update variables, `exit`- ends the command prompt system. 

*autonomous*
  - Using `--autonomous` or `-a` when running the device will run the code written in `autonomous.py` under the `main()` function. Autonomous mode allows the device to operate by its own instead of needing constant user input. 
  - Autonomous mode is left blank is ready to be filled with code to operate to your needs. 
  - Commands in `commands.py` will be able to help you code your device to your needs. 



