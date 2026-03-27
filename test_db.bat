@echo off
rem ===================================================
rem  THONG TIN KET NOI DATABASE (Sua tai day)
rem ===================================================
set DB_SERVER=192.168.10.200\HISSQLSERVER
set DB_NAME=PKDKMYHOAV62025
set DB_USER=sa
set DB_PASSWORD=Myhoa@123!

echo ---------------------------------------------------
echo  KIEM TRA KET NOI DATABASE (KiemTraTrungGio)
echo ---------------------------------------------------
echo Server  : %DB_SERVER%
echo Database: %DB_NAME%
echo User    : %DB_USER%
echo ---------------------------------------------------
echo.
KiemTraTrungGio.exe --test-db
echo.
pause
