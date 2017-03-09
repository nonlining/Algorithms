# python2
from Queue import PriorityQueue

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, raw_input().split(' '))
        self.jobs = [int(s) for s in raw_input().split(' ')]
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print self.assigned_workers[i], self.start_times[i]

    def assign_jobs(self):

        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def sift_down(self, nextFree, index):
        leftNodeIndex = 2 * index + 1
        rightNodeIndex = 2 * index + 2

        minIndex = index

        if leftNodeIndex < len(nextFree) and ((nextFree[leftNodeIndex][0] < nextFree[minIndex][0]) or
        (nextFree[leftNodeIndex][0] == nextFree[minIndex][0] and nextFree[leftNodeIndex][1] < nextFree[minIndex][1])):
            minIndex = leftNodeIndex

        if rightNodeIndex < len(nextFree) and ((nextFree[rightNodeIndex][0] < nextFree[minIndex][0]) or
        (nextFree[rightNodeIndex][0] == nextFree[minIndex][0] and nextFree[rightNodeIndex][1] < nextFree[minIndex][1])):
            minIndex = rightNodeIndex

        if index != minIndex:
            nextFree[index], nextFree[minIndex] = nextFree[minIndex], nextFree[index]
            self.sift_down(nextFree, minIndex)

    def assign_jobs_fast(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)

        next_free_time = [(0, i) for i in range(self.num_workers)]

        for i in range(len(self.jobs)):
          self.assigned_workers[i] = next_free_time[0][1]
          self.start_times[i] = next_free_time[0][0]

          next_free_time[0] = (next_free_time[0][0] + self.jobs[i], next_free_time[0][1])
          self.sift_down(next_free_time, 0)

    def solve(self):
        self.read_data()
        self.assign_jobs_fast()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

