import owiener #https://github.com/orisano/owiener

c = 0
e = 0
N = 0

d = owiener.attack(e, N)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))

dec = pow(c, d, N)
dx = hex(dec)[2:]

msg = []
for i in range(0, len(ds), 2):
    c = chr(int(dx[i:i+2], 16))
    # print(ds[i:i+2])
    # print(c)
    msg.append(c)

print(''.join(msg))
