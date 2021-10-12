
from game_engine.GameEngineToolbox import checkType
import pygame
from game_engine.Object2D import Object2D

class Text(Object2D):

    def __init__(self,name,xPosition,yPosition,fontFamily="freesansbold.ttf",fontSize=32,color=(255,255,255)):
        super(Text,self).__init__(name,xPosition,yPosition,1,1);

        self.color = color;

        self.font = pygame.font.Font(fontFamily, fontSize)
        

        self.setText(self.name);

    def setColor(self,color):
        checkType(color,tuple); 
        self.color = color;

    def setText(self,text):
        self.text = self.font.render(text, True, self.color, (0,0,0));
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.xPosition, self.yPosition)

    def paint(self, screen):
        screen.blit(self.text, self.textRect);