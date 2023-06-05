import serial

# シリアルポートの設定
serial_port = '/dev/serial0'  # Raspberry PiのUARTポートによって異なる場合があります
baud_rate = 9600  # GPSモジュールのボーレートに合わせて設定します

# シリアルポートの初期化
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # GPSデータの読み取り
        line = ser.readline().decode().strip()
        if line.startswith('$GPGGA'):  # GGAセンテンスの場合
            data = line.split(',')
            # 必要なデータの抽出
            utc = data[1]
            latitude = data[2]
            longitude = data[4]
            altitude = data[9]
            print('UTC:', utc)
            print('Latitude:', latitude)
            print('Longitude:', longitude)
            print('Altitude:', altitude)
except KeyboardInterrupt:
    ser.close()
