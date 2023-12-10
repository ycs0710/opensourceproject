import webbrowser
import time
import tkinter as tk
from tkinter import simpledialog
from threading import Thread
import pygame
import subprocess

# 알람 소리 재생 함수
def 재생_알람_소리():
    # Pygame 라이브러리를 사용하여 알람 소리 재생
    pygame.mixer.music.load('alarm_sound.mp3')  # 알람 소리 파일 로드
    pygame.mixer.music.play()  # 알람 소리 재생

# 알람 소리 서서히 감소 함수
def 감소_알람_소리():
    # 알람 소리를 서서히 감소시키는 함수
    pygame.mixer.music.fadeout(1000)  # 1초 동안 서서히 소리 감소

# 알람 끄는 창 생성 함수
def 생성_알람_끄는_창():
    # 알람을 끌 수 있는 창을 생성하는 함수
    창 = tk.Tk()
    창.title("알람 끄기")
    tk.Label(창, text="알람을 끄려면 아래 버튼을 누르세요.", height=2).pack()
    
    # 알람 끄기 버튼 생성 및 설정
    정지_버튼 = tk.Button(창, text="알람 끄기", command=lambda: [감소_알람_소리(), 창.destroy()])
    정지_버튼.pack(pady=10)
    창.attributes('-topmost', True)  # 창을 항상 맨 위에 위치시킴
    창.protocol("WM_DELETE_WINDOW", lambda: [감소_알람_소리(), 창.destroy()])  # 창 닫기 시 알람 소리 감소 및 창 닫기

    창.mainloop()

# 메시지 표시 함수
def 표시_메시지():
    # 사용자에게 정보를 제공하는 메시지 창을 표시하는 함수
    창 = tk.Tk()
    창.title("메시지")
    메시지 = ("5분 후 알람이 울릴 때까지 노래를 실행하고 눈을 감고 휴식을 취하세요.\n"
               "알람이 울리고 나서 5초 후에 눈건강 애니메이션이 실행됩니다.\n"
               "움직이는 초록색 원에 초점을 맞춰서 눈 근육 스트레칭을 해주세요.\n"
               "해당 애니메이션은 1분 30초 후에 종료됩니다.")
    라벨 = tk.Label(창, text=메시지, width=60, height=10, justify=tk.CENTER)
    라벨.pack()
    창.attributes('-topmost', True)  # 창을 항상 맨 위에 위치시킴
    창.after(300000, 창.destroy)  # 5분 후에 창 자동 닫기

    창.mainloop()

# 스트레칭 메시지 표시 함수
def 표시_스트레칭_메시지():
    # 사용자에게 스트레칭을 권장하는 메시지 창을 표시하는 함수
    창 = tk.Tk()
    창.title("스트레칭 시간")
    메시지 = "노래를 틀고 5분 동안 눈을 자주 깜빡이고 먼 곳을 바라보세요."
    라벨 = tk.Label(창, text=메시지, width=60, height=10, justify=tk.CENTER)
    라벨.pack()
    창.attributes('-topmost', True)  # 창을 항상 맨 위에 위치시킴
    창.after(300000, lambda: [창.destroy(), 재생_알람_소리()])  # 5분 후에 창 닫고 알람 재생

    창.mainloop()

# 축하 메시지 표시 함수
def 표시_축하_메시지():
    # 사용자에게 축하 메시지를 제공하는 창을 표시하는 함수
    창 = tk.Tk()
    창.title("축하 메시지")
    메시지 = "축하합니다! 당신의 소중한 시력을 지키셨습니다!"
    라벨 = tk.Label(창, text=메시지, width=60, height=10, justify=tk.CENTER)
    라벨.pack()
    창.attributes('-topmost', True)  # 창을 항상 맨 위에 위치시킴
    창.protocol("WM_DELETE_WINDOW", lambda: [감소_알람_소리(), 창.destroy()])
    창.after(10000, lambda: [감소_알람_소리(), 창.destroy()])  # 10초 후에 창 닫기 및 알람 소리 감소

    창.mainloop()

# 사용자 입력을 받는 함수 (수정)
def 사용자_입력_받기():
    # 사용자로부터 필요한 입력(전체 시간, 음악 선택, 간격)을 받는 함수
    루트 = tk.Tk()
    루트.withdraw()
    전체_시간_분 = simpledialog.askstring("입력", "전체 이용 시간을 분 단위로 입력하세요:")
    if not 전체_시간_분 or not 전체_시간_분.isdigit():
        return None
    전체_초 = int(전체_시간_분) * 60  # 분을 초로 변환
    선택 = simpledialog.askstring("입력", "멜론 또는 유튜브 중 하나를 입력하세요:")
    if not 선택 or 선택.lower() not in ["멜론", "유튜브"]:
        return None
    주소 = "https://www.melon.com/" if 선택.lower() == "멜론" else "https://www.youtube.com/"
    간격 = simpledialog.askstring("입력", "몇 분 간격으로 웹사이트를 열까요?:")
    if not 간격 or not 간격.isdigit():
        return None
    간격_초 = int(간격) * 60
    return 전체_초, 주소, 간격_초

# 웹사이트를 여는 함수 및 알람 기능 함수 
def 웹사이트_여는_알람_기능():
    # 사용자 설정에 따라 웹사이트를 여는 주기적인 작업을 수행하는 함수
    pygame.init()

    사용자_입력 = 사용자_입력_받기()
    if not 사용자_입력:
        print("입력이 취소되었거나 잘못되었습니다.")
        return
    전체_초, 주소, 간격_초 = 사용자_입력

    시작_시간 = time.time()
    while time.time() - 시작_시간 < 전체_초:
        webbrowser.open(주소)  # 설정된 주소로 웹브라우저 열기
        print(f"{주소}로 이동합니다.")

        메시지_스레드 = Thread(target=표시_메시지)  # 메시지 표시 스레드 시작
        메시지_스레드.start()

        time.sleep(300)  # 5분 대기
        재생_알람_소리()  # 알람 소리 재생

        알람_끄기_스레드 = Thread(target=생성_알람_끄는_창)  # 알람 끄는 창 스레드 시작
        알람_끄기_스레드.start()

        time.sleep(5)  # 5초 대기
        subprocess.Popen(["python", "눈건강애니메이션.py"]).wait()  # 눈건강 애니메이션 실행

        스트레칭_스레드 = Thread(target=표시_스트레칭_메시지)  # 스트레칭 메시지 스레드 시작
        스트레칭_스레드.start()
        스트레칭_스레드.join()  # 스트레칭 메시지 창이 닫힐 때까지 기다림

        축하_스레드 = Thread(target=표시_축하_메시지)  # 축하 메시지 스레드 시작
        축하_스레드.start()

        time.sleep(간격_초)  # 사용자가 설정한 간격만큼 대기

# 함수 실행
웹사이트_여는_알람_기능()