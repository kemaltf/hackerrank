# 1 ------------.|.------------
# 2 ---------.|..|..|.---------
# 3 ------.|..|..|..|..|.------
# 4 ---.|..|..|..|..|..|..|.---
# 5 ----------WELCOME----------
# 6 ---.|..|..|..|..|..|..|.---
# 7 ------.|..|..|..|..|.------
# 8 ---------.|..|..|.---------
# 9 ------------.|.------------

# ---------
# -WELCOME-

# baca polanya:
## ada 9 baris
## ada 9 * 3 kolom

## .|.
# baris 1: 1
# baris 2: 3
# baris 3: 5
# baris 4: 7

# baris 6 - 5 1: 7
# baris 7 - 5 2: 5
# baris 8 - 5 3: 3
# baris 9 - 5 4: 1


# bikin rumus
# perhatikan polanya setiap baris naik 2
# 7 - 5 = 2
# 5 - 3 = 2
# Un = a + (n-1)b
# un = 1 + (n-1)2
# un = 1 + 2n - 2
# un = 2n - 1 #n adalah baris

# un = a + (n-1)b
# un = 7 -2n+2
# un = 9-2n
# garis tengah itu
# baris + 1 / 2
# 9 - 5 = 4
# 3 - 2 = 1


def door(totalBaris, totalKolom):
    barisMid = (totalBaris + 1) // 2
    baseToMid = totalBaris - barisMid
    for baris in range(totalBaris):
        if baris + 1 == barisMid:
            print(
                "-" * ((totalKolom - 7) // 2)
                + "WELCOME"
                + "-" * ((totalKolom - 7) // 2)
            )
        else:
            if baris < baseToMid:
                specialChar = (2 * (baris + 1)) - 1
                specialCharTotal = specialChar * 3
                totalStrip = (totalKolom - specialCharTotal) // 2
                print(("-" * totalStrip) + (".|." * specialChar) + ("-" * totalStrip))
            else:
                specialChar = totalBaris - (2 * (baris + 1 - barisMid))
                specialCharTotal = specialChar * 3
                totalStrip = totalKolom - specialCharTotal
                totalStrip = (totalKolom - specialCharTotal) // 2
                print(("-" * totalStrip) + (".|." * specialChar) + ("-" * totalStrip))


baris, kolom = input().split(" ")
N = int(baris)
M = int(kolom)

for i in range(1, N // 2 + 1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(M, "-"))

print("WELCOME".center(M, "-"))

for i in range(N // 2, 0, -1):
    pattern = ".|." * (2 * i - 1)
    print(pattern.center(M, "-"))

# door(int(baris), int(kolom))
# door(baris, kolom)
