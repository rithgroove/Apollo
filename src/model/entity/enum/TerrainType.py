from enum import Enum

class TerrainType(Enum):
    """
    A enumeration class for the type of terrain of the map tyle
    
    Attributes:
    -----------
    DIRT : str
        Value = "Dirt". Dirt tile
    WATER : str
        Value = "Water". Water Tile 
    GRASS : str
        Value = "Grass". Grass Tile 
    """
    
    DIRT = "Dirt"
    WATER = "Water" 
    GRASS = "Grass" 