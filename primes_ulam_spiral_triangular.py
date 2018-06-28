
def is_prime(x):
    flag = False
    if x < 2:
        return False
    else:
        for count in range(2, x):
            if x % count == 0:
                flag = True
                break
        if flag == True:
            return False
        return True



def is_prime2(x):
    if x < 2:
        return False
    else:
        for count in range(2, x):
            if x % count == 0:
                return False

        return True

def getRanges(maxNum):
    ranges = list()

    r = 1
    while r**2 < maxNum:
        ranges.append(list(range((r-1)**2+1, r**2+1)))
        r = r+1

    return ranges;

from PIL import Image, ImageDraw

maxSize = 3800
maxNum = 5000

im = Image.new("L", (maxSize, maxSize), 255)

draw = ImageDraw.Draw(im)

draw.line([(10,10), (500, 50)], 0)

posX = maxSize/2
posY = maxSize/2
count = 1
step = 10
rectSize = 2
numSteps = 1
numStepsLeft = 1
repetition = 1
spiralType = 2  # 1 = square, 2 = triangular
secondSegment = True

ranges = getRanges(maxNum)

# Initial direction
if spiralType == 1:
    deltaX = 0
    deltaY = step
elif spiralType == 2:
    deltaX = -step
    deltaY = step


for r in ranges:

    index = 1
    for count in r:
        # draw rectangle
        if is_prime2(count):
            draw.rectangle([(posX-rectSize, posY-rectSize), (posX+rectSize, posY+rectSize)], 0, 0)
        else:
            draw.rectangle([(posX-rectSize+1, posY-rectSize+1), (posX+rectSize-1, posY+rectSize-1)], 255, 0)

#        if count > 1:
#            draw.line([(posX-deltaX, posY-deltaY), (posX, posY)], 0)

        if index == 1 or index == len(r)/2+0.5:
            # Change direction
            if spiralType == 1:
                if  deltaX != 0: # right to up or left to down
                    deltaY = -deltaX
                    deltaX = 0
                else:
                    deltaX = deltaY
                    deltaY = 0
            elif spiralType == 2:
                if deltaY == 0:
                    if secondSegment:
                        deltaX = -step
                        deltaY = -step
                    else:
                        secondSegment = True
                elif deltaY == -step:
                    deltaY = step
                else:
                    deltaX = step
                    deltaY = 0
                    if count > 1:
                        secondSegment = False



        posX += deltaX
        posY += deltaY
        index+=1


del draw

# write to stdout
#im.save(sys.stdout, "PNG")
im.show()
