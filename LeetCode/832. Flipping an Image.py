class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(int(len(row)/2)):
                temp = row[i]
                row[i] = row[len(row)-1-i]
                row[len(row)-1-i] = temp
                
        for row in image:
            for i in range(len(row)):
                if row[i] == 1:
                    row[i] = 0
                else:
                    row[i] = 1
                    
        return image

#Runtime: 52 ms, faster than 57.62% of Python3 online submissions for Flipping an Image.
#Memory Usage: 14.1 MB, less than 92.22% of Python3 online submissions for Flipping an Image.