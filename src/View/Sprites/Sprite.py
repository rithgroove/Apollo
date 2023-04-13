import pygame
class Sprite:

	def __init__(self,image_path):
		self.image_path = image_path
		self.position = (0,0)

	def __draw__(self,window):
		return False