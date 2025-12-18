# dym

# Domain Eşleştirme ve Öğrenme Sistemi (Prototip)

Bu proje, verilen bir hedef kelimeyekarşılık gelen **domain adresini** tespit etmeyi amaçlayan prototiptir.  
Sistem, kullanıcı girdilerini analiz ederek mevcut kayıtlarla **benzerlik oranı üzerinden eşleştirme** yapar ve zamanla **kendi veritabanını genişletir**.  
Eğer hedef herhangi bir listede yoksa, **Google Custom Search API** aracılığıyla otomatik olarak internette arama yapar ve bulduğu domainleri kaydeder.


## Proje Özeti

Proje, iki farklı domain listesi ve bir sayaç sistemi kullanarak **öğrenen bir yapı** oluşturur:
- `domains.json` → Ana (onaylı) domain listesi  
- `domains1.json` → Yedek (öğrenme) listesi  
- `counter.json` → Yedek listedeki domainlerin kaç kez eşleştiğini sayar  

Belirli bir domain, yeterli sayıda (örneğin 5 kez) doğrulama aldığında **yedek listeden ana listeye taşınır**.  
Bu sayede sistem, kullanıcı etkileşimleriyle **kademeli olarak kendini geliştirir**.


## Çalışma Mantığı

1. **Kullanıcıdan hedef alınır.**
2. **Ana listedeki kayıtlarla benzerlik kontrolü yapılır.**
   - `fuzzywuzzy` kütüphanesi kullanılarak benzerlik oranı hesaplanır.
   - %50 üzeri benzerlik oranı eşleşme kabul edilir.
3. **Ana listede bulunmazsa yedek liste kontrol edilir.**
   - %40 üzeri benzerlik oranı değerlendirilir.
   - Domain 5 kez tekrarlandığında ana listeye taşınır.
4. **Her iki listede de yoksa Google API ile arama yapılır.**
   - İlk bulunan domain alınarak yedek listeye eklenir.


## Kullanılan Teknolojiler ve Modüller

| Teknoloji | Amaç |
|------------|------|
| Python | Uygulamanın geliştirilmesi |
| fuzzywuzzy | String benzerlik oranı hesaplama |
| requests | Google API üzerinden veri çekme |
| json | Verilerin yerel olarak saklanması |
| Google Custom Search API | Domain bilgisinin internette aranması |
## Geliştirme Planı

Bu sürüm, **prototip** olarak tasarlanmıştır.  
İlerleyen aşamalarda proje bir **web arayüzü** ile entegre edilerek Kullanıcıların tarayıcı üzerinden sorgu yapabildiği bir sistem haline getirilmesini hedefliyorum.


## Notlar

- Google Custom Search API için `API_KEY` ve `CX_KEY` bilgileri ayarlar.py dosyasından ayarlanmalı.
- Uygulama şu anda seri olarak çalışmaz. Test amaçlı yapılmıstır.
