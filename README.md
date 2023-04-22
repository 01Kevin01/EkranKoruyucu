# EkranKoruyucu
Ekran Koruyucu

Bu kod, rastgele bir konuma saati yazdırarak ekranda hareketli bir saat göstergesi oluşturur. Kodun açıklamaları şu şekildedir:

- `clear_screen()` fonksiyonu, ekrandaki tüm içeriği siler.
- `os.get_terminal_size()` fonksiyonu, terminal penceresinin boyutlarını döndürür.
- `random.randint()` fonksiyonu, belirtilen aralıkta rastgele bir tam sayı döndürür.
- `time.strftime()` fonksiyonu, belirtilen biçimlendirme ile mevcut tarihi ve saatini bir dize olarak döndürür.
- `str.split()` metodu, bir dizedeki öğeleri belirtilen ayırıcıya göre ayırarak bir liste döndürür.
- ANSI kaşifinde belirtildiği gibi, `\033[Xm` karakter dizisi, X değerine göre renk değiştirme veya diğer biçimlendirme işlemleri yapmak için kullanılır. Bu örnekte, saatin renklerini rastgele belirlemek için kullanılır.
- `print()` fonksiyonu, belirtilen dizeyi ekrana yazdırır. `\033[y;xH` karakter dizisi, imleci belirtilen satır ve sütuna taşır.
- `time.sleep()` fonksiyonu, belirtilen süre boyunca programı bekletir. Bu örnekte, her bir saat diliminde bir saniye bekletir.
