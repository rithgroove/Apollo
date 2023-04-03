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
    """
    
    def __init__(self, name, position, terrainType, blocked = False):
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
        ---
        return:
            (int x, int y)
    """
        return (self.position[0],self.position[1])

    def getHeight(self):
    """ 
        get the elevation of the tile.
        ---
        return:
            int height
    """
        return self.position[2]

    def is_passable(self,player):
    """
        a method to check if this tile is passable
        ---
        return:
            bool is_passable (true = passable, false = unpassable)
    """
        for unit in self.units:
            if (unit.player != player):
                return False
        for obstacle in self.obstacles:
            if not obstacles.is_passable:
                return False
        return not self.blocked

    def is_unit_exist(self,unit = None):
    """
        a method to return if a unit exist in the tiles. 
        if unit parameter is not defined, 
        this method will return if there's any unit on this tile (occupied). 
        ---
        return:
            bool unit_exists (true = unit is here, false = unit not here)
    """
        if unit is None:
            return len(self.units) > 0
        else:
            return unit in self.units
