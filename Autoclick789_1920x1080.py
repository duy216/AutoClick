import pyautogui
import time
import cv2
import numpy as np
import pymsgbox
import logging
import configparser
from datetime import datetime
import winsound
import os
import math
import random


config = configparser.RawConfigParser()
config.read('config.txt')
details_dict = dict(config.items('Config'))

TILE = 0.98
base_money = int(details_dict["base_money"])
cat_lo = int(details_dict["cat_lo"])
cat_lai = int(details_dict["cat_lai"])
cat_lai_tien = int(details_dict["cat_lai_tien"])
auto_shutdown = details_dict["auto_shutdown"]
ti_le_gap = float(details_dict["ti_le_gap"])
dao_cay_so = int(details_dict["dao_cay_so"])
danh_theo_lich_su = int(details_dict["danh_theo_lich_su"])
capture = details_dict["capture"]
sanjackpot = int(details_dict["sanjackpot"])
tham_lam = int(details_dict["tham_lam"])
chenh_lech_nguy_hiem = int(details_dict["chenh_lech_nguy_hiem"])
pattern_cl = details_dict["pattern_cl"].split(',')
pattern_cl1 = details_dict["pattern_cl1"].split(',')
pattern_cl0 = details_dict["pattern_cl0"].split(',')

config_str = '''
base_money={0}
cat_lo={1}
cat_lai={2}
auto_shutdown={3}
ti_le_gap={4}
dao_cay_so={5}
danh_theo_lich_su={6}
capture={7}
chenh_lech_nguy_hiem={8} 
'''.format(base_money, cat_lo, cat_lai, auto_shutdown, ti_le_gap, dao_cay_so, danh_theo_lich_su, capture, chenh_lech_nguy_hiem)

# Speed up autogui action
pyautogui.PAUSE = 0.001
pyautogui.FAILSAFE = False

buttonx_chan, buttony_chan = 636, 442
buttonx_le, buttony_le = 1283, 450
buttonx_8, buttony_8 = 766, 496
buttonx_9, buttony_9 = 951, 492


cnt_89 = 0
chon = ""
money = base_money
chonben = "chan"

# pattern_cl = list()
# for i in range(0, cat_lo):
#     pattern_cl.append("le")
# pattern_cl = ['le', 'le', 'le', 'chan', 'chan', 'le', 'chan', 'le', 'chan']
# pattern_chan = ['le', 'le', 'le', 'chan', 'chan', 'le', 'chan', 'le', 'chan']

BASE_100 = 100
BASE_500 = 500
BASE_1000 = 1000
BASE_5000 = 5000

pymsgbox.rootWindowPosition = "+900+100"


# LOGGER
now = datetime.now()  # current date and time
date_time = now.strftime("%m%d%Y_%H%M%S")
logging.basicConfig(filename="Autoclick789_{0}.log".format(date_time),
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.INFO)


def read_config():
    global base_money, cat_lo, cat_lai, cat_lai_tien, ti_le_gap

    config = configparser.RawConfigParser()
    config.read('config.txt')
    details_dict = dict(config.items('Config'))

    log_info_and_print("reload config")
    base_money = int(details_dict["base_money"])
    cat_lo = int(details_dict["cat_lo"])
    cat_lai = int(details_dict["cat_lai"])
    cat_lai_tien = int(details_dict["cat_lai_tien"])
    ti_le_gap = float(details_dict["ti_le_gap"])


def log_info_and_print(s):
    print(s)
    logger.info(s)


def log_debug_and_print(s):
    print(s)
    logger.debug(s)


def shutdown():
    if auto_shutdown == "1":
        os.system("shutdown /s /t 1")


def intro():
    global config_str
    s = '''
    Tool ***************** 
    Create by   : DuyNN
    Date        : 2022-12-16
    Version     : Pro max
    Support resolution 1920x1080
    '''

    log_info_and_print(s)
    log_info_and_print(config_str)


def mse(img1, img2):
    h, w, c = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))
    return mse, diff


def chon_giong_con_truoc_cua_san(contruoccuasan):
    return contruoccuasan


def chon_khac_con_truoc_cua_san(contruoccuasan):
    return "le" if contruoccuasan == "chan" else "chan"


def chon_ngau_nhien():
    return "le" if random.randint(0, 1) == 1 else "chan"


