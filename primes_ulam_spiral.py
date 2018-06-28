
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


from PIL import Image, ImageDraw

maxSize = 3800
maxNum = 100000

im = Image.new("L", (maxSize, maxSize), 255)

draw = ImageDraw.Draw(im)

posX = maxSize/2
posY = maxSize/2
count = 1
deltaX = 10
deltaY = 0
rectSize = 2
numSteps = 1
numStepsLeft = 1
repetition = 1

#draw.rectangle([(posX-rectSize*2, posY-rectSize*2), (posX+rectSize*2, posY+rectSize*2)], 0, 0)
#draw.line((400,0, 400,800), 0)
#draw.line((0, 400, 800, 400), 0)


for count in range(1, maxNum):
    # draw rectangle
    if is_prime2(count):
        draw.rectangle([(posX-rectSize, posY-rectSize), (posX+rectSize, posY+rectSize)], 0, 0)
    else:
        draw.rectangle([(posX-rectSize+1, posY-rectSize+1), (posX+rectSize-1, posY+rectSize-1)], 255, 0)

    #if count > 1:
        #draw.line([(posX, posY), (posX+deltaX, posY+deltaY)], 0)


    posX = posX + deltaX
    posY = posY + deltaY

    numStepsLeft = numStepsLeft - 1

    # calculate number steps left and change direction
    if numStepsLeft == 0:
        if repetition == 1:
            numStepsLeft = numSteps
            repetition = 2
        else:
            repetition = 1
            numSteps = numSteps + 1
            numStepsLeft = numSteps

        # Change direction
        if deltaX != 0: # right to up or left to down
            deltaY = -deltaX
            deltaX = 0
        else:
            deltaX = deltaY
            deltaY = 0





del draw

# write to stdout
#im.save(sys.stdout, "PNG")
im.show()
