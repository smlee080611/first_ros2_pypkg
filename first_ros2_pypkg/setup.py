from setuptools import find_packages, setup

package_name = 'first_ros2_pypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='smlee080611',
    maintainer_email='smlee080611@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_pub = first_ros2_pypkg.hello_pub:main',
            'hello_sub = first_ros2_pypkg.hello_sub:main',
        ],
    },
)
