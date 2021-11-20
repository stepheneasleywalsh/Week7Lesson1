# Ask for base
b = int(input("base b:"))

# Ask for n
n = int(input("power n:"))

# Make blank message
message = ""

# For loop that adds times to the message
for x in range(1,n+1):
    message += str(b)+" X "

# Add the answer to the message
answer = b**n
message += "= "+str(answer)

# Remove the stray X = at the end
message = message.replace("X =","=")
print(message)

# Quit
quit()