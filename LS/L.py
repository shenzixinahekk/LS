import pygame
import time
import writem  # 自编模块


# 建立函数
def jl(location, picture):
    screen.blit(location, picture)


def wz(neirong, xy, size):
    font = pygame.font.Font("C:\Windows\Fonts\simsun.ttc", size)
    text = font.render(neirong, True, (0, 0, 0), (255, 255, 255))
    screen.blit(text, xy)


def xsxy():
    global Pp
    screen.blit(s, [0, 0])

    b = 0
    for i in mjlist:  # 显示现有民居
        if i > 0:
            mj = jl(picture_hs[i - 1], [int(b % 8) * 100, int(b / 8) * 100])
        b += 1

    b = 0
    for i in sdlist:  # 显示现有商店
        if i > 0:
            sd = jl(picture_ss[i - 1], [int(b % 8) * 100, int(b / 8) * 100])
        b += 1

    b = 0
    for i in xxlist:  # 显示现有学校
        if i > 0:
            xx = jl(picture_cs[i - 1], [int(b % 8) * 100, int(b / 8) * 100])
        b += 1

    b = 0
    for i in yhlist:  # 显示现有银行
        if i > 0:
            yh = jl(picture_bs[i - 1], [int(b % 8) * 100, int(b / 8) * 100])
        b += 1

    nember_school = 0
    for i in xxlist:
        nember_school += (i * (1 + i)) / 2
    Pp = all_people
    if nember_school >= 1:
        Pp = int(1.1 ** nember_school * all_people)
    wz(("People: " + str(people + Pp) + "     All People:" + str(Pp) + "     Money:" + str(money)), [0, 0], 20)
    pygame.display.flip()


def lan(first, second, third, fourth):  # 显示栏，（）中first等为判定
    jl(picture_l, [3, 660])  # 栏
    jl(picture_c, [770, 658])  # 叉
    if first:
        jl(picture_hs[mjlist[xvhao]], [14, 680])
    if second:
        jl(picture_ss[sdlist[xvhao]], [125, 680])
    if third:
        jl(picture_cs[xxlist[xvhao]], [236, 680])
    if fourth:
        jl(picture_bs[yhlist[xvhao]], [347, 680])


def dlzc():
    global zhanghao, mima, all_people, people, money, mjlist, sdlist, xxlist, yhlist
    wanjiapd = input("登录（1），注册（2），查看游戏说明（3）")
    if wanjiapd == "1":
        zhanghao = input("账号：")
        while True:
            mima = input("密码：")
            first_line, all_people, people, money, mjlist, sdlist, xxlist, yhlist = writem.read(zhanghao + ".txt")
            if first_line == mima:
                print("登录成功，祝你游戏愉快！")
                break
            else:
                print("密码错误，请重新输入")


    elif wanjiapd == "2":
        print("如果你是一位新手玩家，建议您在阅读说明后再进行游戏")
        time.sleep(1)
        zhanghao = input("输入新账号：")
        mima = input("创建新密码：")

        all_people = 0
        people = 0
        money = 200

        mjlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sdlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        xxlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        yhlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        print("创建成功，祝你游戏愉快！")

    elif wanjiapd == "3":
        print("""
            迷你城市游戏说明
            1，打开游戏，运行（exe可执行文件、快捷方式直接双击打开，py文件可在python的IDLE中打开）。
            2，根据提示，若要登录打“1”，注册打“2”。
            3，输入账号密码（登录输错账号会报错，重新进入游戏再登即可）。
            4，等待后进入游戏主界面，点击土地可建造房屋，有绿框标注选中土地。
            5，栏中暂时有民居、商店、学校、银行4种建筑，各个建筑的作用、建造要求已标明于图标旁。
            6，开始时拥有200元，建议初次先建造 民居*2 加 商店*1，否则会陷入死局。
            7，祝玩家游戏愉快！
            注：注册的账号只能在本机上使用""")
        print()
        print()
        dlzc()


# 初始化
pygame.init()

# 引入图像
picture_k = pygame.image.load("lvkuang.png")

picture_l = pygame.image.load("lan.png")

picture_c = pygame.image.load("X.png")

picture_hs = [pygame.image.load("house first.png"),
              pygame.image.load("house second.png"),
              pygame.image.load("house third.png"),
              pygame.image.load("house fourth.png")]

picture_ss = [pygame.image.load("shop first.png"),
              pygame.image.load("shop second.png"),
              pygame.image.load("shop third.png"),
              pygame.image.load("shop fourth.png")]

