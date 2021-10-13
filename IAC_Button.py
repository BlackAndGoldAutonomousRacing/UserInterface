from game_engine.Button import Button





class IAC_Button(Button):

    def __init__(self, name, func_to_call, objectDraw, xPosition, yPosition, xSize, ySize, params):
        super().__init__(name, func_to_call, objectDraw, xPosition, yPosition, xSize, ySize, params=params, color=(255,0,0));



    def onButtonClick(self):
        if (self.color == (255,0,0)):
            self.color = (0,255,0);
        else:
            self.color = (255,0,0);
        self.updateButtonParams();
        return super().onButtonClick();

        