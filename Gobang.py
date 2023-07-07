import sys
from tabnanny import check
import pygame
import os

# -------------------------------  全局变量  --------------------------------
# 棋盘变量:chesscolor 1 : 黑子 2 : 白子
chess = [[0]*15 for i in range(15)] 
chesscolor = 1

# -------------------------------  全局函数  --------------------------------
# -------------------------------  第一场景  --------------------------------
# 第一模块选项
def judge1(x,y):
    if x >= 150 and x <= 350 and y >= 192 and y <= 248:
        start_sound.play()
        return 1
    elif x >= 200 and x <= 300 and y >= 332 and y <= 388:
        start_sound.play()
        return 2
    return 0

# -------------------------------  第二场景 (人人对战) --------------------------------
# 开始按钮
def started1(x,y):
    if x >= 150 and x <= 350 and y >= 122 and y <= 178:
        start_sound.play()
        return 1

# 画棋盘
def drawline(screen):
    black = (0,0,0)
    for i in range(0,15) :
        start = (40 + i * 30,40)
        end = (40 + i * 30,460)
        pygame.draw.line(screen,black,start,end,1)
    for i in range(0,15) :
        start = (40,40 + i * 30)
        end = (460,40 + i * 30)
        pygame.draw.line(screen,black,start,end,1)
    pygame.draw.line(screen,black,(40,250),(460,250),2)
    pygame.draw.line(screen,black,(250,40),(250,460),2)
    pygame.draw.circle(screen,black,(250,250),6,0)
    pygame.draw.circle(screen,black,(130,130),5,0)
    pygame.draw.circle(screen,black,(370,370),5,0)
    pygame.draw.circle(screen,black,(370,130),5,0)
    pygame.draw.circle(screen,black,(130,370),5,0)

# 画棋子
def drawboard(screen):
    for i in range(0,15):
        for j in range(0,15):
            if chess[i][j] == 1 :
                pygame.draw.circle(screen,(0,0,0),(40+30*i,40+30*j),12,0)
            elif chess[i][j] == 2:
                pygame.draw.circle(screen,(235,235,235),(40+30*i,40+30*j),12,0)

# 改变棋子颜色
def changechess(x,y):
    if x < 40 or x > 460 or y < 40 or y > 460:
        return 1
    x-=40 
    y-=40
    i = x // 30
    j = y // 30
    if (x % 30) > 15 : 
        i += 1
    if (y % 30) > 15 :
        j += 1
    if chess[i][j] == 1 or chess[i][j] == 2 :
        return 1
    chess[i][j] = chesscolor
    down_sound.play()

# 画提示
def drawtip(screen,chesscolor):
    font = pygame.font.Font('font/方正综艺简体.ttf',25)
    black = font.render("黑方",True,(0,0,0),None)
    white = font.render("白方",True,(255,255,255),None)
    blackrect = black.get_rect()
    whiterect = white.get_rect()
    blackrect.center = (140,15)
    whiterect.center = (360,15)
    if chesscolor == 1:
        screen.blit(black,blackrect)
        pygame.draw.circle(screen,(0,0,0),(250,15),12,0)
    elif chesscolor == 2:
        screen.blit(white,whiterect)
        pygame.draw.circle(screen,(255,255,255),(250,15),12,0)
    
# 画工具栏
def drawtool(screen):
    font = pygame.font.Font("font/华康圆体W7.TTF",20)
    restart = font.render("[重新开始]",True,black,None)
    exit = font.render("[返回首页]",True,black,None)
    exitrect = exit.get_rect()
    restartrect = restart.get_rect()
    # print(exitrect)
    # print(restartrect)
    restartrect.center = (160,480)
    exitrect.center = (340,480)
    screen.blit(restart,restartrect)
    screen.blit(exit,exitrect)            

# 重新开始
def is_restart(x,y):
    if x >= 113 and x <= 207 and y >= 470 and y <= 490 :
        start_sound.play()
        return 1
    return 0

# 返回首页
def is_return_one(x,y):
    if x >= 150 and x <= 350 and y >= 272 and y <= 328:
        start_sound.play()
        return 1

