def stretch():
    for index in range(2):
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 122)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 120)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
        basic.pause(200)
    for index2 in range(2):
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 120)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 40)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
        basic.pause(200)
def dance3():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 50)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 50)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 50)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 50)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 50)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 120)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(200)
def dance2():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 0)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 50)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 50)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 130)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 130)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)

def on_received_number(receivedNumber):
    pass
radio.on_received_number(on_received_number)

def fart():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 150)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 30)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 150)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 30)
    basic.pause(500)
def slow4(num: number, num2: number, num3: number):
    global D3, degrees, D2
    reset()
    D3 = num
    degrees = num2 - num
    D2 = degrees / num3
    for index3 in range(num3):
        D3 = D3 + D2
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, D3)
        basic.pause(100)
    reset()
# slow

def on_button_pressed_a():
    reset()
    slow1(40, 140, 11)
    basic.pause(200)
    slow2(140, 40, 11)
    basic.pause(200)
    slow3(44, 133, 22)
    basic.pause(200)
    slow4(133, 44, 11)
input.on_button_pressed(Button.A, on_button_pressed_a)

def dance4():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 130)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 50)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 130)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 130)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 60)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 133)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 133)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 50)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 133)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    robotbit.servo(robotbit.Servos.S2, 90)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
    basic.pause(200)
def slow3(num4: number, num22: number, num32: number):
    global D3, degrees, D2
    reset()
    D3 = num4
    degrees = num22 - num4
    D2 = degrees / num32
    for index4 in range(num32):
        D3 = D3 + D2
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, D3)
        basic.pause(100)
    reset()
def dance1():
    for index5 in range(2):
        pins.servo_write_pin(AnalogPin.P0, 88)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 120)
        pins.servo_write_pin(AnalogPin.P0, 88)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
        pins.servo_write_pin(AnalogPin.P0, 90)
        basic.pause(200)
        pins.servo_write_pin(AnalogPin.P0, 180)
        for index6 in range(2):
            Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
            basic.pause(200)
            Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 120)
            basic.pause(200)
            Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
            basic.pause(200)
        for index7 in range(2):
            slow4(90, 133, 5)
            basic.pause(100)
            Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
            basic.pause(100)
            slow3(90, 50, 4)
            basic.pause(100)
            Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
        reset()
def Go_Back():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 120)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 80)
    basic.pause(200)
# n1= start angle
# n2= end angle
# n3=n. step
def slow1(num5: number, num23: number, num33: number):
    global degrees, D2, D3
    reset()
    degrees = num23 - num5
    D2 = degrees / num33
    D3 = num5
    for index8 in range(num33):
        D3 = D3 + D2
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, D3)
        basic.pause(100)
    reset()
def dance5():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 80)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 80)
    basic.pause(333)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 100)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 80)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 100)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 70)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 60)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)

def on_button_pressed_ab():
    moon()
    basic.pause(200)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def dance6():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 125)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 125)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 80)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 135)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 45)

def on_button_pressed_b():
    basic.show_number(0)
    for index9 in range(1):
        dance1()
        basic.pause(200)
    reset()
    basic.show_number(1)
    for index10 in range(1):
        jitter()
    basic.pause(200)
    basic.show_number(2)
    for index11 in range(2):
        basic.show_arrow(ArrowNames.NORTH)
        for index12 in range(3):
            walk1()
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_number(3)
        for index13 in range(3):
            Go_Back()
    basic.pause(200)
    basic.show_number(4)
    for index14 in range(3):
        moon()
    reset()
    basic.pause(200)
    basic.show_number(5)
    for index15 in range(1):
        dance4()
    reset()
    basic.show_number(6)
    for index16 in range(1):
        dance2()
    basic.pause(200)
    basic.show_number(7)
    for index17 in range(2):
        dance5()
    basic.pause(200)
    basic.show_number(8)
    for index18 in range(2):
        happy()
    basic.pause(500)
    reset()
    basic.show_number(9)
    for index19 in range(2):
        dance6()
    basic.pause(200)
    basic.show_number(10)
    for index20 in range(2):
        stretch()
    reset()
input.on_button_pressed(Button.B, on_button_pressed_b)

def jitter():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 105)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 75)
    basic.pause(100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 60)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 95)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 85)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 60)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 70)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 110)
    basic.pause(500)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    basic.pause(200)
def happy():
    for index21 in range(2):
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 130)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
        basic.pause(333)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 50)
        basic.pause(500)
    for index22 in range(2):
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 150)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
        basic.pause(333)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 30)
        basic.pause(500)

def on_received_value(name, value):
    global backward, right, right_motor, left_motor
    left = 0
    if name.compare("mgy") == 0:
        backward = value
    if name.compare("mgx") == 0:
        right = value
    right_motor = -1 * backward - right
    left_motor = -1 * backward + left
radio.on_received_value(on_received_value)

def slow2(num6: number, num24: number, num34: number):
    global D3, degrees, D2
    reset()
    D3 = num6
    degrees = num24 - num6
    D2 = degrees / num34
    for index23 in range(num34):
        D3 = D3 + D2
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, D3)
        basic.pause(100)
    reset()
def walk1():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 60)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 60)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 80)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 120)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 120)
    basic.pause(200)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 100)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 120)
    basic.pause(200)
def moon():
    for index24 in range(2):
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 122)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 58)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
        basic.pause(200)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
        basic.pause(200)
    for index25 in range(2):
        basic.pause(500)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 58)
        basic.pause(500)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
        basic.pause(500)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 122)
        basic.pause(500)
        Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 90)
def reset():
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO1, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO2, 90)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO3, 95)
    Kitronik_Robotics_Board.servo_write(Kitronik_Robotics_Board.Servos.SERVO4, 90)
left_motor = 0
right_motor = 0
right = 0
backward = 0
D2 = 0
degrees = 0
D3 = 0
serial.redirect_to_usb()
reset()
radio.set_group(1)
strip = neopixel.create(DigitalPin.P16, 4, NeoPixelMode.RGB)
for index26 in range(1):
    basic.pause(200)
    basic.show_leds("""
        . # # # .
                # . . . #
                . . . . .
                . # . # .
                # # . # #
    """)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.pause(200)
strip.show_color(neopixel.hsl(0, 0, 0))
music.set_built_in_speaker_enabled(True)

def on_forever():
    if right_motor > 500 and left_motor > 500:
        for index27 in range(2):
            walk1()
    if right_motor < -300 and left_motor < -400:
        for index28 in range(2):
            Go_Back()
    if right_motor < 20 and left_motor < 20:
        basic.pause(500)
    if left_motor >= 400:
        robotbit.servo(robotbit.Servos.S4, 60)
        basic.pause(333)
        robotbit.servo(robotbit.Servos.S3, 60)
    elif left_motor >= 0:
        robotbit.servo(robotbit.Servos.S4, 100)
        basic.pause(333)
        robotbit.servo(robotbit.Servos.S3, 120)
    else:
        robotbit.servo(robotbit.Servos.S4, 100)
        basic.pause(333)
        robotbit.servo(robotbit.Servos.S3, 80)
    if right_motor > 222:
        robotbit.servo(robotbit.Servos.S2, 80)
        basic.pause(200)
        robotbit.servo(robotbit.Servos.S1, 100)
    elif right_motor > 0:
        robotbit.servo(robotbit.Servos.S2, 100)
        basic.pause(300)
        robotbit.servo(robotbit.Servos.S1, 90)
    else:
        robotbit.servo(robotbit.Servos.S2, 120)
        basic.pause(111)
        robotbit.servo(robotbit.Servos.S1, 70)
basic.forever(on_forever)
