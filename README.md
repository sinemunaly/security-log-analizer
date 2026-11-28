# Güvenlik Log Analizi ve Olay Takip Sistemi
EBLG443 — Tasarım Kalıpları | v0.2

CSV ve JSON giriş kayıtlarını ortak modele dönüştüren, şüpheli girişleri tespit eden ve olay durumlarını yöneten yerel Python prototipi.

## Çalıştırma
Python 3.10+ ile proje kökünde `python main.py` komutunu çalıştırıyorum ilk. Olay yönetimi için `python main.py --interactive` kullanıyorum

## Tasarım kalıpları
| Kalıp | Dosya | Amaç |
|---|---|---|
| Adapter | log_reader.py | CSV/JSON uyarlama |
| Builder | analysis_config.py | Analiz yapılandırması |
| Strategy | detection.py | Değiştirilebilir tespit algoritmaları |
| State | incident.py | İzinli durum geçişleri |


