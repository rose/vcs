import sys, os, shutil

vcsname = ".vcs"
ignore = [vcsname, ".git"]


def get(filename):
    f = open(os.path.join(vcsname, filename))
    value = f.readline()
    f.close()
    return value


def set(filename, value):
    f = open(os.path.join(vcsname, filename), 'w')
    f.write(value)
    f.close()


def help(args):
    print ("Available commands:")
    for c in commands:
        print ("  " + c)


def init(args):
    if os.path.exists(vcsname):
        print("A file or directory named " + vcsname + " already exists.  Remove it and try again.")
        exit(2)
    os.mkdir(vcsname)
    set('latest', '0')
    set('head', '0')


def update_latest():
    old = int(get('latest'))
    new = str(old + 1)
    set('latest', new)
    set('head', new)
    return new


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
        print ("Current directory is not a vcs repository!  Run vcs init.")
        exit(2)
    update_latest()
    dest_dir = os.path.join(vcsname, get('latest'))
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
        which = get('latest')
    source_dir = os.path.join(vcsname, which)
    if not os.path.isdir(source_dir):
        print("Invalid checkout, no backup named " + which)
        exit(2)
    set('head', which)
    for filename in os.listdir(source_dir):
        clobber_copy(filename, source_dir, '.')


def current(args):
    print("Head is currently at checkout " + get('head'))


commands = {
    "help": help,
    "backup": backup,
    "checkout": checkout,
    "current": current,
    "init": init,
    }


def run_command(command, args):
    if command not in commands:
        print ("Invalid command: " + command)
        commands["help"]([''])
        exit(2)
    commands[command](args)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Please specify what you want to do!")
        exit(2)
    run_command(sys.argv[1], sys.argv[2:])
