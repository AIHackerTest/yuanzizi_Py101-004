~ 用于存放本周任务成果。
# Feature
---
----天气资料来自「心知天气」、「OepnWeatherMap」、「YahooWeather」提供----

* 输入城市名，返回该城市的天气数据；
    - 城市名可以是中文 或者 拼音全拼
* 输入 h 或 help，打印帮助文档；
* 输入 quit 或 exit，退出程序的交互
    - 在退出程序之前，打印查询过的所有城市。


# Require
---
* Python 3.6
* requests 2.14.2


# Usage
---
* 主程序
    - get_weather_from_API.py
* utils 文件夹
    - 将主程序脚本内函数放入help.py
    - 将定值变量或程序默认配置参数变量入const_value.py
* resource 文件夹
    - cityname.txt 存放城市的中英文字符

# Update
---
### V1 2017-08-28
#### Features
1. 正式发布，可以查询实时中国城市天气
