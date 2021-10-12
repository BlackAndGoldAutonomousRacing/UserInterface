from game_engine.ObjectDraw import ObjectDraw
from game_engine.Text import Text
import time

colorRed = (255,0,0);
colorGreen = (0,255,0);

screenSizeX = 1000;
screenSizeY = 1000;

objectDraw = ObjectDraw(screenSizeX,screenSizeY);

text1 = Text("testText",screenSizeX/2,screenSizeY/2);

objectDraw.add(text1);

objectDraw.start();



i = 1;
while(True):
    i+=1;
    if (i % 10 == 0):
        text1.setColor(colorRed);
    else:
        text1.setColor(colorGreen);

    text1.setText(f"Testing text: {i}");
    objectDraw.run();
    time.sleep(0.5);

