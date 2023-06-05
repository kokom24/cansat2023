import serial

# シリアルポートの設定
ser = serial.Serial('/dev/serial0', 19200, timeout=1)

# メッセージの送信
message = "Hello, IM920!"
ser.write(message.encode())

# シリアルポートのクローズ
ser.close()
