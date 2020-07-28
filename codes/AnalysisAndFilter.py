import os
import sys
import re
from shutil import copytree

# 获取代码文件所在路径
path = "D:\\SAMPLES"
os.chdir(path)

dir_paths = os.listdir(os.getcwd())

# dir_path = os.getcwd() + "/" +sys.argv[0]

dir_path = ""

for dir in dir_paths:
    # print("=="*10)
    # print (dir)
    current_dir = "D:\\SAMPLES\\"+dir+"\\.mooctest"
    os.chdir(current_dir)
    code_sum = 0
    with open("answer.py", "r", encoding='UTF-8') as my_code:

        my_lines = my_code.readlines()
        serial_num_list = [[], []]
        printnum = 0
        constnum = 0
        printconstnum = 0

        for serial_num, line in enumerate(my_lines):
            serial_num = serial_num + 1

            try:
                if re.search(r"print", line):
                    printnum = printnum + 1
                    l_parent = line.find('(')
                    r_parent = line.find(')')
                    print_content = line[l_parent+1:r_parent]
                    if print_content.isdigit() or print_content.find("'") != -1 or print_content.find('"') != -1:
                        printconstnum = printconstnum + 1

            except IndexError:
                print("")

            if re.search(r"if", line):
                serial_num_list[0].append(serial_num)
                left = line.find('f')
                right = line.find(':')
                judgement = line[left+2:right]
                rparent = judgement.rfind(')')
                equal_position = judgement.rfind("==")
                if equal_position != -1:
                    rightvalue = judgement[equal_position+2:rparent].strip()
                    if rightvalue.isdigit() or rightvalue.find("'") != -1 or rightvalue.find('"') != -1:
                        constnum = constnum + 1

            if re.search(r"else", line):
                serial_num_list[0].append(serial_num)
                left = line.find('f')
                right = line.find(':')
                judgement = line[left + 2:right]
                rparent = judgement.rfind(')')
                equal_position = judgement.rfind("==")
                if equal_position != -1:
                    rightvalue = judgement[equal_position + 1:rparent].strip()
                    if rightvalue.isdigit() or rightvalue.find("'") != -1 or rightvalue.find('"') != -1:
                        constnum = constnum + 1

            if re.search(r"elif", line):
                serial_num_list[0].append(serial_num)
                left = line.find('f')
                right = line.find(':')

                judgement = line[left+2:right]
                rparent = judgement.rfind(')')
                equal_position = judgement.rfind("==")
                if equal_position != -1:
                    rightvalue = judgement[equal_position+1:rparent].strip()
                    if rightvalue.isdigit() or rightvalue.find("'") != -1 \
                            or rightvalue.find('"') != -1 or rightvalue.isalpha():
                        constnum = constnum + 1
            code_sum += 1

    serial_num_sum1 = 0
    serial_num_sum2 = 0

    for ser in serial_num_list[0]:
        serial_num_sum1 += 1
    for ser in serial_num_list[1]:
        serial_num_sum2 += 1

    serial_num_sum = serial_num_sum1 + serial_num_sum2
    exp_rate = 100 * (serial_num_sum / code_sum)
    print_rate = 100 * (printnum / code_sum)

    casenum = 0

    with open("testCases.json", "r", encoding='UTF-8') as my_code:
        my_lines = my_code.readlines()
        for serial_num, line in enumerate(my_lines):
            serial_num = serial_num + 1
            casenum = casenum + line.count("{")

    if (print_rate > 30) and (code_sum < 30):
        try:
            copytree("D:\\SAMPLES\\"+dir, "D:\\_PrintFilter\\"+dir)
        except FileExistsError:
            print("")

    print("%s| if else的行数为:%d,总行数为%d | if else率为%d%% | print行数为%d | 常量数量为%d | 用例数量为%d"
          % (current_dir, serial_num_sum, code_sum, exp_rate, printnum, constnum, casenum))
