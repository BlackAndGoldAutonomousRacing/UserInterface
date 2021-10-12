from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
from game_engine.Button import Button
import time
import subprocess


colorRed = (255,0,0);
colorGreen = (0,255,0);


def sendCommand(commandStr, shell=True):
    subprocess.run(commandStr, shell=shell);

def createButtons(buttons, objectDraw):
    xStep = objectDraw.screenSizeX / len(buttons);
    i = 0;
    for key in buttons:
        print(buttons[key]);
        newBtn = Button(key, lambda : sendCommand(buttons.get(key)),objectDraw, i * xStep + xStep/2 , screenSizeY-screenSizeY*0.1,xSize=xStep,ySize=screenSizeY*0.1);
        objectDraw.add(newBtn);
        i += 1;


screenSizeX = 1000;
screenSizeY = 500;

objectDraw = ObjectDraw(screenSizeX,screenSizeY);


buttonsDict = {
    "CT11": "echo 'command send ct11'",
    "launch cameras": "echo 'hello'",
    "launch long control": "echo 'launching auton beep boop'"
};

createButtons(buttonsDict,objectDraw);



text1 = Text("testText",screenSizeX/2,screenSizeY/2);

def buttonFunc():
    print("button was pressed!");

Button1 = Button("testButton",buttonFunc,objectDraw,screenSizeX/2,screenSizeY*2/3,100,10);

objectDraw.add(Button1);
objectDraw.add(text1);

objectDraw.start();



i = 1;
while(True):
    i+=1;
    if (i//100 % 2 == 0):
        text1.setColor(colorRed);
    else:
        text1.setColor(colorGreen);

    text1.setText(f"Testing text: {i}");
    objectDraw.run();
    time.sleep(0.01);

