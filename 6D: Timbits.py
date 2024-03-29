timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

# step 3: buy as many large boxes as you can
bigBoxes = int(timbitsLeft / 40)
totalCost = totalCost + bigBoxes * 6.19    # update the total price
timbitsLeft = timbitsLeft - 40 * bigBoxes  # calculate timbits still needed

if timbitsLeft >= 20:                # step 4, can we buy a medium box?
    totalCost = totalCost + 3.39
    timbitsLeft = timbitsLeft - 20
if timbitsLeft >= 10:                # step 5, can we buy a small box?
    totalCost = totalCost + 1.99
    timbitsLeft = timbitsLeft - 10

totalCost = totalCost + timbitsLeft * .20 # step 6
print(float(totalCost))                         # step 7


#-------or
#this method is more complicated than it needs to be, but just another option

timbitsLeft = int(input()) # step 1: get the input
totalCost = 0              # step 2: initialize the total cost

# step 3: buy as many large boxes as you can
bigBoxes = int(timbitsLeft / 40)
totalCost = totalCost + bigBoxes * 6.19    # update the total price
timbitsLeft = timbitsLeft - 40 * bigBoxes  # calculate timbits still needed

if timbitsLeft >= 20: 
    mediumBox = int(timbitsLeft/20)           # step 4, can we buy a medium box?
    totalCost = totalCost + mediumBox * 3.39
    timbitsLeft = timbitsLeft - 20 * mediumBox 
if timbitsLeft >= 10:      
    smallBox = int(timbitsLeft/10)          # step 5, can we buy a small box?
    totalCost = totalCost + smallBox * 1.99
    timbitsLeft = timbitsLeft - 10 * smallBox

totalCost = totalCost + timbitsLeft * 0.2 # step 6
print(totalCost)                         # step 7

