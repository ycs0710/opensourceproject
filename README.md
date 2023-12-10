# 눈건강프로그램

이 프로그램은 눈 건강을 유지하고 눈의 피로를 줄이기 위해 개발된 프로그램입니다. 


## 개발 배경

저는 눈이 매우 안좋고, 컴퓨터 공학과 특성 상 컴퓨터를 오래 봐야 하기 때문에 눈 건강에 관심이 갈 수 밖에 없었고, 

결국 평소 눈을 사용하는 습관이 중요하단 걸 깨달은 후 눈감기, 멀리보기 와 같은 습관을 들이려고 노력했습니다.

따라서 이와 같은 경험을 통해 위 습관을 도와줄 수 있는 프로그램의 필요성을 느껴 만들게 되었습니다.


## 주요 기능

1. 전체 프로그램 유지 시간 설정 기능: 프로그램을 시작 하면 입력합니다(숫자를 입력 할 때 단위 없이 숫자만 적어야 합니다)

2. 몇분 마다 기능을 반복할 지 정하는 기능: 1. 이후에 입력합니다.
   (한번의 루틴을 도는 시간이 최소 11분 30초 정도이니 최소한 15분 이상으로 설정해야 합니다/ 의사선생님들의 추천은 1~2시간 간격입니다)

4. 눈감기와 눈 깜빡이기, 멀리보기 등을 하면서 들을 노래를 틀 웹사이트를 선택하고 여는 기능: 멜론 또는 유튜브 중 선택하여 웹사이트를 엽니다.

5. 눈 근육 스트레칭 애니메이션: 움직이는 원에 초점을 맞추면 눈 근육을 스트레칭 합니다(원 도형 색은 과학적으로 눈에 가장 편안한 색으로 설정하였습니다)

6. 설명 메시지: 설명이 필요 할 때마다 설명 메시지가 뜹니다.

7. 알람 기능: 기능이 끝나거나, 다른 기능을 시작해야 할 때, 필요시 알람 소리가 울립니다. 알람을 끌 수 있는 창도 같이 뜹니다.


## 라이센스

이 프로그램은 MIT 라이센스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.


## 참고 자료, 프로그램


이 프로그램은 다음 자료와 프로그램을 참고하고 이용하여 개발되었습니다.

