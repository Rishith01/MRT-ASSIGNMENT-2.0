import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
import random

class Rover2Publisher(Node):
    def __init__(self):
        super().__init__('d_rover2')
        self.publisher_ = self.create_publisher(Point, 'topic2', 10)
        self.timer = self.create_timer(1, self.publish_location)

    def publish_location(self):
        location = Point()
        location.x = random.uniform(0, 200)
        location.y = random.uniform(0, 200)
        location.z = random.uniform(0, 200)
        self.publisher_.publish(location)

def main(args=None):
    rclpy.init(args=args)
    rover2_publisher = Rover2Publisher()
    rclpy.spin(rover2_publisher)
    rover2_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

