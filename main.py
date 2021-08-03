### Auto LoL Code
### Author: nxhdev2002
### Github: github.com/nxhdev2002

import requests, time, pyautogui, re, clipboard
reg = r"LOL(.*?) "
post = input("post: ")
access_token = input("token: ")

def click():
    ## move and click to code inputhttps://github.com/nxhdev2002/lolAutoCode/blob/master/a.py
    pyautogui.moveTo(1200, 825)
    pyautogui.click()

    ## paste code
    pyautogui.keyDown("ctrl")
    pyautogui.press("a")
    pyautogui.press("v")
    pyautogui.keyUp("ctrl")

    # select submit
    pyautogui.moveTo(1300, 825)
    pyautogui.click()
    time.sleep(0.5)
    
    # select ok
    pyautogui.moveTo(1105, 718)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(974, 711)
    pyautogui.click()

def main():
    a = ''
    while True:
        # get lastest comment from graph api
        r = requests.get(f"https://graph.facebook.com/{post}/comments?order=reverse_chronological&access_token={access_token}&limit=1")
        cmt = r.json()['data'][0]['message']
        # regex & split LOL Code
        rs = re.findall(reg, cmt)
        if (len(rs) > 0):
            # check if code is new code
            if ("LOL" + rs[0] != a):
                print("LOL" + rs[0])
                clipboard.copy("LOL" + rs[0])
                click()
                a = "LOL" + rs[0]

if __name__ == "__main__":
    main()
