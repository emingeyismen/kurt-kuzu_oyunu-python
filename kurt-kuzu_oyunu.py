import random

def kuzu_oyunu():
    print("Kuzu Oyununa Hoş Geldiniz!")
    print("Kuzular yerleştiriliyor...")
    
    # Kuzuların pozisyonlarını rastgele belirle
    kuzu_pozisyonu = random.randint(1, 3)
    
    while True:
        tahmin = int(input("Kuzuyu hangi kapının arkasında olduğunu tahmin edin (1, 2 veya 3): "))
        
        if tahmin == kuzu_pozisyonu:
            print("Tebrikler! Kuzu doğru kapının arkasında!")
            break
        else:
            print("Üzgünüm, kuzu o kapının arkasında değil. Başka bir kapıyı deneyin!")

# Oyunu başlat
kuzu_oyunu()