def metin_donustur(girdi_dosyasi_adi, cikti_dosyasi_adi):
    """
    Belirtilen girdi dosyasındaki her satırı işleyerek:
    - "Limitsiz" kelimesini "NULL" ile değiştirir.
    - "Kalan gün: (herhangi bir sayı)" ifadesini satırdan siler.

    Args:
        girdi_dosyasi_adi (str): Okunacak dosyanın adı (örn. 'giris.txt').
        cikti_dosyasi_adi (str): Dönüştürülmüş verinin yazılacağı dosyanın adı (örn. 'cikis.txt').
    """
    try:
        with open(girdi_dosyasi_adi, 'r', encoding='utf-8') as infile:
            satirlar = infile.readlines()

        donusturulmus_satirlar = []
        import re
        for satir in satirlar:
            # 1. "Limitsiz" kelimesini "NULL" ile değiştir
            donusturulmus_satir = satir.replace("Limitsiz", "NULL")

            # 2. "Kalan gün: (herhangi bir sayı)" kısmını sil
            donusturulmus_satir = re.sub(r'Kalan gün: \d+', '', donusturulmus_satir)

            donusturulmus_satirlar.append(donusturulmus_satir.strip())

        with open(cikti_dosyasi_adi, 'w', encoding='utf-8') as outfile:
            for satir_yaz in donusturulmus_satirlar:
                outfile.write(satir_yaz + '\n')

        print(f"Dönüşüm tamamlandı. Sonuçlar '{cikti_dosyasi_adi}' dosyasına yazıldı.")

    except FileNotFoundError:
        print(f"Hata: '{girdi_dosyasi_adi}' dosyası bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Kodu kullanırken:
# 1. Resimdeki metinleri 'giris.txt' adında bir dosyaya kopyalayın.
# 2. Aşağıdaki fonksiyon çağrısını kullanın:
metin_donustur('giris.txt', 'duzenlenmis_metinler.txt')