import random
from queue import Queue

def simulate_hot_potato(names, num):
    queue = Queue()
    # get eveyone into game
    for p in names:
        queue.enqueue(p)
    # dequeue and enqueue people until only 1 person is left (the person who throws a potato (the one at front of queue) goes to the rear)
    while queue.size() > 1:
        for j in range(num):
            p = queue.dequeue()
            queue.enqueue(p)
        queue.dequeue()
    
    return queue.dequeue() 


print(simulate_hot_potato(['Areg', 'Sargis', 'Rafayel'], num=random.randint(3, 21)))
        