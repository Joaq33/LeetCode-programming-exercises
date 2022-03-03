class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = [start]
        while queue:
            newqueue = []
            for item in queue:
                visited.add(item)
                if arr[item] == 0:
                    return True
                if item + arr[item] < len(arr) and item + arr[item] not in visited:
                    newqueue.append(item + arr[item])
                if item - arr[item] >= 0 and item - arr[item] not in visited:
                    newqueue.append(item - arr[item])
            queue = newqueue
        return False
