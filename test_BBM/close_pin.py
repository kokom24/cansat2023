import pigpio
pi = pigpio.pi()


def close_gps(rx):
    pi.bb_serial_read_close(rx)
    pi.stop()

    
if __name__ == '__main__':
    RX = [17, 27]
    for rx in RX:
        close_gps(rx)