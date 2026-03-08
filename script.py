def run_script():
    print("Ton script démarre ici")

    import time
import os

def signaler_numero(numero):
    # Ouvrir l'application WhatsApp sur l'émulateur
    os.system("adb shell am start -n com.whatsapp/com.whatsapp.MainActivity")
    
    # Attendre que l'application soit ouverte
    time.sleep(5)
    
    # Signaler le numéro de téléphone
    os.system(f"adb shell input tap 540 1010")  # Ouvrir le menu de signalements
    os.system(f"adb shell input tap 940 210")  # Sélectionner le type de signalement
    os.system(f"adb shell input tap 1040 1010")  # Sélectionner le numéro de téléphone à signaler
    os.system(f"adb shell input tap 540 1120")  # Sélectionner le numéro de téléphone saisi
    os.system(f"adb shell input tap 340 1010")  # Envoyer le signalement
    
    print("Signalement envoyé.")

def main():
    # Demander au utilisateur de saisir le numéro de téléphone à signaler
    numero = input("Entrez le numéro de téléphone : ")
    
    print("\nTraitement en cours...")
    print(f"Numéro de téléphone saisi : {numero}")
    
    # Lancer l'émulateur Android
    os.system("adb start-server")
    
    # Signaler le numéro de téléphone 100000 fois
    for _ in range(100000):
        signaler_numero(numero)
        
    print("Signalements envoyés.")

if __name__ == "__main__":
    main()
