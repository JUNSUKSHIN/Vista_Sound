import os

f= open('position_log.txt','r')
out = open('matrix_quotes.txt', 'w')
lines = f.read().splitlines()

last_string = "-1"

tca_x, tca_y, tca_z = (0, 0, 0)
tma_x, tma_y, tma_z = (0, 0, 0)

cnt = 0


for line in lines:
    time_t, camera, marker = line.split("/")

    if (last_string == "-1") or (last_string == time_t):

        last_string = time_t

        ca_x, ca_y, ca_z = map(float, camera[1:-1].split(", "))
        ma_x, ma_y, ma_z = map(float, marker[1:-1].split(", "))

        tca_x = tca_x + ca_x
        tca_y = tca_y + ca_y
        tca_z = tca_z + ca_z

        tma_x = tma_x + ma_x
        tma_y = tma_y + ma_y
        tma_z = tma_z + ma_z

        cnt = cnt + 1

    else:
        fca_x = tca_x / cnt
        fca_y = tca_y / cnt
        fca_z = tca_z / cnt

        fma_x = tma_x / cnt
        fma_y = tma_y / cnt
        fma_z = tma_z / cnt

        out.writelines(time_t + "/" + str(round(fca_x, 3)) + ", " + str(round(fca_y, 3)) + ", " + str(round(fca_z, 3)) + "/" + str(round(fma_x, 3)) + ", " + str(round(fma_y, 3)) + ", " + str(round(fma_z, 3)) + "\n")

        last_string = "-1"

        tca_x, tca_y, tca_z = (0, 0, 0)
        tma_x, tma_y, tma_z = (0, 0, 0)

        cnt = 0

f.close()
out.close()


