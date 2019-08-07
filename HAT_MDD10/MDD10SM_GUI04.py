"""
8/7 今までのプログラムを全て結合し実験用のGUI作成する
"""
import RPi.GPIO as GPIO		
from time import sleep
import tkinter as tk

root = tk.Tk()
root.title("移動ロボットを動かそう!")
root.geometry("1600x1000")

# HAT MDD10の設定
GPIO.setmode(GPIO.BCM)			
GPIO.setwarnings(False)			# enable warning from GPIO
AN1 = 12				# set pwm1 pin on MD10-hat
AN2 = 13				# set pwm2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat(右)
DIG2 = 24				# set dir2 pin on MD10-Hat(左)

GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output

right_wheel = GPIO.PWM(AN1, 100)			# set pwm for M1
left_wheel = GPIO.PWM(AN2, 100)			# set pwm for M2
SPEED_RIGHT = 0
SPEED_LEFT = 0

right_wheel.start(SPEED_RIGHT)
left_wheel.start(SPEED_LEFT)


def forward(event):
    global SPEED_RIGHT, SPEED_LEFT
    print(SPEED_RIGHT, SPEED_LEFT)
    if (SPEED_RIGHT + 10 or SPEED_LEFT + 10) > 50:
        label1.config(text="左: {0}  右: {1}    操作できません".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT + 10
        SPEED_LEFT = SPEED_LEFT + 10
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def back(event):
    global SPEED_RIGHT, SPEED_LEFT
    print(SPEED_RIGHT, SPEED_LEFT)
    if (SPEED_RIGHT - 10 or SPEED_LEFT - 10) < -50:
        label1.config(text="左: {0}  右: {1}    操作できません".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT - 10
        SPEED_LEFT = SPEED_LEFT - 10
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def left(event):
    global SPEED_RIGHT, SPEED_LEFT
    print(SPEED_RIGHT, SPEED_LEFT)
    if (SPEED_RIGHT + 5 > 50) or (SPEED_LEFT - 5 < -50) :
        label1.config(text="左: {0}  右: {1}    操作できません".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT + 5
        SPEED_LEFT = SPEED_LEFT - 5
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))

def right(event):
    global SPEED_RIGHT, SPEED_LEFT
    print(SPEED_RIGHT, SPEED_LEFT)
    if (SPEED_RIGHT - 5 < -50) or (SPEED_LEFT + 5 > 50) :
        label1.config(text="左: {0}  右: {1}    操作できません".format(SPEED_LEFT, SPEED_RIGHT))
    else:
        SPEED_RIGHT = SPEED_RIGHT - 5
        SPEED_LEFT = SPEED_LEFT + 5
        if SPEED_RIGHT >= 0:
            GPIO.output(DIG1, GPIO.HIGH)
        else:
            GPIO.output(DIG1, GPIO.LOW)
        if SPEED_LEFT >= 0:
            GPIO.output(DIG2, GPIO.HIGH)
        else:
            GPIO.output(DIG2, GPIO.LOW)
        label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))


def stop(event):
    global SPEED_RIGHT, SPEED_LEFT
    SPEED_RIGHT = 0
    SPEED_LEFT = 0
    label1.config(text="左: {0}  右: {1}".format(SPEED_LEFT, SPEED_RIGHT))




#----------------------------------------------
STOP_BUTTON_X=1000
STOP_BUTTON_Y=400

BUTTON_HEIGTH = 15
BUTTON_WIDTH = 30

Button_Forward = tk.Button(text="前", height=BUTTON_HEIGTH, width=BUTTON_WIDTH)
Button_Forward.bind("<Button-1>", forward)
Button_Forward.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y-300)

Button_Back = tk.Button(text="後", height=BUTTON_HEIGTH, width=BUTTON_WIDTH)
Button_Back.bind("<Button-1>", back)
Button_Back.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y+300)

Button_Right = tk.Button(text="右", height=BUTTON_HEIGTH, width=BUTTON_WIDTH)
Button_Right.bind("<Button-1>", right)
Button_Right.place(x=STOP_BUTTON_X+300, y=STOP_BUTTON_Y)

Button_Left = tk.Button(text="左", height=BUTTON_HEIGTH, width=BUTTON_WIDTH)
Button_Left.bind("<Button-1>", left)
Button_Left.place(x=STOP_BUTTON_X-300, y=STOP_BUTTON_Y)

Button_Stop = tk.Button(text="停", height=BUTTON_HEIGTH, width=BUTTON_WIDTH)
Button_Stop.bind("<Button-1>", stop)
Button_Stop.place(x=STOP_BUTTON_X, y=STOP_BUTTON_Y)



#var = tk.DoubleVar()
#value = tk.Scale(root, label='速さ', length=300, tickinterval=10, orient='h', from_=0, to=100, variable=var, command=State)
#value.place(x=175, y=300)

label1= tk.Label(root)
label1.config(text="停止")
label1.place(x=350, y=400)

root.mainloop()