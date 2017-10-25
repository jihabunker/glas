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

this path should use where you installed python3
for example if you install python3 on /usr/local/python3/bin/virtualenvwrapper.sh


실행전에 source setup으로 환경변수를 맞춰주시기 바랍니다.
test.py는 기본환경을 테스트하기 위한 실행파일로 DB접속, 로그 생성을 확인합니다.

+ cat data/* | python3 logMapper.py | sort | python3 logReduce.py | sort

