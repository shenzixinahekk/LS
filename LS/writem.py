def write(name, things):
    def listw(file, thing):
        file.write("list_start:\n")
        for th in thing:
            lxs = type(th)
            if lxs == int:
                th = (str(th))
                file.write("it:" + th + "\n")

            elif lxs == float:
                th = (str(th))
                file.write("ft:" + th + "\n")

            elif lxs == str:
                file.write("st:" + th + "\n")

            elif lx == list:
                listw(file, th)
        file.write("list_over:\n")

    file = open(name, 'w')

    for thing in things:
        lx = type(thing)
        if lx == list:
            listw(file, thing)

        elif lx == int:
            th = (str(thing))
            file.write("it:" + th + "\n")

        elif lx == float:
            th = (str(thing))
            file.write("ft:" + th + "\n")

        elif lx == str:
            file.write("st:" + thing + "\n")
    file.close


def read(name):  # #########################################################################

    def listr(lines, ind):
        lis = []  # 列表中包含的项（每一个元素是一行，最后的list_over:一行不在列表内
        l = []  # return项
        a = 1  # 用来判定是否结束（初始为 1）
        indfb = ind + 1  # 建立索引副本，这个副本此时指在list_start的下一行
        while True:  # 导入此列表包含项
            if lines[indfb][:-1] == 'list_over:':
                a -= 1  # 当发现'list_over:'时判定 -1
            elif lines[indfb][:-1] == 'list_start:':
                a += 1  # 当发现'list_start:'时判定 +1（防止大列表内有多个小列表导致误判）
            if a == 0:  # 当a=0时结束
                break
            else:
                lis.append(lines[indfb])  # 将这一行加入（包含\n）
            indfb += 1  # 每次将索引副本增加 1

        a = 0
        ind = len(lis)
        sy = 0
        for i in lis:  # 将lis中的东西判定属性并导入最终return的列表
            if a > 0:
                continue

            a -= 1

            if i[:3] == 'it:':
                it = int(i[3:-1])
                l.append(it)

            elif i[:3] == 'st:':
                it = i[3:-1]
                l.append(it)

            elif i[:3] == 'ft:':
                it = float(i[3:-1])
                l.append(it)

            elif i[:-1] == 'list_start:':  # 如果其中还有小列表就再上一次函数
                re, a = listr(lis, sy)  # ggggggggggg小小列表索引问题
                a = a + 1
                l.append(re)
            sy += 1
        return l, ind  # -----------以上为用来读取列表格式的函数

    file = open(name, 'r')
    lines = file.readlines()  # 将文件中所有的东西赋给lines
    things = []  # return的列表
    ind = 0  # 每次循环结束时的值为本次所读取的行数
    lens = len(lines)  # lens的值为文件中的行数，最后的\n不算1列
    while True:
        if lens == ind:  # 当上一次读取的已经是最后一行时，跳出循环
            break
        elif lines[ind][:3] == 'it:':
            it = int(lines[ind][3:-1])
            things.append(it)
        elif lines[ind][:3] == 'st:':
            it = lines[ind][3:-1]
            things.append(it)
        elif lines[ind][:3] == 'ft:':
            it = float(lines[ind][3:-1])
            things.append(it)
        elif lines[ind][:-1] == 'list_start:':  # 此时ind为上一次循环的行数，即本次循环lines的索引值
            it, indand = listr(lines, ind)  # 进入到再函数体中
            # lines:总文件；ind:此时list_start的索引行数
            ind += indand + 1
            things.append(it)
        ind += 1
    file.close
    return things
