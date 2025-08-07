print("PETROL OFİSİNE HOŞGELDİNİZ!")
while True:
  print("Lütfen Yapmak İstediginiz İslemi Seciniz:\n\n1-Yakit Dolumu\n2-Yikama ve Hava dolumu\n3-Market\n4-Yanlıs Girdim By Byeee")
  a=input()
  
  try:
     islem=int(a)
     if islem==1:
      print(islem,"- 🚗  Yakit Dolumu adlı islemi sectiniz",end=".\n")
      break
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