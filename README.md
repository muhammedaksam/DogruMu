# Reddit Doğruluk Kontrol Botu

Kullanıcı tarafından sağlanan rastgele bir sorguyla ilgili talep analizini almak için [Google Doğruluk Kontrol Araçları API](https://developers.google.com/fact-check/tools/api/)'sini kullanan bir reddit botu. Bot, kaynak ve kaynağın değerlendirmesi de dahil olmak üzere en alakalı iddiaları güzel bir şekilde sunacaktır (en azından deneyecektir). Bu bot, şüpheli bir yoruma yanıt olarak gerçeği yayınlamak amacıyla etkili bir yol sağlamak içindir. Botu çağıran kullanıcı, iddiayı bulmak için gerekli anahtar kelimeleri sağlamalıdır - aşağıdaki kullanıma bakın.

# Kullanım
Bot şu anda aşağıdaki subredditleri izlemektedir.

r/Turkey<br/>
r/TurkeyDogrulama<br/>
r/TarihTarih<br/>
r/TarihiSeyler<br/>
r/TurkeyJerky<br/>

İçerisinde `!dogrumu <sorgu>` bulunduran mesajlar, *\<sorgu> aramada kullanılacak kelime ve/ya kelime dizisidir*, doğruluk kontrolü ile alakalı sonuçları aramak için kullanılır. Bu nedenle, yorumunuz ne kadar özlü ve alakalı olursa, iyi bir sonuç alma olasılığınız o kadar yüksek olur.

**Örnek kullanım ve cevap:**

![example](bot_example.PNG)

# Önemli Notlar

Google'ın iddia kontrol araması mükemmel değildir, kaynakların kendisine sağladığı iddialara ve kullanıcının sağladığı ifadelere dayanır. Bot bu nedenle her zaman en alakalı sonuçları döndürmez veya bunları listede ilk sıraya koymaz.

**Botun sağladığı kaynakları kontrol etmiyorum**, bot da bu amaca hizmet edip linkliyor. Doğruluk kontrolünden şüpheniz varsa, bağlantıyı tıklayın ve kendiniz karar verin.

# Geribildirim/Katkıda Bulunma
Feel free to open issues or pull requests under the relevant tabs to this fork or main repository.
