# EXP74.py - Job Scheduling with Non-overlapping Times (DP)

import bisect

def job_scheduling(start_time, end_time, profit):
    """Maximum profit from non-overlapping jobs"""
    jobs = list(zip(end_time, start_time, profit))
    jobs.sort()
    
    n = len(jobs)
    dp = [0] * (n + 1)
    
    for i in range(n):
        end, start, prof = jobs[i]
        
        j = bisect.bisect_right(jobs, (start,)) - 1
        
        new_profit = jobs[i][2] + (dp[j + 1] if j >= 0 else 0)
        dp[i + 1] = max(dp[i], new_profit)
    
    return dp[n]

print("=" * 70)
print("Job Scheduling with Non-overlapping Times")
print()

print("Test Case 1:")
start1 = [1, 2, 3, 3]
end1 = [3, 4, 5, 6]
profit1 = [50, 10, 40, 70]
result1 = job_scheduling(start1, end1, profit1)
print(f"startTime = {start1}")
print(f"endTime = {end1}")
print(f"profit = {profit1}")
print(f"Output: {result1}")
print("Explanation: Choose jobs 0 and 3 -> profit = 50 + 70 = 120")
print()

print("Test Case 2:")
start2 = [1, 2, 3, 4, 6]
end2 = [3, 5, 10, 6, 9]
profit2 = [20, 20, 100, 70, 60]
result2 = job_scheduling(start2, end2, profit2)
print(f"startTime = {start2}")
print(f"endTime = {end2}")
print(f"profit = {profit2}")
print(f"Output: {result2}")
print("Explanation: Choose jobs 0,3,4 -> profit = 20+70+60 = 150")
print("=" * 70)
