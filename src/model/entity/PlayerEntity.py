class PlayerEntity:
    """
    A class representing a player in the game.

    Attributes:
    -----------
    name : str
        The name of the player
    energy : List of Energy
        The current energy of the player
    armor : int
        The armor value of the player
    damage : int
        The damage value of the player
    level : int
        The current level of the player

    Methods:
    --------
    __init__(self, name: str, health: int, energy: int, armor: int, damage: int, level: int)
        Constructs a new PlayerEntity instance.

    attack(self, target: UnitEntity)
        Performs an attack on the target UnitEntity.

    receive_damage(self, amount: int)
        Receives damage from an attack.

    heal(self, amount: int)
        Heals the player for the given amount.

    restore_energy(self, amount: int)
        Restores energy to the player for the given amount.

    is_alive(self)
        Returns True if the player is alive (health > 0), False otherwise.
    """
    
    def __init__(self, name: str, units, orbs, gateway):
        """
        Constructs a new PlayerEntity instance.

        :param name : The name of the player
        :param units: List of units this player control
        :param orbs: The orbs that player started with 
        :param gateway: The main gateway the player will use
        """
        self.name = name
        self.units = units
        self.orbs = orbs
        self.energy_pool = []
        self.main_gateway = gateway
        self.gateway = []
        self.gateway.append(gateway)
        self.glory = 0

    def __str__(self):
        text  = f"[Player]\n"
        text += f"name   = {self.name}\n"
        text += f"status = {self.status}\n"

        return text

    def add_glory(self, additional_glory: int):
        """
        Methods to add glory to this player. 
        Glory will be gained when:
        - killing enemy units (1 points)
        - killing enemy leader (2 points)
        - destroying enemy gateway (1 points)
        - destroying main enemy gateay (3 points)

        :param additional_glory: the amount of additional_glory
        """
        self.glory += additional_glory

    def is_winning(self):
        """
        Methods to check if this player is winning the game

        :return: true if the player won the game.
        """
        if glory >= 5:
            return True
        if len(orbs >= 10):
            return True
        return False

    def is_elimininated(self):
        """
        Methods to check if this player have lost and eliminated from the game

        :return: true if the player lost the game
        """
        if len(self.units) == 0 and self.main_gateway is None and len(self.gateway) == 0:
            return True
        return False
