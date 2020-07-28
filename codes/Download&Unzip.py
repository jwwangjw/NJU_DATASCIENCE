# encoding:utf-8

import json
import urllib.request
import urllib.parse
import os
import importlib
import sys
import os, os.path
import zipfile
import random


#839-148=691个用例
#344个归属upload记录（归属80个题目的提交记录）
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


importlib.reload(sys)

f = open('test_data.json', encoding='utf-8')
res = f.read()

data = json.loads(res)
keys=list(data.keys())
for i in range(10):
    j=keys[random.randint(0,len(keys)-1)]
    cases = data[j]["cases"]
    print(j)
    i = 0

    for case in cases:
        print(case["case_id"], case["case_type"])
        filename = urllib.parse.quote(os.path.basename(case["case_zip"]))
        urllib.request.urlretrieve("http://mooctest-site.oss-cn-shanghai.aliyuncs.com/target/" + filename,
                               str(j)+'_'+case["case_id"]+'_'+str(i) + '.zip')
        os.mkdir(str(j)+'_'+case["case_id"]+'_'+str(i))
        unzip_file(str(j)+'_'+case["case_id"]+'_'+str(i) + '.zip',str(j)+'_'+case["case_id"]+'_'+str(i))
        i = i + 1
