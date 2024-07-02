char1 = "hemantnegi"
count = {}
for char in char1:
    if char in count:
        count[char] +=1
    else:
        count[char] =1
print(count)