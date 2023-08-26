import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class Hello_Sub(Node):
    
    def __init__(self):
        super().__init__('hello_sub')
        qos_profile = QoSProfile(depth = 10)
        self.hello_sub = self.create_subscription(String, 'helloworld', self.subscribe_topic_message, qos_profile)
        
    def subscribe_topic_message(self, msg):
        self.get_logger().info("Received message: {}".format(msg.data))


def main(args = None):
    rclpy.init(args = args)
    node = Hello_Sub()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyborad Interrupt")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()