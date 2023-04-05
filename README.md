# opis struktury repozytorium:

Opis poszczególnych elementów struktury:

README.md - plik opisujący cel projektu, sposób instalacji i użytkowania,
requirements.txt - plik z listą zależności projektu,

ip_monitoring/ - pakiet zawierający kod źródłowy programu,
    __init__.py - pusty plik inicjalizujący pakiet,
    config.py - plik zawierający konfigurację programu (np. adresy IP, porty, itp.),
    db.py - plik zawierający definicje tabel i funkcje dostępu do bazy danych,
    monitor.py - główny plik programu, który uruchamia monitorowanie adresów IP,
    utils.py - plik zawierający przydatne funkcje pomocnicze,

tests/ - folder z testami jednostkowymi,
    __init__.py - pusty plik inicjalizujący pakiet,
    test_config.py - plik z testami konfiguracji programu,
    test_db.py - plik z testami funkcji dostępu do bazy danych,
    test_monitor.py - plik z testami monitorowania adresów IP,
    test_utils.py - plik z testami funkcji pomocniczych,

scripts/ - folder z przykładowymi skryptami,
    install.sh - skrypt instalujący zależności i konfigurujący program,
    start_monitoring.sh - skrypt uruchamiający monitorowanie adresów IP.


# Set up Ip-Scaner


Run commend:
    python 




