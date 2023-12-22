import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String
from geometry_msgs.msg import Point, Pose

class BaseStationSubscriber(Node):
    def __init__(self):
        super().__init__('basestation')
        
        # Subscribe to topic1 (std_msgs/Float32) to receive altitude values
        self.subscription1 = self.create_subscription(
            Float32,
            'topic1',
            self.callback_topic1,
            10
        )
        self.subscription1  # prevent unused variable warning

        # Subscribe to topic2 (geometry_msgs/Point) to receive location data
        self.subscription2 = self.create_subscription(
            Point,
            'topic2',
            self.callback_topic2,
            10
        )
        self.subscription2  # prevent unused variable warning

        # Subscribe to topic3 (std_msgs/String) to receive mission status
        self.subscription3 = self.create_subscription(
            String,
            'topic3',
            self.callback_topic3,
            10
        )
        self.subscription3  # prevent unused variable warning

    def callback_topic1(self, msg):
        self.get_logger().info(f"Received Altitude: {msg.data}")

    def callback_topic2(self, msg):
        self.get_logger().info(f"Received Location: x={msg.x}, y={msg.y}, z={msg.z}")

    def callback_topic3(self, msg):
        self.get_logger().info(f"Mission Status: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    basestation_subscriber = BaseStationSubscriber()
    rclpy.spin(basestation_subscriber)
    basestation_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

