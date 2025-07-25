# Bu kodu bir Python dosyasına (örneğin, "donusturucu.py" olarak) kaydedin.

def odeme_durumu_donustur(girdi_dosyasi_adi, cikti_dosyasi_adi):
    """
    Belirtilen girdi dosyasındaki ödeme durumu metinlerini,
    verilen kurala göre sayısal değerlere dönüştürür ve yeni bir dosyaya yazar.

    Kural:
    1 = Ücretsiz
    2 = Ödenmiş
    3 = Ödememiş (Bu örnekte yok ama dahil edildi)

    Args:
        girdi_dosyasi_adi (str): Okunacak dosyanın adı (örn. 'ücretsizaa.txt').
        cikti_dosyasi_adi (str): Dönüştürülmüş verinin yazılacağı dosyanın adı (örn. 'donusturulmus_veri.txt').
    """
    donusum_sozlugu = {
        "Ücretsiz": "1",
        "Ödenmiş": "2",
        "Ödememiş": "3" # Eğer bu durum da dosyanızda varsa
    }

    try:
        with open(girdi_dosyasi_adi, 'r', encoding='utf-8') as infile:
            satirlar = infile.readlines()

        donusturulmus_satirlar = []
        for satir in satirlar:
            satir = satir.strip() # Satır sonu karakterini ve boşlukları kaldır
            if satir in donusum_sozlugu:
                donusturulmus_satirlar.append(donusum_sozlugu[satir])
            else:
                # Eşleşmeyen bir durum varsa olduğu gibi bırak veya hata ver
                donusturulmus_satirlar.append(satir)
                print(f"Uyarı: '{satir}' için bir dönüşüm bulunamadı, olduğu gibi bırakıldı.")

        with open(cikti_dosyasi_adi, 'w', encoding='utf-8') as outfile:
            for donusturulmus_satir in donusturulmus_satirlar:
                outfile.write(donusturulmus_satir + '\n')

        print(f"Dönüşüm tamamlandı. Sonuçlar '{cikti_dosyasi_adi}' dosyasına yazıldı.")

    except FileNotFoundError:
        print(f"Hata: '{girdi_dosyasi_adi}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Fonksiyonu çağırma
# 'ücretsizaa.txt' dosyasının bu Python koduyla aynı klasörde olduğundan emin olun.
odeme_durumu_donustur('ücretsizaa.txt', 'donusturulmus_odeme_durumlari.txt')