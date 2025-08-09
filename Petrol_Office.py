def ana_menu():
   while True:
     print("Lütfen Yapmak İstediginiz İslemi Seciniz:\n\n1-Yakit Dolumu\n2-Yikama ve Hava dolumu\n3-Market\n4-Yanlıs Girdim By Byeee")
     a=input()
     try:
        islem=int(a)
        if islem==1:
         print(islem,"- 🚗  Yakit Dolumu adlı islemi sectiniz",end=".\n")
         yakit_dolumu()
        elif islem==2:
         print(islem,"- 🧼  Yikama ve Hava dolumu adlı islemi sectiniz",end=".\n")
         break
        elif islem==3:
         print(islem,"- 🛒  Market adlı islemi sectiniz",end=".\n")
         break
        elif islem==4:
         print(" 👋  Lütfen Soldaki Çikisi Kullaniniz , Hayirli Yolculuklar Dileriz :)")
         break
        else:
         print(" ⚠️  Yanlis Girdi Lütfen Tekrar Deneyiniz...\n")     
     except ValueError:
         print("❌  Geçersiz giriş! Lütfen sadece **sayı** giriniz (1-4).\n")
         
def yakit_dolumu():
    while True:
      print("\n 🚗 Doldurmak İstediğiniz Yakit Tipini Seciniz...:",end="\n")
      print("1- Benzin (VPower) ")
      print("2- Benzin (Fuelsave) ")
      print("3- Dizel (FuelSave) ")
      print("4- Dizel (VPower) ")
      print("5- LPG")   
      print("6- Electric (AC) ")
      print("7- Electric (DC) ")
      print("8- Geri")
    
      try:
          secim = int(input("Seçiminiz : "))

          if secim == 1:
                print("⛽ Benzin (VPower) Seçildi")
          elif secim == 2:
                print("⛽ Benzin (FuelSave) Seçildi")
          elif secim == 3:
                print("⛽ Dizel (FuelSave) Seçildi")
          elif secim == 4:
                print("⛽ Dizel (VPower) Seçildi")
          elif secim == 5:
                print("🛢️ LPG Seçildi")
          elif secim == 6:
                print("⚡ Electric (AC) Seçildi")
          elif secim == 7:
                print("⚡ Electric (DC) Seçildi")
          elif secim == 8:
                print("↩️ Ana menüye dönülüyor...\n")
                return
          else:
                print("⚠️ Geçersiz giriş! Lütfen tekrar deneyin.")
      except ValueError:
       print("❌ Lütfen sadece sayı giriniz.")
            
            
            
print( "PETROL OFİSİNE HOŞGELDİNİZ!")
ana_menu()
