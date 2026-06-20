# EXP73.py - Job Assignment to Minimize Max Worker Time

def minimize_max_working_time(jobs, k):
    """Minimize maximum working time across k workers"""
    jobs.sort(reverse=True)
    workers = [0] * k
    
    def backtrack(job_idx):
        if job_idx == len(jobs):
            return max(workers)
        
        min_max_time = float('inf')
        for i in range(k):
            workers[i] += jobs[job_idx]
            min_max_time = min(min_max_time, backtrack(job_idx + 1))
            workers[i] -= jobs[job_idx]
            
            if workers[i] == 0:
                break
        
        return min_max_time
    
    return backtrack(0)

print("=" * 60)
print("Job Assignment to Minimize Max Worker Time")
print()

print("Test Case 1:")
jobs1 = [3, 2, 3]
k1 = 3
result1 = minimize_max_working_time(jobs1, k1)
print(f"Input: jobs = {jobs1}, k = {k1}")
print(f"Output: {result1}")
print("Explanation: Each person gets one job, max time = 3")
print()

print("Test Case 2:")
jobs2 = [1, 2, 4, 7, 8]
k2 = 2
result2 = minimize_max_working_time(jobs2, k2)
print(f"Input: jobs = {jobs2}, k = {k2}")
print(f"Output: {result2}")
print("Explanation: Worker1: [1,2,8]=11, Worker2: [4,7]=11")
print("=" * 60)
