// Transcrypt'ed from Python, 2019-09-20 19:42:48
var random = {};
var sys = {};
var time = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_random__ from './random.js';
__nest__ (random, '', __module_random__);
import * as __module_sys__ from './sys.js';
__nest__ (sys, '', __module_sys__);
import * as __module_time__ from './time.js';
__nest__ (time, '', __module_time__);
var __name__ = '__main__';
var __left0__ = tuple ([13, 27, 32, 37, 38, 39, 40]);
export var enter = __left0__ [0];
export var esc = __left0__ [1];
export var space = __left0__ [2];
export var left = __left0__ [3];
export var up = __left0__ [4];
export var right = __left0__ [5];
export var down = __left0__ [6];
window.onkeydown = (function __lambda__ (event) {
	return event.keyCode != up && event.keyCode != down && event.keyCode != left && event.keyCode != right && event.keyCode != space;
});
export var KEYMAPPING = dict ({13: 'enter', 27: 'esc', 32: 'space', 37: 'left', 38: 'up', 39: 'right', 40: 'down', 85: 'u', 78: 'n', 66: 'b', 80: 'p'});
export var IMAGESDICT = dict ({'uncovered goal': '<img class="over" src="/static/pic/RedSelector.png">', 'covered goal': '<img class="over" src="/static/pic/Selector.png">', 'star': '<img class="over" src="/static/pic/Star.png">', 'corner': '<img src="/static/pic/Wall_Block_Tall.png">', 'wall': '<img src="/static/pic/Wood_Block_Tall.png">', 'inside floor': '<img src="/static/pic/Plain_Block.png">', 'outside floor': '<img src="/static/pic/Grass_Block.png">', 'title': '<img src="/static/pic/star_title.png">', 'solved': '<img src="/static/pic/star_solved.png">', 'princess': '<img class="over" src="/static/pic/princess.png">', 'boy': '<img class="over" src="/static/pic/boy.png">', 'catgirl': '<img class="over" src="/static/pic/catgirl.png">', 'horngirl': '<img class="over" src="/static/pic/horngirl.png">', 'pinkgirl': '<img class="over" src="/static/pic/pinkgirl.png">', 'rock': '<img class="over" src="/static/pic/Rock.png">', 'short tree': '<img class="over" src="/static/pic/Tree_Short.png">', 'tall tree': '<img class="over" src="/static/pic/Tree_Tall.png">', 'ugly tree': '<img class="over" src="/static/pic/Tree_Ugly.png">'});
export var TILEMAPPING = dict ({'x': IMAGESDICT ['corner'], '#': IMAGESDICT ['wall'], 'o': IMAGESDICT ['inside floor'], ' ': IMAGESDICT ['outside floor']});
export var OUTSIDEDECOMAPPING = dict ({'1': IMAGESDICT ['rock'], '2': IMAGESDICT ['short tree'], '3': IMAGESDICT ['tall tree'], '4': IMAGESDICT ['ugly tree']});
export var currentImage = 0;
export var PLAYERIMAGES = [IMAGESDICT ['princess'], IMAGESDICT ['boy'], IMAGESDICT ['catgirl'], IMAGESDICT ['horngirl'], IMAGESDICT ['pinkgirl']];
export var OUTSIDE_DECORATION_PCT = 20;
export var html = document;
export var win = window;
export var Starpusher =  __class__ ('Starpusher', [object], {
	__module__: __name__,
	get __init__ () {return __get__ (this, function (self) {
		self.timeStart = time.time ();
		self.currentImage = 0;
		self.tile = [];
		self.container = html.createElement ('div');
		self.container.style.backgroundColor = 'Silver';
		self.container.style.height = 'auto';
		self.container.style.width = '950px';
		self.container.style.padding = 0;
		self.container.style.display = 'none';
		self.container.innerHTML = 'Ala mak ota 2';
		html.body.appendChild (self.container);
		self.boxes = [];
		for (var i = 0; i < 5; i++) {
			self.box = html.createElement ('div');
			self.box.style.backgroundColor = 'SkyBlue';
			self.box.style.height = '80px';
			self.box.style.width = '800px';
			self.box.innerHTML = 'box';
			self.boxes.append (self.box);
			self.container.appendChild (self.box);
		}
		self.boxes [1].innerHTML = 'Press arrow keys...';
		self.boxes [3].innerHTML = '<img src="/static/pic/Grass_Block.png">';
		self.keyCode = null;
		win.addEventListener ('keydown', self.keydown);
		win.addEventListener ('keyup', self.keyup);
		win.setInterval (self.py_update, 1500);
		self.levels = self.readLevelsFile ('/static/starPusherLevels.txt');
		print ('Levels:' + len (self.levels));
		self.board = html.getElementById ('board');
		self.timeStart = time.time ();
		self.boardInfo = html.getElementById ('info');
		self.currentLevelIndex = 0;
		self.initLevel (self.currentLevelIndex);
	});},
	get initLevel () {return __get__ (this, function (self, levelIndex) {
		self.levelObj = self.levels [levelIndex];
		self.mapObj = self.decorateMap (self.levelObj ['mapObj'], self.levelObj ['startState'] ['player']);
		self.gameStateObj = dict ({'player': tuple ([0, 0]), 'stepCounter': 0, 'timeCounter': 0, 'stars': [], 'playerUndo': [], 'starsUndo': []});
		self.gameStateObj.player = self.levelObj ['startState'].player;
		self.gameStateObj.stepCounter = self.levelObj ['startState'].stepCounter;
		self.gameStateObj.timeCounter = self.levelObj ['startState'].timeCounter;
		self.gameStateObj.stars = self.levelObj ['startState'].stars;
		self.gameStateObj.playerUndo = self.levelObj ['startState'].playerUndo;
		self.gameStateObj.starsUndo = self.levelObj ['startState'].starsUndo;
		self.tile = [];
		self.board.innerHTML = '';
		for (var y = 0; y < len (self.mapObj); y++) {
			self.tile.append ([]);
		}
		for (var y = 0; y < len (self.mapObj); y++) {
			for (var x = 0; x < len (self.mapObj [0]); x++) {
				self.tile [y].append ([]);
			}
		}
		var mapSurf = self.drawMap (self.mapObj, self.gameStateObj, self.levelObj ['goals']);
		self.timeStart = time.time ();
	});},
	get keydown () {return __get__ (this, function (self, event) {
		self.keyCode = event.keyCode;
		self.boxes [1].innerHTML = (('Klawisz: ' + self.keyCode) + ' - ') + KEYMAPPING [self.keyCode];
		self.tileUpdate (KEYMAPPING [self.keyCode]);
		if (self.isLevelFinished (self.levelObj, self.gameStateObj) || KEYMAPPING [self.keyCode] == 'n') {
			self.currentLevelIndex++;
			self.initLevel (self.currentLevelIndex);
		}
		else if (KEYMAPPING [self.keyCode] == 'b') {
			self.currentLevelIndex--;
			self.initLevel (self.currentLevelIndex);
		}
		else if (KEYMAPPING [self.keyCode] == 'p') {
			self.currentImage++;
			if (self.currentImage >= len (PLAYERIMAGES)) {
				self.currentImage = 0;
			}
			var mapSurf = self.updateMap (self.mapObj, self.gameStateObj, self.levelObj ['goals']);
		}
		else if (__in__ (KEYMAPPING [self.keyCode], ['up', 'left', 'down', 'right'])) {
			var moved = self.makeMove (self.mapObj, self.gameStateObj, KEYMAPPING [self.keyCode]);
			if (moved) {
				var mapSurf = self.updateMap (self.mapObj, self.gameStateObj, self.levelObj ['goals']);
				self.gameStateObj ['stepCounter']++;
				self.gameStateObj ['timeCounter'] = int (time.time () - self.timeStart);
				if (self.isLevelFinished (self.levelObj, self.gameStateObj)) {
					var __left0__ = divmod (self.gameStateObj ['timeCounter'], 60);
					var m = __left0__ [0];
					var s = __left0__ [1];
					var timeCounterMsg = (m == 0 ? s + ' sec' : ((m + ' min ') + s) + ' sec');
					self.board.innerHTML += ((('<div class="inner"><img src="/static/pic/star_solved.png"><div style="margin:10px;" class="fontDecoration2 fontLGuy">Steps: ' + self.gameStateObj ['stepCounter']) + '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Time: ') + timeCounterMsg) + '</div></div>';
				}
			}
		}
		else if (KEYMAPPING [self.keyCode] == 'u' && len (self.gameStateObj ['playerUndo']) > 0) {
			self.gameStateObj ['player'] = self.gameStateObj ['playerUndo'].py_pop ();
			self.gameStateObj ['stars'] = self.gameStateObj ['starsUndo'].py_pop ();
			var mapSurf = self.updateMap (self.mapObj, self.gameStateObj, self.levelObj ['goals']);
		}
	});},
	get keyup () {return __get__ (this, function (self, event) {
		self.keyCode = null;
	});},
	get py_update () {return __get__ (this, function (self) {
		self.boxes [0].innerHTML = 'Random: ' + random.randint (1, 100);
	});},
	get tileUpdate () {return __get__ (this, function (self, key) {
		var MAPPING = dict ({'up': 'outside floor', 'down': 'inside floor', 'left': 'wall', 'right': 'corner', 'undefined': 'inside floor', 'enter': 'outside floor', 'esc': 'corner', 'space': 'wall'});
		self.boxes [2].innerHTML = MAPPING [key];
		self.boxes [3].innerHTML = IMAGESDICT [MAPPING [key]];
	});},
	get readLevelsFile () {return __get__ (this, function (self, filename) {
		var content = null;
		var xmlhttp = new XMLHttpRequest ();
		xmlhttp.open ('GET', filename, false);
		xmlhttp.send ();
		var content = xmlhttp.responseText.py_split ('\r\n');
		var levels = [];
		var levelNum = 0;
		var mapTextLines = [];
		var mapObj = [];
		for (var lineNum = 0; lineNum < len (content); lineNum++) {
			var line = content [lineNum].rstrip ('\r\n');
			if (__in__ (';', line)) {
				var line = line.__getslice__ (0, line.find (';'), 1);
			}
			if (line != '') {
				mapTextLines.append (line);
			}
			else if (line == '' && len (mapTextLines) > 0) {
				var maxWidth = -(1);
				for (var i = 0; i < len (mapTextLines); i++) {
					if (len (mapTextLines [i]) > maxWidth) {
						var maxWidth = len (mapTextLines [i]);
					}
				}
				for (var i = 0; i < len (mapTextLines); i++) {
					mapTextLines [i] += ' ' * (maxWidth - len (mapTextLines [i]));
				}
				for (var x = 0; x < len (mapTextLines); x++) {
					mapObj.append ([]);
				}
				for (var y = 0; y < len (mapTextLines); y++) {
					for (var x = 0; x < maxWidth; x++) {
						mapObj [y].append ((mapTextLines [y] [x] != 0 && mapTextLines [y] [x] ? mapTextLines [y] [x] : ' '));
					}
				}
				var startx = null;
				var starty = null;
				var goals = [];
				var stars = [];
				for (var x = 0; x < maxWidth; x++) {
					for (var y = 0; y < len (mapObj [x]); y++) {
						if (__in__ (mapObj [x] [y], tuple (['@', '+']))) {
							var startx = x;
							var starty = y;
						}
						if (__in__ (mapObj [x] [y], tuple (['.', '+', '*']))) {
							goals.append (tuple ([x, y]));
						}
						if (__in__ (mapObj [x] [y], tuple (['$', '*']))) {
							stars.append (tuple ([x, y]));
						}
					}
				}
				var gameStateObj = dict ({'player': tuple ([startx, starty]), 'stepCounter': 0, 'timeCounter': 0, 'stars': stars, 'playerUndo': [], 'starsUndo': []});
				var levelObj = dict ({'width': maxWidth, 'height': len (mapObj), 'mapObj': mapObj, 'goals': goals, 'startState': gameStateObj});
				levels.append (levelObj);
				var mapTextLines = [];
				var mapObj = [];
				var gameStateObj = dict ({});
				levelNum++;
			}
		}
		return levels;
	});},
	get decorateMap () {return __get__ (this, function (self, mapObj, startxy) {
		var __left0__ = startxy;
		var startx = __left0__ [0];
		var starty = __left0__ [1];
		var mapObjCopy = [];
		for (var y = 0; y < len (mapObj); y++) {
			mapObjCopy.append ([]);
		}
		for (var y = 0; y < len (mapObj); y++) {
			for (var x = 0; x < len (mapObj [0]); x++) {
				mapObjCopy [y].append (mapObj [y] [x]);
			}
		}
		for (var x = 0; x < len (mapObjCopy); x++) {
			for (var y = 0; y < len (mapObjCopy [0]); y++) {
				if (__in__ (mapObjCopy [x] [y], tuple (['$', '.', '@', '+', '*']))) {
					mapObjCopy [x] [y] = ' ';
				}
			}
		}
		self.floodFill (mapObjCopy, startx, starty, ' ', 'o');
		for (var x = 0; x < len (mapObjCopy); x++) {
			for (var y = 0; y < len (mapObjCopy [0]); y++) {
				if (mapObjCopy [x] [y] == '#') {
					if (self.isWall (mapObjCopy, x, y - 1) && self.isWall (mapObjCopy, x + 1, y) || self.isWall (mapObjCopy, x + 1, y) && self.isWall (mapObjCopy, x, y + 1) || self.isWall (mapObjCopy, x, y + 1) && self.isWall (mapObjCopy, x - 1, y) || self.isWall (mapObjCopy, x - 1, y) && self.isWall (mapObjCopy, x, y - 1)) {
						mapObjCopy [x] [y] = 'x';
					}
				}
				else if (mapObjCopy [x] [y] == ' ' && random.randint (0, 99) < OUTSIDE_DECORATION_PCT) {
					mapObjCopy [x] [y] = random.choice (list (OUTSIDEDECOMAPPING.py_keys ()));
				}
			}
		}
		return mapObjCopy;
	});},
	get floodFill () {return __get__ (this, function (self, mapObj, x, y, oldCharacter, newCharacter) {
		if (mapObj [x] [y] == oldCharacter) {
			mapObj [x] [y] = newCharacter;
		}
		if (x < len (mapObj) - 1 && mapObj [x + 1] [y] == oldCharacter) {
			self.floodFill (mapObj, x + 1, y, oldCharacter, newCharacter);
		}
		if (x > 0 && mapObj [x - 1] [y] == oldCharacter) {
			self.floodFill (mapObj, x - 1, y, oldCharacter, newCharacter);
		}
		if (y < len (mapObj [x]) - 1 && mapObj [x] [y + 1] == oldCharacter) {
			self.floodFill (mapObj, x, y + 1, oldCharacter, newCharacter);
		}
		if (y > 0 && mapObj [x] [y - 1] == oldCharacter) {
			self.floodFill (mapObj, x, y - 1, oldCharacter, newCharacter);
		}
	});},
	get isWall () {return __get__ (this, function (self, mapObj, x, y) {
		if (x < 0 || x >= len (mapObj) || y < 0 || y >= len (mapObj [x])) {
			return false;
		}
		else if (__in__ (mapObj [x] [y], tuple (['#', 'x']))) {
			return true;
		}
		return false;
	});},
	get drawMap () {return __get__ (this, function (self, mapObj, gameStateObj, goals) {
		var mapSurf = '';
		var nl = '\n';
		for (var x = 0; x < len (mapObj); x++) {
			mapSurf += '<div class="up">' + nl;
			var row = html.createElement ('div');
			row.className = 'up';
			self.board.appendChild (row);
			for (var y = 0; y < len (mapObj [x]); y++) {
				var cellInner = '';
				if (__in__ (mapObj [x] [y], TILEMAPPING)) {
					var baseTile = TILEMAPPING [mapObj [x] [y]];
				}
				else if (__in__ (mapObj [x] [y], OUTSIDEDECOMAPPING)) {
					var baseTile = TILEMAPPING [' '];
				}
				mapSurf += '<span>' + baseTile;
				cellInner += baseTile;
				var cell = html.createElement ('span');
				row.appendChild (cell);
				self.tile [x] [y] = cell;
				if (__in__ (mapObj [x] [y], OUTSIDEDECOMAPPING)) {
					mapSurf += OUTSIDEDECOMAPPING [mapObj [x] [y]];
					cellInner += OUTSIDEDECOMAPPING [mapObj [x] [y]];
				}
				else if (__in__ (str (tuple ([x, y])), str (gameStateObj ['stars']))) {
					if (__in__ (str (tuple ([x, y])), str (goals))) {
						mapSurf += IMAGESDICT ['covered goal'];
						cellInner += IMAGESDICT ['covered goal'];
					}
					mapSurf += IMAGESDICT ['star'];
					cellInner += IMAGESDICT ['star'];
				}
				else if (__in__ (str (tuple ([x, y])), str (goals))) {
					mapSurf += IMAGESDICT ['uncovered goal'];
					cellInner += IMAGESDICT ['uncovered goal'];
				}
				mapSurf += '</span>' + nl;
				if (str (tuple ([x, y])) == str (gameStateObj ['player'])) {
					mapSurf += PLAYERIMAGES [self.currentImage];
					cellInner += PLAYERIMAGES [self.currentImage];
				}
				cell.innerHTML = cellInner;
			}
			mapSurf += '</div>' + nl;
		}
		return mapSurf;
	});},
	get updateMap () {return __get__ (this, function (self, mapObj, gameStateObj, goals) {
		var __left0__ = gameStateObj ['player'];
		var playerX = __left0__ [0];
		var playerY = __left0__ [1];
		var x1 = playerX - 2;
		if (x1 < 0) {
			var x1 = 0;
		}
		var x2 = playerX + 3;
		if (x2 > len (mapObj)) {
			var x2 = len (mapObj);
		}
		var y1 = playerY - 2;
		if (y1 < 0) {
			var y1 = 0;
		}
		var y2 = playerY + 3;
		if (y2 > len (mapObj [0])) {
			var y2 = len (mapObj [0]);
		}
		for (var x = x1; x < x2; x++) {
			for (var y = y1; y < y2; y++) {
				var cellInner = '';
				if (__in__ (mapObj [x] [y], TILEMAPPING)) {
					var baseTile = TILEMAPPING [mapObj [x] [y]];
				}
				else if (__in__ (mapObj [x] [y], OUTSIDEDECOMAPPING)) {
					var baseTile = TILEMAPPING [' '];
				}
				cellInner += baseTile;
				if (__in__ (mapObj [x] [y], OUTSIDEDECOMAPPING)) {
					cellInner += OUTSIDEDECOMAPPING [mapObj [x] [y]];
				}
				else if (__in__ (str (tuple ([x, y])), str (gameStateObj ['stars']))) {
					if (__in__ (str (tuple ([x, y])), str (goals))) {
						cellInner += IMAGESDICT ['covered goal'];
					}
					cellInner += IMAGESDICT ['star'];
				}
				else if (__in__ (str (tuple ([x, y])), str (goals))) {
					cellInner += IMAGESDICT ['uncovered goal'];
				}
				if (str (tuple ([x, y])) == str (gameStateObj ['player'])) {
					var currentImage = 0;
					cellInner += PLAYERIMAGES [self.currentImage];
				}
				self.tile [x] [y].innerHTML = cellInner;
			}
		}
		return 'mapSurf';
	});},
	get makeMove () {return __get__ (this, function (self, mapObj, gameStateObj, playerMoveTo) {
		var __left0__ = gameStateObj ['player'];
		var playerx = __left0__ [0];
		var playery = __left0__ [1];
		var stars = gameStateObj ['stars'];
		if (playerMoveTo == 'left') {
			var xOffset = 0;
			var yOffset = -(1);
		}
		else if (playerMoveTo == 'down') {
			var xOffset = 1;
			var yOffset = 0;
		}
		else if (playerMoveTo == 'right') {
			var xOffset = 0;
			var yOffset = 1;
		}
		else if (playerMoveTo == 'up') {
			var xOffset = -(1);
			var yOffset = 0;
		}
		if (self.isWall (mapObj, playerx + xOffset, playery + yOffset)) {
			return false;
		}
		else {
			var starsIsChanged = false;
			if (__in__ (str (tuple ([playerx + xOffset, playery + yOffset])), str (stars))) {
				if (!(self.isBlocked (mapObj, gameStateObj, playerx + xOffset * 2, playery + yOffset * 2))) {
					var starsIsChanged = true;
					gameStateObj ['starsUndo'].append ([]);
					var l = len (gameStateObj ['starsUndo']) - 1;
					for (var s of gameStateObj ['stars']) {
						gameStateObj ['starsUndo'] [l].append (s);
					}
					var ind = stars.index (tuple ([playerx + xOffset, playery + yOffset]));
					var sId = 0;
					for (var s of stars) {
						if (str (tuple ([playerx + xOffset, playery + yOffset])) == str (s)) {
							var ind = sId;
						}
						sId++;
					}
					stars [ind] = tuple ([stars [ind] [0] + xOffset, stars [ind] [1] + yOffset]);
				}
				else {
					return false;
				}
			}
			gameStateObj ['playerUndo'].append (gameStateObj ['player']);
			if (!(starsIsChanged)) {
				gameStateObj ['starsUndo'].append ([]);
				var l = len (gameStateObj ['starsUndo']) - 1;
				for (var s of gameStateObj ['stars']) {
					gameStateObj ['starsUndo'] [l].append (s);
				}
			}
			gameStateObj ['player'] = tuple ([playerx + xOffset, playery + yOffset]);
			return true;
		}
	});},
	get isBlocked () {return __get__ (this, function (self, mapObj, gameStateObj, x, y) {
		if (self.isWall (mapObj, x, y)) {
			return true;
		}
		else if (x < 0 || x >= len (mapObj) || y < 0 || y >= len (mapObj [x])) {
			return true;
		}
		else if (__in__ (str (tuple ([x, y])), str (gameStateObj ['stars']))) {
			return true;
		}
		return false;
	});},
	get isLevelFinished () {return __get__ (this, function (self, levelObj, gameStateObj) {
		for (var goal of levelObj ['goals']) {
			if (!__in__ (str (goal), str (gameStateObj ['stars']))) {
				return false;
			}
		}
		return true;
	});}
});
export var starpusher = Starpusher ();

//# sourceMappingURL=starpusher.map