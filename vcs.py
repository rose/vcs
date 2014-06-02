import sys, os, shutil

def help():
    print ("Usage: vcs.py args")

commands = {
    "help": help
    }

def run_command(command, args):
    if command not in commands:
        print (command + " is not a valid command")
        exit(2)
    commands[command](args)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        commands["help"]()
        exit(2)
    run_command(sys.argv[1], sys.argv[2:])
