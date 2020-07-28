import os

all_users = []
all_problems = []
users_count = []
problems_count = []

path = "D:\\_ManualFilter"
os.chdir(path)

dir_paths = os.listdir(os.getcwd())

# dir_path = os.getcwd() + "/" +sys.argv[0]

dir_path = ""

for dir in dir_paths:
    info = dir.split('_')
    if info[0] not in all_users:
        all_users.append(info[0])
    if info[1] not in all_problems:
        all_problems.append(info[1])

for i in range(len(all_users)):
    users_count.append(0)

for i in range(len(all_problems)):
    problems_count.append(0)

for dir in dir_paths:
    info = dir.split('_')
    users_count[all_users.index(info[0])] = users_count[all_users.index(info[0])] + 1
    problems_count[all_problems.index(info[1])] = problems_count[all_problems.index(info[1])] + 1

path = "D:\\SAMPLES"

os.chdir(path)

dir_paths = os.listdir(os.getcwd())

# dir_path = os.getcwd() + "/" +sys.argv[0]

dir_path = ""

n = 0
howmanyproblems_haveusersdone = []

for i in range(len(all_users)):
    howmanyproblems_haveusersdone.append(0)

for dir in dir_paths:
    if '_' in dir:
        info = dir.split('_')
        if info[0] in all_users:
            howmanyproblems_haveusersdone[all_users.index(info[0])] = howmanyproblems_haveusersdone[all_users.index(info[0])] + 1


print(all_users)
print(all_problems)
print(users_count)
print(problems_count)
print(howmanyproblems_haveusersdone)
