"""
    文件分离
        一个文件，文件名："talk.txt"。在文件中保存一些对话信息
        格式如下：
        老王：吃了吗
        老李：没那，您呢？
        老张：你二位干什么呢
        老李：遛弯啊，刚买菜回来啊
        老张：是啊
    通过程序将该文件进行分离，每个任务的说话内容，重新写入到一个
    新的文件中，文件以这个人的名字命名。
"""
person = {}

f = open("talk.txt", "r")

for each_line in f:
    if each_line[0:] != '\n':  # 分行
        (role, line_spoken) = each_line.split('：', 1)  # 分割人物与话语
        if role not in person:
            person[role] = [line_spoken]
        else:
            person[role].append(line_spoken)

f.close()

for name in person:
    with open(name + ".txt", "w") as fw:
        fw.writelines(person[name])