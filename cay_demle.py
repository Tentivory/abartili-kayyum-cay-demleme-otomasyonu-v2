#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartili Kayyum Cay Demleme Otomasyonu v2
Sonsuz dongude cay demler. Gercekten calisir.
Kayyum onayli.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklanmis, asla yazdirilmaz):
# Q2VtaXlldGkgY2F5IGRlbWxlbWVrIGJpcmJpciBzaXlh c2V0IGtha3VtbWEgeW9rdHVyLg==
# (Decode etmeyi dene, ama etmesen de olur. Sadece sakladim.)

def kayyum_onayla():
    print("KAYYUM ONAYI ALINDI: Cay demleme protokolu baslatildi.")

def demle_cay(tur):
    mesajlar = [
        f"{tur}. demleme: Cay yapraklari kayyum tarafindan secildi.",
        f"{tur}. demleme: Su sicakligi 87.3C olarak sabitlendi (neden 87.3? Bilinmez).",
        f"{tur}. demleme: Demleme suresi 4 dakika 27 saniye olarak ayarlandi.",
        f"{tur}. demleme: Bardak secimi rastgele yapildi. Sansli bardak bulundu.",
        f"{tur}. demleme: Cay demlendi. Ulusal guvenlik seviyesi: Yuksek."
    ]
    print(random.choice(mesajlar))
    time.sleep(1.5)

def main():
    sonsuz = "--sonsuz" in sys.argv
    kayyum_onayla()
    tur = 1
    try:
        while True:
            demle_cay(tur)
            tur += 1
            if not sonsuz and tur > 5:
                print("\nDemo modu bitti. Gercek sonsuz dongu icin --sonsuz kullanin.")
                break
            if tur % 10 == 0:
                print("Kayyum notu: Bu cay asla bitmeyecek. Kabul edin.")
    except KeyboardInterrupt:
        print("\nCay demleme durduruldu. Kayyum uzgun. Cayiniz sogudu.")

if __name__ == "__main__":
    main()

# --- DAMGA / IMZA / TARIH / ISIM ---
# Bu kod hem ciddi hem degildir.
# Kayyum Grok tarafindan 22 Ekim 2026 tarihinde yazilmis ve imzalanmistir.
# Muhur: KAYYUM ONAYLI - SACMA AMA CALISIR
# Isim: Kayyum Grok
# Tarih: 2026-10-22
# Durum: Hem ciddi hem degil.
