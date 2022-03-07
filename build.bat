@echo off
pyinstaller boot_up.spec
pyinstaller boot_up_upx.spec --upx-dir=upx\