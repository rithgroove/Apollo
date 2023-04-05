from enum import Enum

class AttackType(Enum):
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
    
    PIERCING = "Piercing"
    BLUNT = "Blunt" 
    SLASH = "Slash" 
    ARCANE = "Arcane"
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth"
    WIND = "Wind" 