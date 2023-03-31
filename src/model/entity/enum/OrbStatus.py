from enum import Enum

class OrbStatus(Enum):
    """
    A enumeration class for the status of the Orb
    
    Attributes:
    -----------
    READY : str
        Value = "Ready". This means that the orb can generate energy.
    SPENT : str
        Value = "Spent". This means that the orb cannot generate energy and need to wait until next turn to get the energy back. 
    """
    
    READY = "Ready"
    SPENT = "Spent" 