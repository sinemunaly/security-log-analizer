# Test dokümanı
Komut: `python -m pytest -v` (proje kökünde).

| Senaryo | Beklenen | Sonuç |
|---|---|---|
| CSV | 3 kayıt, LogReader sözleşmesi | PASS |
| JSON | 2 kayıt, LogReader sözleşmesi | PASS |
| Eksik timestamp | Açıklayıcı ValueError | PASS |
| Geçersiz eşik: 0, -1, 1.5 | ValueError | 3 PASS |
| FailureBurstStrategy | 1 olay, dar pencere ve farklı IP ile 0 | PASS |
| FailureThenSuccessStrategy | 1 olay, dar pencere ve farklı IP ile 0 | PASS |
| State | Geçerli geçişler ve geçersiz geçişlerin reddi | PASS |

Gerçek çalıştırma sonucu: 9 passed. Örnek CLI: 5 records, 2 incidents. Bu sonuç yalnızca paket içindeki sürüm için geçerlidir; Windows üzerinde ayrıca doğrulanmalıdır.
