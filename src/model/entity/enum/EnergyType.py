from enum import Enum

class EnergyType(Enum):
    """
    A enumeration class for the type of energy that can be generated. 
    In future version more energy will be added
    
    Attributes:
    -----------
    FIRE : str
        "Fire"
    WATER : str
        "Water"
    Earth : str
        "Earth"    
    """
    ANY  = "ANY"    
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth" 