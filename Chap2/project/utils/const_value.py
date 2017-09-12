"""
Author: Yuanzizi
Github: https://github.com/Yuanzizi/
Edition：v 0.1
Edit date: 2017.08.23
Descrition:
    ------------------------------------------------
    该文件为各个天气API 的配置参数
    -------------------------------------------------
"""
LOCATION = 'beijing'  # 所查询缺省位置，可以使用城市拼音、v3 ID、经纬度等

# 心知天气配置文件

KEY_XZ = 'f2lx47fh1996xypy'  # 原子申请的 API key
UID_XZ = "U1CB842326"  # 原子申请的用户ID

API_XZ = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT_XZ = 'c'  # 单位
LANGUAGE_XZ = 'zh-Hans' # 查询结果的返回语言



# OpenWeatherMap 配置文件
"""
    OpenWeatherMap http://openweathermap.org/api
    API 地址：
        api.openweathermap.org/data/2.5/weather?q=London,uk?appid={APPID_OWM}
    参数说明：
        q：
         	城市名称，city可通过城市英文名称、ID和经纬度进行查询，	必选
        appid：
         	用户认证key 	必选 	your key
        units:
            default, 绝对温度
            units=metric,摄氏度
            units=imperial，华氏度
        lang：
            lang=zh_cn, 中文
            """
APPID_OWM = '7dd907ccf0bf04b078d04403cfea138c'  # 原子申请的 API key，10分钟调用一次
API_OWM = 'http://api.openweathermap.org/data/2.5/weather'  # API URL，可替换为其他 URL
UNIT_OWM = 'metric'  # 单位
LANGUAGE_OWM = 'zh_cn' # 查询结果的返回语言

# 和风天气 配置文件
"""
    和风天气 https://www.heweather.com/documents
    API 地址：
        实况天气（免费用户）：https://free-api.heweather.com/v5/now?city=yourcity&key=yourkey
    参数说明：
        city：
         	城市名称，city可通过城市中英文名称、ID、IP和经纬度进行查询，经纬度查询格式为：经度,纬度 	必选 	city=北京，city=beijing，city=CN101010100，city= 60.194.130.1，city=120.343,36.088
        key：
         	用户认证key 	必选 	your key
        lang：
         	多语言，可以不使用该参数，默认为中文 	可选 	详见多语言参数值
"""
APPID_HF = '8727f04981a0467fb4c91e25e95811b9  '  # 原子申请的 API key
API_HF = 'https://free-api.heweather.com/v5/now'  # API URL，实况天气
LANGUAGE_HF = 'zh-cn' # 查询结果的返回语言


# Yahoo天气 配置文件
"""
    Yahoo天气 https://developer.yahoo.com/weather/

    API 地址：
        https://query.yahooapis.com/v1/public/yql?format=json&q=
        q：
         	YSL语法，yahoo like-sql language ,比如：
            select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="beijing")
"""
APPID_Yahoo = '8727f04981a0467fb4c91e25e95811b9  '  # 原子申请的 API key
API_Yahoo = 'https://query.yahooapis.com/v1/public/yql'  # API URL，实况天气
LANGUAGE_Yahoo = 'zh-cn' # 查询结果的返回语言
