# coding:utf-8
class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name,"销毁掉了…………"

pt1 = Point(x=20,y=10)
pt2 = pt1
pt3 = pt1

print id(pt1),id(pt2),id(pt3)

del pt1,pt2,pt3





