num = int(input())
for y in range(num):
    text = ""
    text = (" "*(num-1-y) + "*"*((y+1)*2-1))
    print(text)
