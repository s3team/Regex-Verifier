from .myyacc import *
import sys

def IR2RE(ir):
	for statement in ir:
		statement = (statement[-1] == "\n") and statement[0:-1] or statement
		yacc.parse(statement)
	return names["_verigex"]