sensor_info ={
    "device_name": "Temperature Sensor 01",
    "location":"Lab A",
    "unit":"°C",
    "threshold": 23.5
}
senor_value=[22.5, 23.1,22.8,24.0,23.6]
new_value= float(input("请输入新的温度读数："))
senor_value.append(new_value)
def calculate_average(values):
    total=0
    for value in values:
        total = total + value
        calculated_average = total / len(values)
    return calculated_average
def check_readings(values,threshold):
    high_count = 0
    for value in values:
        if value > threshold:
            print("偏高")
            high_count = high_count + 1
        else:
            print("正常")
    return high_count
print("传感器名称",sensor_info["device_name"])
print("安装位置",sensor_info["location"])
print("平均读数",calculate_average(senor_value))
high_count = check_readings(senor_value, sensor_info["threshold"])
check_readings(senor_value,high_count)
print("偏高读数数量：", high_count)