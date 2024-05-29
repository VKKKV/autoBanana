import random
import time
import win32api
import win32gui
import win32con

def get_hwnd():
    point = win32api.GetCursorPos()
    hwnd = win32gui.WindowFromPoint(point)
    return hwnd

if __name__ == '__main__':

    # move arrow to the window of banana and get the hwnd
    time.sleep(2)
    hwnd = get_hwnd()
    print("hwnd: "+str(hwnd))


    count=0
    while True:
        # get the position
        x, y, w, h = win32gui.GetWindowRect(hwnd)
        click_x = x + int(w * 0.5)
        click_y = y + int(h * 0.59)
        win32gui.SetForegroundWindow(hwnd)
        # set position
        win32api.SetCursorPos((click_x, click_y))
        count += 1
        print('auto count: '+str(count)+"\ntap position: "
              +str(click_x)+','+str( click_y))
        # tap banana
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.1+round(random.random(),3))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # wait for next tap

        clickInterval = 60
        time.sleep(clickInterval+random.randint(0,5)+round(random.random(),3))

