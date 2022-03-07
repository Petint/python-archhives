@echo off
set loopcount=11
:loop
python mondatcsinalo.py >> \\PETRASBALINT-PC\slk-t25
set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
