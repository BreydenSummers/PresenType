#!/usr/bin/env python3
import curses
import subprocess
import time

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # The command to be typed out
    command = "echo Hello, World!"
    command_index = 0
    
    # Display a simple prompt
    stdscr.addstr(0, 0, "$ ")
    
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
        time.sleep(0.1)
    
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
    
    # Wait for another key press before exiting
    stdscr.getch()

# Initialize curses
curses.wrapper(main)

