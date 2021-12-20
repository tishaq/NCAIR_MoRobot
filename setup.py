from setuptools import setup

package_name = 'ncairobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ncair',
    maintainer_email='ncair@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'driver_node = ncairobot.driver_node:main',
            'img_publisher = ncairobot.webcam_pub:main',
        ],
    },
)
