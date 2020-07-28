import re
import sys
delete = input()
# 读取直到输入结束
while True:
    line = sys.stdin.readline()
    if not line:
        break
    # re.sub是替换方法，第一个参数时要替换的字符，第二个是替换后的字符，这里用空替换in和空格
    li = re.sub(delete.upper(), "", line)
    lii = re.sub(delete.lower(), "", li)
    res = re.sub("[ ]", "", lii)
    print(res, end="")
print()