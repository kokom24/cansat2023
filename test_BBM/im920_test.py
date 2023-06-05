import serial
import random
import time

# シリアルポートの設定
serial_port = '/dev/ttyAMA0'  # 使用するシリアルポートのパス
baud_rate = 19200  # ボーレート

# シリアルポートの初期化
ser = serial.Serial(serial_port, baud_rate, timeout=3)

while True:
    # ランダムな数字の生成 (0から99まで)
    random_number = random.randint(0, 99)

    # 数字の送信
    data = f'{random_number}\r\n'.encode('utf-8')
    ser.write(data)
    print(f'Sent: {random_number}')

    # 1秒待機
    time.sleep(1)

# シリアルポートのクローズ
ser.close()
