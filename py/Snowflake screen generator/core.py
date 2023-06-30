#from time import sleep as t_wait
import random

class core:

	_data = []

	def generate(size):
		...
		#core._data = 0
		data = []
		for this_y in range(size[1]):
			for this_x in range(size[0]):
				rmin = 0
				rmax = 1

				'''
				# x
				if this_x == (size[0] / 2):
					...
				elif this_x < (size[0] / 2):
					rmin += rmin / ( 1 / ( size[0] - this_x ) )
				elif this_x > size[0]:
					rmin += rmin / ( 1 / ( this_x - size[0] ) )

				# y
				if this_y == (size[1] / 2):
					...
				elif this_y < (size[1] / 2):
					rmin += rmin / ( 1 / ( size[1] - this_y ) )
				elif this_y > (size[1] / 2):
					rmin += rmin / ( 1 / ( this_y - size[1] ) )
				'''
				#blackwhite = 255
				blackwhite = random.uniform(rmin,rmax)

				data.append(blackwhite)   # R
				data.append(blackwhite)   # G
				data.append(blackwhite)   # B
				data.append(255)                # A
				core._data = data


	def get_data():
		return core._data
	
	

