import geoEN
import geoTR

def choose_language():
    while True:
        print("Choose your language / Dilinizi seçin:")
        print("1: English\n2: Türkçe\n3: Exit / Çıkış")
        choice = input("Make your choice (1-3): ")

        if choice == "1":
            geoEN.main()
        elif choice == "2":
            geoTR.main()
        elif choice == "3":
            print("Exiting the program / Programdan çıkılıyor.")
            break
        else:
            print("Invalid choice, please try again / Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    choose_language()