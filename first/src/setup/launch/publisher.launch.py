from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    publisher = Node(
            package='publisher',
            namespace='first',
            executable='talker',
            name='publisher'
    )

    ld.add_action(publisher)

    return ld
