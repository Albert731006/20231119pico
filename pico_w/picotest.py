import machine
import utime

# 设置震动传感器连接的引脚
vibration_pin = machine.Pin(16, machine.Pin.IN)

# 初始化计数器和计时器
count = 0
start_time = utime.ticks_ms()

while True:
    # 读取震动传感器的电压值
    voltage = vibration_pin.value()

    # 判断电压值，输出相应的信息
    if voltage == 1:
        count += 1

    # 获取当前时间
    current_time = utime.ticks_ms()

    # 计算时间差
    elapsed_time = utime.ticks_diff(current_time, start_time)

    # 判断是否在30秒内，并且收到5次震动信号
    if elapsed_time < 30000 and count >= 5:
        print("機器人正在移動")
        # 重置计数器和计时器
        count = 0
        start_time = utime.ticks_ms()

    # 如果超过30秒，重置计数器和计时器
    elif elapsed_time >= 30000:
        count = 0
        start_time = utime.ticks_ms()

    # 等待一段时间，可以根据需要调整
    utime.sleep(0.1)
    
    



