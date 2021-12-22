#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 4
def compute():
	ans = sum(1 for i in range(10000) if is_lychrel(i))
	return str(ans)


def is_lychrel(n):
	for i in range(50):
		n += int(str(n)[ : : -1])
		if str(n) == str(n)[ : : -1]:
			return False
	return True


if __name__ == "__main__":
	print(compute())


# In[2]:


#Question 1
def compute():
    isprime = list_primality(999999)

    def is_circular_prime(n):
        s = str(n)
        return all(isprime[int(s[i:] + s[: i])] for i in range(len(s)))

    ans = sum(1
              for i in range(len(isprime))
              if is_circular_prime(i))
    return str(ans)


def list_primality(n):
	
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y


if __name__ == "__main__":
    print(compute())


# In[3]:


#Question 2
    import sympy
sum=0
lst1=[]

for num in range(1,1000):
    
    if sympy.isprime(num) is True:
        sum+=num
        lst1.append(sum)

print("The sum list 1 is: ",lst1)

lst2=[]
for sum in lst1:
    if sum<1000:
        if sympy.isprime(sum)==True:
            lst2.append(sum)
print("The list 2 is: ",lst2)
print("The required answer is :",max(lst2))


# In[7]:


# Question 5
# Circular Queue implementation 


class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()



obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()


# In[8]:


# Question 6
from queue import Queue
 
class Stack:
     
    def __init__(self):
         
       
        self.q1 = Queue()
        self.q2 = Queue()
             
        # To maintain current number
        # of elements
        self.curr_size = 0
 
    def push(self, x):
        self.curr_size += 1
 
        # Push x first in empty q2
        self.q2.put(x)
 
        # Push all the remaining
        # elements in q1 to q2.
        while (not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()
 
        # swap the names of two queues
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q
 
    def pop(self):
 
        # if no elements are there in q1
        if (self.q1.empty()):
            return
        self.q1.get()
        self.curr_size -= 1
 
    def top(self):
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]
 
    def size(self):
        return self.curr_size
 
# compile tym Code
if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
 
    print("current size: ", s.size())
    print(s.top())
    s.pop()
    print(s.top())
    s.pop()
    print(s.top())
 
    print("current size: ", s.size())
 


# In[ ]:




