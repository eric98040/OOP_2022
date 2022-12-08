# Linked list operations in Python


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList : 
    def __init__(self) : 
        self.head = None
    
    def insert_front(self,value) :
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def insert_last(self,value) : 
        new_node = Node(value)

        if not self.head : 
            self.head = new_node
            return
        
        last_node = self.head
        
        while last_node.next : 
            last_node = last_node.next
        last_node.next = new_node
        
    def insert_after(self,prev_node,value) :
        new_node = Node(value)
        if not prev_node : 
            print("The given previous node must be in the LinkedList")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def deleteNode(self, value) : 
        if not self.head : 
            return
        
        temp = self.head
        
        while temp.data != value : 
            if not temp.next:
                print("The given value is not in the LinkedList")
                return
            temp = temp.next
            
        next= temp.next.next
        temp.next = None
        temp.next = next
        
    def search(self,key) : 
        temp = self.head
        
        while temp.data != key : 
            
            if not temp.next : 
                return False
            
            temp = temp.next
        return True

    # selection sort와 같이 구현
    def sortLinkedList(self,head) :
        
        current = head
        idx = Node(None)
            
        if not head : 
            return
        else : 
            while current : 
                
                idx = current.next
                
                while not idx : 
                    if current.data > idx.data : 
                        current.data, idx.data = idx.data, current.data
                    idx = idx.next
                    
                current = current.next
                
    
                    
            
    def printList(self) :
        temp = self.head

        while temp : 
            print(temp.data, end= ' ')
            temp = temp.next
            



if __name__ == '__main__':

    llist = LinkedList()
    llist.insert_last(1)
    llist.insert_front(2)
    llist.insert_front(3)
    llist.insert_last(4)
    llist.insert_after(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()
    