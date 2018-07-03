lines = []
rectSize = 4
maxSize = 12000
rule = 30
maxRows = 2000

def getCell(rule, cleft, ccenter, cright):
    number = (cleft*4)+(ccenter*2)+cright
    result = (rule & int(2**number)) / (2**number)
    return result

def getNextLine(row):
    prevline = lines[row-1]
    length = len(prevline)

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
    length = len(lines[row])
    startX = (maxSize/2) - ((length // 2) * rectSize)
    posY = (1 + row) * rectSize

    elem = 0
    while elem < length:
        posX = startX + (elem * rectSize)
        if lines[row][elem] == 1:
            draw.rectangle([(posX, posY), (posX+rectSize, posY+rectSize)], 0, 0)
        else:
            draw.rectangle([(posX, posY), (posX+rectSize, posY+rectSize)], 255, 255)

        elem += 1

from PIL import Image, ImageDraw
import math

im = Image.new("L", (maxSize, int(maxSize/2)), 255)
draw = ImageDraw.Draw(im)

lines.append([1])
lines.append([getCell(rule, 0, 0, 1), getCell(rule, 0, 1, 0), getCell(rule, 1, 0, 0)])

row = 2
while row < maxRows:
    lines.append(getNextLine(row))
    row += 1

row = 0
while row < maxRows:
    if row % 10 == 0:
        print("Drawing row ", row)
    drawRow(row)
    im.save("D:\\users\\moncho\\test_" + str(row).zfill(4) + ".jpg", "JPEG")
    row += 1

im.show()
