import random, sys, time
# import copy

enter, esc, space, left, up, right, down = 13, 27, 32, 37, 38, 39, 40

window.onkeydown = lambda event: event.keyCode != up and event.keyCode != down and event.keyCode != left and event.keyCode != right and event.keyCode != space # Prevent scrolldown on spacebar press

KEYMAPPING = {13:"enter",27:"esc",32:"space",37:"left",38:"up",39:"right",40:"down",85:"u",78:"n",66:"b",80:"p"}

# IMAGESDICT = {
#     'grass':'<img src="/static/pic/Grass_Block.png">',
#     'plain':'<img src="/static/pic/Plain_Block.png">',
#     'wall':'<img src="/static/pic/Wall_Block_Tall.png">',
#     'wood':'<img src="/static/pic/Wood_Block_Tall.png">'
# }

IMAGESDICT = {'uncovered goal': '<img class="over" src="/static/pic/RedSelector.png">',
              'covered goal': '<img class="over" src="/static/pic/Selector.png">',
              'star': '<img class="over" src="/static/pic/Star.png">',
              'corner': '<img src="/static/pic/Wall_Block_Tall.png">',
              'wall': '<img src="/static/pic/Wood_Block_Tall.png">',
              'inside floor': '<img src="/static/pic/Plain_Block.png">',
              'outside floor': '<img src="/static/pic/Grass_Block.png">',
              'title': '<img src="/static/pic/star_title.png">',
              'solved': '<img src="/static/pic/star_solved.png">',
              'princess': '<img class="over" src="/static/pic/princess.png">',
              'boy': '<img class="over" src="/static/pic/boy.png">',
              'catgirl': '<img class="over" src="/static/pic/catgirl.png">',
              'horngirl': '<img class="over" src="/static/pic/horngirl.png">',
              'pinkgirl': '<img class="over" src="/static/pic/pinkgirl.png">',
              'rock': '<img class="over" src="/static/pic/Rock.png">',
              'short tree': '<img class="over" src="/static/pic/Tree_Short.png">',
              'tall tree': '<img class="over" src="/static/pic/Tree_Tall.png">',
              'ugly tree': '<img class="over" src="/static/pic/Tree_Ugly.png">'}

# These dict values are global, and map the character that appears
# in the level file to the Surface object it represents.
TILEMAPPING = {'x': IMAGESDICT['corner'],
                '#': IMAGESDICT['wall'],
                'o': IMAGESDICT['inside floor'],
                ' ': IMAGESDICT['outside floor']}
OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
                        '2': IMAGESDICT['short tree'],
                        '3': IMAGESDICT['tall tree'],
                        '4': IMAGESDICT['ugly tree']}

# PLAYERIMAGES is a list of all possible characters the player can be.
# currentImage is the index of the player's current player image.
currentImage = 0
PLAYERIMAGES = [IMAGESDICT['princess'],
                IMAGESDICT['boy'],
                IMAGESDICT['catgirl'],
                IMAGESDICT['horngirl'],
                IMAGESDICT['pinkgirl']]

# The percentage of outdoor tiles that have additional
# decoration on them, such as a tree or rock.
OUTSIDE_DECORATION_PCT = 20
html = document
win = window

