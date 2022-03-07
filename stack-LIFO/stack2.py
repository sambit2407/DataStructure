import collections,queue


# stack_deque=collections.deque()
# stack_deque.append(5)
# stack_deque.append(10)
# stack_deque.append(90)
#
# print(stack_deque)
# stack_deque.pop()
# print(stack_deque)

stack_queue=queue.LifoQueue()
stack_queue.put(12,13)
print( stack_queue.get())



