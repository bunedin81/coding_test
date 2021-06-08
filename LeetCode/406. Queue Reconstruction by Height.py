class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        new_list = []
        people.sort(key=lambda x:[x[0], -x[1]], reverse=True)
        #print(people)
        
        for i in people:
            new_list.insert(i[1], i)
            #print(new_list)
        return new_list

#Runtime: 116 ms, faster than 36.24% of Python3 online submissions for Queue Reconstruction by Height.
#Memory Usage: 14.9 MB, less than 30.64% of Python3 online submissions for Queue Reconstruction by Height.