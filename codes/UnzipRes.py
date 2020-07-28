import os
import shutil
import zipfile

dirList = []


def un_zip(file_name):
    """解压单个文件"""
    zip_file = zipfile.ZipFile(file_name)           #读取zip文件
    if os.path.isdir(file_name[0:-4]):             #判断是否存在文件夹，file_name[0:20]是为了方便我去掉日期和.zip的后缀
        pass
    else:
        os.mkdir(file_name[0:-4])                 #创建文件夹

    for names in zip_file.namelist():             #解压
        zip_file.extract(names,file_name[0:-4])
    zip_file.close()
    print(file_name[0:-4],'解压成功')


def un_zip_Tree(path):                        # 解压文件夹中的zip文件
    if not os.path.exists(path):               # 如果本地文件夹不存在，则创建它
        os.makedirs(path)
    for file in os.listdir(path):               #listdir()返回当前目录下清单列表
        Local = os.path.join(path, file)        #os.path.join()用于拼接文件路径
        if os.path.isdir(file):  # 判断是否是文件
            if not os.path.exists(Local):           #对于文件夹：如果本地不存在，就创建该文件夹
                os.makedirs(Local)
            un_zip_Tree(path)
        else:  # 是文件
            if os.path.splitext(Local)[1] == '.zip':            #os.path.splitext(Remote)[1]获取文件扩展名，判断是否为.zip文件
                un_zip(Local)


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

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.zip':
                L.append(os.path.join(root, file))
    return L


names=file_name("C:/Users/lenovo/PycharmProjects/codeReview")
res_t=[]
for i in range(len(names)):
    temp=names[i].split('/')
    var=temp[4].split('\\')
    if var[1][-4:]=='.zip':
        res_t.append(var[1])
name=[]
x=0
for j in range(len(res_t)):
    name.append(res_t[j][:-4])
res=[]
for l in range(len(name)):
    un_zip_Tree("C:/Users/lenovo/PycharmProjects/codeReview"+'/'+name[l])









