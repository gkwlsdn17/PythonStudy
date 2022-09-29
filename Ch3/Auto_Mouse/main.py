import pyautogui
import time

import pyperclip

region = ["서울", "시흥", "청주", "부산", "영덕"]

addr_x = 146
addr_y = 55
start_x = 393
start_y = 212
end_x = 1061
end_y = 871

for r in region:
    pyautogui.moveTo(addr_x, addr_y)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(r+" 날씨")
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyautogui.screenshot(f'screenshot_{r}_weather.png', region=(start_x, start_y, end_x-start_x, end_y-start_y))
