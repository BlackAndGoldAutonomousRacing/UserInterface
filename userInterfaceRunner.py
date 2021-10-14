


from IAC_Button import IAC_Button
from IAC_textBox_Button import IAC_textBox_Button
from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
from game_engine.Sprite import Sprite
import time
import subprocess
from math import sqrt

colorRed = (255,0,0);
colorGreen = (0,255,0);

screenSplitText = 0.25;
screenSplitButton = 0.9;

subFuncs = [];


def sendCommand(commandStr, shell=True):
    subprocess.run(commandStr, shell=shell);

def createButtons(buttons, objectDraw):
    xStep = objectDraw.screenSizeX / len(buttons);
    
    multFromBtm = 1-screenSplitButton;

    screenSizeY = objectDraw.screenSizeY;
    
    i = 0;
    for key in buttons:
        newBtn = IAC_Button(key, sendCommand,objectDraw, i * xStep + xStep/2 , screenSizeY-screenSizeY*multFromBtm,xSize=xStep,ySize=screenSizeY*multFromBtm, params=buttons[key]);
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
    yStep = objectDraw.screenSizeY*screenSplitText // (1+len(topics));

    fontSize = 1.0 * yStep;

    i = 0;
    for topicName in topics:
        
        text1 = Text(topicName,screenSizeX*0.5-10*fontSize,(5+fontSize) * i + fontSize,fontSize=fontSize,highLightColor=(10,10,10));
        objectDraw.add(text1);

        
        textUpdate = TextUpdater(text1, topics[topicName]);

        # createsubscription
        subFuncs.append(textUpdate.subFunction);
    
        i += 1;

   







# define params and make objectDraw

screenScale = 1.5;
screenSizeX = int(1000 * screenScale);
screenSizeY = int(500 * screenScale);

diagonal = sqrt(screenSizeY**2 + screenSizeX**2);

objectDraw = ObjectDraw(screenSizeX,screenSizeY,frameCaption="Black and Gold Autonomous Racing Control Suite");



# create background image
print(diagonal);
background = Sprite("backgroundlogo",screenSizeX/2,screenSizeY*0.45,scaling=diagonal/1000,imgSource="assets/Blackandgoldlogo.png");
objectDraw.setBackgroundColor((0,0,0));
objectDraw.add(background);






# create pointless add-ons to make it look cooler
hologram1 = Sprite("hologram_rotator_1", screenSizeX*0.9,screenSizeY*0.7,diagonal/9000,"assets/hologram rotator.png");
hologram1.setAngularVelocity(0.5);
objectDraw.add(hologram1);

hologram2 = Sprite("hologram_rotator_2", screenSizeX*0.07,screenSizeY*0.17,diagonal/10000,"assets/hologram_radar.jpg");
hologram2.setAngularVelocity(-0.7);
objectDraw.add(hologram2);


# create buttons and text messages


# title, command
buttonsDict = {
    "CT11": ("echo 'command send ct11'",""),
    "launch lidar": ("echo 'launch lidar'","echo 'stop lidar'"),
    "launch long control": ("echo 'long_control set true'","echo 'long_control set false'")
};

createButtons(buttonsDict,objectDraw);

velocityButton = IAC_textBox_Button("set target velocity",objectDraw, screenSizeX*0.5,screenSizeY*0.75,200,screenSizeY*(1-screenSplitButton));

objectDraw.add(velocityButton);


# topicname, (lower, upper)
textDict = {
    "novatel/bottom/bestpos" : (10,1000),
    "raptor_dbw_interface/imu" : (1,100),
    "raptor_dbw_interface/ctstate": (0,20),
    "raptor_dbw_interface/wheel_speed_report": (10,11),
    "raptor_dbw_interface/imu_error": (10,500),
    "raptor_dbw_interface/gps_covariance": (100,300)
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
    
    msg1 = msg(i%500);
    for fun in subFuncs:
        fun(msg1);

    objectDraw.run();
    time.sleep(0.01);

