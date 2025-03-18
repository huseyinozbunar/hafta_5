t1 = '01.01.2005'
t1 = '12.30.2010'

tarih1 = t1.split('.')
tarih2 = t1.split('.')
yıl1 = int(tarih1[-1])
yıl2 = int(tarih2[-1])
ay1 = int(tarih1[-2])
ay2 = int(tarih2[-2])
gun1 = int(tarih1[-3])
gun2 = int(tarih2[-3])

print(yıl1, ay1, gun1)

kategory = ['saglik', 'dunya', 'teknoloji']
gazeteler = ['sabah', 'hurriyet', 'milliyet']

ay_gunleri = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def artik_yil(yil):
    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)
for m in gazeteler:
    gaste = 'www.{}.com.tr'.format(m)
    for k in kategory:
        for i in range(yıl1, yıl2 + 1):
            for j in range(1, 13):
                if j == 2 and artik_yil(i):
                    max_gun = 29
                else:
                    max_gun = ay_gunleri[j - 1]

                for gun in range(1, max_gun + 1):
                    print("{}/{}/{}-{:02}-{:02}".format(gaste, k, i, j, gun))