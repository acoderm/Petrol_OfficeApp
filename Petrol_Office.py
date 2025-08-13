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
             yikama_havadolum()
           elif islem==3:
             print(islem,"- 🛒  Market adlı islemi sectiniz",end=".\n")
             market()
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
            
                  
def yikama_havadolum():
           while True:
             print("\n 🧼/🚿 Yikama ve ༄ Hava Doldurma Seçeneklerinden Birini Seçiniz...\n")
             print("1- 🧼/🚿 Yikama ")
             print("2- ༄ Hava Dolumu ")
             print("3- ↩️ Geri \n")
             
             seciminiz = int(input("Seciminiz:\n"))
             
             if seciminiz== 1:
                      print("\n 🧼/🚿 Yikama Seçildi")
             elif seciminiz == 2:
                   print("༄ Hava Dolumu Seçildi")
             elif seciminiz == 3:
                   print("↩️ Ana menüye dönülüyor...\n")
                   return
             else:
                      print("⚠️ Geçersiz giriş! Lütfen tekrar deneyin.")
            
def market():
      
           while True:
             print("\n 7/24 Markete Hosgeldiniz...\n")
             print("Lütfen HAngi Ürünü Almak istediğinizi Seciniz:\n")
             print("1- 🥤 İçecekler ")
             print("2- 🍔 Gıda ")
             print("3- ↩️ Geri \n")
             seciminiz_=int(input(seciminiz_))
             if seciminiz_==1:
                  print("🥤 Hangi İceceği Secmek İstersiniz...")
                  print("1- 🥤 Su ")
                  print("2- 🥤 Soda ")
                  print("3- 🥤 Kola")
                  print("4- 🥤  Gazoz \n")
                  print("5- ↩️ Geri \n")
                  
                  secenek=int(input(secenek))
                  add_cash=0
                  if secenek ==1:
                   print("Seçilen Seçenek SU, Ücret :25 Kredi")
                   print("Lütfen Belirli Bir Kredi Giriniz")
                   if add_cash == 25:
                     print("25 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 30 : 
                     print("30 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 50 : 
                     print("50 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 100 : 
                    print("100 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 200 : 
                    print("200 Kredi Eklenmiştir... GÜle GÜle Kullanın...")  
                  
                  if secenek ==2:
                   print("Seçilen Seçenek SU, Ücret :25 Kredi")
                   print("Lütfen Belirli Bir Kredi Giriniz")
                   if add_cash == 25:
                     print("25 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 30 : 
                     print("30 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 50 : 
                     print("50 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 100 : 
                    print("100 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 200 : 
                    print("200 Kredi Eklenmiştir... GÜle GÜle Kullanın...") 
                    
                  if secenek ==3:
                   print("Seçilen Seçenek SU, Ücret :25 Kredi")
                   print("Lütfen Belirli Bir Kredi Giriniz")
                   if add_cash == 25:
                     print("25 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 30 : 
                     print("30 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 50 : 
                     print("50 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 100 : 
                    print("100 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 200 : 
                    print("200 Kredi Eklenmiştir... GÜle GÜle Kullanın...")  
                
                  if secenek ==4:
                   print("Seçilen Seçenek SU, Ücret :25 Kredi")
                   print("Lütfen Belirli Bir Kredi Giriniz")
                   if add_cash == 25:
                     print("25 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 30 : 
                     print("30 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 50 : 
                     print("50 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 100 : 
                    print("100 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                   if add_cash== 200 : 
                    print("200 Kredi Eklenmiştir... GÜle GÜle Kullanın...")
                    
                  if secenek == 5:
                   print("↩️ Ana menüye dönülüyor...\n")
                   return market
                  
"""   if secim==2:
                    print("🥤 Hangi Gıdayı Secmek İstersiniz...")
                    print("1- 🥤 Pide ")
                    print("2- 🥤 Lahmacun ")
                    print("3- 🍔 Hamburger")
                    print("4- Schinitzel")
                    print("5- Köfte Ekmek")
                    print("6- Adana Kebap")
                    print("7- Urfa Kebap")
                    print("8- Pizza")
                    print("9- ↩️ Geri \n")
                    secenek=int(input(secenek))
                    print("Lütfen Belirli Bir Kredi Giriniz")
                    print("25")
                    print("30")
                    print("50")
                    print("100")    
                    print("200")   
                    secenek=int(input(secenek))   """
                   
print( "PETROL OFİSİNE HOŞGELDİNİZ!")
ana_menu()
