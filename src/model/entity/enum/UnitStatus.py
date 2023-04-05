from enum import Enum

class UnitStatus(Enum):
    """
    A enumeration class for the status of the Buff
    
    Attributes:
    -----------
    ACTIVE : str
        Value = "Active". This means that the buff is active.
    EXPIRED : str
        Value = "Expired". This means that the buff has expired.
    """
    COOLINGDOWN = "CoolingDown" 
    READY = "Ready" 
    DEPLOYED = "Deployed"
