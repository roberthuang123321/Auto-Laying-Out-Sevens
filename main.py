import pyautogui, time
pyautogui.useImageNotFoundException()
# 偵測梅花1~13的副程式
def c_find(i, a, b, c, d):
    try :
        i[0] = pyautogui.locateOnScreen('c1.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass
    try:
        i[1] = pyautogui.locateOnScreen('c2.png', confidence=0.93, region=(a, b, c, d))
    except :
        pass
    try :
        i[2] = pyautogui.locateOnScreen('c3.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass

    try :
        i[3] = pyautogui.locateOnScreen('c4.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass
    try:
        i[4] = pyautogui.locateOnScreen('c5.png', confidence=0.95, region=(a, b, c, d))
    except :
        pass
    try :
        i[5] = pyautogui.locateOnScreen('c6.png', confidence=0.95, region=(a, b, c, d))
    except:
        pass

    try :
        i[6] = pyautogui.locateOnScreen('c7.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass
    try:
        i[7] = pyautogui.locateOnScreen('c8.png', confidence=0.94, region=(a, b, c, d))
    except :
        pass
    try :
        i[8] = pyautogui.locateOnScreen('c9.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try :
        i[9] = pyautogui.locateOnScreen('c10.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try :
        i[10] = pyautogui.locateOnScreen('c11.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[11] = pyautogui.locateOnScreen('c12.png', confidence=0.94, region=(a, b, c, d))
    except :
        pass
    try :
        i[12] = pyautogui.locateOnScreen('c13.png', confidence=0.99, region=(a, b, c, d))
    except:
        pass

# 偵測方塊1~13的副程式
def d_find(i, a, b, c, d):
    try:
        i[0] = pyautogui.locateOnScreen('d1.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[1] = pyautogui.locateOnScreen('d2.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[2] = pyautogui.locateOnScreen('d3.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[3] = pyautogui.locateOnScreen('d4.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[4] = pyautogui.locateOnScreen('d5.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[5] = pyautogui.locateOnScreen('d6.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[6] = pyautogui.locateOnScreen('d7.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[7] = pyautogui.locateOnScreen('d8.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[8] = pyautogui.locateOnScreen('d9.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[9] = pyautogui.locateOnScreen('d10.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[10] = pyautogui.locateOnScreen('d11.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[11] = pyautogui.locateOnScreen('d12.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[12] = pyautogui.locateOnScreen('d13.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
# 偵測紅心1~13的副程式
def h_find(i, a, b, c, d):
    try:
        i[0] = pyautogui.locateOnScreen('h1.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[1] = pyautogui.locateOnScreen('h2.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[2] = pyautogui.locateOnScreen('h3.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[3] = pyautogui.locateOnScreen('h4.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[4] = pyautogui.locateOnScreen('h5.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[5] = pyautogui.locateOnScreen('h6.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[6] = pyautogui.locateOnScreen('h7.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[7] = pyautogui.locateOnScreen('h8.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[8] = pyautogui.locateOnScreen('h9.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[9] = pyautogui.locateOnScreen('h10.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[10] = pyautogui.locateOnScreen('h11.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[11] = pyautogui.locateOnScreen('h12.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[12] = pyautogui.locateOnScreen('h13.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
# 偵測黑桃1~13的副程式
def s_find(i, a, b, c, d):
    try:
        i[0] = pyautogui.locateOnScreen('s1.png', confidence=0.9, region=(a, b, c, d))
    except:
        pass
    try:
        i[1] = pyautogui.locateOnScreen('s2.png', confidence=0.9, region=(a, b, c, d))
    except:
        pass
    try:
        i[2] = pyautogui.locateOnScreen('s3.png', confidence=0.9, region=(a, b, c, d))
    except:
        pass

    try:
        i[3] = pyautogui.locateOnScreen('s4.png', confidence=0.9, region=(a, b, c, d))
    except:
        pass
    try:
        i[4] = pyautogui.locateOnScreen('s5.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass
    try:
        i[5] = pyautogui.locateOnScreen('s6.png', confidence=0.93, region=(a, b, c, d))
    except:
        pass

    try:
        i[6] = pyautogui.locateOnScreen('s7.png', confidence=0.9, region=(a, b, c, d))
    except:
        pass
    try:
        i[7] = pyautogui.locateOnScreen('s8.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[8] = pyautogui.locateOnScreen('s9.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[9] = pyautogui.locateOnScreen('s10.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass

    try:
        i[10] = pyautogui.locateOnScreen('s11.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[11] = pyautogui.locateOnScreen('s12.png', confidence=0.94, region=(a, b, c, d))
    except:
        pass
    try:
        i[12] = pyautogui.locateOnScreen('s13.png', confidence=0.99, region=(a, b, c, d))
    except:
        pass



# 進入網頁
pyautogui.FAILSAFE = True
pyautogui.click(897, 1063)
pyautogui.PAUSE = 1
pyautogui.click(170, 53)
pyautogui.PAUSE = 1
pyautogui.typewrite(' https://laijunbin.github.io/sevens/ ')
pyautogui.press('enter')
pyautogui.PAUSE = 1
pyautogui.click(61, 176)
# 設定檯面&手牌list
c_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
h_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

c_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
h_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
s_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#回合程式
for i in range(1, 14):
    print("round", i)
    pyautogui.moveTo(59, 198)
    # 每回合重置list
    c_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    h_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s_table_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    c_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    d_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    h_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s_hand_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 等待對手出牌
    time.sleep(6)
    # 每回合重新偵測檯面上、手牌有甚麼
    c_find(c_table_list, 464, 289, 198, 340)   #梅花table region(464, 289, 198, 340)
    d_find(d_table_list, 719, 289, 198, 340)   #方塊table region(719, 289, 198, 340)
    h_find(h_table_list, 994, 289, 198, 340)   #紅心table region(994, 289, 198, 340)
    s_find(s_table_list, 1286, 289, 198, 340)   #黑桃table region(1286, 289, 198, 340)

    c_find(c_hand_list, 580, 660, 621, 294)  #  手牌 region(580, 660, 621, 294)
    d_find(d_hand_list, 580, 660, 621, 294)
    h_find(h_hand_list, 580, 660, 621, 294)
    s_find(s_hand_list, 580, 660, 621, 294)

    print(c_table_list)  #debug用 看偵測的對不對
    print(d_table_list)
    print(h_table_list)
    print(s_table_list)
    print(c_hand_list)
    print(d_hand_list)
    print(h_hand_list)
    print(s_hand_list)
    # 有7就直接先脫手
    if c_hand_list[6] != 0 :
        pyautogui.click(c_hand_list[6])

        continue


    elif d_hand_list[6] != 0 :
        pyautogui.click(d_hand_list[6])

        continue


    elif h_hand_list[6] != 0:
        pyautogui.click(h_hand_list[6])

        continue


    elif s_hand_list[6] != 0:
        pyautogui.click(s_hand_list[6])

        continue

    # 判斷要出甚麼
    else :

            for j in range(1, 13):

                if j<6 :
                    if c_table_list[j] !=0 :
                        if c_hand_list[j-1] !=0 :
                            pyautogui.click(c_hand_list[j-1])
                            break
                        elif d_table_list[j] != 0:
                            if d_hand_list[j - 1] != 0:
                                pyautogui.click(d_hand_list[j - 1])
                                break
                            elif h_table_list[j] != 0:
                                if h_hand_list[j - 1] != 0:
                                    pyautogui.click(h_hand_list[j - 1])
                                    break
                                elif s_table_list[j] != 0:
                                    if s_hand_list[j - 1] != 0:
                                        pyautogui.click(s_hand_list[j - 1])
                                        break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                        elif h_table_list[j] != 0:
                            if h_hand_list[j - 1] != 0:
                                pyautogui.click(h_hand_list[j - 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break

                    elif d_table_list[j] !=0 :
                        if d_hand_list[j-1] !=0 :
                            pyautogui.click(d_hand_list[j-1])
                            break
                        elif h_table_list[j] != 0:
                            if h_hand_list[j - 1] != 0:
                                pyautogui.click(h_hand_list[j - 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break
                    elif h_table_list[j] !=0 :
                        if h_hand_list[j-1] !=0 :
                            pyautogui.click(h_hand_list[j-1])
                            break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break
                    elif s_table_list[j] !=0 :
                        if s_hand_list[j-1] !=0 :
                            pyautogui.click(s_hand_list[j-1])
                            break
                elif j == 6 :
                    if c_table_list[j] != 0:
                        if c_hand_list[j - 1] != 0:
                            pyautogui.click(c_hand_list[j - 1])
                            break
                        elif c_hand_list[j + 1] != 0:
                            pyautogui.click(c_hand_list[j + 1])
                            break
                        elif d_table_list[j] != 0:
                            if d_hand_list[j - 1] != 0:
                                pyautogui.click(d_hand_list[j - 1])
                                break
                            elif d_hand_list[j + 1] != 0:
                                pyautogui.click(d_hand_list[j + 1])
                                break
                            elif h_table_list[j] != 0:
                                if h_hand_list[j - 1] != 0:
                                    pyautogui.click(h_hand_list[j - 1])
                                    break
                                elif h_hand_list[j + 1] != 0:
                                    pyautogui.click(h_hand_list[j + 1])
                                    break
                                elif s_table_list[j] != 0:
                                    if s_hand_list[j - 1] != 0:
                                        pyautogui.click(s_hand_list[j - 1])
                                        break
                                    elif s_hand_list[j + 1] != 0:
                                        pyautogui.click(s_hand_list[j + 1])
                                        break

                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                                elif s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break

                        elif h_table_list[j] != 0:
                            if h_hand_list[j - 1] != 0:
                                pyautogui.click(h_hand_list[j - 1])
                                break
                            elif h_hand_list[j + 1] != 0:
                                pyautogui.click(h_hand_list[j + 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                                elif s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break

                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break
                            elif s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break


                    elif d_table_list[j] != 0 :
                        if d_hand_list[j - 1] != 0:
                            pyautogui.click(d_hand_list[j - 1])
                            break
                        elif d_hand_list[j + 1] != 0:
                            pyautogui.click(d_hand_list[j + 1])
                            break
                        elif h_table_list[j] != 0:
                            if h_hand_list[j - 1] != 0:
                                pyautogui.click(h_hand_list[j - 1])
                                break
                            elif h_hand_list[j + 1] != 0:
                                pyautogui.click(h_hand_list[j + 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j - 1] != 0:
                                    pyautogui.click(s_hand_list[j - 1])
                                    break
                                elif s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break

                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break
                            elif s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break

                    elif h_table_list[j] != 0 :
                        if h_hand_list[j - 1] != 0:
                            pyautogui.click(h_hand_list[j - 1])
                            break
                        elif h_hand_list[j + 1] != 0:
                            pyautogui.click(h_hand_list[j + 1])
                            break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j - 1] != 0:
                                pyautogui.click(s_hand_list[j - 1])
                                break
                            elif s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break

                    elif s_table_list[j] != 0:
                        if s_hand_list[j - 1] != 0:
                            pyautogui.click(s_hand_list[j - 1])
                            break
                        elif s_hand_list[j + 1] != 0:
                            pyautogui.click(s_hand_list[j + 1])
                            break

                elif 6 < j < 12:
                    if c_table_list[j] != 0:
                        if c_hand_list[j + 1] != 0:
                            pyautogui.click(c_hand_list[j + 1])
                            break
                        elif d_table_list[j] != 0:
                            if d_hand_list[j + 1] != 0:
                                pyautogui.click(d_hand_list[j + 1])
                                break
                            elif h_table_list[j] != 0:
                                if h_hand_list[j + 1] != 0:
                                    pyautogui.click(h_hand_list[j + 1])
                                    break
                                elif s_table_list[j] != 0:
                                    if s_hand_list[j + 1] != 0:
                                        pyautogui.click(s_hand_list[j + 1])
                                        break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break
                        elif h_table_list[j] != 0:
                            if h_hand_list[j + 1] != 0:
                                pyautogui.click(h_hand_list[j + 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break

                    elif d_table_list[j] != 0:
                        if d_hand_list[j + 1] != 0:
                            pyautogui.click(d_hand_list[j + 1])
                            break
                        elif h_table_list[j] != 0:
                            if h_hand_list[j + 1] != 0:
                                pyautogui.click(h_hand_list[j + 1])
                                break
                            elif s_table_list[j] != 0:
                                if s_hand_list[j + 1] != 0:
                                    pyautogui.click(s_hand_list[j + 1])
                                    break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break
                    elif h_table_list[j] != 0:
                        if h_hand_list[j + 1] != 0:
                            pyautogui.click(h_hand_list[j + 1])
                            break
                        elif s_table_list[j] != 0:
                            if s_hand_list[j + 1] != 0:
                                pyautogui.click(s_hand_list[j + 1])
                                break
                    elif s_table_list[j] != 0:
                        if s_hand_list[j + 1] != 0:
                            pyautogui.click(s_hand_list[j + 1])
                            break


                else :

                    for j in range(0, 13):
                        if c_hand_list[j] !=0 :
                            pyautogui.click(c_hand_list[j])
                            break
                        elif d_hand_list[j] !=0 :
                            pyautogui.click(d_hand_list[j])
                            break
                        elif h_hand_list[j] !=0 :
                            pyautogui.click(h_hand_list[j])
                            break
                        elif s_hand_list[j] !=0 :
                            pyautogui.click(s_hand_list[j])
                            break


# 偵測並點選結束畫面的提示
loc =0
try :
    loc = pyautogui.locateOnScreen('end.png', confidence=0.9)
except :
    pass
while loc == 0:
    time.sleep(0.1)
    try :
        loc = pyautogui.locateOnScreen('end.png', confidence=0.9)
    except :
        pass
pyautogui.click(loc)