picture_cs = [pygame.image.load("school first.png"),
              pygame.image.load("school second.png"),
              pygame.image.load("school third.png"),
              pygame.image.load("school fourth.png")]

picture_bs = [pygame.image.load("bank first.png"),
              pygame.image.load("bank second.png"),
              pygame.image.load("bank third.png"),
              pygame.image.load("bank fourth.png")]

# 初始化变量、列表
a = True
must = True

# 启
print("这是一个城市养成游戏")
print("当然，如果你是以像其他游戏那样的唯美画风而来的话")
print("那么你可以走了（因为连作者本人都不这么认为）")
print()
print()
dlzc()
# 主程序*************


screensize = [800, 800]
screen = pygame.display.set_mode(screensize)  # 设定屏幕大小
screen.fill([255, 255, 255])  # 建立屏幕（同时设定颜色）
s = pygame.image.load("screen.png")  # 设定背景图片
pygame.display.set_caption('Little_City')  # 设定窗口名称

xsxy()  # 显示现有

# 主循环**********


time_start = time.time()  # 开始时间
running = True
while running:
    for event in pygame.event.get():

        time_end = time.time()
        t = time_end - time_start
        if t >= 1:  # 判定时间并加钱
            nember_shop = 0
            for i in sdlist:
                nember_shop += (i * (1 + i)) / 2  # 算出商店数量

            nember_bank = 0
            for i in yhlist:
                nember_bank += (i * (1 + i)) / 2  # 算出银行数量

            money += int(3 * nember_shop * (1.3 ** nember_bank) * t)
            wz(("People: " + str(people + Pp) + "     All People:" + str(Pp) + "     Money:" + str(money)), [0, 0], 20)
            pygame.display.flip()
            time_start = time.time()

        if not a:
            # 显示建筑目的!!!!!!!!!!!!!!!!!!!!!!!!!!
            x, y = pygame.mouse.get_pos()
            if 14 < x < 114 and 680 < y < 780 and mjpd:
                wz("money:-" + str(50 * (mjlist[xvhao] + 1)), [14, 660], 20)
                wz("people:+" + str(int(5 * (mjlist[xvhao] + 2) * (mjlist[xvhao] + 1) / 2)), [14, 680], 20)
                pygame.display.flip()

            elif 125 < x < 225 and 680 < y < 780 and sdpd:
                wz("money:-" + str(75 * (sdlist[xvhao] + 1)) + " and +" + str(3 * (sdlist[xvhao] + 1)) + "/s",
                   [125, 660], 20)
                wz("people:-" + str(int(4 * (sdlist[xvhao] + 1))), [125, 680], 20)
                pygame.display.flip()

            elif 236 < x < 336 and 680 < y < 780 and xxpd:
                wz("money:-" + str(500 * (xxlist[xvhao] + 1)), [236, 660], 20)
                wz("people:-" + str(int(10 * (xxlist[xvhao] + 1))) + " and all*1.1", [236, 680], 20)
                pygame.display.flip()

            elif 347 < x < 447 and 680 < y < 780 and yhpd:
                wz("money:-" + str(2000 * (yhlist[xvhao] + 1)) + " and v*1.3", [347, 660], 20)
                wz("people:-" + str(30 * (yhlist[xvhao] + 1)), [347, 680], 20)
                pygame.display.flip()

            else:
                lan(mjpd, sdpd, xxpd, yhpd)

        if event.type == pygame.QUIT:  # 判定退出并保存
            things = [mima, all_people, people, money, mjlist, sdlist, xxlist, yhlist]
            writem.write(zhanghao + ".txt", things)
            wz("Save...", [100, 100], 50)
            pygame.display.flip()
            time.sleep(1)
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and must:  # 判定按下鼠标

            if a:  # 选中
                a = False
                xy = []  # 位置
                xy.append(int(event.pos[0] / 100) * 100)
                xy.append(int(event.pos[1] / 100) * 100)
                xvhao = int((xy[0] + xy[1] * 8) / 100)  # 序号
                xsxy()

                lk = jl(picture_k, xy)  # 绿框
                l = jl(picture_l, [3, 660])  # 栏
                c = jl(picture_c, [770, 658])  # 叉
                d = 0
                if sdlist[xvhao] == 0 and mjlist[xvhao] != 4 and xxlist[xvhao] == 0 and yhlist[xvhao] == 0:
                    lzmj = jl(picture_hs[mjlist[xvhao]], [14, 680])  # 栏中民居
                    mjpd = True
                else:
                    mjpd = False
                    d += 1
                if mjlist[xvhao] == 0 and sdlist[xvhao] != 4 and xxlist[xvhao] == 0 and yhlist[xvhao] == 0:
                    lzsd = jl(picture_ss[sdlist[xvhao]], [125, 680])  # 栏中商店
                    sdpd = True
                else:
                    sdpd = False
                    d += 1
                if sdlist[xvhao] == 0 and xxlist[xvhao] != 4 and mjlist[xvhao] == 0 and yhlist[xvhao] == 0:
                    lzxx = jl(picture_cs[xxlist[xvhao]], [236, 680])  # 栏中学校
                    xxpd = True
                else:
                    xxpd = False
                    d += 1
                if sdlist[xvhao] == 0 and yhlist[xvhao] != 4 and mjlist[xvhao] == 0 and xxlist[xvhao] == 0:
                    lzyh = jl(picture_bs[yhlist[xvhao]], [347, 680])  # 栏中银行
                    yhpd = True
                else:
                    yhpd = False
                    d += 1
                pygame.display.flip()
                if d == 4:
                    wz("MAX", [3, 660], 40)
                    pygame.display.flip()
                    must = False
                    time.sleep(3)
                    a = True
                    must = True

                    xsxy()

            else:
                if 770 < event.pos[0] < 795 and 658 < event.pos[1] < 683:  # 点叉
                    xsxy()
                    a = True


                elif 14 < event.pos[0] < 114 and 680 < event.pos[1] < 780 and mjpd:  # 点民居
                    if money >= 50 * (mjlist[xvhao] + 1):
                        money -= 50 * (mjlist[xvhao] + 1)
                        all_people += int(5 * ((mjlist[xvhao] + 2) * (mjlist[xvhao] + 1) / 2))
                        mjlist[xvhao] += 1
                        xsxy()
                        a = True
                    else:
                        p = wz("You don't have enough money", [0, 380], 40)
                        pygame.display.flip()
                        must = False
                        time.sleep(3)
                        xsxy()
                        must = True
                        a = True



                elif 125 < event.pos[0] < 225 and 680 < event.pos[1] < 780 and sdpd:  # 点商店
                    nember_school = 0
                    for i in xxlist:
                        nember_school += (i * (1 + i)) / 2
                    Pp = all_people
                    if nember_school >= 1:
                        Pp = int(1.1 ** nember_school * all_people)
                    if money >= 75 * (sdlist[xvhao] + 1) and (people + Pp) >= 4 * (sdlist[xvhao] + 1):
                        money -= 75 * (sdlist[xvhao] + 1)
                        people -= int(4 * (sdlist[xvhao] + 1))
                        sdlist[xvhao] += 1
                        xsxy()
                        a = True
                    else:
                        p = wz("You don't have enough money or people", [0, 380], 40)
                        pygame.display.flip()
                        must = False
                        time.sleep(3)
                        xsxy()
                        must = True
                        a = True



                elif 236 < event.pos[0] < 336 and 680 < event.pos[1] < 780 and xxpd:  # 点学校
                    nember_school = 0
                    for i in xxlist:
                        nember_school += (i * (1 + i)) / 2
                    Pp = all_people
                    if nember_school >= 1:
                        Pp = int(1.1 ** nember_school * all_people)
                    if money >= 500 * (xxlist[xvhao] + 1) and (people + Pp) >= (10 * (xxlist[xvhao] + 1)):
                        money -= 500 * (xxlist[xvhao] + 1)
                        people -= 10 * (xxlist[xvhao] + 1)
                        xxlist[xvhao] += 1
                        xsxy()
                        a = True
                    else:
                        p = wz("You don't have enough money or people", [0, 380], 40)
                        pygame.display.flip()
                        must = False
                        time.sleep(3)
                        xsxy()
                        must = True
                        a = True


                elif 347 < event.pos[0] < 447 and 680 < event.pos[1] < 780 and yhpd:  # 点银行
                    nember_school = 0
                    for i in xxlist:
                        nember_school += (i * (1 + i)) / 2
                    Pp = all_people
                    if nember_school >= 1:
                        Pp = int(1.1 ** nember_school * all_people)
                    if money >= 2000 * (yhlist[xvhao] + 1) and (people + Pp) >= (30 * (yhlist[xvhao] + 1)):
                        money -= 2000 * (yhlist[xvhao] + 1)
                        people -= 30 * (yhlist[xvhao] + 1)
                        yhlist[xvhao] += 1
                        xsxy()
                        a = True
                    else:
                        p = wz("You don't have enough money or people", [0, 380], 40)
                        pygame.display.flip()
                        must = False
                        time.sleep(3)
                        xsxy()
                        must = True
                        a = True

pygame.quit()
