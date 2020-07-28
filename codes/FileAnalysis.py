import json
import urllib.request
import urllib.parse
import os
import importlib
import sys
import os, os.path
import zipfile

dirList = []


def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0o777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')
        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir): os.mkdir(ext_dir, 0o777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def findDir_BaseFunction(pathname):
    global dirList
    if os.path.isdir(pathname):
        files = os.listdir(pathname)
        if (len(files)) > 0:
            for i in files:
                ipath = str(pathname) + "/" + str(i)
                if os.path.isdir(ipath):
                    dirList.append(i)
                    findDir_BaseFunction(ipath)
        else:
            dirList.append(pathname)
            return dirList
    else:
        print("请输入正确的路径名")


def findDir(pathname):
    if os.path.isdir(pathname):
        print()
    files = os.listdir(pathname)
    if (len(files)) > 0:
        dirList.append(pathname)
    findDir_BaseFunction(pathname)


findDir("C:/Users/lenovo/PycharmProjects/codeReview")
filenameList = []
for i in range(len(dirList)):
    if (dirList[i][0]).isnumeric():
        filenameList.append(dirList[i])
result = []
for j in range(len(filenameList)):
    list1 = filenameList[j].split('_')
    result.append(list1)
    count1 = 0
importlib.reload(sys)
f = open('test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
count = []
count1 = []
Tf = []
for m in range(len(result)):
    cases = data[result[m][0]]["cases"]
    file = open(str(filenameList[m]) + '/.mooctest' + '/testCases.json', encoding='utf-8')
    fi = file.read()
    data_testCase = json.loads(fi)
    count1.append(len(data_testCase))
    for case in cases:
        if case["case_id"] == result[m][1]:
            flag = True
            records = case["upload_records"]
            n = len(records) - 1
            if n>=1:
                while n >= 0:
                    if (records[n]["score"] <= records[n - 1]["score"])and records[n-2]["score"]==100:
                        flag = False
                    n=n-1
                Tf.append(flag)
            else:
                Tf.append(False)
b = 0
for w in range(len(Tf)):
    if Tf[w] == True:
        cases = data[result[w][0]]["cases"]
        for case in cases:
            if (case["case_id"] == result[w][1]):
                records = case["upload_records"]
                c = 0
                for record in records:
                    urllib.request.urlretrieve(record["code_url"],
                                               result[w][0] + '_' + result[w][1] + '_' + "uploadrecord" + '_' + str(
                                                   c) + '_' + str(record["score"]) + '.zip')
                    c = c + 1
                    print(result[w][0] + '_' + result[w][1] + '_' + "uploadrecord" + '_' + str(
                        c) + '_' + str(record["score"]) + '.zip')
                b = b + 1
                print(b)
