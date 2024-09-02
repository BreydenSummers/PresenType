import curses
import subprocess
import time
import argparse


def main(stdscr):
    parser = argparse.ArgumentParser(description='An easy to use tool to assist in doing technical presentations. ')
    parser.add_argument('inputfile', type=open, help='The input file containing the commands to be ran.')
    
    args = parser.parse_args()
    commands = args.inputfile.read().split('\n')
    stdscr.clear()

    for command in commands:
        # Clear screen
        # The command to be typed out
        command_index = 0
        # Display a simple prompt
        stdscr.addstr("$ ")
        # Infinite loop to emulate the terminal
        while command_index < len(command):
            # Get user input (wait for key press)
            key = stdscr.getch()
            # Get the current character from the command to type
            char_to_type = command[command_index]
            # Add the character to the screen
            stdscr.addch(char_to_type)
            # Update the index
            command_index += 1
            # Refresh the screen
            stdscr.refresh()
            # Small delay for more realistic typing effect
            #time.sleep(0.1)
        # After typing is done, move to the next line
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
    # Wait for escape key press
    while stdscr.getch() != 27:
        pass


    # Clear screen
    stdscr.clear()
# Initialize curses
curses.wrapper(main)

