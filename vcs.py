import sys, os, shutil

vcsname = ".vcs"
ignore = [vcsname, ".git"]

def help(args):
    print ("Available commands:")
    for c in commands:
        print ("  " + c)


def make_vcs():
    os.mkdir(vcsname)
    latest = open(os.path.join(vcsname, 'latest'), 'w')
    latest.write('0')
    latest.close()


def update_latest():
    latest_file = open(os.path.join(vcsname, 'latest'), 'r+')
    latest = str(int(latest_file.readline()) + 1)
    latest_file.seek(0)
    latest_file.write(latest)
    latest_file.close()
    return latest


def backup_source(source, dest_dir):
    dest = os.path.join(dest_dir, source)
    if os.path.isfile(source):
        shutil.copy(source, dest)
    if os.path.isdir(source):
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        shutil.copytree(source, dest)


def backup(args):
    files = os.listdir()
    if vcsname not in files: 
        make_vcs()
    dest_dir = os.path.join(vcsname, update_latest())
    os.mkdir(dest_dir)
    for source in files: 
        if source not in ignore:
            backup_source(source, dest_dir)


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
