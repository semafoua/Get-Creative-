#milestone 1
#Creatiing shapes
def createCircle (red,green,blue,cX,cY,radius,depth):
    report = f"circle {red} {green} {blue} {cX} {cY} {radius} {depth}"
    return report
print(createCircle(255,0,0,0,0,10,20))
print(createCircle(0,255,0,-10,-40,10,20))
print(createCircle(0,0,255,20,25,25,0))

def createRectangle (red,green,blue,x1,y1,x2,y2,depth):
    report = f"rectangle {red} {green} {blue} {x1} {y1} {x2} {y2} {depth}"
    return report

"""print(createRectangle(255,0,0,0,0,10,20,1))
print(createRectangle(0,255,0,-10,-40,10,20,2))
print(createRectangle(0,0,255,20,25,25,0,3))"""

def createSmileyFace ():
    report = []
    report.append(createCircle(0,0,0,100,100,75,0))
    report.append(createCircle(0,0,0,80,85,15,0))
    report.append(createCircle(0,0,0,120,85,15,0))
    report.append(createRectangle(0,0,0,80,130,120,130,0))
    report.append(createRectangle(0,0,0,5,5,194,194,0))
    return report

#test case!
"""temp = (createSmileyFace())

actual = ['circle 0 0 0 100 100 75 0', 'circle 0 0 0 80 85 15 0', 'circle 0 0 0 120 85 15 0', 'rectangle 0 0 0 80 130 120 130 0', 'rectangle 0 0 0 5 5 194 194 0']

if (temp == actual):
    print("We did it!")
else:
    print("Error somewhere")"""

#Milestone 2

circleTemp = [(createCircle(255,0,0,0,0,10,20)),createCircle(0,255,0,-10,-40,10,20)]

def getCircles(shapeList):
    report = []
    for item in shapeList:
        circle = {}
        item = item.split()
        if (item[0] == "circle"):
            circle["color"] = [int(item[1]),int(item[2]),int(item[3])]
            circle["x"] = int(item[4])
            circle["y"] = int(item[5])
            circle["radius"] = int(item[6])
            circle["depth"] = int(item[7])
            report.append(circle)
    return report

#data1 = getCircles(createCircle(255,0,0,0,0,10,20))
"""temp = getCircles(['circle 177 2 178 -49 -40 38 -6', 'rectangle 31 215 94 94 -7 12 44 9', 'rectangle 38 16 212 -12 3 72 96 0', 'rectangle 236 91 194 49 -77 74 -45 -3', 'circle 113 66 137 -71 -41 39 5'])
expected = [{'color': [177, 2, 178], 'x': -49, 'y': -40, 'radius': 38, 'depth': -6}, {'color': [113, 66, 137], 'x': -71, 'y': -41, 'radius': 39, 'depth': 5}]
print(temp == expected)"""
#getCircles(circleTemp)

rectTemp = [createRectangle(255,0,0,0,0,10,20,1)]
def getRectangles(shapeList):
    report = []
    for item in shapeList:
        rect = {}
        item = item.split()
        if (item[0] == "rectangle"):
            rect["color"] = [int(item[1]),int(item[2]),int(item[3])]
            rect["x1"] = int(item[4])
            rect["y1"] = int(item[5])
            rect["x2"] = int(item[6])
            rect["y2"] = int(item[7])
            rect["depth"] = int(item[8])
            report.append(rect)
    return report

"""temp = (getRectangles(['circle 28 146 66 -55 11 3 -7', 'rectangle 184 175 28 -35 11 -85 -29 -3', 'circle 68 235 249 -39 -80 52 -7']))
expected = [{'color': [184, 175, 28], 'x1': -35, 'y1': 11, 'x2': -85, 'y2': -29, 'depth': -3}]
print("Problem 2")
print(temp == expected)"""


