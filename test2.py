#!/usr/bin/env python3
# ROS版本代码
import rospy
from robot_sdk import GripperClient
from std_srvs.srv import SetBool, SetBoolResponse  # 使用标准布尔服务

class GripperROSNode:
    def __init__(self):
        # 1. 初始化节点
        rospy.init_node('gripper_controller')
        
        # 2. 从参数服务器读取硬件地址，而非硬编码
        robot_ip = rospy.get_param('~robot_ip', '192.168.1.100')
        
        # 3. 初始化硬件驱动（封装在节点内部）
        self.gripper = GripperClient(robot_ip)
        
        # 4. 创建一个ROS服务，对外提供 `control` 接口
        self.srv = rospy.Service('~control', SetBool, self.handle_control_request)
        
        rospy.loginfo("夹爪ROS节点已启动，等待服务请求...")
    
    def handle_control_request(self, req):
        """服务请求处理回调函数"""
        try:
            if req.data:  # 如果请求中的 data 字段为 True
                self.gripper.open()
                result = True
                message = "夹爪已打开"
            else:         # 如果请求中的 data 字段为 False
                self.gripper.close(position=50, speed=100, force=50)
                result = True
                message = "夹爪已关闭"
            # 返回服务响应
            return SetBoolResponse(success=result, message=message)
        except Exception as e:
            return SetBoolResponse(success=False, message=str(e))
    
    def run(self):
        rospy.spin() # 保持节点运行，等待服务调用

if __name__ == '__main__':
    node = GripperROSNode()
    node.run()