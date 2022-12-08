'''

1. 배열
- 메모리의 연속 공간에 값이 채워져 있는 형태의 자료구조
- 배열의 값은 인덱스를 통해 참조할 수 있음, 선언한 자료형의 값만 저장할 수 있음

<특징>

- 인덱스를 사용하여 값에 바로 접근할 수 있음
- 새로운 값을 삽입하거나 특정 인덱스에 있는 값을 삭제하기 어려움
- 값을 삽입하거나 삭제하려면 해당 인덱스 주변에 있는 값을 이동시키는 과정이 필요함
- 배열의 크기는 선언할 때 지정할 수 있으며, 한 번 선언하면 크기를 늘리거나 줄일 수 있음
- 구조가 간단하므로 코딩 테스트에서 많이 이용함

2. 리스트 
- 값과 포인터를 묶은 노드라는 것을 포인터로 연결한 자료구조

<특징>
- 인덱스가 없으므로 값에 접근하려면 head 포인터부터 순서대로 접근해야 함 -> 값에 접근하는 속도가 느림
- 포인터로 연결되어 있으므로 데이터를 삽입하거나 삭제하는 연산 속도가 빠름
- 선언할 때 크기를 별도로 지정하지 않아도 됨. 다시 말해 리스트의 크기는 정해져 있지 않으며, 크기가 변하기 쉬운 데이터를 다룰 때 적합함
- 포인터를 저장할 공간이 필요하므로 배열보다 구조가 복잡함

3. 파이썬에서는 배열과 리스트를 구별하지 않음
- 컴퓨터 공학에서는 일반적으로 배열과 리스트를 구분
- 파이썬에서는 배열과 리스트의 특징까지 모두 가지도록 List를 구현


< Linked Lists >

- 값과 포인터를 묶은 노드라는 것을 포인터로 연결한 자료구조
• Data structure for storing a sequential collection.
• Unlike a standard Python list, it will allow us to insert at the beginning quickly.• 

• The idea is to store the items in individual objects called nodes.
• A special node is the head of the list.
• Each node stores a reference to the next node in the list.

< Types of linked lists >

• Linked lists can be of multiple types.
• Singly, doubly, and circular linked list.
• We will cover singly and doubly linked lists.


- Each node consists of (노드 = 값(item) + 포인터(reference of the next nodes))
• A data item
• An address (reference) of the next node

< Linked list operations > 

-  Traversal
• Access each element of the linked list

-  Insertion
• Add a new element to the linked list

-  Deletion
• Remove the existing elements

-  Search
• Find a node in the linked list

- Sort
• Sort the nodes of the linked list

< Why linked lists? >

- The power of a linked list comes from the ability to break the chain and rejoin it.
(E.g. if you wanted to put an element 4 between 1 and 2, the steps would be)
    • Create a new struct node and allocate memory to it.
    • Add its data value as 4
    • Point its next pointer to the struct node containing 2 as the data value
    • Change the next pointer of "1" to the node we just created.
- Doing something similar in an array would have required shifting the positions of all the subsequent elements.




'''




class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next


'''
< Operations at the Head and the Tail > 

- At the head and the tail, insertion and deletion should work differently.

< Insert Operations > : allocate memory & store data는 공통

- Insert at the beginning
    • Allocate memory for new node
    • Store data
    • Change next of new node to point to head
    • Change head to point to recently created node’

- Insert at the End
    • Allocate memory for new node
    • Store data
    • Traverse to last node
    • Change next of last node to recently created node

- Insert at the Middle
    • Allocate memory and store data for new node
    • Traverse to node just before the required position of new node • Change next pointers to include new node in between
    
< Delete Operations >
   
- Delete from beginning
    • Point head to the second node

- Delete from end
    • Traverse to second last element • Change its next pointer to null

- Delete from middle
    • Traverse to element before the element to be deleted
    • Change next pointers to exclude the node from the chain
    
    
'''