class Solution:
    def getArea(self, bottom_left, top_right):
        width = top_right[0] - bottom_left[0]
        height = top_right[1] - bottom_left[1]
        
        return width * height
    
    def findIntersection(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        rx1 = max(ax1, bx1)
        ry1 = max(ay1, by1)
        rx2 = min(ax2, bx2)
        ry2 = min(ay2, by2)
        
        if rx1 >= rx2 or ry1 >= ry2:
            return 0
        
        return self.getArea((rx1, ry1), (rx2, ry2))
    
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        this is geometry!
        
        to get the width and height a rectangle R with points (ax1, ay1) and (ax2, ay2)
        
        width = ax2 - ax1
        height = ay2 - ay1
        
        now the area is just width x height
        
        the tricky part is if we have another rectangle B, there might be an intersection
        
        to find if an intersection exists, we can calculate the points of the intersected rectangle
        
        rx1 = max(ax1, bx1)
        ry1 = max(ay1, by1)
        rx2 = min(ax2, bx2)
        ry2 = min(ay2, by2)
        
        if rx1 >= rx2 or ry1 >= ry2:
            no intersection
        else:
            intersection
            
        the total area covered by the two rectangles is
        area(A) + area(B) - area(A intersect B)
        """
        
        area1 = self.getArea((ax1, ay1), (ax2, ay2))
        area2 = self.getArea((bx1, by1), (bx2, by2))
        intersection = self.findIntersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
        return area1 + area2 - intersection
        
        