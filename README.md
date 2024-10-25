# Просмотр времени последней загрузки компьютера
Использовано:
- [regex101.com](https://regex101.com/)
- Python 3.10.2
- Pyinstaller 4.10
- Немножечко мозгов и скилла

---

Клонирование:
```
git clone https://github.com/JDM170/show_computer_boot_up_time.git --recurse-submodules
```

---

Запуск:
```
python main.py
```

---

Сборка (без UPX):
```
pyinstaller --clean --console --onefile --name show_computer_boot_up_time main.py
```

Сборка (с UPX):
```
pyinstaller --clean --console --onefile --upx-dir=upx\ --name show_computer_boot_up_time main.py
```