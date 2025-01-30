@echo off
setlocal enabledelayedexpansion

:: Set the title for the Command Prompt window
title Paket Yükleniyor...

:: List of packages to install
set packages=jwt==1.5.0 kash==1.6.0 kiki==0.1.0 kivy==2.0.0 kivymd==1.1.0 langid==1.1.6 langchain==0.0.40 lazy-object-proxy==1.8.1 Levenshtein==0.20.11 lxml==4.9.3 magic==1.5.0 markdown-it-py==2.2.0 markdown2==2.4.0 marshmallow==3.19.0 marshmallow-sqlalchemy==0.25.0 matplotlib==3.8.0 mbedtls==2.7.0 msgpack==1.0.5 multiprocess==0.70.14 music21==6.4.0 mutagen==1.47.0 mypy==1.0.0 nanodet==0.2.0 nasdaq==0.0.1 netaddr==0.7.19 networkx==2.10.0 nltk==3.7 numpy==1.25.1 oauthlib==3.2.2 opencv-python==4.6.0 opencv-python-headless==4.6.0 pandas==2.0.3 pdfminer==2021.9.30 phonenumbers==8.12.32 Pillow==9.4.0 pipenv==2023.6.8 pipreqs==0.4.11 plotly==5.11.0 pillow-simd==9.4.0 protobuf==4.22.0 pyautogui==0.9.54 pycryptodome==3.16.0 pyemoji==0.2.0 pyinstaller==6.1.1 pyodbc==4.0.39 pyppeteer==1.0.2 pyqt5==5.15.9 pytesseract==0.5.0 pyttsx3==2.90 pywin32==305 requests==2.28.2 requests-html==0.10.0 retry==0.9.2 ruemal==0.2.0 selenium==4.7.2 sentencepiece==0.1.96 simplejson==3.18.0 simple-py==0.9.2 six==1.16.0 snappy==1.2.3 social-auth-core==5.2.1 speechrecognition==3.8.1 sphinx==5.4.3 sqlalchemy==2.0.15 ssl==1.17.0 tensorflow==2.14.0 torch==2.1.0 tornado==6.4.0 tqdm==4.67.0 twisted==23.7.0 urllib3==1.26.15 watchdog==2.3.0 websocket-client==1.3.3 websocket-server==1.2.0 yt-dlp==2024.1.0 yfinance==0.2.10

:: Install each package and update the title with the package name
for %%p in (%packages%) do (
    title Yuklenen Paket: %%p
    pip install %%p
)

:: Reset the title once done
title Paket Yükleme Tamamlandı!
