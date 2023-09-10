class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        section_visited = [0]*n
        
        for i in range(len(rounds) - 1):
            if rounds[i] < rounds[i+1]:
                for j in range(rounds[i], rounds[i+1]):
                    section_visited[j-1] += 1
            else:
                for j in range(rounds[i], n+1):
                    section_visited[j-1] += 1
                for j in range(1, rounds[i+1]):
                    section_visited[j-1] += 1
                
        section_visited[rounds[-1]-1] += 1
        max_occurance = max(section_visited)
        return [i+1 for i,section in enumerate(section_visited) if section == max_occurance]