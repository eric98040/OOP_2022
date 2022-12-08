'''
< Iterator >

* Iterable = 반복가능한 

* 반복 가능한 데이터, 객체에 적용되는 의미

* Iterable object = list, tuple, dictionary, set, range()함수 객체, file, class로 정의된 객체

• Iterable object -> for element in Iterable object 으로 처리 가능



* Iterator = 객체의 한 종류 (객체의 element, member를 순서대로 엑세스 할 수 있는 객체)

• "iterable한 객체"가 iter()함수를 통하여 "iterator 객체"

• 순서대로 자료를 가져온 이후에는 그 데이터는 폐기해버림, 메모리 사용에 제약이 따르는 대규모 데이터처리에 매우 효과적임
- 즉, next() 후에는 반환된 데이터는 원래 iterator에서 사라진다 (popleft()와 비슷한 느낌)

* iterator 객체 생성 = iterable한 객체의 "__iter__()" method 사용 or iter()함수 사용
* iterator 객체에서 순서대로 element 가져오기 : 순서대로 next()함수 or "__next__()" method 사용



• 반복을 이용해 어떤 처리를 수행하는 객체를 이터레이터(Iterator)라고 합니다.

• 여기서 파이썬에서 반복을 사용하는 모든 툴을 Iteration Tool/Context라 합니다.

• 대표적으로 for, comprehesion, map 등이 있습니다.

- 툴만 가지고는 구현이 어렵겠죠? 

• 실제 이터레이션을 수행할 공간의 객체를 뜻하는 Iterable Object(file, list, tuple, dict, set, range()) 와 수행처리 객체인 Iterator Object(__next__)가 있습니다. 

• Iterable Object는 모든 객체가 다 되는것이 아니고 반복이 가능한 것만 사용할 수 있습니다.  그림과 같은 형태로 수행을 하게 됩니다.



< Iterator 사용법 > 

- Iterable Object ( __iter__, file, list, tuple) --객체 선택--> Iteration Tool/Context (for, comprehension, map,..) --반복 수행--> Iterator Object(__next__)

• for 문을 예로 들면, for 안에 __next__ 인자가 있어서 Iterable Object인 list 안에서 자동적으로 반복을 수행하게 됩니다.



< iter, next >

- 이 과정을 수동으로 할 수 있습니다. 

• 어쩌다가 수동으로 조절을 해야할 경우가 생기긴 하지만 거의 쓰진 않습니다.

• for 문이 어떻게 움직이는지 느낌은 알 수 있을겁니다.

• 파이썬의 내장 함수인 iter와 next를 이용합니다.

• iter 는 __iter__ 를 호출하고 next 는 __next__를 호출합니다. 

• iter를 이용해 이터레이터를 만들고 next로 반복을 수행하도록 요청을 합니다.

•더 이상 가져올 게 없으면 StopIteration이 발생됩니다. 

• StopIteration 오류를 없앤다면 자동화가 가능하겠네요.

< Generator > 

• 제너레이터는 이터레이터를 생성해주는 함수입니다. 
• 이터레이터는 클래스에 __iter__, __next__ 또는 __getitem__ 메서드를 구현해야 하지만 제너레이터는 함수 안에서 yield라는 키워드만 사용하면 끝입니다. 
• 그래서 제너레이터는 이터레이터보다 훨씬 간단하게 작성할 수 있습니다.

• 함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)을 지정합니다.

< Genertaor 특성 > 

. 단, 이터레이터는 __next__ 메서드 안에서 직접 return으로 값을 반환했지만 제너레이터는 yield에 지정한 값이 __next__ 메서드(next 함수)의 반환값으로 나옵니다. 
. 또한, 이터레이터는 raise로 StopIteration 예외를 직접 발생시켰지만 제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생합니다.


• 전위 순회, 중위 순회, 후위 순회

    - 트리를 읽을 때에 대전제는 왼쪽부터 오른쪽으로 읽는다는 것이다. 
    - "방문"은 자신의 번호를 출력하는 print() 함수로 표현한다. 
    - 이 출력 함수의 위치에 따라서 트리를 순회하는 방법을 구분하는 것이다.
    - 중요 point : 순서가 헷갈리면 가장 작은 subtree 부터 순서를 결정하고 -> 그걸 또 하나의 tree로 본 후에 계속해서 덩어리를 키운다.

  # pre_order(DFS, 자기 자신을 먼저 출력) : 전위 순회 = 현재 -> 왼쪽 -> 오른쪽  
  # in_order(DFS, 자기 자신 출력이 중앙에 있음) : 중위 순회 = 왼쪽 -> 현재 -> 오른쪽
  # post_order(DFS, 자기 자신 출력을 가장 나중에 함): 후위 순회 = 왼쪽 -> 오른쪽 -> 현재
  # layer_order(BFS, 각 레벨마다의 노드를 탐색) : 레벨 순회 = 같은 depth에 있는 트리부터 왼쪽 -> 오른쪽 & 큐로 구현



'''




