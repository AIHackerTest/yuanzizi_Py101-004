#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Program name: Bulls And Cows Advanced Edition
    Author: Yuanzizi
    Github: https://github.com/Yuanzizi/
    Edition：v x.x
    Edit date: 2017.08.xx
"""

Main

  即使是一个打算被用作脚本的文件, 也应该是可导入的. 并且简单的导入不应该导致这个脚本的
  主功能(main functionality)被执行, 这是一种副作用. 主功能应该放在一个main()函数中.

  在Python中, pydoc以及单元测试要求模块必须是可导入的. 你的代码应该在执行主程序前总是
  检查 if __name__ == '__main__' , 这样当模块被导入时主程序就不会被执行.

def main():
      ...

if __name__ == '__main__':
    main()

所有的顶级代码在模块导入时都会被执行. 要小心不要去调用函数, 创建对象, 或者执行那些不应该在使用pydoc时执行的操作.

0. 空行
顶级定义之间空两行, 方法定义之间空一行

顶级定义之间空两行, 比如函数或者类定义.
方法定义, 类定义与第一个方法之间, 都应该空一行. 函数或方法中, 某些地方要是你觉得合适, 就空一行.

1. 空格
    括号内不要有空格
    不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾).
    在二元操作符两边都加上一个空格, 比如赋值(=), 比较,布尔
    当'='用于指示关键字参数或默认参数值时, 不要在其两侧使用空格.
        Yes: def complex(real, imag=0.0): return magic(r=real, i=imag)

2. 用4个空格来缩进代码,绝对不要用tab
foo_bar(self, width, height, color='black', design=None, x='foo',
        emphasis=None, highlight=0)
foo = {
    long_dictionary_key1:
        long_dictionary_value1,
    long_dictionary_key2:
        long_dictionary_value2,
           ...
       }

3. 行长度:每行不超过80个字符,圆括号, 中括号和花括号中的行隐式的连接起来
    以下情况除外： 长的导入模块语句  &&   注释里的URL

4. 宁缺毋滥的使用括号

5. 函数和方法,生成器
    文档字符串应该包含函数做什么, 以及输入和输出的详细描述. 通常, 不应该描述"怎么做",
    除非是一些复杂的算法. 文档字符串应该提供足够的信息, 当别人编写代码调用该函数时,
    他不需要看一行代码, 只要看文档字符串就可以了. 对于复杂的代码, 在代码旁边加注释会
    比使用文档字符串更有意义.

    关于函数的几个方面应该在特定的小节中进行描述记录， 这几个方面如下文所述. 每节应
    该以一个标题行开始. 标题行以冒号结尾. 除标题行外, 节的其他内容应被缩进2个空格.

Args:
    列出每个参数的名字, 并在名字后使用一个冒号和一个空格, 分隔对该参数的描述.如果描述
    太长超过了单行80字符,使用2或者4个空格的悬挂缩进(与文件其他部分保持一致). 描述应该
    包括所需的类型和含义.

    如果一个函数接受*foo(可变长度参数列表)或者**bar (任意关键字参数), 应该详细列出*foo和**bar.

Returns: (或者 Yields: 用于生成器)
    描述返回值的类型和语义. 如果函数返回None, 这一部分可以省略.

Raises:
    列出与接口有关的所有异常.
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass

6. 类
    如果一个类不继承自其它类, 就显式的从object继承. 嵌套类也一样.

    类应该在其定义下有一个用于描述该类的文档字符串. 如果你的类有公共属性(Attributes),
    那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.
class SampleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""

7 命名

模块/包/函数/方法 ：module_name, package_name, method_name,function_name,
类/异常：ClassName,  ExceptionName,
变量：GLOBAL_VAR_NAME, instance_var_name, function_parameter_name, local_var_name.
