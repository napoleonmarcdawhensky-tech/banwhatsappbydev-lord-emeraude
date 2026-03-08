def run_script():
    print("Ton script démarre ici")

    import os
import time
import requests

def signaler_numero(numero, rate):
    print(f"Signaler le numéro de téléphone : {numero}")
    for i in range(rate):
        # Ouvrir un chat en tapant sur les coordonnées (540, 1010)
        os.system("adb shell input tap 540 1010")
        
        # Ouvrir report en tapant sur les coordonnées (940, 210)
        os.system("adb shell input tap 940 210")
        
        # Choisir report en taprant sur les coordonnées (1040, 1010)
        os.system("adb shell input tap 1040 1010")
        
        # Choisir reepot en tapant sur les coordonnées (540, 1120)
        os.system("adb shell input tap 540 1120")
        
        # Choisir genre en tapant sur les coordonnées (440, 1010)
        os.system("adb shell input tap 440 1010")
        
        # Envoyer le signalement en tapant sur les coordonnées (340, 1010)
        os.system("adb shell input tap 340 1010")
        
        # Envoyer le signalement via API WhatsApp
        url = "https://www.whatsapp.com/ldp/report"
        data = {
            "phone": numero,
            "report_type": "spam"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        try:
            response = requests.post(url, data=data, headers=headers)
            if response.status_code == 200:
                print(f"Succès pour le numéro {numero}")
            else:
                print(f"Erreur pour le numéro {numero} : {response.text}")
        except Exception as e:
            print(f"Erreur pour le numéro {numero} : {e}")
        
        print(f"Signalement {i} envoyé pour {numero}")
        time.sleep(0.001)

def main():
    # Vérifier si l'appareil est connecté
    output = os.popen("adb devices").read()
    if "device" not in output:
        print("Erreur : appareil non connecté")
        return
    
    # Demander au utilisateur de saisir le numéro de téléphone à signaler
    numero = input("Saisir le numéro de téléphone à signaler : ")
    
    # Demander au utilisateur de saisir le nombre de signalements à envoyer
    rate = int(input("Saisir le nombre de signalements à envoyer : "))
    
    signaler_numero(numero, rate)

if __name__ == "__main__":
    main()
