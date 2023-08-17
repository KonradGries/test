i = 0

Liste = []

while i <= 10:

    Liste.extend([i])

    i= i + 1 
i = 0
while i <= 10:

    Liste.insert(i, i+i)
    Liste.pop()
    i  = i +1

print (Liste)       