def danh_vao_dau(cl89, so_tien):

    temp = so_tien
    cnt5000 = temp // BASE_5000
    temp = temp % BASE_5000
    cnt1000 = temp // BASE_1000
    temp = temp % BASE_1000
    cnt500 = temp // BASE_500
    temp = temp % BASE_500
    cnt100 = temp // BASE_100
    print("5000:1000:500:100")
    print(cnt5000, cnt1000, cnt500, cnt100)
    if cl89 == "chan":
        buttonx = buttonx_chan
        buttony = buttony_chan
    elif cl89 == "le":
        buttonx = buttonx_le
        buttony = buttony_le
    elif cl89 == "8":
        buttonx = buttonx_8
        buttony = buttony_8
    elif cl89 == "9":
        buttonx = buttonx_9
        buttony = buttony_9

    if cnt5000:
        click_base_chip(BASE_5000)
    for i in range(0, cnt5000):
        pyautogui.click(buttonx, buttony)
    if cnt1000:
        click_base_chip(BASE_1000)
    for i in range(0, cnt1000):
        pyautogui.click(buttonx, buttony)
    if cnt500:
        click_base_chip(BASE_500)
    for i in range(0, cnt500):
        pyautogui.click(buttonx, buttony)
    if cnt100:
        click_base_chip(BASE_100)
    for i in range(0, cnt100):
        pyautogui.click(buttonx, buttony)


def bet(cl, so_tien):

    danh_vao_dau(cl, so_tien)
        
    return cl


# Only use function when capture image fisrt time for a resolution
def get_real_image():

    log_info_and_print("Captute Image first time at a computer ")
    im1_state = pyautogui.screenshot(region=(798, 877, 50, 40))
    im1_state.save('Image/100.PNG')

    im1_state = pyautogui.screenshot(region=(907, 875, 50, 40))
    im1_state.save('Image/500.PNG')

    im1_state = pyautogui.screenshot(region=(1017, 874, 50, 40))
    im1_state.save('Image/1000.PNG')

    im1_state = pyautogui.screenshot(region=(1128, 877, 50, 40))
    im1_state.save('Image/5000.PNG')

    im1_state = pyautogui.screenshot(region=(638, 356, 148, 11))
    im1_state.save('Image/CDC.PNG')

    im_CL = pyautogui.screenshot(region=(1348, 625, 5, 5))
    im_CL.save('Image/ConMucCL_capture.PNG')


def chon_day_tiep_theo():
    global history, win_at, danh_theo_lich_su, cat_lo, dao_cay_so, dict_win, dict_lose, cnt

    # chuki = random.randint(1, cat_lo-2)
    # ret = history[(-8 - chuki - 1):-chuki]
    # ret = pattern_cl
    # ret = [e if idx != cnt-1 else chon_khac_con_truoc_cua_san(e) for idx,e in enumerate(ret)]

    if history[-1] == 'chan':
        ret = pattern_cl0
    else:
        ret = pattern_cl1

    # temp=cnt
    # ret[cnt] = "le" if ret[cnt] == "chan" else "chan"
    # # if not danh_theo_lich_su:
    #     ret = ["le" if e == "chan" else "chan" for e in ret]
    # else:
    #     ret = pattern_cl1 if history[-1] == "chan" else pattern_cl0
    # if 0 < dao_cay_so < cat_lo:
    #     for i in range(dao_cay_so, cat_lo):
    #         if dict_lose[i] - dict_win[i] > 0 and (dict_lose[i] - dict_win[i]) % 2 == 0:
    #         # if math.fabs(dict_lose[i] - dict_win[i]) % 2 == 0:
    #             log_info_and_print("Dao cay so " + str(i))
    #             ret[i-1] = "chan" if ret[dao_cay_so-1] == "le" else "le"
    #             break

    log_info_and_print('history: ' + str(history[-cat_lo:]))
    log_info_and_print('chon_day_tiep_theo: ' + str(ret))

    return ret


lai_1_day = 0
alpha = 0
# tien_moi_luot = [1, 3, 4, 7.9, 15.5, 31.7, 63.5, 127.5, 256, 512, 1024, 2546, 5194, 10597, 21618]
# tien_moi_luot = [1, 2, 4, 9, 18, 40, 80, 127.5, 256, 512, 1024, 2546, 5194, 10597, 21618]
# tien_moi_luot = [1, 2, 4, 9, 5, 25, 50, 100, 256, 512, 1024, 2546, 5194, 10597, 21618]
tien_moi_luot = [1, 2, 1.5, 2.5, 3.5, 5, 8, 24.5, 50, 102, 250]
# tien_moi_luot = [1, 0.9, 3, 6, 12, 25, 50, 105, 250]
# tien_moi_luot = [1, 2, 3, 1, 3, 2, 15, 30, 60, 120, 250]

