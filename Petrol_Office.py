def ana_menu():
         while True:
           print("Lütfen Yapmak İstediginiz İslemi Seciniz:\n")
           print("1-Yakit Dolumu\n")
           print("2-Yikama ve Hava dolumu\n")
           print("3-Market\n")
           print("4-Yanlıs Girdim By Byeee")
           islem=int(input())
           
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
            
                  
def Yikama_Havadolum():
           while True:
             print("\n 🧼 Yikama ve Hava Doldurma Seçeneklerinden Birini Seçiniz...")
             print("1- 🧼 Yikama ")
             print("2-  Hava Dolumu ")
             print("3- ↩️ Geri \n")
             
             secim = int(input("Seciminiz:"))
             
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
          
          
                  
print( "PETROL OFİSİNE HOŞGELDİNİZ!")
ana_menu()
