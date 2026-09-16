sensor_info = {
    "name": "Temperature Sensor 01",
    "location": "Lab A",
    "unit": "°C",
    "threshold": 23.5
}

sensor_values = [22.5, 23.1, 22.8, 24.0, 23.6]


def calculate_average(values):
    total = 0

    for value in values:
        total = total + value

    return total / len(values)


def check_readings(values, threshold):
    for value in values:
        if value > threshold:
            print(value, "：读数偏高")
        else:
            print(value, "：读数正常")


print("传感器名称：", sensor_info["name"])
print("安装位置：", sensor_info["location"])
print("异常阈值：", sensor_info["threshold"], sensor_info["unit"])

average_value = calculate_average(sensor_values)
print("平均读数：", average_value)

check_readings(sensor_values, sensor_info["threshold"])