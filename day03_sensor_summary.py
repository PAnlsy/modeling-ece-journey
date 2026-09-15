sensor_values = [22.5, 23.1, 22.8, 24.0, 23.6]

print(sensor_values)
print("第一个数据：", sensor_values[0])
print("数据数量：", len(sensor_values))

total = 0

for value in sensor_values:
    print("当前传感器读数：", value)

    total = total + value

    if value > 23.5:
        print(value, "：读数偏高")
    else:
        print(value, "：读数正常")

average = total / len(sensor_values)
print("平均读数：", average)

count = 1

while count <= 5:
    print("第", count, "次采样完成")
    count = count + 1