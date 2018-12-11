from greenery import fsm
from greenery.lego import parse
import signal
import time  


def issubset(regex1, regex2):
	# return True if regex1 is subset of regex2, which means 
	# all the strings matched by r1 is can be matched by r2
    subregex = parse(regex1)
    supregex = parse(regex2)
    s = subregex & (supregex.everythingbut())
    start = time.time()
    elapsed = 0 
    if s.empty():
    	return "Verified"
    else:
        counterexample = ""
        while elapsed < 30:  
            if not counterexample == "Timeout":
                break
            generator = s.strings()
            counterexample = next(generator)
            elapsed = time.time() - start
        return str(counterexample)

def isEquiv(regex1, regex2):
    result1 = issubset(regex1, regex2)
    result2 = issubset(regex2, regex1)
    if result1 == "Verified" and result2 == "Verified":
        return "Verified"
    else:
        if not result1 == "Verified":
            return result1
        else:
            return result2
