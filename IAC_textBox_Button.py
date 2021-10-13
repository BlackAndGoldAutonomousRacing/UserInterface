
from game_engine.Button import Button

import subprocess

import pygame 


#keys = {'1':pygame.K_1}
class IAC_textBox_Button(Button):

    def __init__(self, name, objectDraw, xPosition, yPosition, xSize, ySize):
        super().__init__(name, self.buttonPress, objectDraw, xPosition, yPosition, xSize, ySize, color=(255,0,0));


        self.objectDraw = objectDraw;

        self.enteringVelocity = False;
        self.velocityCommand = "";

    # when the button is pressed
    def buttonPress(self,params=0):
        self.enteringVelocity = True;

        
        self.setColor((0,100,30));
        self.velocityCommand = "";

        

        

    def update(self):
        if(self.enteringVelocity):
            for keyEvent in self.objectDraw.keyEvents:
                if (keyEvent.key == pygame.K_BACKSPACE):
                    self.velocityCommand = self.velocityCommand[0:-1];
                elif (keyEvent.key == pygame.K_RETURN):
                    self.enteringVelocity = False;
                    subprocess.run(f"echo 'setVelocity {self.velocityCommand}'",shell=True);
                    self.setColor((255,0,0));
                    self.velocityCommand = "";
                    self.text = self.name;  
                    self.updateButtonParams();   
                    return;    
                else:
                    self.velocityCommand += keyEvent.unicode;
            
            self.text = "Send velocity: " + self.velocityCommand;
            self.updateButtonParams();
                

 