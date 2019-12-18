robot_map = [[1, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1]]
initial_place = robot_map[0][0]
destination = robot_map[2][6]
for m in range(3):
    robot_map[m][0] = 1
for n in range(6):
    robot_map[0][n] = 1
for i in range(1, 3):
    for j in range(1, 7):
        if robot_map[i][j] == 1:
            robot_map[i][j] = robot_map[i - 1][j] + robot_map[i][j -1]

print(robot_map[2][6])