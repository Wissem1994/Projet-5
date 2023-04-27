import os
import subprocess

# Spécifiez le nom de votre notebook et l'URL de votre repository GitHub
notebook_name = r"C:\Users\wiss\Python\Projet_5\Model\CHAOUCH_Wissem_2_notebook_test_032023.ipynb"
github_url = "https://github.com/Wissem1994/Projet-5.git"

# Initialisez un nouveau dépôt Git
subprocess.run("git init", shell=True)

# Ajoutez votre notebook à l'index Git
subprocess.run(f"git add {notebook_name}", shell=True)

# Faites un commit de votre notebook
commit_message = "Premier commit : ajout du notebook"
subprocess.run(f"git commit -m '{commit_message}'", shell=True)

# Connectez votre dépôt local à votre repository GitHub
subprocess.run(f"git remote add origin {github_url}", shell=True)

# Récupérez les modifications les plus récentes du repository distant
subprocess.run("git fetch", shell=True)

# Poussez votre notebook vers votre repository GitHub
subprocess.run("git push origin master", shell=True)

print("Votre notebook a été enregistré sur Git et GitHub avec succès !")
