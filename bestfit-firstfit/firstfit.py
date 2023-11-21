from memory import makeMemory, displayMemory, Job

def firstfit(job, mem):
    for i in mem:
        if i.getSize() >= job.size and not i.busy:
            i.addJob(job)
            return
    print("No free partition of job size available")
    
if __name__ == "__main__":
    size, minsize = 0, 0
    # print("Input the size of the memory you want to work with:")
    # size = int(input())
    # print("Include the minimum size of each memory partition:")
    # minsize = int(input())
    mem = makeMemory()
    displayMemory(mem)
    start = 'yes'
    while start.lower().startswith('y'):
        print('For all your job sizes, write a list of comma separated values')
        size = input().split(',')
        # job = Job(size)
        # bestfit(job, mem)
        for i in size:
            job = Job(int(i))
            firstfit(job, mem)
        print()
        displayMemory(mem)
        start = "n"