import sys, os, shutil

def help(args):
    print ("Available commands:")
    for c in commands:
        print ("  " + c)


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
        print ("Please specify what you want to do!")
        exit(2)
    run_command(sys.argv[1], sys.argv[2:])