# 返回首页(2)
def is_return(x,y):
    if x >= 293 and x <= 387 and y >= 470 and y <= 490:
        start_sound.play()
        return 1

# 判断输赢 (核心算法实现)
def select_winner():
    for i in range(0,15):
        for j in range(0,15):
            if chess[i][j] == 1 or chess[i][j] == 2 :
                """左"""
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x-1) < 0:
                        break;
                    if chess[x][y] == chess[x-1][y]:
                        num=num+1
                        x=x-1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''右'''
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x+1) > 14:
                        break;
                    if chess[x][y] == chess[x+1][y]:
                        num=num+1
                        x=x+1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''上'''
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (y + 1) > 14:
                        break;
                    if chess[x][y] == chess[x][y+1]:
                        num=num+1
                        y=y+1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''下'''
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (y-1) < 0:
                        break;
                    if chess[x][y] == chess[x][y-1]:
                        num=num+1
                        y=y-1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''左上'''
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x-1) < 0 or (y-1) < 0:
                        break;
                    if chess[x][y] == chess[x-1][y-1]:
                        num=num+1
                        x = x - 1
                        y = y - 1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''左下'''
                x = i
                y = j                
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x-1) < 0 or (y+1)>14:
                        break;
                    if chess[x][y] == chess[x-1][y+1]:
                        num=num+1
                        x = x - 1
                        y = y + 1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''右上'''
                x = i
                y = j                
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x+1)>14 or (y-1)<0:
                        break;
                    if chess[x][y] == chess[x+1][y-1]:
                        num=num+1
                        x = x + 1
                        y = y - 1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                '''右下'''
                x = i
                y = j
                num = 1
                while True:
                    if x < 0 or x > 14 or y < 0 or y > 14 or (x+1)>14 or (y+1)>14:
                        break;
                    if chess[x][y] == chess[x+1][y+1]:
                        num=num+1
                        x = x + 1
                        y = y + 1
                    else :
                        break
                if num >=5 :
                    return chess[i][j]
                                
# --------------------------------   第三场景   -------------------------------

# 绘画结束画面
def drawend(screen,winner):
    font = pygame.font.Font("font/方正综艺简体.ttf",50)
    win1 = font.render("恭喜黑方获得胜利!",True,black,None)
    win2 = font.render("恭喜白子获得胜利!",True,white,None)
    restart = font.render("[重新开始]",True,black,None)
    zhu = font.render("[返回主菜单]",True,black,None)
    restartrect = restart.get_rect()
    zhurect = zhu.get_rect() 
    win1rect = win1.get_rect()
    win2rect = win2.get_rect()
    # print(restartrect)
    # print(zhurect)
    win1rect.center = (250,80)
    win2rect.center = (250,80)
    restartrect.center = (250,220)
    zhurect.center = (250,360)
    if winner == 1:
        screen.blit(win1,win1rect)
    elif winner == 2:
        screen.blit(win2,win2rect)
    screen.blit(restart,restartrect)
    screen.blit(zhu,zhurect)    

# 第三场景选项
def judge2(x,y):
    if x >= 133 and x <= 367 and y >= 192 and y <= 248:
        start_sound.play()
        return 1
    # elif x >= 108 and x <= 392 and y >= 332 and y <= 388:
    #     start_sound.play()
    return 2

# ---------------------------------   主函数   --------------------------------
# 初始化pygame
pygame.init()
pygame.mixer.init()
# 加载背景音乐

# pygame.mixer.music.load("music/bgm.ogg")
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play()

# 设定主窗口标题
pygame.display.set_caption("五子棋V1.0.0")
# 图片加载
# icon = pygame.image.load("images/qipan.png")
background0 = pygame.image.load("images/background0.jpg")
background = pygame.image.load("images/background.jpg")
# pygame.display.set_icon(icon)
# 字体加载
font = pygame.font.Font('font/BABYFACE.TTF',50)
# 音效加载
start_sound = pygame.mixer.Sound("music/start.wav")
start_sound.set_volume(0.2)
down_sound = pygame.mixer.Sound("music/down.wav")
down_sound.set_volume(0.2)
victory_sound = pygame.mixer.Sound("music/victory.wav")
victory_sound.set_volume(0.6)
# 主窗口
screen = pygame.display.set_mode((500,500))
# 颜色
black  = (0,0,0)
white = (255,255,255)
# 主循环
zero = True # 主循环条件
first = True # 第一场景条件
third = True # 第三场景条件    

