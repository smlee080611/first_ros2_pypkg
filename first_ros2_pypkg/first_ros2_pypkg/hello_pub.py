import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String


class Hello_Pub(Node):

    def __init__(self):
        super().__init__("hello_pub")
        qos_profile = QoSProfile(depth = 10)
        self.hello_pub = self.create_publisher(String, 'helloworld', qos_profile)
        self.timer = self.create_timer(1, self.publish_hello_msg)
        self.count = 0

    def publish_hello_msg(self):
        msg = String()
        msg.data = 'helloworld{}'.format(self.count)
        self.hello_pub.publish(msg)
        self.get_logger().info('published message: {}'.format(msg.data))
        self.count += 1


def main(args = None):
    rclpy.init(args = args)
    node = Hello_Pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyborad Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()