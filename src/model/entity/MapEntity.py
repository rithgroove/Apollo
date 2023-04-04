from .TileEntity import TileEntity

class MapEntity:
    """
    A class representing the game map.

    Attributes:
    -----------
    tiles : List of List of TileEntity
        A 2D list of TileEntities representing the tiles on the game map.
    width : int
        The width of the game map.
    length : int
        The length of the game map.

    Methods:
    --------
    __init__(self, width:int, height:int)
        Constructs a new MapEntity instance with the given width and height.

    get_tile(self, x:int, y:int) -> TileEntity:
        Returns the TileEntity at the given (x, y) coordinates on the map.

    set_tile(self, x:int, y:int, tile:TileEntity) -> None:
        Sets the TileEntity at the given (x, y) coordinates on the map.

    get_adjacent_tiles(self, x:int, y:int) -> List[TileEntity]:
        Returns a list of adjacent TileEntities to the given (x, y) coordinates on the map.

    get_neighbors(self, x:int, y:int, distance:int) -> List[Tuple[int, int]]:
        Returns a list of coordinates (as tuples) that are within the given distance of the given (x, y) coordinates on the map.
    """

    def __init__(self, width: int, length: int):
        """
        Constructs a new MapEntity instance with the given width and height.

        :param width: The width of the game map.
        :param length : The height of the game map.
        """
         for y in range(height)] for x in range(width)]
        self.width = width
        self.length = length

    def get_tile(self, x: int, y: int) -> TileEntity:
        """
        Returns the TileEntity at the given (x, y) coordinates on the map.

        :param x:The x-coordinate of the tile to retrieve.
        :param y:The y-coordinate of the tile to retrieve.

        :return: The TileEntity at the given coordinates.
        """
        return self.tiles[x][y]

    def set_tile(self, x: int, y: int, tile: TileEntity) -> None:
        """
        Sets the TileEntity at the given (x, y) coordinates on the map.

        Parameters:
        -----------
        x : int
            The x-coordinate of the tile to set.
        y : int
            The y-coordinate of the tile to set.
        tile : TileEntity
            The TileEntity to set at the given coordinates.
        """
        self.tiles[x][y] = tile

    def get_adjacent_tiles(self, x: int, y: int) -> List[TileEntity]:
        """
        Returns a list of adjacent TileEntities to the given (x, y) coordinates on the map.

        Parameters:
        -----------
        x : int
            The x-coordinate of the tile to get the adjacent tiles of.
        y : int
            The y-coordinate of the tile to get the adjacent tiles of.

        Returns:
        --------
        adjacent_tiles : List of TileEntity
            A list of TileEntities that are adjacent to the given tile.
        """
        adjacent_tiles = []
        if x > 0:
            adjacent_tiles.append(self.get_tile(x - 1, y))
        if x < self.width - 1:
            adjacent_tiles.append(self.get_tile(x + 1
