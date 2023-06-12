import RPi.GPIO as GPIO
import time

# モーターのピン番号を設定します
left_motor_pin = 1  # 左モーターのピン番号正しいのに変える！
right_motor_pin = 2  # 右モーターのピン番号

# GPIOの設定
GPIO.setmode(GPIO.BOARD)
GPIO.setup(left_motor_pin, GPIO.OUT)
GPIO.setup(right_motor_pin, GPIO.OUT)

# モーターを回転させる関数
def rotate(duration):
    GPIO.output(left_motor_pin, GPIO.HIGH)
    GPIO.output(right_motor_pin, GPIO.LOW)
    time.sleep(duration)
    GPIO.output(left_motor_pin, GPIO.LOW)
    GPIO.output(right_motor_pin, GPIO.LOW)

# メインの処理
try:
    rotate(1.2)  # 1.2秒間回転させることで約60°回転します、地面との関係によっても秒が変わるはず
except KeyboardInterrupt:
    GPIO.cleanup()
