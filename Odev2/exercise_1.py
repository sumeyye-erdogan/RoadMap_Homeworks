# Angles Sum

class Triangle:

    number_of_sides = 3

    def __init__(self, angle1,angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        sum_angels = self.angle1 + self.angle2 + self.angle3

        if sum_angels == 180:
            return True
        else:
            return False


my_triangle = Triangle(90, 30, 60)

print("Number of sides : {} , check angles: {} ".format(my_triangle.number_of_sides, my_triangle.check_angles()))