from ds2.queue import ListQueue as Queue

class Tree:
    def __init__(self, L):
        iterator = iter(L) # iter() : iterator로 만들어주는 기능 & 같은 level안에서 순환
        self.data = next(iterator)  # next() : 다중 list가 있을 때 '다음' 원소로 들어감
        # next는 루프를 돌다가/ 안 돌다가 할 때 유용함 
        self.children = [Tree(c) for c in iterator]

    def _listwithlevels(self, level, trees):
        trees.append("  " * level + str(self.data))
        for child in self.children:
            child._listwithlevels(level + 1, trees)

    def __str__(self):
        trees = []
        self._listwithlevels(0, trees)
        return "\n".join(trees)

    def __eq__(self, other):
        return self.data == other.data and self.children == other.children

    def height(self):
        if len(self.children) == 0:
            return 0
        else:
            return 1 + max(child.height() for child in self.children)
    
    # def height(self) : 
    #     if not self.children : 
    #         return 0
    #     else :
    #         return 1+ max( c.height() for c in self.children)

    def __contains__(self, k):
        return self.data == k or any(k in ch for ch in self.children)     

# 전위 순회(DFS) : parent -> left -> right

    def preorder(self):
        yield self.data # make generator
        for child in self.children:
            for data in child.preorder():
                yield data    
                
    def __init__(self, L):
        iterator = iter(L) # iter() : iterator로 만들어주는 기능 & 같은 level안에서 순환
        self.data = next(iterator)  # next() : 다중 list가 있을 때 '다음' 원소로 들어감
        # next는 루프를 돌다가/ 안 돌다가 할 때 유용함 
        self.children = [Tree(c) for c in iterator]

    # 후위 순회(DFS) :  left -> right -> parent
    
    def _postorder(self):
        node, childiter = self, iter(self.children)
        stack = [(node, childiter)]
        while stack:
            node, childiter = stack[-1]
            try:
                child = next(childiter)
                stack.append((child, iter(child.children)))
            except StopIteration:
                yield node
                stack.pop()  
            

    def postorder(self):
        return (node.data for node in self._postorder())

    def _layerorder(self):
        node, childiter = self, iter(self.children)
        queue = Queue()
        queue.enqueue((node, childiter))
        while queue:
            node, childiter = queue.peek()
            try:
                child = next(childiter)
                queue.enqueue((child, iter(child.children)))
            except StopIteration:
                yield node
                queue.dequeue()                 

    def layerorder(self):
        return (node.data for node in self._layerorder())
        
    # Set __iter__ to be an alias for preorder.
    __iter__ = preorder # pre, post, lay 중에서 원한는 순회를 여기에 입력

# < iter() 함수 사용 > 
# • 순서대로 자료를 가져온 이후에는 그 데이터는 폐기해버림, 메모리 사용에 제약이 따르는 대규모 데이터처리에 매우 효과적임
# - 즉, next() 후에는 반환된 데이터는 원래 iterator에서 사라진다 (popleft()와 비슷한 느낌)

def printtree(T):
	iterator = iter(T) 
	print(next(iterator)) # root node 반환 및 iterator에서 제거
	for child in iterator:
		printtree(child)
  
# def printtree(T):
#     print(T.data)
#     for child in T.children:
#            printtree(child)
#For test

T = Tree(['c', ['a', ['p'], ['n'], ['t']], ['o', ['n']]])
NewT = Tree(['c', ['a', ['p'], ['n'], ['t']], ['o', ['k']]])

print(T.data)
print(T.children[0])
print(T.children[1])
print(T.children[0].data)
print(T.children[0].children[0])
print(T.children[0].children[1])
print(T.children[0].children[2])
print(T.children[1].data)
print(T.children[1].children[0])

# _listwithlevels 함수와 __str__함수는 같이 사용됨 
print(T.__str__())

# self.data가 같고 & (and) self.children이 같으면 Tree는 같다!
print(T.__eq__(NewT))

# height는 0이 아닐 경우에 1+max(...) 꼴로 작성한다!
print(T.height())

# contains는 self.data가 k이거나, self.children에 하나라도 k가 있으면 통과
print(T.__contains__('c'))
