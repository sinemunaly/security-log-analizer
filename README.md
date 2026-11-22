# security-log-analizer
# Güvenlik Log Analizi ve Olay Takip Sistemi
EBLG443 Tasarım Kalıpları Dönem Projesi
## Amacım
CSV ve JSON güvenlik kayıtlarını ortak formata dönüştürmek,şüpheli girişleri analiz etmek ve güvenlik olaylarını takip etmek.
## Kullanılan Dil
Python 3.10+
## Tasarım Kalıpları
- Adapter (ilk sürümde uygulandı)
- Builder (planlandı)
- Strategy (planlandı)
- State (planlandı)
## Kurulum
python -m venv .venv
python -m pip install pytest
## Çalıştırma
python main.py
## Test
python -m pytest -v
## İlk Sürüm
Adapter kalıbıyla CSV ve JSON güvenlik kayıtlarının LogRecord modeline dönüştürülmesi.
## Kaynaklar
- EBLG443 ders müfredatı
- Refactoring.Guru - Design Patterns
