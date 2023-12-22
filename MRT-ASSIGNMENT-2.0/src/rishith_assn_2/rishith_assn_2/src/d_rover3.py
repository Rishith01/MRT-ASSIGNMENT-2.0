import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class Rover3Publisher(Node):
    def __init__(self):
        super().__init__('d_rover3')
        self.publisher_ = self.create_publisher(String, 'topic3', 10)
        self.timer = self.create_timer(1, self.publish_mission_status)

    def publish_mission_status(self):
        generated_int = random.randint(1, 10)
        if generated_int >= 5:
            status = "Task accomplished"
        else:
            status = "Mission Failed"
        
        msg = String()
        msg.data = status
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    rover3_publisher = Rover3Publisher()
    rclpy.spin(rover3_publisher)
    rover3_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

