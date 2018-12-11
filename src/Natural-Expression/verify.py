from .subset import *
from .compiler import *
import re
import pdb
from .NL2IR import *

def verify(ir, regex):
	spec = IR2RE(ir)
	spec = re.sub(r" ", "", spec)
	return (isEquiv(spec, regex), spec)

def nl2ir(sentence): 
	return interpret(sentence)

def verifyNL(nl_sentence, target_re):
	ir = []
	for sentence in nl_sentence:
		try:
			ir_sentence = nl2ir(sentence)[1]
			ir.append(nl2ir(sentence)[1])
		except:
			return ('', 'Hmm...')
	return verify(ir, target_re)
