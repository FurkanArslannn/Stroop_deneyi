# 🧠 Psikolojik Deney: Sözcüksel Özellikler ve Tepki Süresi Analizi

Bu proje, **PsychoPy** kütüphanesi kullanılarak geliştirilmiş, görsel ve bilişsel performansı ölçen bir psikolojik deney uygulamasıdır.

---

### 📝 Proje Hakkında
Katılımcıların duygusal ve nötr kelimelere verdikleri tepkileri ölçer. Deney, katılımcının kelime içeriğinden ziyade **yazı rengine** ne kadar hızlı odaklanabildiğini test eder.

### 🚀 Deney Aşamaları
* 🏁 **Başlangıç:** Bilgilendirme ve yönerge ekranı.
* 🧪 **Deneme:** Sürece alışmak için 10 soruluk kısa tur.
* 🎯 **Ana Deney:** Duygusal (blok 1) ve nötr (blok 2) kelimelerin karışık sunumu.
* 🏁 **Bitiş:** Özet istatistiklerin sunumu ve veri kaydı.

### 🎮 Kontroller (Renk-Tuş Eşleşmesi)
* 🔵 **Mavi Renk:** `M` tuşu
* 🔴 **Kırmızı Renk:** `K` tuşu
* 🟡 **Sarı Renk:** `S` tuşu
* 🛑 **Çıkış:** `ESC` tuşu

### 📊 Veri Kaydı ve Çıktılar
Veriler her çalışma sonunda otomatik olarak `/data` klasörüne **Excel** formatında aktarılır.
* 📅 **Dosya İsmi:** `deney_YIL-AY-GUN_SAAT.xlsx`
* 📈 **Kaydedilenler:** Deneme no, kelime, doğru tuş, basılan tuş, doğruluk (0/1), tepki süresi (ms).

### 🛠 Teknik Detaylar
* 💻 **Dil:** Python 3
* 📚 **Kütüphaneler:** `psychopy`, `pandas`, `openpyxl`
* ⏱ **Zaman Sınırı:** Her kelime için 2 saniye cevap süresi.
