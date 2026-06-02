import subprocess

def compare_git_branches(branch1, branch2):
    command = f"git diff --name-status {branch1} {branch2}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
compare_git_branches('main', 'modif_print')
# This Python function uses subprocess to run the git diff command
# It compares two branches and prints the files that have changed
# Replace 'branch_1' and 'branch_2' with the actual branch names you want to compare
# Ensure git is installed and accessible from your script's environment