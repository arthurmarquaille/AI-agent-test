import subprocess

def compare_git_branches(branch1, branch2):
    command = f"git diff  {branch1} {branch2}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
compare_git_branches('main', 'modif_print')
