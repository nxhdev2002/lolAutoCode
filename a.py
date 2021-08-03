### Auto LoL Code
### Author: nxhdev2002
### Github: github.com/nxhdev2002

import requests, time, pyautogui, re, clipboard, subprocess, os, ctypes, sys
reg = r"LOL(.*?) "
post = input("post: ")
access_token = input("token: ")

def getToken():
    #League Client command line query
    command = "WMIC PROCESS WHERE name='LeagueClient.exe' GET commandline"
    #Get WMIC output
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read().decode('utf-8')
    #Parse landing token
    return re.findall(r'--landing-token=(.*?)\s\-?\-?', output)[0]

def redeem(code, token):
    r = requests.post('https://bargain.lol.garena.vn/api/enter',
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/11.15.388.2387 (CEF 74) Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Token': token,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Via': '1.1 vegur',
            'Referer': 'https://bargain.lol.garena.vn/?token=' + token
        },
        json = {"code": code,"confirm":True},
    )
    return ( r.json() )

def main():
    token = getToken()
    # print(token)
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
                a = "LOL" + rs[0]
                print(a)
                rs = redeem(a[0:13], token)
                print(rs)
                try:
                    if (rs['current_token_amount'] == 500):
                        print("done")
                        break
                except:
                    pass
if __name__ == "__main__":
    main()
