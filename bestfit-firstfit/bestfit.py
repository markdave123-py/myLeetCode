from memory import makeMemory, displayMemory, Job

def bestfit(job, mem):
    best = None
    for i in mem:
        if not best and i.getSize() > job.size:
            best = i if not i.busy else None
            
        if best and i.getSize() >= job.size and i.getSize() < best.getSize():
            best = i if not i.busy else best
    
    if best is None:
        print("No free partition of job size available")
        
    else:
        best.addJob(job)
        print("Job added successfully")

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
        print('For all you job sizes, write a list of comma separated values')
        size = input().split(',')
        # job = Job(size)
        # bestfit(job, mem)
        for i in size:
            job = Job(int(i))
            bestfit(job, mem)
        print()
        displayMemory(mem)
        start = "n"