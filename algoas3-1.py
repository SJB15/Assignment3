###1###
#helper "Node" class
class Node:
    def __init__(self,idata):
        self.data = idata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

###1###
#Linked list object
class Linked_List(object):

    def __init__(self):
        self.head = None
#adds item to begining of list
    def add(self,item,position):
        temp = Node(item,position)
        temp.setNext(self.head)
        self.head = temp
#removes item from list      
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
#searches for item in list and return boolean
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found            
#checks to see if list is empty, return boolean
    def isEmpty(self):
        return self.head == None
#returns the number of items in list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
#adds a new item to the end of the list
    def append(self,item):
        current = self.head
        if current:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))
        else:
            self.head = Node(item)
#returns position of item in the list
    def index(self,item):
        current = self.head
        while current != None:
            if current.data == item:
                return current.position
            else:
                current = current.next
        #error if item isnt in the list
        print ("item not present in list")        

#adds a new item to the list at a specific position
    def insert(self,item,position):
        if position == 0:
            self.add(item)
        elif position > self.size():
            print("position index out of range")
        elif position == self.size():
            self.AppendNode(item)
        else:
            temp = Node(item, position)
            current = self.head
            previous = None
            while current.position != position:
                previous = current
                current = current.next
            previous.next = temp
            temp.next = current
            temp.back = previous
            current.back = temp
            current = self.head
            self.index_correct(current)

#removes and returns last item in list
    def pop(self):
        if self.size == 0:
            print("list empty")
        else:
           return self.linkedlist.pop()
 #removes and returns the item at a position   
    def pop(self, position):
        if self.size < position:
            print("list too short")
        else:
            return self.linkedlist.pop(position)
    
        

mylist = Linked_List()

mylist.add(41,3)
mylist.add(67,5)
mylist.add(27,1)
mylist.add(83,6)
mylist.add(36,2)
mylist.add(64,4)

print(mylist.size())
print(mylist.search(67))
print(mylist.search(100))
print(mylist.search(83))

mylist.add(100,7)
print(mylist.search(100))
print(mylist.size())

mylist.remove(36)
print(mylist.size())
mylist.remove(64)
print(mylist.size())
mylist.remove(41)
print(mylist.size())
print(mylist.search(27))


#####4####
#stack cllass that creates a new empty stack
class Stack:
    def __init__(self):
        self.stacklist = []
#ckecks to see if stack is empty
    def isEmpty(self):
        if len(self.stacklist)==0:
            return True
        else:
            return False
#removes top item from stack
    def pop(self):
        item = self.stacklist[-1]
        del self.stacklist[-1]
        return item

#adds new item to top of stack
    def push(self, item):
        self.stacklist.append(item)

#returns top item of stack but doesn't remove it
    def peek(self):
        return self.stacklist[0]

#returns number of items on stack
    def size(self):
        count = 0

        for item in self.stacklist:
            count += 1

        return count

#####5###
class Queue():
    #creates a new empty queue
   def __init__(queue):
       self.queuelist = []

#adds new item to rear of queue
   def enqueue(self, item):
       self.queuelist.enqueue(item)

#removes the front item from queue
   def dequeue(self):
       self.queuelist.pop(0)
       return self.queuelist(0)

#tests to see whether queue is empty
   def isEmpty(self):
       if not self.stacklist:
          return True
       else:
          return False

#returns number of items in queue
   def size(self):
        return len(self.stacklist)

####6####
    #creates new deque that's empty
class Deque:
   def __init__(self):
        self.deque = []

#adds new item to front	
   def addFront(self, item):
        self.deque.append(item)

#adds new item to rear
   def addRear(self, item):
        self.deque.insert(0,item)

#removes item from front
   def removeFront(self):
       return self.deque.pop()

#removes item from rear
   def removeRear(self):
       return self.deque.pop(0)

#test to see whether it's empty	    
   def isEmpty(self):
        if not self.deque:
            return True
        else:
            return False
    
#returns number of items in deque
   def size(self):
       return len(self.deque)
    
