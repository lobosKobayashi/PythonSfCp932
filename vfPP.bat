echo -------------- Start:testPyClcLine.vrf----------------- > vrfyOutSum.txt
python -u sfPP.py testPyClcLine.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

echo -------------- testPyExcptn.vrf ------------ >> vrfyOutSum.txt
python -u sfPP.py testPyExcptn.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

echo -------------- testSf.vrf ------------ >> vrfyOutSum.txt
python -u sfPP.py testSf.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

echo -------------- testOctn.vrf ------------ >> vrfyOutSum.txt
python -u sfPP.py testOctn.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

echo -------------- testTlRcGn.vrf ------------ >> vrfyOutSum.txt
python -u sfPP.py testTlRcGn.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

echo -------------- testOp.vrf ------------ >> vrfyOutSum.txt
python -m sfPPOp testOp.vrf
IF ERRORLEVEL 1 GOTO :EOF
type verify.out >> vrfyOutSum.txt

REM echo -------------- testSym.vrf ------------ >> vrfyOutSum.txt
REM python -m sfPPOp testSym.vrf
REM IF ERRORLEVEL 1 GOTO :EOF
REM type verify.out >> vrfyOutSum.txt

findStr /n Error! vrfyOutSum.txt
