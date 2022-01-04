# the node in doubly-linked list
class Node:
    def __init__(self, prev, next):
        # previous node
        self.prev = prev
        # next node
        self.next = next
        # value of current node
        self.value = 0

    # to get previous node
    def get_prev(self):
        return self.prev

    # to get next node 
    def get_next(self):
        return self.next

    # to get the value of current node
    def get_value(self):
        return self.value

    # set previous node 
    def set_prev(self, node):
        self.prev = node

    # set next node
    def set_next(self, node):
        self.next = node

    # set the value of current node
    def set_value(self, val):
        self.value = val


# doubly-linked list
class DoublyLinkedList:
    def __init__(self):
        # # initialize a head node and let it point to this head node 
        # self.head = Node(None, None)
        # # create a end node and let it point to this head node 
        # self.end = self.head
        self.head = None
        self.end = None


    # add a node to the end of linkedlist 
    def add_to_end(self, val):
        # # create a node, set its previous node is the end node and point to None
        # node = Node(self.end, None)
        # # set the value of this new node 
        # node.set_value(val)
        #
        # # let end node point to the new node 
        # self.end.set_next(node)
        # # update new node as the linkedlist end node
        # self.end = node
        if self.head is None:
            self.head = Node(None, None)
            self.head.set_value(val)
            self.end = self.head
        else:
            node = Node(self.end, None)
            node.set_value(val)
            self.end.set_next(node)
            self.end = node


    # add a node to the head of linkedlist 
    def add_to_front(self, val):
        # # create a new node, its previous node is head node and its next node is the next node of the head node
        # node = Node(self.head, self.head.get_next())
        # # set the value for new node
        # node.set_value(val)
        # # set node is the previous node of head next node if head next node is not null
        # if self.head.get_next() is not None:
        #     self.head.get_next().set_prev(node)
        # # let head node point to the new node 
        # self.head.set_next(node)

        if self.head is None:
            self.head = Node(None, None)
            self.head.set_value(val)
            self.end = self.head
        else:
            node = Node(None, self.head)
            node.set_value(val)
            self.head.set_prev(node)
            self.head = node


    # delete node
    def delete(self, val):
        # node = self.head.get_next()
        # #  traverse the linkedlist to find a node with val value
        # while node is not None:
        #     if node.get_value() == val:
        #         node.get_prev().set_next(node.get_next())
        #         if node.get_next() is not None:
        #             node.get_next().set_prev(node.get_prev())
        #         break
        #     node = node.get_next()

        node = self.head
        while node is not None:
            if node.get_value() == val:
                # if need to delete the head node
                if node.get_prev() is None:
                    self.head = node.get_next()
                else:
                    # the previous node of the node will point to the next node after the node
                    node.get_prev().set_next(node.get_next())
                    if node.get_next() is not None:
                        node.get_next().set_prev(node.get_prev())
                break
            node = node.get_next()

    def reverse(self):
        """
        traverse the linkedlist, using delete method and add_to_front method to add every node into linkedlist
        for example,  the orginal linkedlist is 1 2 3 4
        when interating 1st element, delete 1 then add 1 to the front, 1 2 3 4
        when interating 2nd element, delete 2 then add 2 to the front, 2 1 3 4 
        when interating 3rd element, delete 3 then add 3 to the front, 3 2 1 4
        when interating 4th element, delete 4 then add 4 to the front, 4 3 2 1 
        """
        # node = self.head.get_next()
        # while node is not None:
        #     # keep the next node of current node in case fail to traverse linkedlist after deleting
        #     temp = node.get_next()
        #     # delete the node
        #     val = node.get_value()
        #     self.delete(val)
        #     # add the node to the front
        #     self.add_to_front(val)
        #     # keep going to traverse the linkedlist
        #     node = temp
        node = self.head
        while node is not None:
            temp = node.get_next()
            val = node.get_value()
            self.delete(val)
            self.add_to_front(val)
            node = temp

    # compare a list with current linkedlist
    def compare(self, lst):
        # p = self.head.get_next()
        p = self.head
        pos = 0
        Len = len(lst)
        # traverse linkedlist and list at the same time, it will return false when they are not equal 
        while (p is not None) and pos < Len:
            if p.get_value() != lst[pos]:
                return False
            p = p.get_next()
            pos += 1
        # their value as same as their length  
        if p is None and pos == Len:
            return True
        else:
            return False

    
    def find(self, val):
    # return the index(as it would be in a list) of the first occurrence of val
        pos = 0
        # node = self.head.get_next()
        node = self.head
        while node is not None:
            if val == node.get_value():
                return pos
            pos += 1
            node = node.get_next()

    # this method only for test
    def printf(self):
        node = self.head
        print(node.get_value(), end="")
        node = node.get_next()
        while node is not None:
            print(", %d" % node.get_value(), end="")
            node = node.get_next()
        print()



