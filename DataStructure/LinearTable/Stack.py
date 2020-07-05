from DataStructure.LinkedList import *


# 定义栈类,后进先出,从首节点进,从首节点出
class Stack(LinkedList):
    # 直接从链表类进行继承
    def __init__(self, *args):
        super().__init__(*args)

    # 将数据推入栈中,返回入栈的节点
    def push(self, value):
        self.after_insert(0, value)
        return self.first_node.next_node

    # 将数据从栈中弹出,返回弹出的节点
    def pop(self):
        if not self.get_data_size():
            return None
        temp = self.first_node.next_node
        self.first_node.next_node = temp.next_node
        return temp
