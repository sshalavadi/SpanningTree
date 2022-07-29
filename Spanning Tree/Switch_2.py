# Spanning Tree project for GA Tech OMS-CS CS 6250 Computer Networks
#
# This defines a Switch that can can send and receive spanning tree 
# messages to converge on a final loop free forwarding topology.  This
# class is a child class (specialization) of the StpSwitch class.  To 
# remain within the spirit of the project, the only inherited members
# functions the student is permitted to use are:
#
# self.switchID                   (the ID number of this switch object)
# self.links                      (the list of swtich IDs connected to this switch object)
# self.send_message(Message msg)  (Sends a Message object to another switch)
#
# Student code MUST use the send_message function to implement the algorithm - 
# a non-distributed algorithm will not receive credit.
#
# Student code should NOT access the following members, otherwise they may violate
# the spirit of the project:
#
# topolink (parameter passed to initialization function)
# self.topology (link to the greater topology structure used for message passing)
#
# Copyright 2016 Michael Brown, updated by Kelly Parks
#           Based on prior work by Sean Donovan, 2015, updated for new VM by Jared Scott and James Lohse

from Message import *
from StpSwitch import *


class Switch(StpSwitch):

    def __init__(self, idNum, topolink, neighbors):
        # Invoke the super class constructor, which makes available to this object the following members:
        # -self.switchID                   (the ID number of this switch object)
        # -self.links                      (the list of swtich IDs connected to this switch object)
        super(Switch, self).__init__(idNum, topolink, neighbors)

        # TODO: Define a data structure to keep track of which links are part of / not part of the spanning tree.
        self.root_2 = self.switchID
        self.distan_ce_1 = 0
        self.Active__links = []
        self.the_way_in_path = self.switchID

    def send_initial_messages(self):
        # TODO: This function needs to create and send the initial messages from this switch.
        #      Messages are sent via the superclass method send_message(Message msg) - see Message.py.
        #      Use self.send_message(msg) to send this.  DO NOT use self.topology.send_message(msg)
        for each_link_neig in self.links:
            messa_to_pass = Message(self.root_2, self.distan_ce_1, self.switchID, each_link_neig, False)
            self.send_message(messa_to_pass)
        return

    def process_message(self, message):
        # TODO: This function needs to accept an incoming message and process it accordingly.
        #      This function is called every time the switch receives a new message.
        if message < self.root:
            self.root = message.root
            self.distan_ce_1 = message.distance + 1
            self.Active__links[message.origin] = True
            self.the_way_in_path = message.origin

            for each_link_neig in self.Active__links:
                messa_to_pass = message(self.root_2, self.distan_ce_1, self.switchID, each_link_neig, self.the_way_in_path == each_link_neig)
                self.send_message(messa_to_pass)
        
        if message.root_2 == self.root and message.distan_ce_1 + 1 < self.distan_ce_1:
            self.distan_ce_1 = message.distan_ce_1 + 1
            self.Active__links =[message.origin] = True
            self.the_way_in_path = message.origin

            for each_link_neig in self.Active__links:
                messa_to_pass = message(self.root_2, self.distan_ce_1, self.switchID, each_link_neig, self.the_way_in_path == each_link_neig)
                self.send_message(messa_to_pass)
        
        if message.distan_ce_1 + 1 == self.distan_ce_1:
            if message.origin < self.the_way_in_path:
                self.Active__links[self.the_way_in_path] = False
                self.the_way_in_path = message.origin
                
                for each_link_neig in self.Active__links:
                    messa_to_pass = message(self.root_2, self.distan_ce_1, self.switchID, each_link_neig, self.the_way_in_path == each_link_neig)
                    self.send_message(messa_to_pass)

        return

    def generate_logstring(self):
        # TODO: This function needs to return a logstring for this particular switch.  The
        #      string represents the active forwarding links for this switch and is invoked 
        #      only after the simulaton is complete.  Output the links included in the 
        #      spanning tree by increasing destination switch ID on a single line. 
        #      Print links as '(source switch id) - (destination switch id)', separating links 
        #      with a comma - ','.  
        #
        #      For example, given a spanning tree (1 ----- 2 ----- 3), a correct output string 
        #      for switch 2 would have the following text:
        #      2 - 1, 2 - 3
        #      A full example of a valid output file is included (sample_output.txt) with the project skeleton.
        retuen_statetment_ = "switch log string, do not return a static string, build the log string"
"
        links_that_are_sorted = sorted(self.Active__links.items())
        for each_link_neig in self.Active__links:
                links_that_are_sorted.append(str(self.switchID) + '-' + str(each_link_neig))
        return retuen_statetment_