def merge_sort(str):
    if len(str) <= 1:  # subsequence
        return str
    mid = (len(str) // 2)
    left = merge_sort(str[:mid])  # recursively slice
    right = merge_sort(str[mid:len(str)])
    result = []
    # i,j = 0,0

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            # result.append(left[0])
            result.append(left.pop(0))
            # i+= 1
        else:
            # result.append(right[0])
            result.append(right.pop(0))
            # j+= 1

    if len(left) > 0:
        result.extend(merge_sort(left))
    else:
        result.extend(merge_sort(right))
    return result



def lst_to_dict(lst, l, r):
    d = {}
    Len = len(lst)
    # set every value between l and r is None
    for i in range(l, r + 1):
        d[i] = None
    # traverse lst, update every value between l and r in the dictionary 
    for i in range(Len):
        if l <= lst[i] <= r:
            d[lst[i]] = i
    return d


def target_sum(lst, target):

    """
    since given list already sorted, sorting list is a waste time here
    if lst[l]+lst[r] < target, then l += 1
    if lst[l]+lst[r] > target, then r -= 1
    until lst[l]+lst[r] == target, return l, r
    """
    # lst = merge_sort(lst)
    l = 0
    r = len(lst) - 1
    # l,r coming to the middle from two sides 
    while l < r:
        # the sum is smaller than target, let l move rightwards
        if lst[l] + lst[r] < target:
            l += 1
        # the sum is bigger than target, let r move leftwards 
        elif lst[l] + lst[r] > target:
            r -= 1
        else:
        # if lst[l]+lst[r] == target, return l and r right away 
            return l, r




    # h = {}
    # for i, num in enumerate(lst):
    #     n = target - num
    #     if n not in h:
    #         h[num] = i
    #     else:
    #         return tuple([h[n], i])


    # using lst_to_dict to get a list, the range is from 0 to target
    # d = lst_to_dict(lst, 0, target)
    # # print(d)
    # for keys in d:
    #     if not isinstance(d[keys], int):
    #         continue
    #     if isinstance(d[target - keys], int):
    #         Min = min(d[keys], d[target-keys])
    #         Max = max(d[keys], d[target-keys])
    #         return Min, Max


# a = [17, 14, 10, 8, 5, 1, 5, 8, 10, 14, 17]
# l = DoublyLinkedList()
# for i in range(11):
#     l.add_to_front(a[i])
#     l.printf()
#
# # l.delete(4)
# l.printf()
# print("zzz")
# l.reverse()
# l.printf()
#
# print(l.compare(a))
#
# print(l.find(2))

# a = [20, 30, 64, 16, 8, 0, 99, 24, 75, 100, 69]
# a = merge_sort(a)
# print(a)

# b = [2, 1, 10, 0, 4, 3]
# print(lst_to_dict(b, 3, 10))
# print(type(None))

# lst = [1, 2, 3, 5, 9, 15]
# print(target_sum(lst, 7))
