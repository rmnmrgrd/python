width = 1000
lines = []

def is_prime(x):
    if x < 2:
        return False
    else:
        for count in range(2, x):
            if x % count == 0:
                return False

        return True

def drawPoint(num, draw, posX, posY, rectsize):
    posX = (maxSize/2)+posX
    posY = (maxSize/2)+posY

    if is_prime(num):
        draw.rectangle([(posX-rectSize-1, posY-rectSize-1), (posX+rectSize+1, posY+rectSize+1)], 0, 0)
    else:
        draw.rectangle([(posX-rectSize+1, posY-rectSize+1), (posX+rectSize-1, posY+rectSize-1)], 255, 0)

def getNextLine(row):
    prevline = lines[row-1]
    length = lines[row-1].length

    newline = []
    i = 0
    while i < length+2:
        if i == 0:
            newline.append(getCell(rule, 0, 0, prevline[i]))
        elif i == 1:
            newline.append(getCell(rule, 0, prevline[i], prevline[i+1]))
        elif i == length:
            newline.append(getCell(rule, prevline[i-1], prevline[i], 0))
        elif i == length+1:
            newline.append(getCell(rule, prevline[i-1], 0, 0))

        i += 1

    return(newline)

from PIL import Image, ImageDraw
import math



centerX = maxSize/2
centerY = maxSize/2
vertices = 6

im = Image.new("L", (maxSize, maxSize), 255)
draw = ImageDraw.Draw(im)

posX = maxSize/2
posY = maxSize/2


lines.append([1])
lines.append([getCell(rule, 0, 0, 1), getCell(rule, 0, 1, 0), getCell(rule, 1, 0, 0)])
row = 2

while row < 10:
    lines.append(getNextLine(row))


#count = 1
#step = 10
#rectSize = 2
#coordinates = None

#for count in range(1, maxNum):
    ## draw rectangle
    #oldCoordinates = coordinates
    #coordinates = theodorus(count)

    #drawPoint(count, draw, coordinates[0], coordinates[1], rectSize)

#    if count > 1:
#        draw.line(((maxSize/2)+oldCoordinates[0], (maxSize/2)+oldCoordinates[1], (maxSize/2)+coordinates[0], (maxSize/2)+coordinates[1]), 0)
#del draw

# write to stdout
#im.save(sys.stdout, "PNG")
#im.show()
