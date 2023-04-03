class PlayerEntity:
    """
    A class representing a player in the game.

    Attributes:
    -----------
    name : str
        The name of the player
    health : int
        The current health of the player
    max_health : int
        The maximum health of the player
    energy : int
        The current energy of the player
    max_energy : int
        The maximum energy of the player
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
    
    def __init__(self, name: str, health: int, energy: int, armor: int, damage: int, level: int):
        """
        Constructs a new PlayerEntity instance.

        Parameters:
        ---
        name : str
            The name of the player
        health : int
            The current health of the player
        energy : int
            The current energy of the player
        armor : int
            The armor value of the player
        damage : int
            The damage value of the player
        level : int
            The current level of the player
        """
        self.name = name
        self.health = health
        self.max_health = health
        self.energy = energy
        self.max_energy = energy
        self.armor = armor
        self.damage = damage
        self.level = level

    def attack(self, target: UnitEntity):
        """
        Performs an attack on the target UnitEntity.

        Parameters:
        ---
        target : UnitEntity
            The target UnitEntity to attack.
        """
        damage = self.damage - target.armor
        if damage < 0:
            damage = 0
        target.receive_damage(damage)

    def receive_damage(self, amount: int):
        """
        Receives damage from an attack.

        Parameters:
        ---
        amount : int
            The amount of damage received.
        """
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount: int):
        """
        Heals the player for the given amount.

        Parameters:
        ---
        amount : int
            The amount of health to heal.
        """
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def restore_energy(self, amount: int):
        """
        Restores energy to the player for the given amount.

        Parameters:
        ---
        amount : int
            The amount of energy to restore.
        """
        self.energy += amount
        if self.energy > self.max_energy:
            self.energy = self.max_energy

    def is_alive(self):
        """
        Returns True if the player is alive (health > 0), False otherwise.
        """
        return self.health > 0