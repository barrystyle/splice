import os, sys, time, subprocess

def collect_git_history(path):

    git_out = subprocess.run(["git", "log", "--oneline", "--no-color", path], capture_output=True).stdout

    buf = []
    for line in str(git_out).split('\\n'):
        commit = line.split(' ')[0].strip().replace("b'","").replace("'","")
        buf.append(commit)

    revbuf = []
    for line in buf:
        revbuf.insert(0, line)

    return revbuf

def print_as_batchfile(commits, hash):

    toggle = False

    for line in commits:
        if toggle is True:
            print ('read -p wait && git cherry-pick ' + line)
        if hash in line:
            toggle = True

def check_cmd_args():

    total_args = len(sys.argv)

    if total_args < 3:
        print('splice.py <path_of_source_git> <last_commit_hash>')
        sys.exit()

    if not os.path.exists(sys.argv[1]):
        print('path doesnt exist')
        sys.exit()
    
#start here
check_cmd_args()
commits = collect_git_history(sys.argv[1])
print_as_batchfile(commits, sys.argv[2])
