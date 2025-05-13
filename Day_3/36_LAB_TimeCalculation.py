start_hour = int(input())
start_minute = int(input())
duration = int(input())

total_minutes = start_hour * 60 + start_minute + duration
end_hour = (total_minutes // 60) % 24
end_minute = total_minutes % 60

print(f"{end_hour}:{end_minute}")