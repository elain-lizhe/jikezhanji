# 转义字符 \
# \n  换行; \t  制表符; \\  字符\本身也要转义，所以\\表示的字符就是\; r''表示''内部的字符串默认不转义; '''...'''的格式表示多行内容
print('I\'m ok.')  #I'm ok.
print('I\'m learning\nPython.') # I'm learning
                                # Python.
print('\\\n\\')      # \
                     # \

print('\\\t\\') # \       \
print(r'\\\t\\') # \\\t\\
print('''line1   #line1
... line2        #line2
... line3''')    #line3
#命令行内输入，注意在输入多行内容时，提示符由>>>变为...，提示你可以接着上一行输入，注意...是提示符，不是代码的一部分