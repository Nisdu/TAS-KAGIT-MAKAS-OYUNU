
### README for the Rock Paper Scissors Game

---

# Taş Kağıt Makas Oyunu (Rock Paper Scissors Game)

Bu proje, Python ve Tkinter kütüphaneleri kullanılarak geliştirilmiş bir Taş Kağıt Makas oyunudur. Oyun, hem tek kişilik hem de çift kişilik modda oynanabilir. Ayrıca kullanıcı profilleri, skor tablosu, zorluk seviyesi ve ses efektleri gibi özellikler içerir. Bu rehber, projeyi GitHub'a yüklemeniz için gereken tüm adımları detaylı bir şekilde açıklar.

---

## İçindekiler

1. [Proje Hakkında](#proje-hakkında)
2. [Gereksinimler](#gereksinimler)
3. [Kurulum](#kurulum)
4. [Kullanım](#kullanım)
    - [Ana Menü](#ana-menü)
    - [Profil Yönetimi](#profil-yönetimi)
    - [Oyun Modları](#oyun-modları)
    - [Zorluk Seviyeleri](#zorluk-seviyeleri)
    - [Skor Tablosu](#skor-tablosu)
    - [Ses Efektleri](#ses-efektleri)
5. [Kod Yapısı](#kod-yapısı)
    - [Profil Yönetimi](#profil-yönetimi)
    - [Oyun Akışı](#oyun-akışı)
    - [Oyun Sonu ve Skorlar](#oyun-sonu-ve-skorlar)
6. [Geliştirme Planları](#geliştirme-planları)
7. [Katkıda Bulunma](#katkıda-bulunma)

---

## Proje Hakkında

Bu proje, klasik Taş Kağıt Makas oyununu bilgisayara taşımayı amaçlayan bir Python projesidir. Oyun, kullanıcı dostu bir arayüzle sunulmakta ve hem eğitici hem de eğlenceli bir deneyim sunmaktadır. Proje, oyuncu profillerinin yönetimi, çeşitli zorluk seviyeleri ve ses efektleri gibi özelliklerle zenginleştirilmiştir.

## Gereksinimler

Proje aşağıdaki kütüphaneleri kullanmaktadır:

- Python 3.x
- Tkinter (Python ile birlikte gelir)
- PIL (Pillow) - Resim işleme için
- Pygame - Ses efektleri için
- JSON - Profil verilerini saklamak için

Ayrıca, oyun resim dosyaları (`tas.png`, `kagit.png`, `makas.png`) ve ses dosyaları (`win_sound.wav`, `lose_sound.wav`, `tie_sound.wav`) gerekmektedir.

## Kurulum

1. **Gereksinimleri Yükleyin**: Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:
    ```bash
    pip install pillow pygame
    ```

2. **Proje Dosyalarını İndirin**: Proje dosyalarını GitHub'dan indirin veya klonlayın:
    ```bash
    git clone https://github.com/kullaniciadi/rock-paper-scissors-game.git
    cd rock-paper-scissors-game
    ```

3. **Gerekli Dosyaları Yükleyin**: `tas.png`, `kagit.png`, `makas.png` resim dosyalarını ve `win_sound.wav`, `lose_sound.wav`, `tie_sound.wav` ses dosyalarını proje klasörüne yerleştirin.

## Kullanım

Projeyi çalıştırmak için ana Python dosyasını çalıştırın:

```bash
python rock_paper_scissors.py
```

### Ana Menü

Oyun açıldığında kullanıcıyı ana menü karşılar. Ana menüde aşağıdaki seçenekler bulunmaktadır:

- **Tek Kişilik Oyna**: Bilgisayara karşı oynamak için seçilir.
- **Çift Kişilik Oyna**: İki oyuncunun birbirine karşı oynaması için seçilir.
- **Eğitim**: Oyunun kurallarını ve nasıl oynandığını açıklayan bir eğitim modunu açar.
- **Skor Tablosu**: Oyuncu profillerinin kazanç, kayıp ve beraberlik istatistiklerini görüntüler.
- **Çıkış**: Oyunu kapatır.

### Profil Yönetimi

Kullanıcılar oyun oynamadan önce bir profil seçmelidir. Profil seçim ekranında mevcut profiller arasından seçim yapabilir veya yeni bir profil oluşturabilirsiniz. Profil oluştururken, profil ismi girilir ve bu isimle bir profil kaydedilir.

### Oyun Modları

- **Tek Kişilik Mod**: Bu modda oyuncu bilgisayara karşı oynar. Oyuncu, taş, kağıt veya makas arasında seçim yapar ve bilgisayarın seçimiyle karşılaştırılır.
- **Çift Kişilik Mod**: İki oyuncu birbirine karşı oynar. Her iki oyuncu da kendi profilini seçer ve ardından oyun başlar.

### Zorluk Seviyeleri

Tek kişilik modda, oyuncular zorluk seviyesini seçebilir:

- **Kolay**: Bilgisayar rastgele seçim yapar.
- **Orta**: Bilgisayar belirli bir olasılıkla oyuncunun kazanma durumuna göre seçim yapar.
- **Zor**: Bilgisayar oyuncunun kaybetmesini sağlamak için stratejik seçimler yapar.

### Skor Tablosu

Skor tablosunda, tüm profillerin kazanma, kaybetme ve beraberlik istatistikleri görüntülenir. Her oyuncunun oyun sonrası istatistikleri güncellenir.

### Ses Efektleri

Oyun, farklı sonuçlar için ses efektleri içerir:

- **Kazanma**: Oyuncu kazandığında `win_sound.wav` dosyası çalınır.
- **Kaybetme**: Oyuncu kaybettiğinde `lose_sound.wav` dosyası çalınır.
- **Beraberlik**: Beraberlik durumunda `tie_sound.wav` dosyası çalınır.

## Kod Yapısı

### Profil Yönetimi

- **load_profiles()**: Profilleri JSON dosyasından yükler.
- **save_profiles()**: Profilleri JSON dosyasına kaydeder.
- **create_profile(name)**: Yeni bir profil oluşturur.
- **update_profile(name, result)**: Profil istatistiklerini günceller.

### Oyun Akışı

- **main_menu()**: Ana menü arayüzünü oluşturur.
- **single_player_menu()**: Tek kişilik oyun modunu başlatır.
- **two_player_menu()**: Çift kişilik oyun modunu başlatır.
- **select_profile()**: Profil seçimi yapılmasını sağlar.
- **start_game()**: Oyun ekranını başlatır.
- **play(player_choice)**: Oyuncunun seçimine göre bilgisayarın veya diğer oyuncunun seçimiyle karşılaştırır ve sonucu belirler.

### Oyun Sonu ve Skorlar

- **display_score()**: Oyun sonuçlarını ve skorları gösterir.
- **ask_restart()**: Oyun sonrasında kullanıcıya yeni bir oyuna başlamak isteyip istemediğini sorar.

## Geliştirme Planları

- **Çevrimiçi Oyun Modu**: Gelecekte iki oyuncunun çevrimiçi olarak birbirine karşı oynayabileceği bir mod eklemeyi planlıyoruz.
- **GUI Geliştirmeleri**: Daha gelişmiş grafikler ve animasyonlar eklemeyi hedefliyoruz.
- **Gelişmiş AI**: Bilgisayarın stratejik oyun oynama kabiliyetini artırmayı planlıyoruz.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen bir `fork` oluşturun, değişikliklerinizi yapın ve bir `pull request` gönderin. Tüm katkılar değerlendirilip projeye eklenebilir.

