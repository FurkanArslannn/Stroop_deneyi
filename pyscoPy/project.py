from psychopy import visual, core, event
import random
from datetime import datetime
import os
import pandas as pd #bunu df=pd.DataFrame(veriler) yazdığımızdan dolayı ekledim

veriler = []
trial_no =0

# 1. Genel Ayarlar ve Pencere
win = visual.Window([1000, 700], color="black", units="pix")
soru_saati = core.Clock() # Her soru için sıfırlanacak saat

# Renk ve Tuş Atamaları
renk_ayarlari = [
    {"renk_ing": "blue", "tus": "m"},
    {"renk_ing": "red", "tus": "k"},
    {"renk_ing": "yellow", "tus": "s"}
]

# Sayaçlar
dogru_sayisi = 0
yanlis_sayisi = 0
toplam_tepki_suresi = 0 

# 2. Kelime Grupları (Doğrudan liste olarak tanımlandı)
deneme_kelimeleri = ["kibir","vahşet","yalan","kavga","samimiyet","hoşgörü","hazine","düğün","masa","köprü"]

blok_1 = [
    "tutku", "gurur", "coşku", "iyilik", "neşe", "hürriyet", "şefkat",
    "onur", "cesaret", "memnun", "zafer", "mucize", "keyifli",
    "servet", "zenginlik", "barış", "kazanç", "beceri", "kahkaha",
    "harika", "üzüntü", "tehdit", "dehşet", "çaresiz", "kıskançlık",
    "utanç", "endişe", "hüzün", "kuşku", "nefret", "gözyaşı",
    "mezar", "felaket", "kusur", "yoksul", "hasar", "suçlu",
    "katil", "haksızlık", "çirkin"
]
blok_2 = [
    "kütle", "ceket", "ırmak", "lezzet", "sofra", "taşıt", "bilet",
    "makyaj", "biber", "yastık", "gözlük", "sergi", "bellek",
    "heykel", "cisim", "özet", "zeytin", "söylem", "şahıs",
    "böbrek", "gümüş", "tohum", "vapur", "durak", "mantar",
    "bakkal", "surat", "pilav", "seçmen", "ressam", "kıymet",
    "çorap", "çatal", "havlu", "çadır", "eklem", "cetvel",
    "takip", "bilek", "maksat"
]

# Blokları kendi içinde karıştır
random.shuffle(blok_1)
random.shuffle(blok_2)
ana_deney_listesi = blok_1 + blok_2

# 3. Görsel Objeler
uyarici = visual.TextStim(win, text="", height=60, bold=True)
sabitleme_noktasi = visual.TextStim(win, text="+", height=50, color="white")
yonerge_metni = visual.TextStim(win, text="""Değerli Katılımcı,

Bu çalışma Türkçenin sözcüksel özelliklerini incelemeyi amaçlamaktadır. Bu amaçla ekranda Türkçe sözcükler gösterilecektir. 
Sizden bu sözcüklerin hangi renkte yazıldıklarını klavye üzerinde belirlenen tuşlara basarak belirtmeniz istenmektedir. 

Buna göre;

Mavi renkli sözcükler için M harfine, 
Kırmızı renkli sözcükler için K harfine,
Sarı renkli sözcükler için S harflerine basınız.

Bu süreçte olabildiğince hızlı olmaya ve doğru cevap vermeye dikkat ediniz.

Katılımınız için teşekkür ederiz.

Kabul etmek ve başlamak için BOŞLUK tuşuna basınız.""", height=20, wrapWidth=850)



#EXCEL KAYDETME
def kaydet_excel():
    if not veriler:
        return
    df = pd.DataFrame(veriler)
    klasor = "data"
    if not os.path.exists(klasor):
        os.makedirs(klasor)
    dosya_adi = f"deney_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    df.to_excel(os.path.join(klasor, dosya_adi), index=False)



# 4. Yardımcı Fonksiyon
def soru_sor(kelime, sure_siniri=2.0):
    global dogru_sayisi, yanlis_sayisi, toplam_tepki_suresi, trial_no
    
    trial_no += 1
    
    # 0.5 saniye "+"
    sabitleme_noktasi.draw()
    win.flip()
    core.wait(0.5)
    
    # kelime + renk
    hedef_renk = random.choice(renk_ayarlari)
    uyarici.text = kelime
    uyarici.color = hedef_renk["renk_ing"]
    
    uyarici.draw()
    win.flip()
    
    soru_saati.reset()
    cevap = event.waitKeys(maxWait=sure_siniri, keyList=['m', 'k', 's', 'escape'], timeStamped=soru_saati)
    
    if cevap is None:  # süre doldu
        yanlis_sayisi += 1
        tepki_suresi = sure_siniri * 1000
        toplam_tepki_suresi += tepki_suresi
        basilan_tus = None
        dogru_mu = 0

    else:
        tus, basılma_ani = cevap[0]

        if tus == 'escape':
            kaydet_excel()
            win.close()
            core.quit()

        tepki_suresi = basılma_ani * 1000
        toplam_tepki_suresi += tepki_suresi
        basilan_tus = tus

        if tus == hedef_renk["tus"]:
            dogru_sayisi += 1
            dogru_mu = 1
        else:
            yanlis_sayisi += 1
            dogru_mu = 0

    # EXCEL VERİ KAYDI
    veriler.append({
        "trial_no": trial_no,
        "kelime": kelime,
        "renk": hedef_renk["renk_ing"],
        "dogru_tus": hedef_renk["tus"],
        "basilan_tus": basilan_tus,
        "dogru_mu": dogru_mu,
        "tepki_suresi_ms": tepki_suresi
    })
    
    win.flip()
    core.wait(0.1)
# 5. Deney Akışı

# Yönerge
yonerge_metni.draw()
win.flip()
event.waitKeys(keyList=['space'])

# --- DENEME KISMI (Sıralı) ---
for k in deneme_kelimeleri:
    soru_sor(k)

# Blok Geçiş Uyarısı
visual.TextStim(win, text="Deneme aşaması bitti.\n\nAna deneye başlamak için bir tuşa basın.").draw()
win.flip()
event.waitKeys()

# --- ANA DENEY KISMI (Karışık Bloklar) ---
for k in ana_deney_listesi:
    soru_sor(k)

# 6. Sonuç Ekranı
sonuc_ekrani = f"""
Deney Tamamlandı.

Toplam Tepki Süresi: {toplam_tepki_suresi:.0f} ms
Ortalama Tepki Süresi: {toplam_tepki_suresi / (dogru_sayisi + yanlis_sayisi):.2f} ms
Doğru Sayısı: {dogru_sayisi}
Yanlış Sayısı: {yanlis_sayisi}

Kapatmak için bir tuşa basın.
"""
visual.TextStim(win, text=sonuc_ekrani, height=30).draw()
win.flip()

#DENEY SONU Sonuç ekranında beklnene kısım
event.waitKeys()

kaydet_excel()
win.close()
core.quit()