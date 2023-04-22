import random
import time
import os

def clear_screen():
    # ekrandaki tüm içeriği siler
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    # ekranın boyutlarını alır
    columns, rows = os.get_terminal_size()

    # saat için kullanılacak renkleri belirler
    hour_color = random.randint(30, 37) # ANSI renk kodları
    minute_color = random.randint(30, 37)
    second_color = random.randint(30, 37)

    # mevcut zamana göre saat, dakika ve saniyeyi ayırır
    current_time = time.strftime("%H:%M:%S")
    hour, minute, second = current_time.split(':')

    # saat göstergesini oluşturur
    clock = f"\033[{hour_color}m{hour}\033[0m:\033[{minute_color}m{minute}\033[0m:\033[{second_color}m{second}\033[0m"

    # rastgele bir konum seçer
    x = random.randint(0, max(0, columns - len(clock)))
    y = random.randint(0, max(0, rows - 1))

    # saati rastgele bir konuma yazdırır
    clear_screen()
    print('\033[{};{}H{}'.format(y+1, x+1, clock))

    # 1 saniye bekle
    time.sleep(1)
