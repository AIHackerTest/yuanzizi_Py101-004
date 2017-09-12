#
# lis = range(10)
#
# for i in lis:
#     print ("序号：%s   值：%s" % (lis.index(i) + 1, i))
#     print (i)
import json

# data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
#
# # json = json.dumps(data)
# print(json)
# print(json.dumps({'B': 'Runoob', 'A': 7}, sort_keys=True,
# #       indent=4, separators=(',', ': ')))
# jsonData = {"A":{"a":1,"b":2,"c":3,"d":4,"e":5},"B":6}
# # def print_dict(dic):
# #     # 打印字典
# #     for key,value in dic:
# #         # if type(dic[key]) is list:
# #         #     # print("\t",end="")
# #         #     print_dict(dic[key])
# #         if type(dic[key]) is dict:
# #             print(key)
# #             print("\t",end="")
# #             print_dict(dic[key])
# #         else:
# #             # print(dic[key])
# #             return dic[key]
# #
# # print(print_dict(jsonData))
#
#
# def printList(list1):
#     for elements in list1:
#         if isinstance(elements,list) or isinstance(elements, tuple):
#             printList(elements) #递归调用函数本身进行深层次的遍历
#         elif isinstance(elements, dict):
#             for i,v in elements.items():
#                 print("\t",i)
#         else :
#             print(elements)
#
#
# def printDict(dict1):
#     for i,v in dict1:
#         print(i)
#         if isinstance(v,dict):
#             printDict(v)
#         else:
#             print(v)
#
# def list_all_dict(dict_a,i=-1):
#     i += 1
#     if isinstance(dict_a,dict) : #使用isinstance检测数据类型
#         for k,v in dict_a.items():
#             print('\t'*i,"%s : " %(k))
#             list_all_dict(v,i) #自我调用实现无限遍历
#     elif isinstance(dict_a,list):
#         for item in dict_a:
#             list_all_dict(item,i)
#     else:
#         print('\t'*i,dict_a)
# list1 =  {"a":{"aa":11},"b":2}
# import pdb
def printJSON(d,obj,i=-1,str_key=""):
    """格式化 JSON 包1
    Arug:
        d:
            将JSON 存储为 没有嵌套 的dict
        obj:
            递归对象，可以是dict，list，str
        i：
            格式计数器，为了输出缩进
        str_key：
            存储键名的字符串

    """
    i += 1
    if isinstance(obj,dict) : #使用isinstance检测数据类型
        for k,v in obj.items():
            print('\t'*i,"%s : " %(k))
            str_key1 = str_key +"_" + k
            # print(str_key1)
            printJSON(d,v,i,str_key1) #自我调用实现无限遍历
    elif isinstance(obj,list):
        for item in obj:
            # str_key1 = str_key +"_" + item
            printJSON(d,item,i,str_key)
    else:
        print('\t'*i,obj)
        # print(str_key)
        d[str_key] = obj

    # return d
    # print(str(d))
person = {"result":[{"male":{"name":"Shawn"}, "female":{"name":"Betty","age":23},"children":{"name":{"first_name":"李", "last_name":{"old":"明明","now":"铭"}},"age":4}}]}

r = {'results': [{'location': {'id': 'WX4FBXXFKE4F', 'name': '北京', 'country': 'CN', 'path': '北京,北京,中国', 'timezone': 'Asia/Shanghai', 'timezone_offset': '+08:00'}, 'now': {'text': '多云', 'code': '4', 'temperature': '30'},'last_update': '2017-08-25T18:25:00+08:00'}]}
list1 =  {"a":{"aa":11},"b":{"bb":22,"BB":22},"c":3}
list2 = [1,[22,22,222],3,4,[1,2]]
d = {}
# printJSON(d,list1,i=-1,str_key="")
printJSON(d,r,i=-1,str_key="XZ")

for k, v in d.items():
    print(k, v)
# list_all_dict(person)
#
# d["aa"] = 1
# d["bb"] = 2
# print(d)
#
