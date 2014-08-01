__author__ = 'BluABK <abk@blucoders.net'

# This is a module specification, which contains everything you need to get started on writing a module.

# Imports
import ConfigParser

# Variables
commandsavail = "wishfulthinking, pipedreams, 42, imagination"

# Classes


class Config:  # Mandatory Config class
    config = ConfigParser.RawConfigParser()

    def __init__(self):
        self.config.read('config.ini')

    def sample(self):
        return str(self.config.get('sample', 'sampleitem'))

cfg = Config()

# Functions


def help():
    cmdlist = list()
    cmdlist.append("Syntax: %scommand help arg1..argN" % cfg.cmdsym())
    cmdlist.append("Available commands: %s (* command contains sub-commands)" % commandsavail)
    return cmdlist