hunk = [{'x': -15, 'y': -42, 'depth': 20, 'color': [0, 255, 0]}, {'x': -15,'y': -41, 'depth': 20, 'color': [0, 255, 0]}, {'x': -15, 'y': -40, 'depth':20, 'color': [0, 255, 0]}, {'x': -15, 'y': -39, 'depth': 20, 'color':[0, 255, 0]}, {'x': -15, 'y': -38, 'depth': 20, 'color': [0, 255, 0]},{'x': -14, 'y': -43, 'depth': 20, 'color': [0, 255, 0]}, {'x': -14,'y': -42, 'depth': 20, 'color': [0, 255, 0]}, {'x': -14, 'y': -38, 'depth':20, 'color': [0, 255, 0]}, {'x': -14, 'y': -37, 'depth': 20, 'color':[0, 255, 0]}, {'x': -13, 'y': -44, 'depth': 20, 'color': [0, 255, 0]},{'x': -13, 'y': -36, 'depth': 20, 'color': [0, 255, 0]}, {'x': -12,'y': -45, 'depth': 20, 'color': [0, 255, 0]}, {'x': -12, 'y': -44, 'depth':20, 'color': [0, 255, 0]}, {'x': -12, 'y': -36, 'depth': 20, 'color':[0, 255, 0]}, {'x': -12, 'y': -35, 'depth': 20, 'color': [0, 255, 0]},{'x': -11, 'y': -45, 'depth': 20, 'color': [0, 255, 0]}, {'x': -11,'y': -35, 'depth': 20, 'color': [0, 255, 0]}, {'x': -10, 'y': -45, 'depth':20, 'color': [0, 255, 0]}, {'x': -10, 'y': -35, 'depth': 20, 'color':[0, 255, 0]}, {'x': -9, 'y': -45, 'depth': 20, 'color': [0, 255, 0]},{'x': -9, 'y': -35, 'depth': 20, 'color': [0, 255, 0]}, {'x': -8, 'y':-45, 'depth': 20, 'color': [0, 255, 0]}, {'x': -8, 'y': -44, 'depth':20, 'color': [0, 255, 0]}, {'x': -8, 'y': -36, 'depth': 20, 'color':[0, 255, 0]}, {'x': -8, 'y': -35, 'depth': 20, 'color': [0, 255, 0]},{'x': -7, 'y': -44, 'depth': 20, 'color': [0, 255, 0]}, {'x': -7, 'y':-36, 'depth': 20, 'color': [0, 255, 0]}, {'x': -6, 'y': -43, 'depth': 20, 'color': [0, 255, 0]}, {'x': -6, 'y': -42, 'depth': 20, 'color':[0, 255, 0]}, {'x': -6, 'y': -38, 'depth': 20, 'color': [0, 255, 0]},{'x': -6, 'y': -37, 'depth': 20, 'color': [0, 255, 0]}, {'x': -5, 'y':-42, 'depth': 20, 'color': [0, 255, 0]}, {'x': -5, 'y': -41, 'depth':20, 'color': [0, 255, 0]}, {'x': -5, 'y': -40, 'depth': 20, 'color':[0, 255, 0]}, {'x': -5, 'y': -39, 'depth': 20, 'color': [0, 255, 0]},{'x': -5, 'y': -38, 'depth': 20, 'color': [0, 255, 0]}]
def convertCircle(circleDict, pixels):
    pixels = pixels
    radius = circleDict["radius"]
    depth = circleDict["depth"]
    xCenter = circleDict["x"]
    yCenter = circleDict["y"]
    color = circleDict["color"]

    xRangeMin = xCenter - radius
    xRangeMax = xCenter + radius

    yRangeMin = yCenter - radius
    yRangeMax = yCenter + radius
    
    for x in range(xRangeMin, xRangeMax+1):
        for y in range(yRangeMin, yRangeMax+1):
            xDist = abs(x-xCenter)
            yDist = abs(y-yCenter)
            tempR = ((abs(xDist**2 + yDist**2-radius**2)**0.5))
            if (tempR <= radius**0.5):
                px={}
                px["x"] = x
                px["y"] = y
                px["depth"] = depth
                px["color"] = color
                pixels.append(px)
    #return pixels
    #print(pixels == hunk)


#print(convertCircle({'color': [0, 255, 0], 'x': -10, 'y': -40, 'radius': 5,'depth': 20},[]))


hunk2 = [{'x': 0, 'y': -1, 'depth': 20, 'color': [0, 255, 0]}, {'x': 0, 'y':3, 'depth': 20, 'color': [0, 255, 0]}, {'x': 1, 'y': -1, 'depth': 20,'color': [0, 255, 0]}, {'x': 1, 'y': 3, 'depth': 20, 'color': [0, 255,0]}, {'x': 2, 'y': -1, 'depth': 20, 'color': [0, 255, 0]}, {'x': 2,'y': 3, 'depth': 20, 'color': [0, 255, 0]}, {'x': 0, 'y': -1, 'depth':20, 'color': [0, 255, 0]}, {'x': 2, 'y': -1, 'depth': 20, 'color': [0,255, 0]}, {'x': 0, 'y': 0, 'depth': 20, 'color': [0, 255, 0]}, {'x':2, 'y': 0, 'depth': 20, 'color': [0, 255, 0]}, {'x': 0, 'y': 1, 'depth':20, 'color': [0, 255, 0]}, {'x': 2, 'y': 1, 'depth': 20, 'color': [0,255, 0]}, {'x': 0, 'y': 2, 'depth': 20, 'color': [0, 255, 0]}, {'x':2, 'y': 2, 'depth': 20, 'color': [0, 255, 0]}, {'x': 0, 'y': 3, 'depth':20, 'color': [0, 255, 0]}, {'x': 2, 'y': 3, 'depth': 20, 'color': [0,255, 0]}]