tien_moi_luot = [1, 0.5, 1, 2, 4, 9, 20, 40, 80]



def play_turn(con_truoc_cua_san):
    global money, cnt, history, chonben, pattern_cl, cnt_lose, cnt_win, alpha, cnt_89

    number_click = ti_le_gap ** cnt
    log_info_and_print("chonben ={0}, number_click={1}".format(chonben, number_click))
    # if alpha > 10:
    #     money = math.ceil(number_click * (base_money + 100))
    # elif alpha < -15:
    #     money = math.floor(number_click * (base_money - 100))
    # else:
    #     money = math.ceil(number_click * base_money)


    money = math.ceil(number_click * base_money) // BASE_100 * BASE_100

# money = math.ceil(tien_moi_luot[cnt] * base_money)
    # money = math.ceil(number_click * base_money)

    # danhgi = con_truoc_cua_san if cnt > 3 else chon_khac_con_truoc_cua_san(con_truoc_cua_san)
    # danhgi = chon_ngau_nhien()
    danhgi = pattern_cl[cnt]
    chon = bet(danhgi, money)

    play_turn_log = "Dat luot so {0} vao {1}, So tien: {2}".format(cnt + 1, chon.upper(), money)
    log_info_and_print(play_turn_log)

    return chon


basemoneyList = [1600, 800, 400]
cat_lo_dict = {400: 11, 800: 10, 1600: 9}
# print(random.choices(numberList, weights=(20, 10, 40, 20, 10), k=1))
# Output [555, 222, 555, 222, 555]


def refresh():
    global cnt, chon, win, money, alpha, cnt_win, cnt_lose, pattern_cl, lai_1_day, base_money, cat_lo
    log_info_and_print("Refresh")

    chon = ""
    lai_1_day = 0
    alpha = cnt_lose - cnt_win
    if tham_lam:
        base_money = random.choices(basemoneyList, weights=(50, 30, 20), k=1)[0]
        cat_lo = cat_lo_dict[base_money]
    # if  cnt >= 5:
    pattern_cl = chon_day_tiep_theo()
    # pattern_cl[cnt] = "le" if pattern_cl[cnt] == "chan" else "chan"
    # pattern_cl[cnt] = "le" if pattern_cl[cnt] == "chan" else "chan"

    cnt = 0


def doc_con_truoc_cua_san():
    im_CL = pyautogui.screenshot(region=(1893, 875, 5, 5))
    im_CL.save('Image/ConMucCL.PNG')
    im_CL = cv2.imread('Image/ConMucCL.PNG')
    error, diff = mse(im_CL, img_ConMucChan)
    log_debug_and_print("Image matching Error between the img_ConMucChan im_CL: {0}".format(error))

    if error < 50:
        contruoccuasan = "chan"
    else:
        contruoccuasan = "le"
    log_info_and_print("Con truoc cua san la {0}".format(contruoccuasan.upper()))
    return contruoccuasan


def prevent_jackpot():
    x, y = (960, 540)

    pyautogui.click(x, y)
    pyautogui.click(x, y)


def shutdown():
    if auto_shutdown == "1":
        os.system("shutdown /s /t 1")


def detect_cat_lo(cnt):
    global cat_lo
    number = cnt
    if number >= cat_lo and not win:
        log_info_and_print("CAT LO. Thua lien tiep {0} con. ".format(cat_lo))
        return True
    return False


def detect_cat_lai():
    global cnt_win, tong_lai

    if cnt_win >= cat_lai or tong_lai >= cat_lai_tien:
        log_info_and_print("CAT LAI. Thang {0} van. ".format(cnt_win))
        return True
    return False


def detect_refresh():
    global cnt

    if cnt not in (3, 4, 5, 6, 7):
        return True
    return False

# Xac suat win:lose ~ 1:1. Neu win > lose thi sac xuat nhung con tiep theo se thua lon hon


def detect_dangerous():
    global cnt_win, cnt_lose, chenh_lech_nguy_hiem

    return True if math.fabs(cnt_win - cnt_lose) >= chenh_lech_nguy_hiem else False


