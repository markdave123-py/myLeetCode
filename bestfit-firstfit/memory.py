from random import randint

class Partition:
    """
    Attributes:
        size -> int
        job -> Job
    methods:
        addJob -> sets job and changes leftover size
        release -> releases job and size
    """
    def __init__(self, size):
        self.size = size
        self.job = None
        self.busy = False
        
    def addJob(self, job):
        if job.size <= self.size and self.busy == False:
            self.job = job
            self.busy = True
        else:
            raise "Size too large"
            
    def release(self):
        self.job = None
        self.busy = False
        
    def getSize(self):
        return self.size
    
    def getJobSize(self):
        return self.job.size

class Job:
    def __init__(self, size):
        self.size = size
        
def makeMemory(size = 1000000, minsize = 10000):
    mem = []
    partition_size = 0
    while True:
        partition_size = randint(minsize, size)
        if size - partition_size < minsize:
            break
        mem.append(Partition(partition_size))
        size -= partition_size
    mem.append(Partition(size))
    return mem
    
def memorySize(mem):
    size = 0
    for i in mem:
        size += i.getSize()
    return size

def displayMemory(mem):
    counter = 0
    for i in mem:
        print(f'Partition {counter} -> {i.getSize()/1000}k\n')
        print(f'Job {counter}       -> {i.getJobSize()/1000 if i.job is not None else 0}k\n')
        print("-------------------------------------")
        counter += 1
            
    

# if __name__ == "__main__":
#     size, minsize = 0, 0
#     # print("Input the size of the memory you want to work with:")
#     # size = int(input())
#     # print("Include the minimum size of each memory partition:")
#     # minsize = int(input())
#     mem = makeMemory()
#     displayMemory(mem)
#     start = 'yes'
#     while start.lower().startswith('y'):
#         print('To add a job, input the job size:')
#         size = int(input())
#         job = Job(size)
#         bestfit(job, mem)
#         displayMemory(mem)
#         print("Do you want to add another job? Y | N:")
#         start = input().lower()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        