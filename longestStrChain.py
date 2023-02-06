class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        graph = defaultdict(set)
        indegree = defaultdict(int)
        for word in words:
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                if new_word in word_set and word not in graph[new_word]:
                    graph[new_word].add(word)
                    indegree[word] += 1
                    
        level = 0
        que = [word for word in words if indegree[word] == 0]
        while que:
            temp = []
            for word in que:

                for child in graph[word]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        temp.append(child)
            que = temp
            level += 1
            
        return level