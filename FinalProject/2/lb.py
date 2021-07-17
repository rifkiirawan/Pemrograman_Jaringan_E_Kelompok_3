class LoadBalancer:
	def __init__(self):
		self.server_list = []
		self.server_list.append(("localhost", 8888))
		self.server_list.append(("localhost", 8889))
		self.server_list.append(("localhost", 8890))
		self.server_list.append(("localhost", 8891))
		self.server_list.append(("localhost", 8892))
		self.counter = 0
		
	def get_server(self):
		server = self.server_list[self.counter]
		self.counter += 1
		if self.counter >= len(self.server_list) :
			self.counter = 0
		return server

if __name__=="__main__": 
	load_balancer = LoadBalancer()