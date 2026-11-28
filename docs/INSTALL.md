# Kurulum ve çalıştırma
1. Python 3.10 veya üzerini kurun.
2. Proje klasörünü VS Code ile açın ve terminali proje kökünde başlatın.
3. `python --version` ile kontrol edin.
4. `python -m venv .venv` ile isteğe bağlı sanal ortam oluşturun.
5. Windows PowerShell: `.\.venv\Scripts\Activate.ps1` (izin sorunu varsa doğrudan `.\.venv\Scripts\python.exe` kullanın).
6. `python -m pip install -r requirements.txt` ile test bağımlılığını kurun.
7. `python main.py` ile örnek analizi çalıştırın.
8. `python -m pytest -v` ile testleri çalıştırın.

`python main.py --interactive` komutunda `1 investigate`, `1 resolve`, `q` komutlarını deneyin.

Özel dosya: `python main.py data/sample.csv data/sample.json --threshold 3 --window 300 --method both --ip 192.0.2.1`
Zaman filtresi: `--start 2026-11-22T10:00:00 --end 2026-11-22T10:05:00`.
CSV virgülle ayrılır; JSON nesne listesi olmalıdır. Alanlar: timestamp (ISO 8601, saat dilimsiz), ip_address, username, result (failure/success). Aynı kayıtları birden fazla dosyada tekrar vermeyin.
