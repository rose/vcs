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
    head = open(os.path.join(vcsname, 'head'), 'w')
    head.write('0')
    head.close()


def update_latest():
    latest_file = open(os.path.join(vcsname, 'latest'), 'r+')
    latest = str(int(latest_file.readline()) + 1)
    latest_file.seek(0)
    latest_file.write(latest)
    latest_file.close()
    set_current(latest)
    return latest


def clobber_copy(filename, source_dir, dest_dir):
    dest = os.path.join(dest_dir, filename)
    source = os.path.join(source_dir, filename)
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    elif os.path.isfile(dest):
        os.remove(dest)
    if os.path.isfile(source):
        shutil.copy(source, dest)
    elif os.path.isdir(source):
        shutil.copytree(source, dest)


def backup(args):
    files = os.listdir()
    if vcsname not in files: 
        make_vcs()
    dest_dir = os.path.join(vcsname, update_latest())
    os.mkdir(dest_dir)
    for source in files: 
        if source not in ignore:
            clobber_copy(source, '.', dest_dir)


def checkout(args):
    which = args[0]
    if which == "":
        print("Please specify which backup you wish to check out")
        exit(2)
    if which == "latest":
        latest_file = open(os.path.join(vcsname, 'latest'), 'r')
        which = latest_file.readline()
        latest_file.close()
    source_dir = os.path.join(vcsname, which)
    if not os.path.isdir(source_dir):
        print("invalid checkout, no backup named " + which)
        exit(2)
    set_current(which)
    for filename in os.listdir(source_dir):
        clobber_copy(filename, source_dir, '.')


def set_current(new_head):
    current_file = open(os.path.join(vcsname, 'head'), 'w')
    current_file.write(str(new_head))
    current_file.close()


def get_current():
    current_file = open(os.path.join(vcsname, 'head'))
    current = current_file.readline()
    current_file.close()
    return current


def current(args):
    print("Head is currently at checkout " + get_current())


commands = {
    "help": help,
    "backup": backup,
    "checkout": checkout,
    "current": current,
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
