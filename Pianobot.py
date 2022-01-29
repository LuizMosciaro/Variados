import time
import pyautogui as py
import win32api, win32con
import keyboard

"url do jogo = https://www.jogos360.com.br/piano_tiles_2_online.html"

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('q') == False:
    if py.pixel(400, 400)[1] == 0:
        click(400, 400)
    if py.pixel(500, 400)[1] == 0:
        click(500, 400)
    if py.pixel(590, 400)[1] == 0:
        click(590, 400)
    if py.pixel(670, 400)[1] == 0:
        click(670, 400)

"x:450,y:300"
"x:530,y:300"
"x:600,y:300"
"x:670,y:300"
"1,1,1"