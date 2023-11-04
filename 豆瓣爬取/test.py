class JobControlBlock:
    def __init__(self, job_id, size):
        self.job_id = job_id
        self.size = size
        self.start_address = None

class MemoryManager:
    def __init__(self, total_size):
        self.total_size = total_size
        self.free_blocks = [(0, total_size)]  # 初始时有一个完整的空闲块
        self.allocated_blocks = []

    def first_fit_allocation(self, job):
        for i, (start, size) in enumerate(self.free_blocks):
            if size >= job.size:
                job.start_address = start
                self.allocated_blocks.append(job)
                if size == job.size:
                    del self.free_blocks[i]
                else:
                    self.free_blocks[i] = (start + job.size, size - job.size)
                return True
        return False

    def release_memory(self, job_id):
        for i, job in enumerate(self.allocated_blocks):
            if job.job_id == job_id:
                self.free_blocks.append((job.start_address, job.size))
                del self.allocated_blocks[i]
                break

    def compact(self):
        self.free_blocks.sort(key=lambda x: x[0])
        new_free_blocks = [(0, self.total_size)]
        for start, size in self.free_blocks:
            if start != new_free_blocks[-1][0] + new_free_blocks[-1][1]:
                new_free_blocks.append((start, size))
            else:
                new_free_blocks[-1] = (new_free_blocks[-1][0], new_free_blocks[-1][1] + size)
        self.free_blocks = new_free_blocks

    def draw_memory_status(self):
        memory_map = ['.' * self.total_size]
        for job in self.allocated_blocks:
            memory_map.append('X' * job.size)
        for start, size in self.free_blocks:
            memory_map.append('.' * size)
        memory_map_str = ' '.join(memory_map)
        print(memory_map_str)

class JobScheduler:
    def __init__(self):
        self.job_queue = []
        self.memory_manager = MemoryManager(1024)
        self.running_jobs = []

    def create_job_queue(self, job_count):
        for i in range(job_count):
            job = JobControlBlock(i+1, 32)  # 假设每个作业的大小为32
            self.job_queue.append(job)

    def run_job_scheduler(self):
        while self.job_queue or self.running_jobs:
            while self.running_jobs and len(self.running_jobs) >= 5:
                self.time_slice_round_robin()
            if self.job_queue:
                job = self.job_queue.pop(0)
                if self.memory_manager.first_fit_allocation(job):
                    self.running_jobs.append(job)
            self.time_slice_round_robin()

    def time_slice_round_robin(self):
        if not self.running_jobs:
            return
        job = self.running_jobs.pop(0)
        # 运行一次时间片
        print(f"Running job {job.job_id}...")
        # 模拟作业完成
        self.memory_manager.release_memory(job.job_id)
        print(f"Job {job.job_id} completed.")
        self.memory_manager.draw_memory_status()

job_scheduler = JobScheduler()
job_scheduler.create_job_queue(20)
job_scheduler.run_job_scheduler()

