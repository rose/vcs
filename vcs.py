import sys, os, shutil

vcsname = ".vcs"
ignore = [vcsname, ".git"]

def help(args):
    print ("Available commands:")
    for c in commands:
        print ("  " + c)


def backup(args):
    files = os.listdir()
    if vcsname not in files:
        os.mkdir(vcsname )
    for source in files:
        if source not in ignore:
            dest = os.path.join(vcsname, source)
            if os.path.isfile(source):
                shutil.copy(source, dest)
            if os.path.isdir(source):
                if os.path.isdir(dest):
                    shutil.rmtree(dest)
                shutil.copytree(source, dest)


commands = {
    "help": help,
    "backup": backup,
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
