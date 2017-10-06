#GLAS
#General log analysis and researching solution
### Python3에서 작성되었습니다.
 ** 가상환경만들기 **
<pre>
Python3 가상환경을 만들기 위해서 pip3를 이용해서 virtualevn 패키지를 설치합니다.
[root@localhost ~]# pip3 install virtualenv
프로젝트를 작업할 디렉토리를 생성합니다.
 [root@localhost ~]# mkdir project
 [root@localhost ~]# cd projec

해당 디렉토리 하위에 .venv 디렉토리에 가상환경을 만들어 줍니다.
 [root@localhost project]# virtualenv -p /usr/bin/python3 .venv
 Already using interpreter /usr/bin/python3
 Using base prefix '/usr'
 New python executable in .venv/bin/python3
 Also creating executable in .venv/bin/python
 Installing setuptools, pip...done.
 root@devflat:/opt/project# ll
 total 12

 만들어진 가상환경을 활성화 합니다.
 [root@localhost project]# source .venv/bin/activate
 (.venv)root@devflat:/opt/project#

위와 같이 환경이 구성이 되면 프로젝트 파일 중 requirements.txt 를 이용해서 추가 패키지를 설치합니다.
(.venv)root@devflat:/opt/project# pip3 install -r requirements.txt
 </pre> 

실행전에 source setup으로 환경변수를 맞춰주시기 바랍니다.
test.py는 기본환경을 테스트하기 위한 실행파일로 DB접속, 로그 생성을 확인합니다.  

+ cat data/* | python3 logMapper.py | sort | python3 logReduce.py | sort

