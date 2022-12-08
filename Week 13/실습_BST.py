'''
< Binary search Tree > 

- 이진 탐색 트리 


• 이진탐색트리란 이진탐색(binary search)과 연결리스트(linked list)를 결합한 자료구조의 일종입니다. 
• 이진탐색의 효율적인 탐색 능력을 유지하면서도, 빈번한 자료 입력과 삭제를 가능하게끔 고안됐습니다.

• 예컨대 이진탐색의 경우 탐색에 소요되는 계산복잡성은 𝑂(log𝑛)으로 빠르지만 자료 입력, 삭제가 불가능합니다. 
• 연결리스트의 경우 자료 입력, 삭제에 필요한 계산복잡성은 𝑂(1)로 효율적이지만 탐색하는 데에는 𝑂(𝑛)의 계산복잡성이 발생합니다.
• 두 마리 토끼를 잡아보자는 것이 이진탐색트리의 목적입니다.

• 각 노드의 왼쪽 서브트리에는 해당 노드의 값보다 작은 값을 지닌 노드들로 이루어져 있다.
• 각 노드의 오른쪽 서브트리에는 해당 노드의 값보다 큰 값을 지닌 노드들로 이루어져 있다.
• 중복된 노드가 없어야 한다.
• 왼쪽 서브트리, 오른쪽 서브트리 또한 이진탐색트리이다.

• 이진탐색트리의 핵심 연산은 검색(retreive), 삽입(insert), 삭제(delete) 세 가지입니다. 
• 이밖에 이진탐색트리 생성(create), 이진탐색트리 삭제(destroy), 해당 이진탐색트리가 비어 있는지 확인(isEmpty), 트리순회(tree traverse) 등의 연산이 있습니다. 파이썬 코드는 다음과 같습니다


⚫Inorder traversal : 중위 순회

• It visits all the nodes in the left child prior to visiting the root
• And then visits all the nodes in the right child after visiting the root.
• This order results in a traversal of the nodes in sorted order according to the ordering of the keys.
• As a result, different BSTs with the same nodes, will have the same inorder traversal.

'''

# Binary Search Tree operations in Python

class Node : 
    def __init__(self,data) : 
        self.data = data
        self.right = None
        self.left = None

def inorder(root) : # 중위 순회
    if root : 
        inorder(root.left)
        print(root.data, end = ' ')
        inorder(root.right)
        
def preorder(root) : # 선위 순회
    if root : 
        print(root.data, end = ' ')
        preorder(root.left)
        preorder(root.right)
        
def postorder(root) : # 후위 순회
    if root :
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = ' ')
        
def insert(node, data) : # node는 원래 있던 기준 값 / data는 삽입할 값
    
    if not node :  # node.right / node.left == None일 때 (자식 노드가 없을 때)
        return Node(data)
    
    if node.data < data : 
        node.right = insert(node.right, data)
    else : 
        node.left = insert(node.left, data)
    return node # 재귀가 끝나고 삽입 위치 위에 있는 node들을 고정(값 fix)


root = Node(5)
root = insert(root,1) # return Node(1)
root = insert(root,3)  # root.right에 return Node(2) & root 반환
root = insert(root,8)
root = insert(root,4)
root = insert(root,2)
root = insert(root,7)

inorder(root)
print()
 
def minValueNode(node) : 
    # 해당 input인 node에서부터 아래로 내려감
    temp = node
    while temp.left : 
        temp = temp.left
    return temp

print("Minimum value node is : ")
print(minValueNode(root).data)

def maxValueNode(node) : 
    # 해당 input인 node에서부터 아래로 내려감
    temp = node
    while temp.right : 
        temp = temp.right
    return temp

print("Maximum value node is : ")
print(maxValueNode(root).data)

def deleteNode(root, data) : 
    
    if not root : 
        return root
    
    if root.data > data :
        root.left = deleteNode(root.left,data)
        
    elif root.data < data :
        root.right = deleteNode(root.right,data)
        
    else : 
        # 자식 노드가 하나만 있거나 아예 없을 경우
        if not root.left :
            temp = root.right
            root = None
            return temp
        elif not root.right : 
            temp = root.left
            root = None
            return temp
    
        # 자식 노드가 두 개 다 있을 경우 : delete는 삭제할 노드와 오른쪽 서브 트리에서 가장 작은 노드의 값을 바꾸면 된다 & 오른쪽 서브 트리를 삭제
        # 이 노드는 왼쪽 서브 트리에 있는 모든 값보다 크고 오른쪽 서브 트리에 있는 값 중 가장 작기 때문이다.
        temp = minValueNode(root.right)
        
        root.data = temp.data
        
        root.right = deleteNode(root.right,temp.data)
        
    return root

'''
------------ My solution end --------------

'''
        
 
 


# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(str(root.key) + "->", end=' ')

        # Traverse right
        inorder(root.right)


# Insert a node
def insert(node, key):

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)

    # Traverse to the right place and insert the node
    # key는 내가 넣고 싶은 값 / node는 원래 있던 기준 값
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node




# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # If the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = deleteNode(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
print("Done!")