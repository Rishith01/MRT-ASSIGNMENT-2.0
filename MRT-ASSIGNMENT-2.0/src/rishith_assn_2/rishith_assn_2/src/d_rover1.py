import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Rover1Publisher(Node):
    def __init__(self):
        super().__init__('d_rover1')
        self.publisher_ = self.create_publisher(Float32, 'topic1', 10)
        self.timer = self.create_timer(1, self.publish_altitude)

    def publish_altitude(self):
        altitude = random.uniform(0, 100)
        msg = Float32()
        msg.data = altitude
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    rover1_publisher = Rover1Publisher()
    rclpy.spin(rover1_publisher)
    rover1_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

