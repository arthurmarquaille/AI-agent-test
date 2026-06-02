import subprocess
import json

def compare_git_branches(branch):
    command_diff = f"git diff --stat main {branch}"
    result_diff = subprocess.run(command_diff, shell=True, text=True, capture_output=True, encoding='utf-8')
    
    if result_diff.returncode != 0:
        print(f"Erreur git: {result_diff.stderr}")
        return
    
    if result_diff.stdout.strip() == '':
        print("No differences found between the branches.")
        return
    
    command_full_diff = f"git diff main {branch}"
    result_full_diff = subprocess.run(command_full_diff, shell=True, text=True, capture_output=True, encoding='utf-8')
    
    if result_full_diff.returncode == 0 and result_full_diff.stdout:
        diff_output = result_full_diff.stdout
        for line in diff_output.split('\n'):
            if line.startswith('@@'):
                print(f"\n{line}")
            elif line.startswith('+') and not line.startswith('+++'):
                print(line)
            elif line.startswith('-') and not line.startswith('---'):
                print(line)

compare_git_branches('modif_print')