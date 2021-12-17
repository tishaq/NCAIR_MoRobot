import time
import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
# import wiringpi

# wiringpi.wiringPiSetupGpio()

backLeftMotor = {"IN1": 23, "IN2":24}
backRightMotor = {"IN1": 26, "IN2":13}
frontRightMotor = {"IN1": 27, "IN2":22}
frontLeftMotor = {"IN1": 25, "IN2":12}

# wiringpi.pinMode(frontLeftMotor["IN1"], 1)
# wiringpi.pinMode(frontLeftMotor["IN2"], 1)
# wiringpi.pinMode(frontRightMotor["IN1"], 1)
# wiringpi.pinMode(frontRightMotor["IN2"], 1)

# wiringpi.pinMode(backLeftMotor["IN1"], 1)
# wiringpi.pinMode(backLeftMotor["IN2"], 1)
# wiringpi.pinMode(backRightMotor["IN1"], 1)
# wiringpi.pinMode(backRightMotor["IN2"], 1)

def move(motor, direction):
    if direction == 0: #clockwise movement
        # wiringpi.digitalWrite(motor["IN1"], 1)
        # wiringpi.digitalWrite(motor["IN2"], 0)
        print("moving "+motor + " in "+direction+" direction")
    elif direction == 1:  #counterclockwise movement
        # wiringpi.digitalWrite(motor["IN1"], 0)
        # wiringpi.digitalWrite(motor["IN2"], 1)
        print("moving "+motor + " in "+direction+" direction")
    else:  #stop movement
        # wiringpi.digitalWrite(motor["IN1"], 0)
        # wiringpi.digitalWrite(motor["IN2"], 0)
        print("moving "+motor + " in "+direction+" direction")

def moveForward():
    move(frontRightMotor, 1)
    move(frontLeftMotor, 1)
    move(backRightMotor, 1)
    move(backLeftMotor, 1)

def moveBackward():
    move(frontRightMotor, 0)
    move(frontLeftMotor, 0)
    move(backRightMotor, 0)
    move(backLeftMotor, 0)

def forceStop():
    move(frontRightMotor, 2)
    move(frontLeftMotor, 2)
    move(backRightMotor, 2)
    move(backLeftMotor, 2)

def left():
    move(frontRightMotor, 0)
    move(frontLeftMotor, 1)
    move(backRightMotor, 1)
    move(backLeftMotor, 0)

def right():
    move(frontRightMotor, 1)
    move(frontLeftMotor, 0)
    move(backRightMotor, 0)
    move(backLeftMotor, 1)

def forwardLeft():
    move(frontRightMotor, 2)
    move(frontLeftMotor, 1)
    move(backRightMotor, 1)
    move(backLeftMotor, 2)

def forwardRight():
    move(frontRightMotor, 1)
    move(frontLeftMotor, 2)
    move(backRightMotor, 2)
    move(backLeftMotor, 1)

def backwardLeft():
    move(frontRightMotor, 0)
    move(frontLeftMotor, 2)
    move(backRightMotor, 2)
    move(backLeftMotor, 0)

def backwardRight():
    move(frontRightMotor, 2)
    move(frontLeftMotor, 0)
    move(backRightMotor, 0)
    move(backLeftMotor, 2)

def turnLeft():
    move(frontRightMotor, 1)
    move(frontLeftMotor, 0)
    move(backRightMotor, 1)
    move(backLeftMotor, 0)

def turnRight():
    move(frontRightMotor, 0)
    move(frontLeftMotor, 1)
    move(backRightMotor, 0)
    move(backLeftMotor, 1)
    
def lateralArc():
    move(frontRightMotor, 0)
    move(frontLeftMotor, 1)
    move(backRightMotor, 2)
    move(backLeftMotor, 2)

class DriverNode(Node):
    def __init__(self):
        super().__init__('driver_node')
        self.driver = self.create_subscription(Twist, "/turtle1/cmd_vel", self.driver_callback, 10)
        self.driver
    def driver_callback(self, msg):
        self.get_logger().info("[Received Message]: %s" % msg.linear.x)
        self.get_logger().info("[Received Message]: %s" % msg.angular.z)
        #check for linear direction
        if(msg.linear.x == 0.0 and msg.angular.z == 0.0):
            self.get_logger().info("Do nothing linear")
            # forceStop()
        elif(msg.linear.x == 2.0):
            self.get_logger().info("Go Forward")
            # moveForward()
        elif(msg.linear.x == -2.0):
            self.get_logger().info("Go Backword")  
            # moveBackward()
        elif(msg.angular.z == 2.0):
            self.get_logger().info("turn left")
            # turnLeft()
        elif(msg.angular.z == -2.0):
            self.get_logger().info("turn right")     
            # turnRight()  

def main(args=None):
    rclpy.init(args=args)
    driver_node = DriverNode()
    rclpy.spin(driver_node)
    
    driver_node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()