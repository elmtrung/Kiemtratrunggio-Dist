
@echo off
setlocal
echo ===================================================
echo   CAU HINH DATABASE CHO KiemTraTrungGio
echo ===================================================

set /p DB_SERVER=Nhap ten Server (VD: localhost, 192.168.1.10): 
set /p DB_NAME=Nhap ten Database (VD: HIS_MISA): 
set /p DB_USER=Nhap User DB (VD: sa): 
set /p DB_PASSWORD=Nhap Password DB: 

echo.
echo Dang luu cau hinh vao file .env...
(
echo DB_SERVER=%DB_SERVER%
echo DB_NAME=%DB_NAME%
echo DB_USER=%DB_USER%
echo DB_PASSWORD=%DB_PASSWORD%
echo APP_HOST=0.0.0.0
echo APP_PORT=5000
echo APP_DEBUG=False
) > .env

echo.
echo [OK] Da luu cau hinh thanh cong!
echo Ban co the chay KiemTraTrungGio.exe ngay bay gio.
pause
