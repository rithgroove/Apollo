from enum import Enum

class CommandStatus(Enum):
    """
    A enumeration class for the status of the Command
    
    Attributes:
    -----------
    INQUEUE : str
        Value = "In queue". This means that the command is in queue and waiting for the execution.
    EXECUTING : str
        Value = "Executing". This means that the command is under execution
    FINISHED : str
        Value = "Finished". This means that the command have been triggered completely. 
    """
    
    INQUEUE = "In queue"
    EXECUTING = "Executing" 
    FINISHED = "Finished"