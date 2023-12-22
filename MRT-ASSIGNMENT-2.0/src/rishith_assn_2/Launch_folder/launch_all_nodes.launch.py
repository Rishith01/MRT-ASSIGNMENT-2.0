from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rishith_assn_2',
            executable='d_rover1',
            name='d_rover1'
        ),
        Node(
            package='rishith_assn_2',
            executable='d_rover2',
            name='d_rover2'
        ),
        Node(
            package='rishith_assn_2',
            executable='d_rover3',
            name='d_rover3'
        ),
    ])

