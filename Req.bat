@echo off
setlocal enabledelayedexpansion


title Paket Yükleniyor...
title Yüklenen Paket: requests
pip install requests
title Yüklenen Paket: colorama / Son Yüklenen Paket: requests
pip install colorama
title Yüklenen Paket: six / Son Yüklenen Paket: colorama
pip install six
title Yüklenen Paket: urllib3 / Son Yüklenen Paket: six
pip install urllib3
title Yüklenen Paket: futures / Son Yüklenen Paket: urllib3
pip install futures
title Yüklenen Paket: SendSms / Son Yüklenen Paket: futures
pip install SendSms
title Yüklenen Paket: sms / Son Yüklenen Paket: SendSms
pip install sms





title Paket Yükleme Tamamlandı!
