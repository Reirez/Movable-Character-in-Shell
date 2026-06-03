from random import randint

class Map: #width n length are reversed
    def __init__(self, pixel):
        self.pixel = pixel
    
    def generate_map(self, width, length):
        """Makes a map based on given WL"""
        self.map = []
        self.width = width
        self.length = length
        for w in range(width):
            y_list = []
            for l in range(length):
                y_list.append(self.pixel)
            self.map.append(y_list)
        """Generates a door on a random point on the map"""
        self.map[randint(0, self.width - 2)][randint(0, self.length - 1)] = "#"
    
    def check_tile(self, symbol):
        """checks if symbol still exists in map"""
        idk = 0
        for x_list in self.map:
            if symbol not in x_list:
                idk += 1
        if idk == self.width:
            return True
    def display_map(self, floor_level):
        """Prints map as a W by L rectangle"""
        print(f"Floor {floor_level}")
        for x_list in self.map:
            x_row = ""
            for x_value in x_list:
                x_row += str(x_value)
            print(x_row)
#make random map generator -dif width n lengths
#add random encounters n doors ?
class Character:
    """An attempt to model a movable character"""
    def __init__(self, width, length, look="T"):
        self.look = look
        self.width = width
        self.length = length
    
    def locate_char(self, map):
        """locates character position"""
        yaxis = 0
        for y in map:
            for x in range(len(y)):
                if map[yaxis][x] == self.look:
                    return yaxis, x
            yaxis += 1
        
    def move(self, direction, map, instance):
        """move in the four directions"""
        yaxiz, xaxiz = self.locate_char(map)
        if direction == "d":
            map[yaxiz][(xaxiz + 1) % self.length] = self.look
            map[yaxiz][xaxiz] = instance.pixel
        elif direction == "w":
            map[(yaxiz - 1) % self.width][xaxiz] = self.look
            map[yaxiz][xaxiz] = instance.pixel
        elif direction == "s":
            map[(yaxiz + 1) % self.width][xaxiz] = self.look
            map[yaxiz][xaxiz] = instance.pixel
        elif direction == "a":
            map[yaxiz][xaxiz - 1] = self.look
            map[yaxiz][xaxiz] = instance.pixel
        else:
            print("\nInvalid move!")
           
    def spawn(self, map):
        """spawns character into map"""
        map[-1][0] = self.look
        
def main():
    """main game loop"""
    floor = 0
    while True:
        map = Map('-')
        map.generate_map(randint(2, 5), randint(2, 10))
        t = Character(map.width, map.length, look = "B")
        t.spawn(map.map)
        map.display_map(floor)
        while True:
            move = input("Enter move (wasd): ")
            t.move(move, map.map, map)
            if map.check_tile('#'):
                floor += 1
                break
            map.display_map(floor)

print("walking sim.\nB - character\n# - door to next level")
if input("Enter 'y' to start: ").lower() == 'y':
    main()
        