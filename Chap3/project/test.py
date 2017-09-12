KEY_XZ = 'f2lx47fh1996xypy'  # 原子申请的 API key
UID_XZ = "U1CB842326"  # 原子申请的用户ID

API_XZ = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
UNIT_XZ = 'c'  # 单位
LANGUAGE_XZ = 'zh-Hans' # 查询结果的返回语言
params_xy = {"KEY_XZ":KEY_XZ,"UID_XZ":UID_XZ,"UNIT_XZ":UNIT_XZ}
XZAPI = {"API_XZ":API_XZ,"params_xy":params_xy}
APIParamsList = []

APIParamsList.append(XZAPI)
print (APIParamsList)
