#!/usr/bin/env /usr/bin/python3
import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Joy

class JoyRecv(Node):
    node_name = 'joy_recv'
    topic_name = 'joy'
    
    def __init__(self) -> None:
        super().__init__(self.node_name)
        self.sub = self.create_subscription(Joy, self.topic_name, self.callback, 10)
    
    def __del__(self):
        pass
    
    def callback(self, joy):
        self.get_logger().info("axis: %f, %f, %f, %f  button%d" %(joy.axes[0], joy.axes[1], joy.axes[2], joy.axes[3], joy.buttons[0]))


def main(args=None):
    rclpy.init(args=args)
    joy_recv = JoyRecv()
    
    try:
        rclpy.spin(joy_recv)
    except KeyboardInterrupt:
        pass
    finally:
        joy_recv.destroy_node()
    

if __name__ == '__main__':
    main()