def click_base_chip(base_chip):
    # Set default base chip
    buttonx_basebet, buttony_basebet = pyautogui.locateCenterOnScreen('Image/{0}.PNG'.format(str(base_chip)), confidence=0.9)
    pyautogui.moveTo(buttonx_basebet, buttony_basebet)
    pyautogui.click(buttonx_basebet, buttony_basebet)


def send_message_telegram():
    pass


intro()
pyautogui.alert(text="Start Auto Click", title='control game', timeout=5000)
log_info_and_print("Chon cua so 789 trong 5 giay")
log_info_and_print("5")
time.sleep(1)
log_info_and_print("4")
time.sleep(1)
log_info_and_print("3")
time.sleep(1)
log_info_and_print("2")
time.sleep(1)
log_info_and_print("1")
time.sleep(1)
log_info_and_print("Start auto click")

history = list()
# detect_jackpot()
img_CDC = cv2.imread('Image/CDC.PNG')
img_ConMucChan = cv2.imread('Image/ConMucChan.PNG')
img_ConMucLe = cv2.imread('Image/ConMucLe.PNG')
win = False
cnt_win = 0
cnt_lose = 0
dict_win = {}
dict_lose = {}

for i in range(1, cat_lo+3):
    dict_win[i] = 0
    dict_lose[i] = 0


if capture == "1":

    get_real_image()
    click_base_chip(BASE_5000)
    exit(0)
# click_base_chip(BASE_100)

# refresh()
cnt = -1
color = "DoiLuotMoi"
tong_lai = 0
while True:

    im1_state = pyautogui.screenshot(region=(891, 492, 141, 27))
    im1_state.save('Image/state.PNG')
    img_state = cv2.imread('Image/state.PNG')

    error, diff = mse(img_state, img_CDC)
    log_debug_and_print("Image matching Error between CDC and state: {0}".format(error))

    if error < 50:
        if color == "DoiLuotMoi":
            # read_config()
            color = "ChoDatTien"

            con_truoc_cua_san = doc_con_truoc_cua_san()
            history.append(con_truoc_cua_san)
            cnt += 1
            if chon == con_truoc_cua_san:
                log_info_and_print("Thang o luot so {0}".format(cnt))
                win = True
                lai_1_day += money*TILE
                dict_win[cnt] += 1
                if lai_1_day > 0:
                    tong_lai += lai_1_day
                    log_info_and_print("Lai 1 day: {0}".format(lai_1_day))
                    refresh()

                cnt_win += 1
                if cnt_win % 20:
                    log_info_and_print(history)

            else:
                if chon != "":
                    win = False
                    cnt_lose += 1
                    lai_1_day -= money
                    dict_lose[cnt] += 1

            if detect_cat_lo(cnt):
                log_info_and_print("Lam lai kho mau")
                tong_lai += lai_1_day
                # base_money = 0
                refresh()
                # break

            if detect_cat_lai():
                log_info_and_print("Tiep tuc")
                # base_money = 0
                # refresh()
                break

            chon = play_turn(con_truoc_cua_san)
            control_game = "Da thang: {0} | Da thua {1} | Con vua xong: {2}, | Dat lenh so: {3} vao ben {4} {5}$" \
                           " | cat lai = {6}, cat lo = {7}".format(
                cnt_win, cnt_lose, con_truoc_cua_san.upper(), cnt + 1, chon.upper(), money, cat_lai, cat_lo)

            control_game = "Da thang: {0} | Da thua {1} \n".format(cnt_win, cnt_lose)
            # control_game += " danh theo lich su = {0}\n".format(danh_theo_lich_su)
            control_game += "Win   :" + str(dict_win) + "\n"
            control_game += "Lose :" + str(dict_lose) + "\n"
            control_game += "Tong lai :" + str(tong_lai) + "\n"
            control_game += "Pattern :" + str(pattern_cl)


            log_info_and_print(control_game)
            pyautogui.alert(text=control_game, title='control game', timeout=12000)

            log_info_and_print("-" * 30)

    else:
        if color == "ChoDatTien":
            color = "DoiLuotMoi"

    time.sleep(3)
    prevent_jackpot()

summary = "Tong so turn cuoc: {0}; Lose:{1} ; Win: {2}".format(cnt_lose + cnt_win, cnt_lose, cnt_win)
log_info_and_print(summary)
log_info_and_print(history)
log_info_and_print(str(dict_win))
log_info_and_print(str(dict_lose))
pyautogui.alert(text="Bye bye", title='control game', timeout=7000)
shutdown()
