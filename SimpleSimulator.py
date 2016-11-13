

import events


class Simple_Simulator:

	def __init__(self, name):
		self.name = name

	#callback function is called when subscribed event happens
	#callback function compare the actual APP launched and the preloaded APP
	#return true if the two APPs are the same, indicating a successful preload
	def callback(self, event):
		print(event.event_type)
		return False

	# def subscribe(self, event_type, callback, event_filter = None):
	# 	uamp_sim.subscribe(event_type, callback)

	# def run(self, event, callback):
	# 	self.subscribe(event, callback)
