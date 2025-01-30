from queue import Queue
from random import randint
from statistics import mean


class Task:

    def __init__(self, pages, timestamp):
        '''Initialize with the size of task in pages and the moment it was created'''
        self.pages = pages
        self.timestamp = timestamp
    
    def get_waiting_time(self, base_time):
        '''Get the time the task waited in the queue'''
        return base_time - self.timestamp


class Printer:

    def __init__(self, print_rate):
        self.rate = print_rate
        self.queue = Queue()
        self.current_task = None
        self.i = 1

    def assign_task(self):
        '''Get a task'''
        self.current_task = self.queue.dequeue()

    def is_busy(self):
        '''Check if the printer took a task'''
        return self.current_task != None
    
    def _print(self):
        '''As pages can go below 0, this means that the printer is a little underutilized and the end result is an approximation'''
        self.current_task.pages -= self.rate / 60 
        if self.current_task.pages <= 0:
            self.current_task = None
            self.i += 1



def printer_simulation(print_rate, num_students, min_pages_task, max_pages_task, duration):
        
    # turn on the printer
    printer = Printer(print_rate=print_rate)
    # how much did each task wait in the queue before printer got to it
    waiting_times = []

    # during each second, the process goes on
    for current_second in range(1, duration+1):
        # during each second theres a 1 / n probability of a printing task being created
        # 10 students - 1 task per 180 seconds on average
        n = 1800 // num_students
        # could be any other number in the range
        if randint(1, n) == n:
            # push a new stack into queue
            new_task = Task(pages=randint(min_pages_task, max_pages_task), timestamp=current_second)
            printer.queue.enqueue(new_task)

        # work on a task if there's one
        if printer.is_busy():
            printer._print()

        # if there's no task or it just finished one, take another one from queue
        elif not printer.is_busy() and not printer.queue.is_empty():
            printer.assign_task()
            wait_time = printer.current_task.get_waiting_time(current_second)
            waiting_times.append(wait_time)


    if len(waiting_times) > 0:
        print(f'{printer.i} tasks completed for {num_students} students in {duration} seconds')
        print(f'Average waiting time for a task: {round(mean(waiting_times), 2)} seconds')
        print(f'Unfinished tasks remaining: {printer.queue.size()}')
        print()
    else:
        print(f"{num_students} students didn't send a single task to the printer in {duration} seconds")
        print()



for _ in range(10):
    printer_simulation(print_rate=10, num_students=10, min_pages_task=1, max_pages_task=20, duration=3600)