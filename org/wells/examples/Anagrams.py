class AnagramFinder:

    def increaseChar(self, info, c):
        if c in info:
            info[c] += 1
        else:
            info[c] = 1

    def decreaseChar(self, info, c):
        if c in info:
            info[c] -= 1
            if info[c] == 0:
                info.pop(c, None)



    def parsePattern(self, pattern):
        patternInfo = {}
        for c in pattern:
            self.increaseChar(patternInfo, c)
        return patternInfo


    def find(self, haystack, pattern):
        results = []
        windowSize = len(pattern)
        patternInfo = self.parsePattern(pattern.lower())
        print("patternInfo: {}".format(patternInfo))
        window = []
        windowInfo = {}

        def appendCharToWindow(c):
            if len(window) == windowSize:
                self.decreaseChar(windowInfo, window.pop(0))
            window.append(c)
            self.increaseChar(windowInfo, c)
            print("window: {}, windowInfo: {}, c: {}".format(window, windowInfo, c))


        if len(haystack) < windowSize :
            return results
        else:
            for c in haystack:
                appendCharToWindow(c.lower())
                if patternInfo == windowInfo:
                    results.append(''.join(window))
            return results


haystack = "aeeEsdfesdesefdfseeesdffvett"
pattern = "eesdf"

results = AnagramFinder().find(haystack, pattern)
print("results: {}".format(len(results)))




