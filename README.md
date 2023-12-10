# 눈건강프로그램

## 개요

이 프로그램은 눈 건강을 유지하고 눈의 피로를 덜기 위해 개발된 알람 프로그램입니다. 프로그램을 실행하면 웹사이트를 여는 동안 노래를 재생하고, 일정 시간이 지난 후에 눈 건강을 돕는 애니메이션을 실행합니다. 이를 통해 규칙적인 눈 동작과 눈 근육 스트레칭을 할 수 있습니다.

## 주요 기능

- **웹사이트를 여는 기능**: 멜론 또는 유튜브 중 선택하여 웹사이트를 엽니다.

- **노래 재생**: 웹사이트가 열리는 동안 노래를 재생합니다.

- **눈 건강 메시지**: 5분 후 알람이 울리기 전에 노래를 듣고 눈을 휴식시킬 수 있도록 메시지를 표시합니다.

- **알람 기능**: 5분이 경과하면 알람 소리가 울립니다.

- **웹사이트 종료 후 애니메이션**: 웹사이트가 닫힌 후 5초 후에 눈 건강 애니메이션을 실행합니다.

- **눈 건강 스트레칭 메시지**: 눈 건강 애니메이션 실행 중에 눈 근육 스트레칭을 안내하는 메시지를 표시합니다.

- **축하 메시지**: 눈 건강 애니메이션이 종료된 후 축하 메시지를 표시합니다.

## 프로그램 실행

프로그램을 실행하려면 다음 단계를 따르세요.

1. 프로그램 파일이 있는 폴더로 이동합니다.

2. 마우스 오른쪽 버튼을 클릭하고 "새로 만들기"를 선택한 후 "텍스트 문서"를 만듭니다.

3. 텍스트 문서의 이름을 "start_alarm.bat" (또는 원하는 다른 이름)로 변경합니다.

4. 마우스 오른쪽 버튼을 클릭하고 "편집"을 선택합니다.

5. 다음 스크립트를 복사하여 텍스트 문서에 붙여넣고 저장합니다. 이때, "경로"는 웹사이트_여는_알람_프로그램.py 파일의 실제 경로로 대체해야 합니다.

   ```batch
   @echo off

   python 경로\웹사이트_여는_알람_프로그램.py
"start_alarm.bat" 파일을 더블 클릭하여 프로그램을 실행합니다.
프로그램 실행 후 웹사이트가 열리고 일정 시간이 지난 후에 알람이 울립니다. 프로그램을 편리하게 실행하려면 바탕 화면 또는 작업 표시줄에 바로가기를 만들어 놓을 수 있습니다. 아이콘을 변경하여 더 쉽게 구별할 수도 있습니다.

라이센스
이 프로그램은 MIT 라이센스를 따릅니다. 자세한 내용은 LICENSE 파일을 참조하세요.

참고 자료
챗지피티
YouTube 영상 링크
눈 건강 관련 블로그 글
필수 라이브러리
프로그램 실행에 필요한 라이브러리는 다음과 같습니다.

Python 3.x
tkinter
pygame
subprocess
webbrowser
time
실행 과정 설명
프로그램을 실행하면 다음과 같은 과정이 진행됩니다.
(코드의 자세한 설명은 주석에 달려있습니다.)

사용자로부터 전체 이용 시간, 웹사이트 선택, 간격을 입력받습니다. 입력 시 단위 없이 숫자만 입력해야 합니다.

웹사이트를 여는 동안 노래를 재생하고, 5분 후에 눈 건강 메시지를 표시합니다.

5분이 지나면 알람 소리가 울립니다. 사용자가 알람을 끌 수 있습니다.

웹사이트를 닫은 후 5초 후에 눈 건강 애니메이션을 실행합니다.

눈 건강 애니메이션 실행 중에 눈 근육 스트레칭을 안내하는 메시지를 표시합니다.

눈 건강 애니메이션이 종료된 후 축하 메시지를 표시합니다.

프로그램은 눈 건강을 유지하고 컴퓨터 사용 시 눈의 피로를 줄이기 위한 도구로 활용할 수 있습니다.