[눈 근육 스트레칭 YouTube 영상 링크](https://www.youtube.com/watch?v=v17nMtAQDOQ),

[눈 건강 관련 블로그 글](https://www.bnviit.com/blog/health/%EC%86%8C%EC%A4%91%ED%95%9C-%EB%82%B4-%EB%88%88%EC%9D%84-%EC%A7%80%ED%82%A4%EB%A0%A4%EB%A9%B4-%EC%9D%BC%EC%83%81-%EC%86%8D-%EC%9E%91%EC%9D%80-%EC%8A%B5%EA%B4%80%EC%9C%BC%EB%A1%9C-%ED%8F%89%EC%83%9D/),

[챗지피티](https://chat.openai.com/)


## 필수 라이브러리

이 코드에서 사용된 라이브러리는 다음과 같습니다:

webbrowser: 웹 브라우저를 제어하기 위해 사용됩니다. 특정 URL을 기본 웹 브라우저에서 열 때 사용됩니다.

time: 시간 관련 기능을 제공하는 라이브러리입니다. time.sleep() 함수는 프로그램을 일정 시간 동안 일시 중지시키는 데 사용됩니다.

tkinter: Python의 표준 GUI (그래픽 사용자 인터페이스) 툴킷입니다. 사용자 인터페이스를 만드는 데 사용되며, 여기서는 다양한 창을 생성하고 관리하는 데 사용됩니다.

simpledialog: tkinter의 일부로, 사용자로부터 간단한 입력을 받는 대화상자를 제공합니다.

threading: 병렬 실행을 위한 스레드를 생성하고 관리하는 기능을 제공합니다. 여기서는 동시에 여러 작업을 처리하는 데 사용됩니다.

pygame: 게임 개발을 위한 라이브러리이지만, 여기서는 알람 소리를 재생하기 위한 목적으로 사용됩니다.

subprocess: 새로운 프로세스를 생성하고, 이들의 입력/출력/에러 파이프를 관리하며, 해당 프로세스의 종료 코드를 얻는 기능을 제공합니다. 여기서는 외부 Python 스크립트를 실행하는 데 사용됩니다.

이러한 라이브러리들은 Python의 표준 라이브러리에 포함되어 있거나 (tkinter, time, webbrowser, threading, subprocess) 외부에서 설치해야 하는 (pygame) 것들입니다. pygame은 별도로 설치해야 할 수 있으며, 이는 Python 패키지 관리자인 pip를 사용하여 설치할 수 있습니다.

참고)
1. 알람에 이용할 Mp3 파일의 이름을 "alarm_sound.mp3" 로 저장해야 하고 눈건강프로그램.py 프로그램과 같은 폴더에 있어야 합니다.

2. 눈건강애니메이션.py 의 파일명을 변경하면 실행되지 않을 수 있습니다.


## 실행 과정과 방법 설명

1. 파이썬, 눈건강애니메이션.py, 눈건강프로그램.py, 필수 라이브러리를 다운 받습니다.

2. 알람에 이용할 Mp3 파일의 이름을 "alarm_sound.mp3" 바꾼 후 눈건강프로그램.py 프로그램과 같은 폴더에 저장합니다.

3. 해당 프로그램을 실행합니다.

4. 설명에 따라 텍스트를 입력합니다.

5. 열린 사이트에서 노래를 선택하여 알람이 울리기 전까지 눈을 감고 노래를 감상하며 휴식합니다.

6. 알람이 울리면 끄고, 1분 30초 동안 생성된 애니메이션의 녹색 공에 초점을 맞춰 눈 근육 스트레칭을 합니다.

7. 1분 30초가 끝나면 메시지를 따라서 사이트에서 노래를 선택하고, 눈을 자주 깜빡이고 먼 곳을 바라봅니다(자리에서 일어나 스트레칭을 하여도 됩니다.)

8. 마지막 알람이 울리면서 축하 메시지를 읽고 종료하면 됩니다.

9. 처음에 입력한 시간동안, 입력한 시간마다 해당 기능이 반복됩니다.

10. 그만하고 싶으면 해당 프로그램을 그냥 종료하시면 됩니다.


## 프로그램 실행 바로가기 생성 방법

1. 프로그램 파일이 있는 폴더로 이동합니다.

2. 마우스 오른쪽 버튼을 클릭하고 "새로 만들기"를 선택한 후 "텍스트 문서"를 만듭니다.

3. 텍스트 문서의 이름을 "start_alarm.bat" (또는 원하는 다른 이름)로 변경합니다.

4. 마우스 오른쪽 버튼을 클릭하고 "편집"을 선택합니다.

5. 다음 스크립트를 복사하여 텍스트 문서에 붙여넣고 저장합니다.

   이때, "경로"는 웹사이트_여는_알람_프로그램.py 파일의 실제 경로로 대체해야 합니다.

   ```batch
      @echo off

      python 경로\웹사이트_여는_알람_프로그램.py
6."start_alarm.bat" 파일을 더블 클릭하여 프로그램을 실행합니다.

   프로그램 실행 후 웹사이트가 열리고 일정 시간이 지난 후에 알람이 울립니다. 

   프로그램을 편리하게 실행하려면 바탕 화면 또는 작업 표시줄에 바로가기를 만들어 놓을 수 있습니다. 아이콘을 변경하여 더 쉽게 구별할 수도 있습니다.


## 개발자 정보

개발자: 유창선

이메일: yoochangsun0710@gmail.com


## TMI

첨부한 mp3 파일은 소향 "안아줘" 입니다.


