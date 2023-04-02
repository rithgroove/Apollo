from enum import Enum

class EnergyType(Enum):
    """
    A enumeration class for the type of energy that can be generated. 
    In future version more energy will be added
    
    Attributes:
    -----------
    ANY : str
        "Any", is not a type, means that any color can be spent for this requirement.
    FIRE : str
        "Fire"
    WATER : str
        "Water"
    Earth : str
        "Earth"    
    """
    ANY  = "Any"    
    FIRE = "Fire"
    WATER = "Water"
    EARTH = "Earth" 