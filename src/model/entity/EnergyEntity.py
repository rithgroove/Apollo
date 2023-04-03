from .enum.EnergyType import EnergyType

class EnergyEntity:
    """
    A single energy entity that can be spent for skills.
    
    Attributes:
    -----------
    name : str
        The name of the energy 
    energyType : EnergyType (string-enum)
        Type of this energy
    source : anyObject
        origin of this energy
    --------
    __init__(self, energytypes: EnergyType, source: anyObject)
        Constructs a new energy instance
    """
    
    def __init__(self, name, energyType, source):
        """
        Constructs a new energy instance
        
        name : str
            The name of the energy 
        energyType : 
            Type of this energy
        source : anyObject
            origin of this energy
        --------
        """

        self.name = name
        self.type = energyType 
        self.source = source
        
