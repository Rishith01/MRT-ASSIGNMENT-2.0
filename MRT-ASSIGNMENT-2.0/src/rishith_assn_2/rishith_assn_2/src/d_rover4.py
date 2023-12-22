import rclpy
from rclpy.node import Node
from custom_msgs.msg import RoverStatus  # Assuming custom message type is defined in custom_msgs package
from geometry_msgs.msg import Pose
from std_msgs.msg import String, Header
import random

class Rover4Publisher(Node):
    def __init__(self):
        super().__init__('d_rover4')
        self.publisher_ = self.create_publisher(RoverStatus, 'topic4', 10)
        self.timer = self.create_timer(1, self.publish_rover_status)

    def publish_rover_status(self):
        rover_status = RoverStatus()
        rover_status.rover_id = random.randint(1, 100)
        rover_status.battery_level = random.uniform(0, 100)
        
        # Setting up current location
        rover_status.current_location = Pose()
        rover_status.current_location.position.x = random.uniform(0, 10)
        rover_status.current_location.position.y = random.uniform(0, 10)
        rover_status.current_location.position.z = random.uniform(0, 10)
        
        # Setting up health status
        if random.random() < 0.5:
            rover_status.health_status = "Good"
        else:
            rover_status.health_status = "Bad"

        self.publisher_.publish(rover_status)

def main(args=None):
    rclpy.init(args=args)
    rover4_publisher = Rover4Publisher()
    rclpy.spin(rover4_publisher)
    rover4_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

