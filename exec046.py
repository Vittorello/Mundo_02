from time import sleep
import emoji

print("=-=-=-="*7)
print("Contagem regressiva até a queima dos fogos!!")
print("=-=-=-="*7)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize("BUM! BUM! POOOW!:fireworks::sparkler:"))