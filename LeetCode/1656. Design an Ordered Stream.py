class OrderedStream:

    stream = []
    visited = []
    ptr = 0
    
    def __init__(self, n: int):
        self.stream = [0 for i in range(n)]
        self.visited = [0 for i in range(n)]
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value
        rtn = []
        
        while self.ptr < len(self.stream):
            if self.stream[self.ptr] != 0 and self.visited[self.ptr] == 0:
                rtn.append(self.stream[self.ptr])
                self.visited[self.ptr] = 1
                self.ptr += 1
            else:
                break
        #print(self.stream)
        #print(self.visited)
        return rtn
        


#Runtime: 228 ms, faster than 37.37% of Python3 online submissions for Design an Ordered Stream.
#Memory Usage: 15.1 MB, less than 29.36% of Python3 online submissions for Design an Ordered Stream.