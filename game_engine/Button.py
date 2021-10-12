
'''
===============================================================================
    Project:        Python Game Engine
	Author:         Alec Pannunzio, afpannun@purdue.edu
===============================================================================
'''


from typing import TextIO
from game_engine.GameEngineToolbox import checkType
from game_engine.GameObject import GameObject
from game_engine.Object2D import Object2D


from pygame_button import Button as BT

default_button_style = {
    "hover_color": (0,255,0),
    "clicked_color": (255,0,0),
    "clicked_font_color": (0,0,0),
    "hover_font_color": (0,0,255),
  #  "hover_sound": pg.mixer.Sound("blipshort1.wav"),
}

class Button(Object2D):

    def __init__(self,name,event_func,objectDraw, xPosition, yPosition,xSize,ySize, text=False, style=default_button_style):
        super(Button,self).__init__(name,xPosition,yPosition,xSize,ySize);
        #checkType(event_func,function.__class__,"event function must be of type function");
        checkType(xPosition,(int,float));
        checkType(yPosition,(int,float));
        checkType(xSize,(int,float));
        checkType(ySize,(int,float));
        
        # if we haven't been passed button text, just use the name of this object
        if (not text):
            text = name;

        self.screen_rect = objectDraw.screen.get_rect()
        self.button = BT((0, 0, xSize, ySize), (255,0,0), event_func, text=text, **style);
        

    def paint(self, screen):
        self.button.rect.center = (self.xPosition, self.yPosition);
        self.button.update(screen);
