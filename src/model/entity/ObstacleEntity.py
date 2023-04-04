class ObstacleEntity:
    """
    Obstacle entity represents a physical obstruction in the game map that units cannot pass through.
    """

    def __init__(self, name:str, x : int, y :int , width:int, length: int , obstacle_type: str):
        """
        Initialize the Obstacle object.
        :param name: the name of this obstacle
        :param x: X coordinate of the obstacle on the map.
        :param y: Y coordinate of the obstacle on the map.
        :param width: how many x tiles does this object occupies
        :param length: how many y tiles does this object occupies
        :param obstacle_type: Type of the obstacle, e.g. "wall", "tree", etc.
        """
        self.name = name 
        self.position = (x,y)
        self.width = width
        self.length = length
        self.obstacle_type = obstacle_type

    def get_coordinates(self) -> tuple[int, int]:
        """
        Get the coordinates of the obstacle.

        :return: Tuple containing X and Y coordinates of the obstacle.
        """
        return self.position

    def get_obstacle_type(self) -> str:
        """
        Get the type of the obstacle.

        :return: String representing the type of the obstacle.
        """
        return self.obstacle_type

    def __str__(self) -> str:
        """
        Get the string representation of the obstacle.

        :return: String representing the obstacle.
        """
        text  =  "[Obstacle]\n"
        text += f"name          = {self.name}\n"
        text += f"position      = ({self.position[0]},{self.position[1]})\n"
        text += f"dimension     = {self.width}x{self.length}\n"
        text += f"obstacle type = {self.obstacle_type}\n"
        return text