#printHunk(hunk2)

def convertRectangle(rectangleDict, pixels):
    #Initialization
    pixels = pixels
    xStart = rectangleDict["x1"]
    yStart = rectangleDict["y1"]
    xEnd = rectangleDict["x2"]
    yEnd = rectangleDict["y2"]
    color = rectangleDict["color"]
    depth = rectangleDict["depth"]
    #Calculating end ranges
    if (yEnd < 0):
        yEndRange = yEnd -1
    else:
        yEndRange= yEnd+1

    if (xEnd < 0):
        xEndRange = xEnd -1      
    else:
        xEndRange= xEnd+1
    #Calculating counting backwards or forwards
    if (xStart < xEndRange):
        xStep = 1
    else:
        xStep = -1
        
    if (yStart < yEndRange):
        yStep = 1
    else:
        yStep = -1
    #Making the top and bottom pingpong style
    for x in range(xStart, xEndRange, xStep):
        for y in range(yStart, yEndRange, (yEnd-yStart)):
            px = {}
            px["x"] = x
            px["y"] = y
            px["depth"] = depth
            px["color"] = color
            pixels.append(px)
    #Making the sides pingpong style
    for y in range(yStart, yEndRange, yStep):
        for x in range(xStart,xEndRange, (xEnd-xStart)):
            px = {}
            px["x"] = x
            px["y"] = y
            px["depth"] = depth
            px["color"] = color
            pixels.append(px)        
    #return pixels
"""
rectMod test only works if I return pixels and I'm not supposed to return pixels :(
test4 = convertRectangle({'color': [30, 255, 0], 'x1': 0, 'y1': -10, 'x2': 42, 'y2': -73, 'depth': 20}, [])
expected = [{'x': 0, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 1, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 1, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 2, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 2, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 3, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 3, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 4, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 4, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 5, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 5, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 6, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 6, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 7, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 7, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 8, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 8, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 9, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 9, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 10, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 10, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 11, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 11, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 12, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 12, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 13, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 13, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 14, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 14, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 15, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 15, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 16, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 16, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 17, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 17, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 18, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 18, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 19, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 19, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 20, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 20, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 21, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 21, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 22, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 22, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 23, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 23, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 24, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 24, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 25, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 25, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 26, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 26, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 27, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 27, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 28, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 28, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 29, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 29, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 30, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 30, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 31, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 31, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 32, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 32, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 33, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 33, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 34, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 34, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 35, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 35, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 36, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 36, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 37, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 37, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 38, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 38, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 39, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 39, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 40, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 40, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 41, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 41, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -10, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -11, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -11, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -12, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -12, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -13, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -13, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -14, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -14, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -15, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -15, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -16, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -16, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -17, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -17, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -18, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -18, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -19, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -19, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -20, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -20, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -21, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -21, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -22, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -22, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -23, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -23, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -24, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -24, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -25, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -25, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -26, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -26, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -27, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -27, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -28, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -28, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -29, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -29, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -30, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -30, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -31, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -31, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -32, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -32, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -33, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -33, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -34, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -34, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -35, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -35, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -36, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -36, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -37, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -37, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -38, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -38, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -39, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -39, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -40, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -40, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -41, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -41, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -42, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -42, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -43, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -43, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -44, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -44, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -45, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -45, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -46, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -46, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -47, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -47, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -48, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -48, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -49, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -49, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -50, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -50, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -51, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -51, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -52, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -52, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -53, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -53, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -54, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -54, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -55, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -55, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -56, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -56, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -57, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -57, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -58, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -58, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -59, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -59, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -60, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -60, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -61, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -61, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -62, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -62, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -63, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -63, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -64, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -64, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -65, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -65, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -66, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -66, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -67, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -67, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -68, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -68, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -69, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -69, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -70, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -70, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -71, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -71, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -72, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -72, 'depth': 20, 'color': [30, 255, 0]}, {'x': 0, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}, {'x': 42, 'y': -73, 'depth': 20, 'color': [30, 255, 0]}]
print(test4 == expected)


def rectMod(expected, test):
    total = 0
    correct = 0
    for px in range(len(expected)):
        expectedDict = (expected[px])
        x = expectedDict["x"]
        y = expectedDict["y"]
        coord = f"{x},{y}"
        if (px in range(len(test))):
            testDict = test[px]
            xTest = testDict["x"]
            yTest = testDict["y"]
            coordTest = f"{xTest},{yTest}"
            if (coord == coordTest):
                print(f"Correct, I expected {coord} and got {coordTest} at px idx: {px}")
                correct+=1
            else:
                print(f"Incorrect. I expected {coord} and got {coordTest} at idx: {px}")
        else:
            print(f"No pixel: Should be {coord}")
            
        total+=1
    print(f"I need {len(expected)-1} idxs, I have {len(test)-1} idxs")
    print(f"{correct-1} idxs/{total-1} idxs")
        
rectMod(expected, test4)
"""
#print(convertRectangle({'color': [0, 255, 0], 'x1': 0, 'y1': -1, 'x2': 2, 'y2':3, 'depth': 20},[]))

