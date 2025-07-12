import rclpy
from rclpy.node import Node

from my_interface.srv import StringLength

class StringLengthServer(Node):

    def __init__(self):
        super().__init__('string_length_server')
        self.srv = self.create_service(StringLength, 'get_string_length', self.string_length_callback)
        self.get_logger().info('start')

    def string_length_callback(self, request, response):
        self.get_logger().info(f'recieve "{request.input_string}"')
        response.length_str = str(len(request.input_string))
        self.get_logger().info(f'send "{response.length_str}"')
        return response

def main(args=None):
    rclpy.init(args=args)
    string_length_server = StringLengthServer()
    rclpy.spin(string_length_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()