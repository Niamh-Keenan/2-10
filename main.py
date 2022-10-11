x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
result = 0

if y < 0:   
    count = -y 
else:
    count = y

while count > 0:
    if x == 0: 
        break   
    result += x        
    count -= 1       
print (result)

