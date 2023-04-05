from typing import List
from .enums import UnitStatus, AttackType
from .buff import Buff
from .orb import OrbEntity


class UnitEntity:
    """
    A class representing a unit entity in the game.

    Attributes:
    -----------
    name : str
        The name of the unit
    max_hp : int
        The maximum hit points of the unit
    attack : int
        The attack power of the unit
    armor : int
        how many damage will the unit block
    move : int
        The movement speed of the unit
    status : UnitStatus
        The current status of the unit
    attack_type : AttackType
        The attack type of the unit (melee or ranged)
    orbs : List[OrbEntity]
        The orbs owned by the unit
    buffs : List[Buff]
        The buffs currently affecting the unit

    Methods
    --------
    __init__(self, name: str, max_hp: int, attack: int, defense: int, speed: int, attack_type: AttackType)
        Constructs a new UnitEntity instance with the specified attributes.

    receive_damage(self, damage: int)
        Receives damage from an attack, taking into account the unit's defense and reducing its hit points accordingly.

    add_buff(self, buff: Buff)
        Adds a buff to the unit, affecting its attributes during battle.

    remove_buff(self, buff: Buff)
        Removes a buff from the unit, restoring its original attributes.

    get_speed(self)
        Calculates the unit's effective speed, taking into account its base speed and any speed-altering buffs.

    attack_enemy(self, enemy: UnitEntity)
        Attacks an enemy unit, reducing its hit points based on the unit's attack power and the enemy's defense.

    use_orb(self, selected_orb: OrbEntity)
        Uses an orb owned by the unit, generating energy or performing some other effect.

    is_alive(self)
        Returns True if the unit is still alive (has hit points remaining), False otherwise.
    """
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, speed: int, attack_type: AttackType):
        """
        Constructs a new UnitEntity instance with the specified attributes.

        Parameters:
        -----------
        name : str
            The name of the unit.
        max_hp : int
            The maximum hit points of the unit.
        attack : int
            The attack power of the unit.
        defense : int
            The defense power of the unit.
        speed : int
            The speed of the unit.
        attack_type : AttackType
            The attack type of the unit (melee or ranged).
        """
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.status = UnitStatus.NORMAL
        self.attack_type = attack_type
        self.orbs = []
        self.buffs = []

    def receive_damage(self, damage: int):
        """
        Receives damage from an attack, taking into account the unit's defense and reducing its hit points accordingly.

        Parameters:
        -----------
        damage : int
            The amount of damage received from the attack.
        """
        damage_taken = max(1, damage - self.defense)
        self.hp -= damage_taken
        if self.hp <= 0:
            self.hp = 0
            self.status = UnitStatus.DEAD

    def add_buff(self, buff: Buff):
        """
        Adds