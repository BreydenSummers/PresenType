import curses
import subprocess
import argparse



parser = argparse.ArgumentParser(description='An easy to use tool to assist in doing technical presentations. ')
parser.add_argument('inputfile', type=open, help='The input file containing the commands to be ran.')

args = parser.parse_args()


# This function allows the user to modify a command on the fly before it is finished
def modify_command(stdscr, command):
    while True:
        key = stdscr.getch()
        if key == 10:
            break
        elif key == 127 or key == curses.KEY_BACKSPACE:
            command = command[:-1]
            y, x = stdscr.getyx()
            stdscr.move(y, x-1)
            stdscr.delch()
            stdscr.refresh()
        else:
            command += chr(key)
            stdscr.addch(key)
            stdscr.refresh()

    return command



def main(stdscr):
    # Read the commands from the input but the last line
    commands = args.inputfile.read().split('\n')[:-1]
    stdscr.clear()
    for command in commands:
        command_index = 0
        # Display a simple prompt
        stdscr.addstr("$ ")


        while command_index < len(command):
            # Get user input (wait for key press)
            key = stdscr.getch()
            
            # Enter edit command mode by pressing backspace
            if key == 127 or key == curses.KEY_BACKSPACE:
                command = modify_command(stdscr, command[0:command_index])
                break
            # Get the current character from the command to type
            char_to_type = command[command_index]
            stdscr.addch(char_to_type)
            command_index += 1
            stdscr.refresh()
        while stdscr.getch() != 10:
            pass
        stdscr.addstr("\n")
        # Execute the command and capture the output
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            # Print the output
            stdscr.addstr(result.stdout)
            if result.stderr:
                stdscr.addstr(result.stderr)
        except Exception as e:
            stdscr.addstr(f"Error: {e}")
        # Refresh the screen to show output
        stdscr.refresh()
    stdscr.addstr("$ ")

    # Wait for escape key press
    while stdscr.getch() != 27:
        pass

    stdscr.clear()
# Initialize curses
curses.wrapper(main)

