lines = []
rectSize = 5
maxSize = 3000
rule = 30
maxRows = 100

def is_prime(x):
    if x < 2:
        return False
    else:
        for count in range(2, x):
            if x % count == 0:
                return False

        return True

def drawPoint(num, draw, posX, posY):
    posX = (maxSize/2)+posX
    posY = (maxSize/2)+posY

    if is_prime(num):
        draw.rectangle([(posX-rectSize-1, posY-rectSize-1), (posX+rectSize+1, posY+rectSize+1)], 0, 0)
    else:
        draw.rectangle([(posX-rectSize+1, posY-rectSize+1), (posX+rectSize-1, posY+rectSize-1)], 255, 0)

def getCell(rule, cleft, ccenter, cright):
    number = (cleft*4)+(ccenter*2)+cright
    result = (rule & int(2**number)) / (2**number)
    print("  Calculated number ", number, " result: ", result)
    return result

def getNextLine(row):
    prevline = lines[row-1]
    length = len(prevline)
    print("Length: ", length)

    newline = []
    i = 0
    while i < length+2:
        if i == 0:
            newline.append(getCell(rule, 0, 0, prevline[i]))
        elif i == 1:
            newline.append(getCell(rule, 0, prevline[i-1], prevline[i]))
        elif i == length:
            newline.append(getCell(rule, prevline[i-2], prevline[i-1], 0))
        elif i == length+1:
            newline.append(getCell(rule, prevline[i-2], 0, 0))
        else:
            newline.append(getCell(rule, prevline[i-2], prevline[i-1],  prevline[i]))
        i += 1

    return(newline)

def drawRow(row):
    print ("Inside drawRow, row = ", row)
    length = len(lines[row])
    print("length: ", length)
    startX = (maxSize/2) - ((length // 2) * rectSize)
    print("startX = ", startX)
    posY = (1 + row) * rectSize
    print("posY = ", posY)

    elem = 0
    while elem < length:
        posX = startX + (elem * rectSize)
        print("Row ", row, " elem ", elem, " posX ", posX, " posY ", posY)
        if lines[row][elem] == 1:
            draw.rectangle([(posX-rectSize, posY-rectSize), (posX+rectSize, posY+rectSize)], 0, 0)

        elem += 1

from PIL import Image, ImageDraw
import math

im = Image.new("L", (maxSize, maxSize), 255)
draw = ImageDraw.Draw(im)

lines.append([1])
lines.append([getCell(rule, 0, 0, 1), getCell(rule, 0, 1, 0), getCell(rule, 1, 0, 0)])
row = 2

while row < maxRows:
    print("Appending row ", row)
    lines.append(getNextLine(row))
    row += 1

row = 0
while row < maxRows:
    print("Drawing row ", row)
    drawRow(row)
    row += 1

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
im.show()
