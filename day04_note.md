# Day 4 学习复盘

今天完成：
- 学习字典 dict 保存传感器名称、位置、单位和异常阈值
- 学习通过键读取字典中的值
- 学习 def 定义函数
- 学习函数参数 values 和 threshold
- 学习 return 返回平均值计算结果
- 编写传感器平均值计算和异常读数检测程序

我理解了：
- 字典使用“键”保存有明确名称的信息，例如 sensor_info["name"]。
- 函数参数是调用函数时传入的信息。
- calculate_average(sensor_values) 会将 sensor_values 传给函数内部的 values。
- check_readings(values, threshold) 需要一组读数和一个异常阈值。
- return 可以把函数内部计算的结果交给外部变量使用。
- 将不同任务拆成函数，代码会更清晰，也更适合后续电子竞赛项目。

明天要学：
- 把传感器数据保存到 CSV 文件
- 从 CSV 文件读取数据
- 对读取到的数据进行分析