import os


def main():
    pocounter = pyccounter = 0
    rootpath = os.path.dirname(os.path.abspath(__file__))
    print('当前工作路径为：%s。' % rootpath)
    print('当前工作路径下的文件夹有：')
    for dir in os.listdir():
        if os.path.isdir(dir) and dir[:1] != '.':
            print(dir, end=' ')
    print()
    while True:
        optdir = input('请输入要操作的文件夹：')
        if not os.path.isdir(optdir):
            print('输入错误，请重试！')
        else:
            break
    cmd = input('此操作将删除所选目录下所有的pyc文件和非中文po文件，确认请按Y：')
    if cmd == 'Y' or cmd == 'y':
        for i in os.walk(optdir):
            for j in i[2]:
                if j[-4:] == '.pyc':
                    pyccounter += 1
                    removefile(os.path.join(i[0], j))
                if j[-3:] == '.po' and j[:2] != 'zh':
                    pocounter += 1
                    removefile(os.path.join(i[0], j))
        print('共删除以上%d个pyc和%d个非中文po文件。' % (pyccounter, pocounter))
    else:
        print('已取消操作！')


def removefile(filename):
    print(filename)
    os.remove(filename)


if __name__ == '__main__':
    main()
