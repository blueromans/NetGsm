class ErrorCode:
    sms_error_codes = {'20': 'Mesaj metni ya da mesaj boyunu kontrol ediniz.',
                       '30': 'Geçersiz kullanıcı adı , şifre veya kullanıcınızın API erişim izninin olmadığını gösterir.Ayrıca eğer API erişiminizde IP sınırlaması yaptıysanız ve sınırladığınız ip dışında gönderim sağlıyorsanız 30 hata kodunu alırsınız. API erişim izninizi veya IP sınırlamanızı , web arayüzden; sağ üst köşede bulunan ayarlar> API işlemleri menüsunden kontrol edebilirsiniz.',
                       '40': 'Gönderici adınızı kontrol ediniz.',
                       '41': 'Gönderici adınızı kontrol ediniz.',
                       '50': 'Gönderilen numarayı kontrol ediniz.',
                       '60': 'Hesabınızda OTP SMS Paketi tanımlı değildir, kontrol ediniz.',
                       '70': 'Input parametrelerini kontrol ediniz.',
                       '80': 'Sorgulama sınır aşımı.(dakikada 100 adet gönderim yapılabilir.)',
                       '100': 'Sistem hatası.'
                       }
