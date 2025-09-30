pitch_line = input()
start_pos = int(input())
step_size = int(input())

message = ""
current_pos = start_pos

for _ in range(len(pitch_line)):
    message += pitch_line[current_pos]
    current_pos = (current_pos + step_size) % len(pitch_line)

print(message)
