# Inherits Program

class POINT3D(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "x: {}, y: {}, z: {} ".format(self.x, self.y, self.z)


my_point = POINT3D(1, 2, 3)
print(my_point.__repr__())
