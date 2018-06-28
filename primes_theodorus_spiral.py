
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


def archimedes(n):
    a = 5
    theta = 1.4142*(n**(1/2))


    r = a*theta

    return [r*math.cos(theta), r*math.sin(theta)]

theodorusCoordinates = []
theodorusCoordinates.append([0, 0])

def theodorus(n):
    r = math.sqrt(n)
    theta = math.atan(1/r) + theodorusCoordinates[n-1][1]
    theodorusCoordinates.append([r, theta])

    return [ 10*r*math.cos(theta), 10*r*math.sin(theta)]

def fermat(n):
    a = 10
    theta = 1.4142*(n**(1/2))

    return [a*math.sqrt(theta)*math.cos(theta), a*math.sqrt(theta)*math.sin(theta)]

from PIL import Image, ImageDraw
import math

maxSize = 3800
maxNum = 50000
centerX = maxSize/2
centerY = maxSize/2
vertices = 6

im = Image.new("L", (maxSize, maxSize), 255)

draw = ImageDraw.Draw(im)

posX = maxSize/2
posY = maxSize/2
count = 1
step = 10
rectSize = 2
coordinates = None

for count in range(1, maxNum):
    # draw rectangle
    oldCoordinates = coordinates
    coordinates = theodorus(count)

    drawPoint(count, draw, coordinates[0], coordinates[1], rectSize)

#    if count > 1:
#        draw.line(((maxSize/2)+oldCoordinates[0], (maxSize/2)+oldCoordinates[1], (maxSize/2)+coordinates[0], (maxSize/2)+coordinates[1]), 0)
del draw

# write to stdout
#im.save(sys.stdout, "PNG")
im.show()
