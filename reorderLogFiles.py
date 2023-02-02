class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        map_ = defaultdict(list)
        digits, letters, mains = [], [], []
        for log in logs:
            i = log.find(" ")
            id_ = log[:i]
            main = log[i+1:]
            if main[0].isdigit():
                digits.append(log)
            else:
                if main not in map_:
                    mains.append(main)
                map_[main].append(id_)
        mains.sort()
        for main in mains:
            for id in sorted(map_[main]):
                letters.append(id+" "+main)
        
        return letters+digits