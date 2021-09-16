import pyautogui, time
lines = ["."]
with open("kelime.txt","a") as metin:
    i = 0
    while i < 1000:
        for line in lines:
            metin.write(line)
            metin.write("\n")
            i += 1
        break

time.sleep(5)

metin = open("kelime.txt","r")

for kelime in metin:
    pyautogui.typewrite(kelime)
    pyautogui.press("enter")

