def correct_distortion(frame):
    import copy
    
    def get_neighbors(x, y, rows, cols):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors.append((nx, ny))
        return neighbors
    
    rows = len(frame)
    cols = len(frame[0])
    corrected_frame = copy.deepcopy(frame)
    
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(i, j, rows, cols)
            neighbor_values = [frame[nx][ny] for nx, ny in neighbors]
            average_value = sum(neighbor_values) / len(neighbor_values)
            if abs(frame[i][j] - average_value) > 20:  # Assuming a threshold of 20 for significant difference
                corrected_frame[i][j] = round(average_value)
    
    return corrected_frame