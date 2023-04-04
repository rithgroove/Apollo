from .enum.EnergyType import EnergyType
from .enum.OrbStatus import OrbStatus
from .EnergyEntity import EnergyEntity
import random

class TileEntity:
    """
    A class that represents a map tile in the game.
    
    Attributes:
    -----------
    name : str
        The name of the tile
    terrainType : TerrainType
        Type of the terrain
    position : (int x,int y,int z)
        position of the tile represented by tuple of 3 
    units : list of Unit
        List of units that is positioned in this tile.
    obstacles : list of obstacle
        List of obstacle that is positioned in this tile.
    buff : list of buff
        List of buff that is positioned in this tile
    blocked : bool
        a boolean that mark this tile blocked or not

    Methods:
    -----------
    def __init__(self, name, position, terrainType, blocked = False)
        Construct a tile

    getLogicalPosition(self):
        return the x and y coordinate of this tile

    def getHeight(self):
        return the elevation of the tile

    def is_occupiable(self):
        a method to check if this tile is empty and can be occupied

    def is_passable(self,player):
        a method to check if this tile is passable

    is_unit_exist(self,unit = None):
        a method to return if the unit exist in the tiles. If unit is none, then return whether there's a unit in this tile or not.
    """
    
    def __init__(self, name, position, terrainType, blocked = False):
        """
        Constructs a new tile

        :param name: The name of the tile.
        :param postion: Tuple of x,y,z position of the tile (z is the elevation of the tile)
        :param terrainType: terrainType enumeration to set the type of the tile
        :param blocked: boolean that marked if this tile is blocked or not (lava tiles for example)
        """
        self.name = name
        self.terrainType = terrainType 
        self.blocked = blocked
        self.position = position
        self.units = []
        self.obstacles = []
        self.buff = []
        
    def getLogicalPosition(self):
        """
        get the x y position of this tile. 
        
        :return: (int x, int y)
        """
        return (self.position[0],self.position[1])

    def getHeight(self):
        """ 
        get the elevation of the tile.
        
        :return: int representing elevation of this tile
        """
        return self.position[2]

    def is_occupiable(self):
        """
        A method to check if this tile is empty and can be occupied. 
        This methods is useful to filter out tiles where the unit can move to.

        :return: bool is_occupiable (true = occupiable, false = unoccupiable)
        """
        if len(self.units) > 0:
            return False
        if len(self.obstacles) > 0:
            return False
        return not self.blocked

    def is_passable(self,player = None):
        """
        a method to check if this tile is passable for the selected player.
        If player is none, will return if the tile blocked for all player.
        
        :param player: The player that we wanted to check.

        :return: bool is_passable (true = passable, false = unpassable)
        """
        if player is not None:
            for unit in self.units:
                if (unit.player != player):
                    return False
            for obstacle in self.obstacles:
                if not obstacles.is_passable:
                    return False
        return not self.blocked

    def is_unit_exist(self,unit = None):
        """
        a method to return if the unit exist in the tiles. 
        if unit parameter is not defined, 
        this method will return if there's any unit on this tile (occupied). 
        

        :return: bool unit_exists (true = unit is here, false = unit not here)
        """
        if unit is None:
            return len(self.units) > 0
        else:
            return unit in self.units

    def __str__(self):
        """
        Get the string of this tile entity

        :return: String representing the tile.
        """
        text  = "[Tile]\n"
        text += f"Name      : {self.name}\n"
        text += f"Position  : ({self.position[0]},{self.position[1]})\n"
        text += f"Elevation : {self.position[2]}\n"
        text += f"Type      : {self.terrainType}\n"
        text += f"Passable  : {self.is_passable()}\n"
        return text
