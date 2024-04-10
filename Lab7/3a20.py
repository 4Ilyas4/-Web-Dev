def make_bricks(small, big, goal):
    max_big_bricks_length = big * 5
    remaining_length = goal - min(goal // 5, big) * 5
    return remaining_length <= small