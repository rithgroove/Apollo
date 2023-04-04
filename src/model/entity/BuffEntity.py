class BuffEntity:
    """
    A class representing a buff that can be applied to a character.

    Attributes:
    -----------
    name : str
        The name of the buff.
    duration : int
        The number of turns the buff lasts for.
    effects : List[Tuple[str, float]]
        A list of tuples representing the effects of the buff.
        Each tuple contains a string representing the name of the effect and
        a float representing the magnitude of the effect.
    """
    def __init__(self, name: str, duration: int, effects: List[Tuple[str, float]]):
        """
        Constructs a new Buff instance.

        :param name: String containinge the name of the buff.
        :param duration: The number of turns the buff lasts for.
        :param effects: List[Tuple[str, float]] 
            A list of tuples representing the effects of the buff.
            Each tuple contains a string representing the name of the effect and
            a float representing the magnitude of the effect.
        """
        self.name = name
        self.max_duration = duration
        self.elapsed = 0
        self.effects = effects
        self.status = "active"

    def update(self, unit):
        print("crap")

    def step(self):
        self.elapsed += 1
        if self.elapsed >= self.max_duration:
            self.status = "expired"