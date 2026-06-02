import subprocess

def compare_git_branches(branch):
    command = f"git diff  main {branch}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result == '' :
        print("No differences found between the branches.")
    else:
        print(result.stdout)
        
compare_git_branches('modif_print')
