# $\color{wheat}{\textbf{PresenType}}$
Is a tool that allows you to create list of commands to run while doing a presentation. You can just type whatever keys you want and it will run your program line by line. You can edit your commands on the fly by hitting backspace to enter edit mode. From there you can hit enter to exit edit mode. 
## $\color{wheat}{\textbf{Usage}}$
```
usage: main.py [-h] inputfile

An easy to use tool to assist in doing technical presentations.

positional arguments:
  inputfile   The input file containing the commands to be ran.

options:
  -h, --help  show this help message and exit
```
##### $\color{wheat}{\text{Example input file:}}$

```
ls
echo hello world!
```
## $\color{wheat}{\textbf{Dependencies}}$
##### $\color{wheat}{\text{Windows:}}$
```bash
pip install windows-curses
```
##### $\color{wheat}{\text{MAC/Linux:}}$
```bash
echo "curses comes in the python standard library on mac and linux!"
```
