# Construct a Queue class in python

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_Empty(self):
        return self.items == []


# Write a Task Manager with a Queue

def task_manager_function():

    task_manager = Queue()

    while True:
        if task_manager.is_Empty():
            next_task = None
        else:
            next_task = task_manager.peek()

        print "Next task:", next_task

        command = raw_input("A)dd task, D)o first task, or Q)uit? ")

        if command == "A":
            task = raw_input("Enter a task: ")
            task_manager.enqueue(task)

        if command == "D":
            print "Completed task: ", task_manager.dequeue()

        if command == "Q":
            break

        else:
            print "That is not a valid command. Try again"



task_manager_function()
