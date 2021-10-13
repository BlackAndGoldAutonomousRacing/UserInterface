from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
from game_engine.Button import Button
import time
import subprocess


colorRed = (255,0,0);
colorGreen = (0,255,0);

screenSplit = 0.9;

subFuncs = [];


def sendCommand(commandStr, shell=True):
    subprocess.run(commandStr, shell=shell);

def createButtons(buttons, objectDraw):
    xStep = objectDraw.screenSizeX / len(buttons);
    
    multFromBtm = 1-screenSplit;

    screenSizeY = objectDraw.screenSizeY;
    
    i = 0;
    for key in buttons:
        print(buttons[key]);
        newBtn = Button(key, sendCommand,objectDraw, i * xStep + xStep/2 , screenSizeY-screenSizeY*multFromBtm,xSize=xStep,ySize=screenSizeY*multFromBtm, params=buttons[key]);
        objectDraw.add(newBtn);
        i += 1;


class TextUpdater():
    def __init__(self, text, valueRange = (-1000000000000000,10000000000000)):
        self.text = text;
        self.valueRange = valueRange
    def subFunction(self,msg):
        self.text.setText(self.text.name + ": " + str(msg.data));
        if (float(msg.data) > self.valueRange[0] and float(msg.data) < self.valueRange[1]):
            self.text.setColor(colorGreen);
        else:
            self.text.setColor(colorRed);


def createTopicStatuses(topics,objectDraw):
    yStep = objectDraw.screenSizeY*screenSplit // (1+len(topics));

    if (yStep < 10):
        fontSize = yStep;
    else:
        fontSize = 30;

    i = 0;
    for topicName in topics:
        
        text1 = Text(topicName,screenSizeX/2,(5+fontSize) * i + fontSize/2,fontSize=fontSize);
        objectDraw.add(text1);

        
        textUpdate = TextUpdater(text1, topics[topicName]);

        # createsubscription
        subFuncs.append(textUpdate.subFunction);
    
        i += 1;

   







# define params and make objectDraw
screenSizeX = 1000;
screenSizeY = 500;

objectDraw = ObjectDraw(screenSizeX,screenSizeY);






# create buttons and text messages


# title, command
buttonsDict = {
    "CT11": "echo 'command send ct11'",
    "launch cameras": "ros2 launch cameras'",
    "launch long control": "echo 'launching auton beep boop'"
};

createButtons(buttonsDict,objectDraw);


# topicname, (lower, upper)
textDict = {
    "novatel/bottom/bestpos" : (10,1000),
    "raptor_dbw_interface/imu" : (1,100),
    "raptor_dbw_interface/ctstate": (10,11)
}

createTopicStatuses(textDict,objectDraw);









# start the engine
objectDraw.start();









# run the engine


class msg():
    def __init__(self,data):
        self.data = data;


i = 1;
while(True):
    i+=1;
    
    msg1 = msg(i);
    for fun in subFuncs:
        fun(msg1);

    objectDraw.run();
    time.sleep(0.01);

