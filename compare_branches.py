import subprocess

def compare_git_branches(branch):
    command = f"git diff --unified=1 main {branch}"
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    
    if result.stdout.strip() == '':
        print("No differences found between the branches.")
    else:
        # Affiche seulement les modifications avec les numéros de lignes
        lines = result.stdout.split('\n')
        for line in lines:
            if line.startswith('@@') or line.startswith('+') or line.startswith('-'):
                if not line.startswith('+++') and not line.startswith('---'):
                    print(line)
        
compare_git_branches('modif_print')
