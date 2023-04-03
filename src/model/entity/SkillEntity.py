class SkillEntity:
    """
    A class representing a skill that a character can use.

    Attributes:
    -----------
    name : str
        The name of the skill.
    mana_cost : int
        The amount of mana required to use the skill.
    effects : List[Tuple[str, float]]
        A list of tuples representing the effects of the skill.
        Each tuple contains a string representing the name of the effect and
        a float representing the magnitude of the effect.
    cooldown : Optional[int]
        The number of turns the skill needs to cooldown after use.
        If None, the skill has no cooldown.
    """
    def __init__(self, name: str, mana_cost: int, effects: List[Tuple[str, float]], cooldown: Optional[int] = None):
        """
        Constructs a new Skill instance.

        Parameters:
        -----------
        name : str
            The name of the skill.
        mana_cost : int
            The amount of mana required to use the skill.
        effects : List[Tuple[str, float]]
            A list of tuples representing the effects of the skill.
            Each tuple contains a string representing the name of the effect and
            a float representing the magnitude of the effect.
        cooldown : Optional[int]
            The number of turns the skill needs to cooldown after use.
            If None, the skill has no cooldown.
        """
        self.name = name
        self.mana_cost = mana_cost
        self.effects = effects
        self.cooldown = cooldown