import curses
from os import system

node_classes = {}
all_nodes = []

class node:

	def __init__(self, nodename, order = 1):

		self.name = nodename
		self.order = order
		self.connections_plus_values = []
		all_nodes.append(nodename)

	def make_connections(self, target_node, connection_value):
		if target_node in all_nodes:
			self.connections_plus_values.append((target_node, connection_value))
			node_classes[target_node].order = self.order+1
		else:
			want_to_make_node = input("That node doe's not exist, do you want to make a new node?")
			if want_to_make_node == "yes" or "Yes":
					node_classes.update({target_node:node(target_node, order = self.order+1)})
					all_nodes.append(target_node)
					self.connections_plus_values.append((target_node, connection_value))
	def print_attributes(self):
		print("Name: {0}\nOrder: {1}\nConnections and values: {2}".format(self.name, self.order,
		self.connections_plus_values))

def create_new_node(node_name):
	node_classes.update({node_name:node(node_name)})
#
#while True:
#	current_input = input(">")
#	if current_input == "help":
#		print(""" 
#		To make a new node type "make-node <nodename>"
#		To make a new connection type "make-connection <start node> <target node> <connection value>
#		To print the attributes of a node type "info <node name>"
#		To print all current node names type "print-all"
#		""")
#	listed_input = current_input.split(" ")
#	if "make-node" in listed_input and len(listed_input) == 2:
#		create_new_node(listed_input[1])
#		print(listed_input)
#	if "make-connection" in listed_input and len(listed_input) == 4:
#		node_classes[listed_input[1]].make_connections(listed_input[2], listed_input[3])
#		print(listed_input)
#		print("Success, connection made")
#	if "info" in listed_input and len(listed_input) == 2:
#		node_classes[listed_input[1]].print_attributes()
#		print(listed_input)
#	if "print-all" in listed_input:
#		print(all_nodes)

###



screen = curses.initscr()
screen.border(0)
screen.addstr(1,2,"Welcome to Nodes/Edges!", curses.A_UNDERLINE)
screen.refresh()
x = screen.getstr(10, 10, 60)
curses.endwin()
