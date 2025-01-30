@echo off
setlocal enabledelayedexpansion


title Paket Yükleniyor...
title Yuklenen Paket: requests
pip install requests
title Yuklenen Paket: colorama / Son Yuklenen Paket: requests
pip install colorama
title Yuklenen Paket: six / Son Yuklenen Paket: colorama
pip install six
title Yuklenen Paket: urllib3 / Son Yuklenen Paket: six
pip install urllib3
title Yuklenen Paket: futures / Son Yuklenen Paket: urllib3
pip install futures
title Yuklenen Paket: SendSms / Son Yuklenen Paket: futures
pip install SendSms
title Yuklenen Paket: sms / Son Yuklenen Paket: SendSms
pip install sms





title Paket Yükleme Tamamlandı!
