from DataStructure.LinkedList import *


# 定义队列类,先进先出,从首节点进,从末节点出
class Queue(LinkedList):
    # 直接从链表类继承
    def __init__(self, *args):
        super().__init__(*args)

    # 将数据推入队列中,返回入栈的节点
    def push(self, value):
        self.after_insert(0, value)
        return self.first_node.next_node

    # 将数据从队列中弹出,返回弹出的节点
    def pop(self):
        if not self.get_data_size():
            return None
        pointer = self.first_node
        while pointer.next_node.next_node.next_node:
            pointer = pointer.next_node
        temp = pointer.next_node
        pointer.next_node = self.last_node
        return temp
