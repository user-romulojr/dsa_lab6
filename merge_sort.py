class Node:
    def __init__(self, data):
        self.data= data
        self.next= None
        
class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        
    def insert_at_beginning(self, data): 
        new_node = Node(data)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.tail=new_node
            self.head=new_node
    
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head:
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=new_node
            self.tail=new_node
    
    def remove_beginning(self):
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            removed_node.next = None
            return removed_node.data
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node= current_node.next
        return False
    
    
    
def merge_sort(ll1, ll2):
    result = LinkedList()
        
    while ll1.head or ll2.head:
        if ll1.head and ll2.head:
            num1 = ll1.head.data
            num2 = ll2.head.data
            if num1 < num2:
                result.insert_at_end(ll1.remove_beginning())
            else:
                result.insert_at_end(ll2.remove_beginning())    
        elif list1.head:
            result.insert_at_end(ll1.remove_beginning())
        else:
            result.insert_at_end(ll2.remove_beginning())
        
    return result



list1 = LinkedList()
list2 = LinkedList()

list1.insert_at_end(1)
list1.insert_at_end(2)
list1.insert_at_end(4)

list2.insert_at_end(1)
list2.insert_at_end(3)
list2.insert_at_end(4)


answer = merge_sort(list1, list2)

it = answer.head
while it:
    print(it.data, end="")
    if(it.next):
        print(" -> ", end="")
    it = it.next
