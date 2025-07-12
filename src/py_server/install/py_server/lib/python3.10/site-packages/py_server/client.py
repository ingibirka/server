import sys
import rclpy
from rclpy.node import Node

from my_interface.srv import StringLength


class StringLengthClientAsync(Node):

    def __init__(self):
        super().__init__('string_length_client_async')
        self.cli = self.create_client(StringLength, 'get_string_length')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = StringLength.Request() 

    def send_request(self, input_string):
        self.req.input_string = input_string
        return self.cli.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    string_length_client = StringLengthClientAsync()

    input_string_from_args = sys.argv[1]
    future = string_length_client.send_request(input_string_from_args)
    rclpy.spin_until_future_complete(string_length_client, future)
    response = future.result()
    string_length_client.get_logger().info(
            f'send "{input_string_from_args}" \nrecieve "{response.length_str}"')
        

    string_length_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()