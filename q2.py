str = input("请输入字符串：")
res = list()   # 结果字符串
stack = list()  # 栈 用于匹配括号

for i in range(len(str)):
    res.append(' ')
    if str[i] == '(':   #匹配到左括号，将位置压入栈
        stack.append(i)
    elif str[i] == ')': #匹配到右括号，检测栈里是否有相应的左括号
        if len(stack) == 0: #未检测到对应的左括号
            res[i] = '?'
        else:
            stack = stack[:len(stack) - 1]

for i in range(len(stack)): #处理剩余没有匹配到的左括号
    res[stack[i]] = 'x'

res = "".join(res)  #将结果转为字符串
print(str)
print(res)