import random

secenek=["taş","kağıt","makas"]
taş=secenek[0]
kağıt=secenek[1]
makas=secenek[2]
kazan1 = []

print("Taş,Kağıt, Makas oyununa hoş geldinizn ")


class oyun():
 def __init__(self):
  i=0 
  while i<3:
    
   if i == 0:
      print("1.set " )  
      self.birinciset() 
      i +=1
   elif i == 1:
      print("2.set " )
      self.ikinset() 
      i +=1 
   elif i == 2:
      print("3.set " )
      self.ücüncüset()
      print()
      print(" Kaybettin Game Ower :) Oyun bitti")
      i +=1 
   
      
      
  
     
     
 def birinciset(Self):
    for secim in range(1,4):
       secim = input("Taş mı kağıt mı makas mı? ")
       bil_secim = random.choice(secenek)
       if secim==taş:
         if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Berabere")
         elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Bilemediniz")
         else:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: makasn Sonuç:Bildiniz")
            
       if secim==kağıt:
          if bil_secim==taş:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Taşn Sonuç: Bildiniz")
            
          elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Berabere")
          else:
            print("Bilgisayarın seçimi: makasn Sonuç:Bilemediniz")
       if  secim==makas:
         if bil_secim==taş:
            
            print("Bilgisayarın seçimi: Taşn Sonuç: Bilemediniz")
            
         elif bil_secim==kağıt:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Bildiniz")
         else:
            print("Bilgisayarın seçimi: makasn Sonuç:Berabere")
       if len(kazan1) ==4 or len(kazan1) ==2:
             print()
             print("kazandınız") 
             exit(0)      
        
    
            
           
 def ikinset(self):
      for secim in range(1,4):
       secim = input("Taş mı kağıt mı makas mı? ")
       bil_secim = random.choice(secenek)
       if secim==taş:
         if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Berabere")
         elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Bilemediniz")
         else:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: makasn Sonuç:Bildiniz")
            
       if secim==kağıt:
          if bil_secim==taş:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Taşn Sonuç: Bildiniz")
            
          elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Berabere")
          else:
            print("Bilgisayarın seçimi: makasn Sonuç:Bilemediniz")
       if  secim==makas:
         if bil_secim==taş:
           
            print("Bilgisayarın seçimi: Taşn Sonuç: Bilemediniz")
            
         elif bil_secim==kağıt:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Bildiniz")
         else:
            print("Bilgisayarın seçimi: makasn Sonuç:Berabere")
       if len(kazan1) ==4 or len(kazan1) ==2:
             print()
             print("kazandınız") 
             exit(0)      
            
        
    
 def ücüncüset(self):
      for secim in range(1,4):
       secim = input("Taş mı kağıt mı makas mı? ")
       bil_secim = random.choice(secenek)
       if secim==taş:
         if bil_secim==taş:
            print("Bilgisayarın seçimi: Taşn Sonuç: Berabere")
         elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Bilemediniz")
         else:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: makasn Sonuç:Bildiniz")
            
       if secim==kağıt:
          if bil_secim==taş:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Taşn Sonuç: Bildiniz")
            
          elif bil_secim==kağıt:
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Berabere")
          else:
            print("Bilgisayarın seçimi: makasn Sonuç:Bilemediniz")
       if  secim==makas:
         if bil_secim==taş:
            
            print("Bilgisayarın seçimi: Taşn Sonuç: Bilemediniz")
         elif bil_secim==kağıt:
            kazan1.append("kazandın")
            print("Bilgisayarın seçimi: Kağıtn Sonuç: Bildiniz")
         else:
            print("Bilgisayarın seçimi: makasn Sonuç:Berabere")
       if len(kazan1) ==4 or len(kazan1) ==2:
             print()
             print("kazandınız") 
             exit(0)  
             
    
oy = oyun()     