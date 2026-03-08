from script import run_script
from style import banner

banner()

print("1 - Lancer script")
print("0 - Quitter")

choix = input("Choix : ")

if choix == "ban":
    run_script()