def processCircles(circleList,pixels):
    for circle in circleList:
        convertCircle(circle,pixels)

def processRectangles(rectangleList, pixels):
    for rect in rectangleList:
        convertRectangle(rect, pixels)

processRectangles([{'color': [30, 255, 0], 'x1': 0, 'y1': -10, 'x2': 42, 'y2': -73, 'depth': 20}], [])
#TODO LEARN TYPE ANNOTATIONS

#Milestone 3

def createImage(color, width, height):
    img = []
    for rows in range(height):
        row = []
        for px in range(width):
            row.append(color)
        img.append(row)
    return img

data = (createImage([1, 2, 3],2,3))
#print(data)

def setPixel(image, x, y, color):
    height = len(image)
    width = len(image[0])
    if y in range(height):
        if x in range(width):
            image[y][x] = color
    #print(image)
            
setPixel(data,0,1,[255,255,255])
setPixel([[[100, 100, 100], [0, 0, 0], [0, 0, 0]]],2,0,[200, 200, 200])
setPixel([[[0, 0, 0], [0, 0, 0], [0, 0, 0]]],0,0,[100, 100, 100])

tempDict = {'depth': 0, 'x': 0, 'y': 0, 'color': [50, 50, 50]}
ThreeD = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

def drawPixel(image, pixelDict):
    xCoord = pixelDict["x"]
    yCoord = pixelDict["y"]
    color = pixelDict["color"]
    setPixel(image,xCoord,yCoord,color)
    
drawPixel(ThreeD, tempDict)
tempDicts = [{'depth': 0, 'x': 0, 'y': 0, 'color': [50, 50, 50]},
 {'depth': -10, 'x': 10, 'y': 0, 'color': [100,100, 100]},
 {'depth': 10, 'x': 2, 'y': 0, 'color': [150, 150, 150]}
 ]
def drawPixels(image, pixelDicts):
    for item in pixelDicts:
        drawPixel(image,item)
    
drawPixels(ThreeD, tempDicts)

def getDepth(pixels):
    return pixels["depth"]

def orderPixels(pixels):
    pixels.sort(key = getDepth)

orderPixels([{'depth': -20, 'x': 0, 'y': 0, 'color': [50, 50, 50]},
             {'depth':-100, 'x': 10, 'y': 0, 'color': [100, 100, 100]},
             {'depth': 10, 'x': 2,'y': 0, 'color': [150, 150, 150]}])

#LETS CREATE AN IMAGE

def writePPM(image, filename):
    height = len(image)
    width = len(image[0])
    f = open(filename, "w")
    f.write("P3\n")
    f.write(str(width) + " " + str(height) + "\n")
    f.write("255\n")

    for y in range(len(image)):
        for x in range(len(image[y])):
            for c in range(len(image[y][x])):
                f.write(str(image[y][x][c]) + " ")
    f.write("\n")
    
    f.close()

def main():
    shapes = createSmileyFace()
    circles = getCircles(shapes)
    rectangles = getRectangles(shapes)

    pixelList = []
    processCircles(circles, pixelList)
    processRectangles(rectangles, pixelList)
    orderPixels(pixelList)
    image = createImage([255,135,0], 200, 200)
    drawPixels(image, pixelList)
    writePPM(image, "smile1.ppm")
    return None

#createCircle (red,green,blue,cX,cY,radius,depth)
#createRectangle (red,green,blue,x1,y1,x2,y2,depth)

