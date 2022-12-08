'''

• Recursion

• Recursion is writing functions that call themselves.
• When you write a recursive function, you write (at least) two pieces:
    • What to do if the input is the smallest possible datum,
    • What to do if the input is larger so that you: 
        ▪ (a) process one piece of the data
        ▪ (b) call the function to deal with the rest.



• 3 ways to understand recursion
    
    - Procedural abstraction
    - Trace it out (use a small problem like downUp to do this) 
    - Little people method

• Procedural Abstraction 1
    - Break the problem down into the smallest pieces that you can write down easily as a function.
    - Re-use as much as possible.


'''

def recursive_func(word) : 
    
    if len(word) ==1 : 
        print(word)
        return
    
    print(word)
    recursive_func(word[1:])
    print(word)
    

'''

< 트리 >

- 트리의 특징 : 
• 순환 구조(cycle)를 지니고 있지 않고, 1개의 루트 노드가 존재
• 루트 노드를 제외한 노드는 단 1개의 부모 노드를 가짐
• 트리의 부분 트리(subtree) 역시 트리의 모든 특징을 따름

- 구성요소 : 설명
• 노드 : 데이터의 index와 value를 표현하는 요소
• 에지 : 노드와 노드의 연결관계를 나타내는 선
• 루트 노드 : 트리에서 가장 상위에 존재하는 노드
• 부모 노드 : 두 노드 사이의 관계에서 상위 노드에 해당하는 노드
• 자식 노드 : 두 노드 사이의 관계에서 하위 노드에 해당하는 노드
• 리프 노드 : 자식 노드가 없는 노드 (가장 하위의 노드가 아님!)
• 서브 트리 : 전체 트리에 속한 작은 트리

- Trees

    • A Tree is a data type that is ideal for representing hierarchical structure.
 
- Tree components

    •Trees are composed of nodes and nodes have 0 or more children or child nodes.
    •A node is called the parent of its children.

- Root Node : 트리에서 가장 상위에 존재하는 노드

    • Each node has (at most) one parent.
    • We are concerned primarily with rooted trees.
        • There is a single special node called the root of the tree.
    
- Leaf Node : 자식 노드가 없는 노드

    • The nodes that do not have any children are called leaves or leaf nodes.

- Edges : connections between two nodes

- Path : 노드의 순서, 길이 = path에 있는 edge의 개수

    • A path in a tree is a sequence of nodes in which each node is a child of the previous node.
    • Length of the path: the number of edges which is one less than the number of nodes in the path.

- Descendants of a node x
    • All nodes y for which there is a path from x to y.
    • If y is a descendant of x, then we say x is an ancestor of y.
    
- Subtree

    • Given a tree T and a node n in that tree, the subtree rooted at n is
    the tree whose root is n that contains all descendants of n.
    
- Depth of a node = path의 길이
    • Length of the path to the node from the root.
    
- Height of a tree = max(path)
    • Maximum depth of any node in the tree. 

'''


'''
# Tree : Abstract Data Type (ADT)


- __init__(L)
• Initialize a new tree given a list of lists. The convention is that the first element in the list is the data and the later elements (if they exist) are the children.


- height()
• Return the height of the tree.


- __str__()
• Return a string representing the entire tree.


__eq__(other)
• Return True if the tree is equal to other. This means that they have the
same data and their children are equal (and in the same order).


- __contains__(k)
• Return True if and only if the tree contains the data k either at the root or
at one of its descendants. Return False otherwise.


- Preorder()
• Return an iterator over the data in the tree that yields values according to
the preorder traversal of the tree.


- Postorder()
• Return an iterator over the data in the tree that yields values according to the postorder traversal of the tree.


- __iter__()
• An alias for preorder.


- layerorder()
• Return an iterator over the data in the tree that yields values according to the layer order traversal of the tree.
 


'''

class Tree:
    def __init__(self,L) : 
        # iter()
        # next()
        iterator = iter(L)
        self.data = next(iterator)
        self.children = [Tree(c) for c in iterator ]
        
    # def printTree(T) : 
    #     iterator = iter(T)
    #     print(next(iterator))
    #     for child in iterator : 
    #         printTree(child)    
    
    
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) # class 내부의 iterator를 우선으로 해서 돌아감
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter))    



class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
      if self.a <= 20:
        x = self.a
        self.a += 1
        return x
      else:
        raise StopIteration # 강제로 띄우다
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter: # for문에서 next를 계속 돌리고 있음
  print(x)