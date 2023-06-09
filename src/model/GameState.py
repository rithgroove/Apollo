class GameState:
    """
    A class representing the state of the game.

    Attributes:
    -----------
    players : List of PlayerEntity
        A list of player entities in the game.
    units : List of UnitEntity
        A list of unit entities in the game.
    map : MapEntity
        The map entity for the game.
    turn_number : int
        The current turn number.
    """

    def __init__(self, players, units, map_entity, turn_number=1):
        """
        Constructs a new GameState instance.

        Parameters:
        -----------
        players : List of PlayerEntity
            A list of player entities in the game.
        units : List of UnitEntity
            A list of unit entities in the game.
        map : MapEntity
            The map entity for the game.
        turn_number : int
            The current turn number. Default is 1.
        """
        self.players = players
        self.units = units
        self.map = map_entity
        self.turn_number = turn_number

    def __str__(self):
        text  = f"[Gamestate]\n"
        text += f"Turn              = {self.turn_number}\n"
        text += f"Number of players = {len(self.players)}\n"
        text += f"Number of units   = {len(self.units)}\n"
        text += f"Map Size          = {self.map.width} x {self.map.length}\n"
        return text
