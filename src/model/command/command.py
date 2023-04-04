from .enum.CommandStatus import CommandStatus
class Command:
    """
    A superclass representing commands generated by skills 

    Attributes:
    -----------
    name: str
    	the name of the command
    status : CommandStatus
    	the status of the command (enum string)
   	duration : double
   		duration of this command (seems like in millisecond)
   	elapsed: double
   		how many time till have been spent on this command
    """
	def __init__(self,name, duration):
        """
        Constructs a new command

        :param name: the name of the command.
        :param duration: the duration of command in milliseconds
        """

		self.name = name
		self.status = CommandStatus.INQUEUE
		self.duration = duration
		self.elapsed = 0

	def execute(self,elapsed_time):
        """
        A function to execute this command

        :param elapsed_time: the elapsed time in milliseconds
        """
		if self.status == CommandStatus.INQUEUE:
			self.status = CommandStatus.EXECUTING
		self.elapsed += elapsed_time
		if self.elapsed_time >= self.duration:
			self.status = CommandStatus.FINISHED
