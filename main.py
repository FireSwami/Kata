def direction(facing, turn):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    for i in directions:
        if i == facing:
            start_index = directions.index(facing)
            if (type(turn) == int) and (-1080 <= turn <= 1080) and (turn % 45 == 0):
                end_index = (start_index + turn // 45) % 8
                return directions[end_index]
            else:
                return "Задайте верный угол поворота (от -1080 до 1080 с шагом 45)"
        else:
            return 'Задайте верную точку отсчета компаса ("N", "NE", "E", "SE", "S", "SW", "W", "NW")'



print(direction('N', 90))