while zero : 
    # 第一场景
    winner = 0
    # index = 0 # 第一场景选项
    if first == True:
        index = 0
    elif first == False:
        index = 1
    while first :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 程序出口
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                index = judge1(x,y)
                if index != 0 and index != 2:
                    first = False
                elif index == 2:
                    pygame.quit()
                    sys.exit()
        screen.blit(background0,(0,0))
        text1 = font.render("五子棋大战",True,(0,0,0),None)
        text2 = font.render("人人对战",True,(0,0,0),None)
        text3 = font.render("退出",True,(0,0,0),None)
        text1rect = text1.get_rect()
        text2rect = text2.get_rect()
        text3rect = text3.get_rect()
        # print(text3rect)
        text1rect.center=(250,80)
        text2rect.center=(250,220)
        text3rect.center=(250,360)
        screen.blit(text1,text1rect)
        screen.blit(text2,text2rect)
        screen.blit(text3,text3rect)
        pygame.display.flip()
    
    # print(index)

    # 第二场景
    second = True
    is_start= True
    # 人人对战
    if index == 1: 
        while is_start :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # 卸载pygame模块
                    sys.exit() # 终止程序
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    # print(event.pos)
                    x,y=event.pos # 获取当前坐标
                    if started1(x,y) == 1 :
                        is_start = False
                    elif is_return_one(x,y) == 1:
                        is_start = False
                        second = False
                        third = False
                        first = True
            
            text = font.render("开始游戏",True,(0,0,0),None)
            text1 = font.render("返回",True,(0,0,0),None)
            textrect = text.get_rect()
            text1rect = text1.get_rect()
            # print(text1rect)
            # print(textrect)
            textrect.center=(250,150)
            text1rect.center=(250,300)
            screen.blit(background,(0,0))
            screen.blit(text,textrect)
            screen.blit(text1,text1rect)
            screen.blit(text,textrect)
            pygame.display.flip() # 更新屏幕内容
        while second :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # 卸载pygame模块
                    sys.exit() # 终止程序
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    # print(event.pos)
                    x,y=event.pos # 获取当前坐标
                    if changechess(x,y) != 1: # 改变棋子颜色
                        if chesscolor == 1 :
                            chesscolor = 2
                        else : 
                            chesscolor = 1
                    if is_restart(x,y) == 1:
                        for i in range(0,15):
                            for j in range(0,15):
                                chess[i][j] = 0
                                chesscolor = 1
                    if is_return(x,y) == 1:
                        third = False
                        second = False
                        first = True
                        chesscolor = 1
                        for i in range(0,15):
                            for j in range(0,15):
                                chess[i][j] = 0
                    elif event.type == pygame.MOUSEMOTION:
                        x,y = event.pos

            winner = select_winner()
            if winner == 1 or winner == 2:
                victory_sound.play()
                second = False
                third = True
            screen.blit(background,(0,0)) # 加载背景
            drawline(screen) # 画棋盘
            drawboard(screen) # 画棋子
            drawtip(screen,chesscolor) # 画提示
            drawtool(screen) # 画工具栏 （重新开始 及 返回首页）
            
            # pygame.draw.circle(screen,(0,0,0),(40,40),12,0)
            # pygame.draw.circle(screen,(235,235,235),(70,40),12,0)
            pygame.display.flip() # 更新屏幕内容

    # 第三场景
    
    while third :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 程序出口
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                index = judge2(x,y)
                if index == 1:
                    third = False
                    # 清空棋盘
                    for i in range(0,15):
                        for j in range(0,15):
                            chess[i][j] = 0
                    chesscolor = 1
                    first = False
                elif index == 2:
                    third = False
                    # 清空棋盘
                    for i in range(0,15):
                        for j in range(0,15):
                            chess[i][j] = 0
                    chesscolor = 1
                    first = True
        screen.blit(background0,(0,0))
        drawend(screen,winner)
        pygame.display.flip()
