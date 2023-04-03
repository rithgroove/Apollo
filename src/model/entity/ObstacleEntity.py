class ObstacleEntity:
    """
    Obstacle entity represents a physical obstruction in the game map that units cannot pass through.
    """

    def __init__(self, x: int, y: int, , obstacle_type: str):
        """
        Initialize the Obstacle object.

        :param x: X coordinate of the obstacle on the map.
        :param y: Y coordinate of the obstacle on the map.
        :param obstacle_type: Type of the obstacle, e.g. "wall", "tree", etc.
        """
        self.x = x
        self.y = y
        self.obstacle_type = obstacle_type

    def get_coordinates(self) -> tuple[int, int]:
        """
        Get the coordinates of the obstacle.

        :return: Tuple containing X and Y coordinates of the obstacle.
        """
        return self.x, self.y

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
        return f"{self.obstacle_type} at ({self.x}, {self.y})"