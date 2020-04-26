class Rectangle(object):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def check_hit(self, position, event):
        x = event.pos[0]
        y = event.pos[1]

        if x >= position.x and x <= position.x + self.width:
            if y >= position.y and y <= position.y + self.height:
                return True

        return False
