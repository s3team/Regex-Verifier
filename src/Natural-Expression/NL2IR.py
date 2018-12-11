# coding: utf-8

import string
import re
import random
import csv
import sys
from os import system
from .rules import *


class eliza:
  
   
  def __init__(self):                           
    self.keys = map(lambda x:re.compile(x[0], re.IGNORECASE), gPats)
    self.values = map(lambda x:x[2], gPats)
    self.dialog = map(lambda x:x[1], gPats)     
  
  #----------------------------------------------------------------------
  # translate: take a string, replace any words found in dict.keys()
  #  with the corresponding dict.values()
  #----------------------------------------------------------------------
  def translate(self,str,dict):
    return str
    
  #----------------------------------------------------------------------
  #  respond: take a string, a set of regexps, and a corresponding
  #    set of response lists; find a match, and return a randomly
  #    chosen response from the corresponding list.
  #----------------------------------------------------------------------
  def respond(self,str):
    # find a match among keys
    self.keys = list(self.keys)
    self.values = list(self.values)
    self.dialog = list(self.dialog)

    for i in range(0,len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        value= random.choice(self.values[i])
        dialog= random.choice(self.dialog[i])
        resp = value + dialog
        posi = dialog.find('%')
        while posi > -1:
          numi = int(dialog[posi+1:posi+2])
          dialog = dialog[:posi] + \
            self.translate(match.group(numi), gReflections) + \
            dialog[posi+2:]
          posi = dialog.find('%')
    
        if dialog[-2:] == '?.': dialog = dialog[:-2] + '.'
        if dialog[-2:] == '??': dialog = dialog[:-2] + '?'               
        
        # we've got a response... stuff in reflected text where indicated
        pos = value.find('%')
        while pos > -1:
          num = int(value[pos+1:pos+2])
          value = value[:pos] + \
            self.translate(match.group(num), gReflections) + \
            value[pos+2:]
          pos = value.find('%')
        # fix munged punctuation at the end
        if value[-2:] == '?.': value = value[:-2] + '.'
        if value[-2:] == '??': value = value[:-2] + '?'
        return [value,dialog]


#----------------------------------------------------------------------
#  error handle
#----------------------------------------------------------------------

def Wrongcase(s):
    f2 = open('wrong.txt','r+')
    f2.read()
    f2.write(s)
    f2.write('\n')
    f2.close()

#----------------------------------------------------------------------
#  command_interface
#----------------------------------------------------------------------
def interpret(sentence):
  # global choice
  result = []
  shell = eliza();

  try:
    while sentence[-1] in "!.\n?": sentence = sentence[:-1]
    feedback = shell.respond(sentence)[0]
    ir = shell.respond(sentence)[1]

  except TypeError:
    Wrongcase(sentence)
    command_interface()

  except EOFError:
    Wrongcase(sentence)
    command_interface()
    
  except UnboundLocalError:
    Wrongcase(sentence)
    command_interface()
    
  except IndexError:
    Wrongcase(sentence)
    command_interface()
    
  except IndentationError:
    Wrongcase(sentence)
    command_interface()

  else:
    result.append(feedback)
    result.append(ir)
    return result

