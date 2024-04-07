class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # set to keep track of visited rooms
        visited = set()
        # dfs function to explore rooms
        def dfs(room):
            # mark the current room as visited
            visited.add(room)
            # explore all keys in the current room
            for i in rooms[room]:
                # if a key leads to an unvisited room, recursively explore that room
                if i not in visited:
                    dfs(i)
        # start dfs from room 0
        dfs(0)
        # check if all rooms have been visited
        return len(visited) == len(rooms)
