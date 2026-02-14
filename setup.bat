
@echo off
setlocal
echo ===================================================
echo   KIEM TRA BAN QUYEN (License Check)
echo ===================================================

:LICENSE_PROMPT
set /p LICENSE_CODE=Nhap ma ban quyen (5 so): 
if "%LICENSE_CODE%"=="" goto LICENSE_PROMPT

echo Dang kiem tra ban quyen...
python validate_license.py %LICENSE_CODE%

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Ma ban quyen KHONG hop le! Vui long kiem tra lai.
    echo.
    goto LICENSE_PROMPT
)

echo [OK] Ban quyen hop le! Tiep tuc cai dat...
echo.

echo ===================================================
echo   CAU HINH DATABASE CHO KiemTraTrungGio
echo ===================================================

echo.
echo Goi script cau hinh ma hoa...
python configure.py

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Cau hinh that bai!
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [OK] Da cau hinh thanh cong (File config.enc da duoc tao)!
echo Ban co the chay KiemTraTrungGio.exe ngay bay gio.
pause