class Starpusher:
    def __init__ (self):
        # self.isLevelcomplete=False
        self.timeStart = time.time()
        self.currentImage=0
        self.tile=[]
        self.jsMoveEvents=[]
        
        self.container = html.createElement('div')
        self.container.style.backgroundColor = 'Silver'
        self.container.style.height = 'auto'
        self.container.style.width = '950px'
        self.container.style.padding = 0
        self.container.style.display = 'none'
        self.container.innerHTML="Ala mak ota 2"

        html.body.appendChild (self.container)
        
        self.boxes = []

        for i in range(5):
            self.box = html.createElement('div')
            self.box.style.backgroundColor = 'SkyBlue'
            self.box.style.height = '80px'
            self.box.style.width = '800px'
            self.box.innerHTML='box'
            self.boxes.append(self.box)
            self.container.appendChild (self.box)
    
        self.boxes[1].innerHTML='Press arrow keys...'        
        self.boxes[3].innerHTML='<img src="/static/pic/Grass_Block.png">'
        self.keyCode = None
        
        win.addEventListener ('keydown', self.keydown)
        win.addEventListener ('keyup', self.keyup)
        # html.body.addEventListener ('touchstart', lambda event: event.preventDefault ())
        html.body.addEventListener ('mousedown', lambda event: event.preventDefault ())
        # win.setInterval (self.update, 1500)    # Install update callback, time in ms

        self.levels = self.readLevelsFile('/static/starPusherLevels.txt')
        print("Levels:"+len(self.levels))
        
        # self.levelObj = self.levels[self.currentLevelIndex]
        # self.mapObj = self.decorateMap(self.levelObj['mapObj'], self.levelObj['startState']['player'])
        # self.boxes[4].innerHTML=str(self.mapObj)
        # gameStateObj = copy.deepcopy(levelObj['startState'])
        # print("init-startState:"+str(self.levelObj['startState']))
        
        # self.gameStateObj = {'player': (0, 0),
        #                         'stepCounter': 0,
        #                         'stars': [],
        #                         'playerUndo': [],
        #                         'starsUndo': []}
        # self.gameStateObj.player=self.levelObj['startState'].player
        # self.gameStateObj.stepCounter=self.levelObj['startState'].stepCounter
        # self.gameStateObj.stars=self.levelObj['startState'].stars
        # self.gameStateObj.playerUndo=self.levelObj['startState'].playerUndo
        # self.gameStateObj.starsUndo=self.levelObj['startState'].starsUndo
        # print("init-gameStateObj:"+str(self.gameStateObj))
        # gameStateObj.player=(1,1)
        # gameStateObj.stepCounter=99
        # gameStateObj.stars=[(1,1),(0,0)]
        # print("startState:"+str(self.levelObj['startState']))
        # print("gameStateObj:"+str(gameStateObj))        
        # mapSurf = self.drawMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
        # self.board = html.createElement('div')
        # # self.container.appendChild (self.board)
        # html.body.appendChild (self.board)
        self.board = html.getElementById ('board')
        self.endSplash = html.getElementById ('endSplash')
        # self.endSplash.addEventListener ('touchstart', (lambda aCell: lambda: self.mouseClick (aCell)) (('next', -1, -1)))  # Returns inner lambda
        self.endSplash.addEventListener ('mousedown', (lambda aCell: lambda: self.mouseClick (aCell)) (('next', -1, -1)))
        # self.board.style.margin = '80px 0 0 40px' # top right bottom left
        # self.board.innerHTML=mapSurf
        self.timeStart = time.time()
        self.boardInfo = html.getElementById ('info')
        self.currentLevelIndex = 0
        self.initLevel(self.currentLevelIndex)
        
    def initLevel (self, levelIndex):
        self.levelObj = self.levels[levelIndex]
        self.mapObj = self.decorateMap(self.levelObj['mapObj'], self.levelObj['startState']['player'])
        self.gameStateObj = {'player': (0, 0),
                                'stepCounter': 0,
                                'timeCounter':0,
                                'stars': [],
                                'playerUndo': [],
                                'starsUndo': []}
        self.gameStateObj.player=self.levelObj['startState'].player
        self.gameStateObj.stepCounter=self.levelObj['startState'].stepCounter
        self.gameStateObj.timeCounter=self.levelObj['startState'].timeCounter
        self.gameStateObj.stars=self.levelObj['startState'].stars
        self.gameStateObj.playerUndo=self.levelObj['startState'].playerUndo
        self.gameStateObj.starsUndo=self.levelObj['startState'].starsUndo
        self.tile.clear()
        self.board.innerHTML=""
        self.endSplash.style.display = 'none'
        # print("mapObj:"+str(self.mapObj))
        for y in range(len(self.mapObj)):
            self.tile.append([])
        for y in range(len(self.mapObj)):
            for x in range(len(self.mapObj[0])):
                self.tile[y].append([])
        # print('h:'+len(self.tile))
        # print('w:'+len(self.tile[0]))
        # print("tile0:"+str(self.tile))
        mapSurf = self.drawMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
        # print("tile0:"+str(self.tile))
        # self.board.innerHTML=mapSurf
        self.timeStart = time.time()
    
    def mouseClick(self, params):
        ev, x, y = params
        playerY, playerX = self.gameStateObj.player
        print('mouseClick: '+str((ev, x, y)))
        print('mouseClick-self.gameStateObj.player: '+str(self.gameStateObj.player))        
        # print(str(cell.innerHTML))
        gameEvent=''        
        PAUSE_MS=200
        if (ev=='next'):            
            gameEvent=self.handleUserAction('next')
        elif (ev=='u'):
            # undo
            self.gameStateObj['player'] = self.gameStateObj['playerUndo'].pop()
            self.gameStateObj['stars'] = self.gameStateObj['starsUndo'].pop()
            # redraw map
            mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])           
        elif (playerX==x and playerY==y):            
            gameEvent=self.handleUserAction('p')
        elif (playerY==y):
            if(playerX>x):
                t=0
                while (x < playerX) and (gameEvent!='levelCompleted'):
                    # gameEvent=self.handleUserAction('left')
                    self.jsMoveEvents.append(win.setTimeout((lambda gameEvent: lambda: self.handleUserAction (gameEvent)) ('left'), t))
                    t+=PAUSE_MS
                    x += 1
            elif(playerX<x):
                t=0
                while (x > playerX) and (gameEvent!='levelCompleted'):
                    # gameEvent=self.handleUserAction('right')
                    self.jsMoveEvents.append(win.setTimeout((lambda gameEvent: lambda: self.handleUserAction (gameEvent)) ('right'), t))
                    t+=PAUSE_MS
                    x -= 1
        elif (playerX==x):
            if(playerY>y):
                t=0
                while (y < playerY) and (gameEvent!='levelCompleted'):
                    # gameEvent=self.handleUserAction('up')
                    self.jsMoveEvents.append(win.setTimeout((lambda gameEvent: lambda: self.handleUserAction (gameEvent)) ('up'), t))
                    t+=PAUSE_MS
                    y += 1
            elif(playerY<y):
                t=0
                while (y > playerY) and (gameEvent!='levelCompleted'):
                    # gameEvent=self.handleUserAction('down')
                    self.jsMoveEvents.append(win.setTimeout((lambda gameEvent: lambda: self.handleUserAction (gameEvent)) ('down'), t))
                    t+=PAUSE_MS
                    y -= 1

    def keydown (self, event):
        self.keyCode = event.keyCode        
        if (self.isLevelFinished(self.levelObj, self.gameStateObj) or KEYMAPPING[self.keyCode]=='n'):
            gameEvent=self.handleUserAction('next')    
        elif (KEYMAPPING[self.keyCode]=='b'):
            self.currentLevelIndex -= 1
            self.initLevel(self.currentLevelIndex)
        elif (KEYMAPPING[self.keyCode]=='p'):
            gameEvent=self.handleUserAction('p')
        elif (KEYMAPPING[self.keyCode] in ['up','left','down','right']):       
            gameEvent=self.handleUserAction(KEYMAPPING[self.keyCode])
        elif (KEYMAPPING[self.keyCode]=='u' and len(self.gameStateObj['playerUndo'])>0):
            gameEvent=self.handleUserAction('u')
     
    
    def keydown0 (self, event):
        self.keyCode = event.keyCode
        # print('keycode:'+self.keyCode)
        self.boxes[1].innerHTML="Klawisz: "+self.keyCode+" - "+KEYMAPPING[self.keyCode]
        self.tileUpdate (KEYMAPPING[self.keyCode])

        # print('isLevelcomplete:'+isLevelcomplete)
        # self.boardInfo.innerHTML='isLevelcomplete:'+isLevelcomplete
       
        if (self.isLevelFinished(self.levelObj, self.gameStateObj) or KEYMAPPING[self.keyCode]=='n'):
            self.currentLevelIndex += 1
            self.initLevel(self.currentLevelIndex)
            #self.isLevelcomplete=False        
        elif (KEYMAPPING[self.keyCode]=='b'):
            self.currentLevelIndex -= 1
            self.initLevel(self.currentLevelIndex)
        elif (KEYMAPPING[self.keyCode]=='p'):
            # Change the player image to the next one.
            self.currentImage += 1
            if (self.currentImage >= len(PLAYERIMAGES)):
                # After the last player image, use the first one.
                self.currentImage = 0
            mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
        elif (KEYMAPPING[self.keyCode] in ['up','left','down','right']):       
            moved = self.makeMove(self.mapObj, self.gameStateObj, KEYMAPPING[self.keyCode])
            if (moved):
                # redraw map
                mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
                # self.board.innerHTML=mapSurf
                # stepcounter
                self.gameStateObj['stepCounter'] += 1
                self.gameStateObj['timeCounter'] = int(time.time() - self.timeStart)
                if (self.isLevelFinished(self.levelObj, self.gameStateObj)):
                    m, s = divmod(self.gameStateObj['timeCounter'], 60)
                    timeCounterMsg = s+' sec' if m==0 else m+' min '+s+' sec'                   
                    self.board.innerHTML+='<div class="inner"><img src="/static/pic/star_solved.png"><div style="margin:10px;" class="fontDecoration2 fontLGuy">Steps: '+self.gameStateObj['stepCounter']+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: '+timeCounterMsg+'</div></div>'
        elif (KEYMAPPING[self.keyCode]=='u' and len(self.gameStateObj['playerUndo'])>0):
            # undo
            self.gameStateObj['player'] = self.gameStateObj['playerUndo'].pop()
            self.gameStateObj['stars'] = self.gameStateObj['starsUndo'].pop()
            # redraw map
            mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
            # self.board.innerHTML=mapSurf

    def keyup (self, event):
        self.keyCode = None 
    
    def handleUserAction (self, userAction):
        if ((userAction=='next') or userAction=='n'):
            #self.isLevelFinished(self.levelObj, self.gameStateObj) and 
            for moveEvent in self.jsMoveEvents:
                win.clearInterval(moveEvent)
            self.jsMoveEvents.clear()
            self.currentLevelIndex += 1
            self.initLevel(self.currentLevelIndex)
            #self.isLevelcomplete=False        
        elif (userAction=='b'):
            self.currentLevelIndex -= 1
            self.initLevel(self.currentLevelIndex)
        elif (userAction=='p'):
            # Change the player image to the next one.
            self.currentImage += 1
            if (self.currentImage >= len(PLAYERIMAGES)):
                # After the last player image, use the first one.
                self.currentImage = 0
            mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
            return 'characterChanged'
        elif ((userAction in ['up','left','down','right']) and (not self.isLevelFinished(self.levelObj, self.gameStateObj))):       
            moved = self.makeMove(self.mapObj, self.gameStateObj, userAction)
            if (moved):
                # redraw map                
                mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
                # self.board.innerHTML=mapSurf
                # stepcounter
                self.gameStateObj['stepCounter'] += 1
                self.gameStateObj['timeCounter'] = int(time.time() - self.timeStart)
                if (self.isLevelFinished(self.levelObj, self.gameStateObj)):
                    m, s = divmod(self.gameStateObj['timeCounter'], 60)
                    timeCounterMsg = s+' sec' if m==0 else m+' min '+s+' sec'                   
                    # self.board.innerHTML+='<div class="inner"><img src="/static/pic/star_solved.png"><div style="margin:10px;" class="fontDecoration2 fontLGuy">Steps: '+self.gameStateObj['stepCounter']+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: '+timeCounterMsg+'</div></div>'
                    # endSplash = html.createElement('div')
                    # endSplash.className='inner'
                    # self.board.appendChild (endSplash)
                    # endSplash.addEventListener ('touchstart', (lambda aCell: lambda: self.mouseClick (aCell)) (('next', -1, -1)))  # Returns inner lambda
                    # endSplash.addEventListener ('mousedown', (lambda aCell: lambda: self.mouseClick (aCell)) (('next', -1, -1)))
                    # self.endSplash.innerHTML='<img src="/static/pic/star_solved.png"><div style="margin:10px;text-align:center;" class="fontDecoration2 fontLGuy">Steps: '+self.gameStateObj['stepCounter']+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: '+timeCounterMsg+'</div>'
                    counter = html.getElementById('counter')
                    counter.innerHTML='Steps: '+self.gameStateObj['stepCounter']+'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: '+timeCounterMsg
                    self.endSplash.style.display = 'initial'
                    return 'levelCompleted'
                return 'moved'
        elif (userAction=='u' and len(self.gameStateObj['playerUndo'])>0):
            # undo
            self.gameStateObj['player'] = self.gameStateObj['playerUndo'].pop()
            self.gameStateObj['stars'] = self.gameStateObj['starsUndo'].pop()
            # redraw map
            mapSurf = self.updateMap(self.mapObj, self.gameStateObj, self.levelObj['goals'])
            # self.board.innerHTML=mapSurf
            return 'undo'
        return 'none'
     
    def update (self):
        self.boxes[0].innerHTML="Random: " + random.randint (1, 100)
    
    def tileUpdate (self, key):
        MAPPING = {
            'up':'outside floor',
            'down':'inside floor',
            'left':'wall',
            'right':'corner',
            'undefined':'inside floor',
            'enter':'outside floor',
            'esc':'corner',
            'space':'wall'
            }
        self.boxes[2].innerHTML=MAPPING[key]
        self.boxes[3].innerHTML=IMAGESDICT[MAPPING[key]]
    
    def readLevelsFile(self, filename):
        # assert os.path.exists(filename), 'Cannot find the level file: %s' % (filename)
        # mapFile = open(filename, 'r')
        
        # Each level must end with a blank line
        # content = mapFile.readlines() + ['\r\n']
        # mapFile.close()
        content = None
        xmlhttp = __new__(XMLHttpRequest())
        xmlhttp.open("GET", filename, False)
        xmlhttp.send()
        content = xmlhttp.responseText.split("\r\n")
        # content = result.

        levels = [] # Will contain a list of level objects.
        levelNum = 0
        mapTextLines = [] # contains the lines for a single level's map.
        mapObj = [] # the map object made from the data in mapTextLines
        # print(range(len(content)))
        # print(len(content))
        for lineNum in range(len(content)):
            # Process each line that was in the level file.
            line = content[lineNum].rstrip('\r\n')
            # print(line)
            if ';' in line:
                # Ignore the ; lines, they're comments in the level file.
                line = line[:line.find(';')]

            # print(line)

            if line != '':
                # This line is part of the map.
                mapTextLines.append(line)
                # print("append:"+line)
            elif line == '' and len(mapTextLines) > 0:

                # A blank line indicates the end of a level's map in the file.
                # Convert the text in mapTextLines into a level object.

                # Find the longest row in the map.
                maxWidth = -1
                for i in range(len(mapTextLines)):
                    if len(mapTextLines[i]) > maxWidth:
                        maxWidth = len(mapTextLines[i])
                # print("h:"+str(len(mapTextLines)))
                # print("w:"+str(maxWidth))
                # Add spaces to the ends of the shorter rows. This
                # ensures the map will be rectangular.
                for i in range(len(mapTextLines)):
                    mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

                # Convert mapTextLines to a map object.
                for x in range(len(mapTextLines)):
                    mapObj.append([])
                for y in range(len(mapTextLines)):
                    for x in range(maxWidth):
                        # print(x)
                        mapObj[y].append(mapTextLines[y][x] if (mapTextLines[y][x]!=0 and mapTextLines[y][x]) else ' ')

                # Loop through the spaces in the map and find the @, ., and $
                # characters for the starting game state.
                startx = None # The x and y for the player's starting position
                starty = None
                goals = [] # list of (x, y) tuples for each goal.
                stars = [] # list of (x, y) for each star's starting position.
                for x in range(maxWidth):
                    for y in range(len(mapObj[x])):
                        if mapObj[x][y] in ('@', '+'):
                            # '@' is player, '+' is player & goal
                            startx = x
                            starty = y
                        if mapObj[x][y] in ('.', '+', '*'):
                            # '.' is goal, '*' is star & goal
                            goals.append((x, y))
                        if mapObj[x][y] in ('$', '*'):
                            # '$' is star
                            stars.append((x, y))

                # Basic level design sanity checks:
                assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, filename)
                assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (levelNum+1, lineNum, filename)
                assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (levelNum+1, lineNum, filename, len(goals), len(stars))

                # Create level object and starting game state object.
                gameStateObj = {'player': (startx, starty),
                                'stepCounter': 0,
                                'timeCounter': 0,
                                'stars': stars,
                                'playerUndo': [],
                                'starsUndo': []}
                levelObj = {'width': maxWidth,
                            'height': len(mapObj),
                            'mapObj': mapObj,
                            'goals': goals,
                            'startState': gameStateObj}

                levels.append(levelObj)

                # print(levelNum)
                # print(str(maxWidth) + " " + str(len(mapObj)))
                # print(str(mapObj))

                # Reset the variables for reading the next map.
                mapTextLines = []
                mapObj = []
                gameStateObj = {}
                levelNum += 1
        return levels
        
    def decorateMap(self, mapObj, startxy):
        # print("decorate-mapObj" +str(mapObj))
        """Makes a copy of the given map object and modifies it.
        Here is what is done to it:
            * Walls that are corners are turned into corner pieces.
            * The outside/inside floor tile distinction is made.
            * Tree/rock decorations are randomly added to the outside tiles.

        Returns the decorated map object."""

        startx, starty = startxy # Syntactic sugar

        # Copy the map object so we don't modify the original passed
        # mapObjCopy = copy.deepcopy(mapObj)
        # mapObjCopy = mapObj
        mapObjCopy=[]
        for y in range(len(mapObj)):
            mapObjCopy.append([])
        for y in range(len(mapObj)):            
            for x in range(len(mapObj[0])):
                mapObjCopy[y].append(mapObj[y][x])

        # print("mapObjCopy:"+str(mapObjCopy))

        # Remove the non-wall characters from the map data
        for x in range(len(mapObjCopy)):
            for y in range(len(mapObjCopy[0])):
                if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                    mapObjCopy[x][y] = ' '

        # Flood fill to determine inside/outside floor tiles.
        self.floodFill(mapObjCopy, startx, starty, ' ', 'o')

        # Convert the adjoined walls into corner tiles.
        for x in range(len(mapObjCopy)):
            for y in range(len(mapObjCopy[0])):

                if mapObjCopy[x][y] == '#':
                    if (self.isWall(mapObjCopy, x, y-1) and self.isWall(mapObjCopy, x+1, y)) or \
                    (self.isWall(mapObjCopy, x+1, y) and self.isWall(mapObjCopy, x, y+1)) or \
                    (self.isWall(mapObjCopy, x, y+1) and self.isWall(mapObjCopy, x-1, y)) or \
                    (self.isWall(mapObjCopy, x-1, y) and self.isWall(mapObjCopy, x, y-1)):
                        mapObjCopy[x][y] = 'x'

                elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < OUTSIDE_DECORATION_PCT:
                    mapObjCopy[x][y] = random.choice(list(OUTSIDEDECOMAPPING.keys()))

        # print("decorate-mapObjCopy:" +str(mapObjCopy))
        return mapObjCopy
        
    def floodFill(self, mapObj, x, y, oldCharacter, newCharacter):
        """Changes any values matching oldCharacter on the map object to
        newCharacter at the (x, y) position, and does the same for the
        positions to the left, right, down, and up of (x, y), recursively."""

        # In this game, the flood fill algorithm creates the inside/outside
        # floor distinction. This is a "recursive" function.
        # For more info on the Flood Fill algorithm, see:
        #   http://en.wikipedia.org/wiki/Flood_fill
        if mapObj[x][y] == oldCharacter:
            mapObj[x][y] = newCharacter

        if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
            self.floodFill(mapObj, x+1, y, oldCharacter, newCharacter) # call right
        if x > 0 and mapObj[x-1][y] == oldCharacter:
            self.floodFill(mapObj, x-1, y, oldCharacter, newCharacter) # call left
        if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
            self.floodFill(mapObj, x, y+1, oldCharacter, newCharacter) # call down
        if y > 0 and mapObj[x][y-1] == oldCharacter:
            self.floodFill(mapObj, x, y-1, oldCharacter, newCharacter) # call up

    def isWall(self, mapObj, x, y):
        """Returns True if the (x, y) position on
        the map is a wall, otherwise return False."""
        if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
            return False # x and y aren't actually on the map.
        elif mapObj[x][y] in ('#', 'x'):
            return True # wall is blocking
        return False

    def drawMap(self, mapObj, gameStateObj, goals):
        mapSurf=""
        nl = "\n"
        # print("drawMap-gameStateObj:"+str(gameStateObj))
        # Draw the tile sprites onto this surface.
        for x in range(len(mapObj)):
            mapSurf+='<div class="up">'+nl
            row = html.createElement('div')
            row.className='up'
            self.board.appendChild (row)
            # self.box.innerHTML='box'
            # self.boxes.append(self.box)
            rowTouch = html.createElement('div')
            rowTouch.className='touch-up'
            self.board.appendChild (rowTouch)
            
            for y in range(len(mapObj[x])):
                cellInner=""
                # spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
                if mapObj[x][y] in TILEMAPPING:
                    baseTile = TILEMAPPING[mapObj[x][y]]
                elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                    baseTile = TILEMAPPING[' ']

                # First draw the base ground/wall tile.
                # mapSurf.blit(baseTile, spaceRect)
                mapSurf+="<span>"+baseTile
                cellInner+=baseTile
                cell = html.createElement('span')
                row.appendChild (cell)
                self.tile[x][y]=cell
                cellTouch = html.createElement('div')
                if (mapObj[x][y]=='o'):
                    cellTouch.className='touch'
                    # cellTouch.addEventListener ('touchstart', (lambda aCell: lambda: self.mouseClick (aCell)) (('board', y, x)))  # Returns inner lambda
                    cellTouch.addEventListener ('mousedown', (lambda aCell: lambda: self.mouseClick (aCell)) (('board', y, x)))
                else:
                    cellTouch.className='notouch'

                rowTouch.appendChild (cellTouch)

                if mapObj[x][y] in OUTSIDEDECOMAPPING:
                    # Draw any tree/rock decorations that are on this tile.
                    # mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
                    mapSurf+=OUTSIDEDECOMAPPING[mapObj[x][y]]
                    cellInner+=OUTSIDEDECOMAPPING[mapObj[x][y]]
                elif (str((x,y)) in str(gameStateObj['stars'])):
                    if (str((x, y)) in str(goals)):
                        # A goal AND star are on this space, draw goal first.
                        # mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                        mapSurf+=IMAGESDICT['covered goal']
                        cellInner+=IMAGESDICT['covered goal']
                    # Then draw the star sprite.
                    # mapSurf.blit(IMAGESDICT['star'], spaceRect)
                    mapSurf+=IMAGESDICT['star']
                    cellInner+=IMAGESDICT['star']
                # if ((x, y) in goals):
                elif str((x, y)) in str(goals):
                    # Draw a goal without a star on it.
                    # mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)                    
                    mapSurf+=IMAGESDICT['uncovered goal']
                    cellInner+=IMAGESDICT['uncovered goal']

                mapSurf+="</span>"+nl

                # Last draw the player on the board.
                if str((x, y)) == str(gameStateObj['player']):
                    # Note: The value "currentImage" refers
                    # to a key in "PLAYERIMAGES" which has the
                    # specific player 
                    # image we want to show.
                    # mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)
                    mapSurf+=PLAYERIMAGES[self.currentImage]
                    cellInner+=PLAYERIMAGES[self.currentImage]

                cell.innerHTML=cellInner

            mapSurf+="</div>"+nl

        return mapSurf
    
    def updateMap(self, mapObj, gameStateObj, goals):
        # Update 5x5 (for undo) tiles around player position
        playerX, playerY = gameStateObj['player']
        x1=playerX-2
        if x1<0:
            x1=0
        x2=playerX+3
        if x2>len(mapObj):
            x2=len(mapObj)
        y1=playerY-2
        if y1<0:
            y1=0
        y2=playerY+3
        if y2>len(mapObj[0]):
            y2=len(mapObj[0])

        for x in range(x1, x2):   #len(mapObj)
            for y in range(y1, y2): #len(mapObj[x])
                cellInner=""
                # spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
                if mapObj[x][y] in TILEMAPPING:
                    baseTile = TILEMAPPING[mapObj[x][y]]
                elif mapObj[x][y] in OUTSIDEDECOMAPPING:
                    baseTile = TILEMAPPING[' ']

                # First draw the base ground/wall tile.
                # mapSurf.blit(baseTile, spaceRect)
                cellInner+=baseTile

                if mapObj[x][y] in OUTSIDEDECOMAPPING:
                    # Draw any tree/rock decorations that are on this tile.
                    # mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
                    cellInner+=OUTSIDEDECOMAPPING[mapObj[x][y]]
                elif (str((x,y)) in str(gameStateObj['stars'])):
                    if (str((x, y)) in str(goals)):
                        # A goal AND star are on this space, draw goal first.
                        # mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
                        cellInner+=IMAGESDICT['covered goal']
                    # Then draw the star sprite.
                    # mapSurf.blit(IMAGESDICT['star'], spaceRect)
                    cellInner+=IMAGESDICT['star']
                # if ((x, y) in goals):
                elif str((x, y)) in str(goals):
                    # Draw a goal without a star on it.
                    # mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)                    
                    cellInner+=IMAGESDICT['uncovered goal']

                # Last draw the player on the board.
                if str((x, y)) == str(gameStateObj['player']):
                    # Note: The value "currentImage" refers
                    # to a key in "PLAYERIMAGES" which has the
                    # specific player 
                    # image we want to show.
                    # mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)
                    currentImage=0
                    cellInner+=PLAYERIMAGES[self.currentImage]

                self.tile[x][y].innerHTML=cellInner


        return "mapSurf"

    def makeMove(self, mapObj, gameStateObj, playerMoveTo):
        """Given a map and game state object, see if it is possible for the
        player to make the given move. If it is, then change the player's
        position (and the position of any pushed star). If not, do nothing.

        Returns True if the player moved, otherwise False."""

        # print("gameStateObj-makeMove-0:"+str(gameStateObj))

        # Make sure the player can move in the direction they want.
        playerx, playery = gameStateObj['player']

        # This variable is "syntactic sugar". Typing "stars" is more
        # readable than typing "gameStateObj['stars']" in our code.
        stars = gameStateObj['stars']
        # print("stars:"+str(stars))

        # The code for handling each of the directions is so similar aside
        # from adding or subtracting 1 to the x/y coordinates. We can
        # simplify it by using the xOffset and yOffset variables.
        if playerMoveTo == 'left': 
            xOffset = 0
            yOffset = -1
        elif playerMoveTo == 'down':
            xOffset = 1
            yOffset = 0
        elif playerMoveTo == 'right':
            xOffset = 0
            yOffset = 1
        elif playerMoveTo == 'up':
            xOffset = -1
            yOffset = 0

        # print("player x:"+str(playerx)+ " y:"+str(playery))
        # print("offset x:"+str(xOffset)+ " y:"+str(yOffset))
        # See if the player can move in that direction.
        if self.isWall(mapObj, playerx + xOffset, playery + yOffset):
            return False
        else:
            starsIsChanged = False
            if str((playerx + xOffset, playery + yOffset)) in str(stars):
                # There is a star in the way, see if the player can push it.
                if not self.isBlocked(mapObj, gameStateObj, playerx + (xOffset*2), playery + (yOffset*2)):
                    # Move the star.
                    starsIsChanged = True
                    # # gameStateObj['starsUndo'] = copy.deepcopy(gameStateObj['stars']) # Undo
                    # gameStateObj['starsUndo'].append(copy.deepcopy(gameStateObj['stars'])) # Undo
                    gameStateObj['starsUndo'].append([])
                    l=len(gameStateObj['starsUndo'])-1
                    for s in gameStateObj['stars']:
                        gameStateObj['starsUndo'][l].append(s)

                    # print("stars index params:"+str((playerx + xOffset, playery + yOffset)))
                    ind = stars.index((playerx + xOffset, playery + yOffset))
                    # print("star id:"+str(ind))
                    sId=0
                    for s in stars:
                        if (str((playerx + xOffset, playery + yOffset))==str(s)):
                            ind=sId
                        sId+=1
                    stars[ind] = (stars[ind][0] + xOffset, stars[ind][1] + yOffset)
                else:
                    return False
            # Move the player upwards.
            gameStateObj['playerUndo'].append(gameStateObj['player']) # Undo
            if (not starsIsChanged):
                # gameStateObj['starsUndo'].append(copy.deepcopy(gameStateObj['stars'])) # Undo
                gameStateObj['starsUndo'].append([])
                l=len(gameStateObj['starsUndo'])-1
                for s in gameStateObj['stars']:
                    gameStateObj['starsUndo'][l].append(s)
            gameStateObj['player'] = (playerx + xOffset, playery + yOffset)
            # print("gameStateObj-makeMove-1:"+str(gameStateObj))
            return True

    def isBlocked(self, mapObj, gameStateObj, x, y):
        """Returns True if the (x, y) position on the map is
        blocked by a wall or star, otherwise return False."""

        if self.isWall(mapObj, x, y):
            return True

        elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
            return True # x and y aren't actually on the map.

        elif str((x, y)) in str(gameStateObj['stars']):
            return True # a star is blocking

        return False

    def isLevelFinished(self, levelObj, gameStateObj):
        """Returns True if all the goals have stars in them."""
        for goal in levelObj['goals']:
            if str(goal) not in str(gameStateObj['stars']):
                # Found a space with a goal but no star on it.
                return False
        return True


starpusher = Starpusher ()
