# 定义节点类,本质为链表的元素
class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


# 定义链表类,实现对链表的各种操作方法
class LinkedList(object):

    def __init__(self, *args):
        self.last_node = Node(value='end', next_node=None)
        self.first_node = Node(value='begin', next_node=self.last_node)
        if args:
            pointer = self.first_node
            for value in args:
                pointer.next_node = Node(value=value, next_node=self.last_node)
                pointer = pointer.next_node

    # 获取起始节点的值
    def __get_first_node_value(self):
        return self.first_node.value

    # 获取末尾节点的值
    def __get_last_node_value(self):
        return self.last_node.value

    # 判断链表是否为空
    def whether_empty(self):
        if self.first_node.next_node == self.last_node:
            return True
        return False

    # 获取链表数据节点的长度
    def get_data_size(self):
        size = 0
        pointer = self.first_node
        while pointer.next_node:  # 从首节点开始循环
            size += 1
            pointer = pointer.next_node
        return size - 1  # 减掉末尾节点

    # 遍历链表,输出链表中所有的值,中间用->表示
    def travel(self):
        pointer = self.first_node
        while pointer.next_node:
            print(pointer.value, end='')
            print(' -> ', end='')
            pointer = pointer.next_node
        print('end')

    # 在末尾节点前插入一个新节点,返回插入的新节点
    def append(self, value):
        new_node = Node(value=value, next_node=self.last_node)
        pointer = self.first_node
        while pointer.next_node:
            if pointer.next_node == self.last_node:
                pointer.next_node = new_node
                return new_node
            pointer = pointer.next_node

    # 在起始节点后插入一个新节点,返回插入的新节点
    def add(self, value):
        pointer = self.first_node
        temp = pointer.next_node
        pointer.next_node = Node(value=value, next_node=temp.next_node)
        return pointer.next_node

    # 在目标序号节点后插入一个新节点,返回插入的新节点,这里的索引是头节点为0,比如after_insert(3,1)就是在索引为3的节点后插入值1,不允许在末尾节点后插入
    def after_insert(self, index, value):
        list_size = self.get_data_size()
        if index > list_size or index < 0:
            raise IndexError(
                'Index out of range! Now the size of linkedlist is {} and the index should not be the end node, so the index should between {} to {}!'.format(
                    list_size + 2, 0, list_size))
        pointer = self.first_node
        for i in range(index):
            pointer = pointer.next_node
        temp = pointer.next_node
        pointer.next_node = Node(value=value, next_node=temp)
        return pointer.next_node

    # 在目标序号的节点前插入一个新节点,返回插入的新节点,这里的索引是头结点为0
    def before_insert(self, index, value):
        list_size = self.get_data_size()
        if index > list_size + 1 or index < 1:
            raise IndexError(
                'Index out of range! Now the size of linkedlist is {} and the index should not be the first node, so the index should between {} to {}!'.format(
                    list_size + 2, 1, list_size + 1))
        pointer = self.first_node
        for i in range(index - 1):
            pointer = pointer.next_node
        temp = pointer.next_node
        pointer.next_node = Node(value=value, next_node=temp)
        return pointer.next_node

    # 删除指定序号的节点,返回删除的节点
    def remove(self, index):
        list_size = self.get_data_size()
        if index < 0 or index > list_size + 1:
            raise IndexError(
                'Index out of range! Now the size of linkedlist is {}, so the index should between {} to {}!'.format(
                    list_size + 2, 0, list_size + 1))
        pointer = self.first_node
        for i in range(index - 1):
            pointer = pointer.next_node
        temp = pointer.next_node
        pointer.next_node = pointer.next_node.next_node
        return temp

    # 输出链表当前信息,包含数据节点的个数,链表的总长度以及链表遍历的结果
    def print_info(self):
        datasize = self.get_data_size()
        print('Now the linkedlist contains {} data nodes, and the total length is {}'.format(datasize, datasize + 2))
        print('Travel the linkedlist: ', end='')
        self.travel()

    # 输出某个序号的指定节点
    def get_node_by_index(self, index):
        list_size = self.get_data_size()
        if index < 0 or index > list_size + 1:
            raise IndexError(
                'Index out of range! Now the size of linkedlist is {}, so the index should between {} to {}!'.format(
                    list_size + 2, 0, list_size + 1))
        pointer = self.first_node
        for i in range(index):
            pointer = pointer.next_node
        return pointer.value