def creativeShapes():
    shapes = []
    #The sky
    for x in range(600):
        shapes.append(createRectangle(190,235-int(x*.2),255, 50, 50, 450, 650 - x, 0))

    #bottom hair
    hair_rad = 75
    for x in range(hair_rad):
        shapes.append(createCircle((255-hair_rad)+x,0+x,50,350,350,hair_rad-x, 15))
    for x in range(hair_rad):
        shapes.append(createCircle((255-hair_rad) + x,0+x,50,150,350,hair_rad-x, 15))
    #top hair
        #left
    for x in range(hair_rad):
        shapes.append(createCircle((255-hair_rad) + x,0+x,50,200,250,hair_rad-x, 20))
        #right
    for x in range(hair_rad):
        shapes.append(createCircle((255-hair_rad) + x,0+x,50,300,250,hair_rad-x, 20))
    #collar"A":["a1","a2"]
    startx = 140
    starty = 400
    height = 65
    for x in range(height):
        shapes.append(createRectangle(int(255-(x*.5)),int(255-(x*.5)),int(255-(x*.25)), startx, starty, 500 - startx, starty + height - x , 18))
    #body
    startx = 100
    starty = 450
    height = 300
    width = 100
    for x in range(height):
        shapes.append(createRectangle(int(0+(x*.2)),int(0+(x*.2)),int(0+(x*.33)), startx, starty, 500 - startx, starty + height - x , 17))

    #spots
    red  = [240,0,0]
    orange = [255, 143, 51]
    yellow = [247,225,59]
    green = [107,227,64]
    blue = [64,227,208]
    purple = [182,70,219]

    spot_rad = 25
    row = 3
    column = [3,2]
    #colors = [red,orange,yellow,green,blue,purple]
    space = 100
    spots = column[0]
    line_height = 72
    startx = 150
    starty = 510

    for rows in range(row):
        for spot in range(spots): 
            for x in range(spot_rad):
                shapes.append(createCircle(230+x,0,0,startx,starty,1+x, 20))
            startx+= space
        if (spots == column[0]):
            startx = 200
            spots = column[1]
        else:
            startx = 150
            spots = column[0]
        starty+=line_height

    #shadows
    count = 4
    startx = 150
    starty = 410
    space = 57
    height = 55
    width = 30
    endx = startx + width
    endy = starty + height

    #FILLED IN RECTANGLE TEMPLATE
    for rect in range(count):
        for x in range(height):
            shapes.append(createRectangle(142-x*2,141-x*2,143-x*2, startx, starty, endx, endy-x, 19))
        startx+=space
        endx = startx + width

    #face
    for x in range(100):
        shapes.append(createCircle(int(255),int(255),int(255),250,320,1+x,20))

    hair_rad_top = 55
     #top top hair
    for x in range(hair_rad_top):
        shapes.append(createCircle(230,0,0,210,245,hair_rad_top-x, 20))
    for x in range(hair_rad_top):
        shapes.append(createCircle(230,0,0,290,245,hair_rad_top-x, 20))
    

    cheek_rad = 35
    #left cheek
    for x in range(cheek_rad):
        shapes.append(createCircle(255,215,209,190,340,cheek_rad-x,20))
    #right cheek
    for x in range(cheek_rad):
        shapes.append(createCircle(255,215,209,310,340,cheek_rad-x,20))

    #left eye
    eye_w = 10
    eye_h = 30
    startx = 215
    starty = 300
    endx = startx+eye_w
    endy = starty+eye_h
    shine_rad = 3
    for x in range(eye_w):
        shapes.append(createRectangle(0,0,0, startx+x, starty+x, endx, endy-x, 20))

    for x in range(shine_rad):
        shapes.append(createCircle(255,255,255,startx,starty,shine_rad-x,22))

        
    startx = 500 - startx - eye_w
    starty = starty
    endx = startx+eye_w
    endy = starty+eye_h
    for x in range(eye_w):
        shapes.append(createRectangle(0,0,0, startx+x, starty+x, endx, endy-x, 20))

    for x in range(shine_rad):
        shapes.append(createCircle(255,255,255,startx,starty,shine_rad-x,22))
        
    #nose
    for x in range(20):
        shapes.append(createCircle(230+x,0+4*x,50,250,340,20-x,20))

    for x in range(4):
        shapes.append(createCircle(255,255,255,240,330,4-x,20))


    return shapes
    
def creative():
    shapes = creativeShapes()
    circles = getCircles(shapes)
    rectangles = getRectangles(shapes)

    pixelList = []
    processCircles(circles, pixelList)
    processRectangles(rectangles, pixelList)
    orderPixels(pixelList)
    image = createImage([255,255,255], 500,700)
    drawPixels(image, pixelList)
    writePPM(image, "creative.ppm")

creative()

print("Refresh!")
