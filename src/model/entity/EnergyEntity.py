from .enum.EnergyType import EnergyType

class EnergyEntity:
    """
    A single energy entity that can be spent for skills.
    
    Attributes:
    -----------
    name : str
        The name of the energy (usually the same as the type)
    energyType : EnergyType
        Type of this energy
    source : anyObject
        origin of this energy
    --------
    __init__(self, energytypes: EnergyType, source: anyObject)
        Constructs a new energy instance
    """
    
    def __init__(self, energyType, source):
        self.name = energyType
        self.type = energyType 
        self.source = source
        
