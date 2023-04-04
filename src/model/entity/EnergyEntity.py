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

    Methods:
    --------
    __init__(self, energytypes: EnergyType, source: anyObject)
        Constructs a new energy instance

    __str__(self):
        Return string representation of this energy
    """
    
    def __init__(self, name:str, energyType:EnergyType, source):
        """
        Constructs a new energy instance
    
        :param name: the name of the energy.
        :param energyType: Type of this energy.
        :param source: origin of this energy.
        """

        self.name = name
        self.type = energyType 
        self.source = source
    
    def __str__(self):
        """
        Get the string of this energy entity

        :return: String representing the energy instance.
        """
        text  = "[Energy]\n"
        text += f"Name   : {self.name}\n"
        text += f"Type   : {self.type}\n"
        if (self.source is not None):
            text += f"Source :\n\t"
            temp = str(self.source).replace("\n","\n\t")
            text += temp
        return text
