from .enum.EnergyType import EnergyType
from .enum.OrbStatus import OrbStatus
from .EnergyEntity import EnergyEntity
import random

class OrbEntity:
    """
    A class representing an orb (Perpetual Resource) for player.
    
    Attributes:
    -----------
    name : str
        The name of the orb
    types : Array of Energy Type
        Type energy this orb generates
    status : OrbStatus
        The status of the orbs 
    --------
    __init__(self, types: type)
        Constructs a new Orb instance with that can produce the energy of the types given.

    harvest_energy(self,selected_Type:EnergyType)
        Return an energy based on selected type, will return random energy based on the type of energy the orbs generate.

    refresh(self)
        A method to refresh the orb, and fill it back with energy. This usually called in clean up phase. 

    have_options(self)
        A method to check whether the orb produce multiple types of energy.
    """
    
    def __init__(self, name, types):
        self.name = name
        self.types = types 
        if (self.types is None):
            self.types = []
        self.status = OrbStatus.READY
        
    def harvest_energy(self, selected_type= None):
        """
        Return an energy based on selected type, will return random energy based on the type of energy the orbs generate.
        Will raise an exception if selected type is not a member of the types attribute.

        Parameters:
        ---
        selected_type : EnergyType
            Default value = None
            the selected energy type.
        """
        if selected_type is None or selected_type = EnergyType.ANY:
            self.status = OrbStatus.SPENT
            return new EnergyEntity(random.choice(self.types),self)
        elif selected_type in self.types:
            self.status = OrbStatus.SPENT
            return new EnergyEntity(selected_type,self)
        else:
            raise Exception("The orb cannot generate that type of energy")
        
    def refresh(self):
        """
        A method to refresh the orb, and fill it back with energy. Basically it change status from OrbStatus.SPENT to ready.
        This usually called in clean up phase, but some skills might be able to call this function.
        To avoid refershing a ready orb, this will throw exception if the orb does not require refresh.
        """
        if (self.status == OrbStatus.SPENT):
            self.status = OrbStatus.READY
        else:
            raise Exception("The Orb does not require refresh")

    def have_options(self):
        """
        A method to check whether the orb produce multiple types of energy. This is will indicates there will be a energy selection step before the orb produces energy.
        """
        if len(self.types) > 1:
            return True
        return False