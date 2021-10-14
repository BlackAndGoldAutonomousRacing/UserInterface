# ROS Client Library for Python
import rclpy
 
# Handles the creation of nodes
from rclpy.node import Node
 
# Handles string messages
from std_msgs.msg import String


from userInterfaceManager import createUI
def msg_to_val(msg):
    return msg.data;

# title, command
buttonsDict = {
    "CT11": ("echo 'command send ct11'",""),
    "launch lidar": ("echo 'launch lidar'","echo 'stop lidar'"),
    "launch long control": ("echo 'long_control set true'","echo 'long_control set false'")
};

# topicname, (lower, upper)
textDict = {
    "novatel/bottom/bestpos" : ((10,1000),msg_to_val,String),
    "raptor_dbw_interface/imu" : ((1,100),msg_to_val,String),
    "raptor_dbw_interface/ctstate": ((0,20),msg_to_val,String),
    "raptor_dbw_interface/wheel_speed_report": ((10,11),msg_to_val,String),
    "raptor_dbw_interface/imu_error": ((10,500),msg_to_val,String),
    "raptor_dbw_interface/gps_covariance": ((100,300),msg_to_val,String)
}

class UserInterface_driver(Node):

  def __init__(self):
 
    # Initiate the Node class's constructor and give it a name
    super().__init__('UserInterface_driver')
 
    self.subscribers = [];

    self.subscription = self.create_subscription(String, 'test', self.listener_callback, 10)
    self.subscription  # prevent unused variable warning



    # create the UI and return the callback functions for the text fields
    self.subFuncs = createUI(buttonsDict=buttonsDict, textDict=textDict);
    

    # create subscribers with topicType and topicName from textDict, and callback function from self.subFuncs
    i = 0;
    for textDictKey in textDict:
        self.subscribers.append(self.create_subscription(textDict[textDictKey][0],f"UI_sub_{textDictKey}",self.subFuncs[i],10))
        i+=1;





 
def main(args=None):
 
  # Initialize the rclpy library
  rclpy.init(args=args)
 
  # Create a subscriber
  userInterface_driver = UserInterface_driver()
 
  # Spin the node so the callback function is called.
  rclpy.spin(userInterface_driver)
 
  # Destroy the node explicitly
  userInterface_driver.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
 
if __name__ == '__main__':
  main()