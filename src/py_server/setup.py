from setuptools import find_packages, setup
package_name = 'py_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'my_interface',],
    zip_safe=True,
    maintainer='ingibirka',
    maintainer_email='kimbap924@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = py_server.service:main',
            'client = py_server.client:main',
        ],
    },
)
