string = "hi my name is sam"
reverse = ""

i = len(string) - 1  

while i >= 0:
    reverse = reverse + string[i]
    i = i - 1

print(reverse)

