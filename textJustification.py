class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        l = 0
        line = []
        for word in words:
            if l+len(word)+len(line) > maxWidth:
                lines.append([line, maxWidth - l])
                line = [word]
                l = len(word)
            else:
                line.append(word)
                l += len(word)
        if line:
            lines.append([line, maxWidth - l])
        res = []
        for i,temp in enumerate(lines):
            line, space_left = temp
            if i == len(lines)-1 or len(line) == 1:
                s = " ".join(line)
                space_left = maxWidth - len(s)
                res.append(s + " " * space_left)
                continue
            space = len(line) - 1
            s = ""
            for index, word in enumerate(line):
                if index < space_left % space:
                    s = s + word + " " * (space_left // space + 1)
                elif index == len(line)-1:
                    s = s + word
                else:
                    s = s + word + " " * (space_left // space)
            res.append(s)
        return res