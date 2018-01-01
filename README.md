#GLAS
#General log analysis and researching solution
### Python3에서 작성되었습니다.
 ** 가상환경만들기 **
<pre>
 ]# sudo pip3 install virtualenv
 ]# sudo pip3 install virtualenvwrapper
 </pre>
virtualenvwrapper can use easy for virtual environment of python.

** Congifure **
1. make default .virtualev directroy on home directory
 ]# make ~/.virtualenvs

2. Registry default WORKON_HOME variable (You can register this on ~/.profile)
 ]# export WORKON_HOME=~/.virtualenvs

3. Add script to ~/.profile in order to run script when user login
 . /usr/lcoal/bin/virtualenvwrapper.sh
  or
 source /usr/local/bin/virtualenvwrapper.sh

윗줄에서 설명하는 가상환경은 반드시 할 필요는 없고 건너 뛰어도 됩니다. 

테스트 전에 mariadb.sql을 참고로 테이블과 DB계정 정보를 맞춰주세요. 

기본값은 conf/glas.conf 파일에 선언이 되어 있습니다. 
해당 값을 각자의 환경에 맞춰서 설정해 주세요 

this path should use where you installed python3
for example if you install python3 on /usr/local/python3/bin/virtualenvwrapper.sh


실행전에 source setup으로 환경변수를 맞춰주시기 바랍니다.
test.py는 기본환경을 테스트하기 위한 실행파일로 DB접속, 로그 생성을 확인합니다.

+ cat data/* | python3 logMapper.py | sort | python3 logReduce.py 



