""" Starts the interpreter agent. """
from interpreter.core.core import Interpreter

interpreter = Interpreter()
interpreter.model = 'azure/gpt-4' # used by litellm to select the model
interpreter.context_window = 10_000

# Starts an interactive chat
interpreter.chat()
