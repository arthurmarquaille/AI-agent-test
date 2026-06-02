import subprocess
import json

def compare_git_branches(branch):
    """Analyse les différences entre la branche main et la branche spécifiée"""
    
    # 1. Récupérer les fichiers modifiés
    command_files = f"git diff --name-status main {branch}"
    result_files = subprocess.run(command_files, shell=True, text=True, capture_output=True)
    
    if result_files.stdout.strip() == '':
        print("No differences found between the branches.")
        return
    
    print(f"\n📊 ANALYSE DES MODIFICATIONS: main → {branch}\n")
    print("=" * 70)
    
    # 2. Récupérer le diff détaillé
    command_diff = f"git diff main {branch}"
    result_diff = subprocess.run(command_diff, shell=True, text=True, capture_output=True)
    
    # 3. Parser les fichiers modifiés
    files_modified = {}
    for line in result_files.stdout.strip().split('\n'):
        if line:
            status, filename = line.split('\t', 1)
            status_map = {'M': '✏️  Modifié', 'A': '➕ Ajouté', 'D': '❌ Supprimé'}
            files_modified[filename] = status_map.get(status, status)
    
    # 4. Afficher le résumé
    print(f"\n📁 Fichiers affectés: {len(files_modified)}\n")
    for filename, status in files_modified.items():
        print(f"  {status:20} {filename}")
    
    # 5. Afficher les modifications détaillées
    print("\n" + "=" * 70)
    print("📝 DÉTAIL DES MODIFICATIONS\n")
    
    current_file = None
    for line in result_diff.split('\n'):
        # En-têtes de fichier
        if line.startswith('diff --git'):
            current_file = line.split(' ')[-1]
            print(f"\n📄 {current_file}")
            print("-" * 70)
        # Numéros de lignes
        elif line.startswith('@@'):
            print(f"  {line}")
        # Lignes ajoutées
        elif line.startswith('+') and not line.startswith('+++'):
            print(f"  \033[92m{line}\033[0m")  # Vert
        # Lignes supprimées
        elif line.startswith('-') and not line.startswith('---'):
            print(f"  \033[91m{line}\033[0m")  # Rouge
    
    # 6. Statistiques
    print("\n" + "=" * 70)
    command_stats = f"git diff --stat main {branch}"
    result_stats = subprocess.run(command_stats, shell=True, text=True, capture_output=True)
    print("📈 STATISTIQUES\n")
    print(result_stats.stdout)

compare_git_branches('modif_print')