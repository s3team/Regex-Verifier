gPats = [

# nl_sentence = "the expression contains 9 digits"
  [r'(.*)expression contains at least (\d*) digit(.*)',
  ["let _verigex be repeat %2 digit"],["Ok!"]],

# part1 contains 'YMSG' and any 6 characters
  [r'(.*)expression contains (part\d*) and (part\d*) and (part\d*)(.*)',
  ["let _verigex be _%2 and _%3 and _%4"],["Ok!"]],  

  [r'(.*)expression contains (part\d*) and (.*) and (part\d*) and (.*) and (part\d*)(.*)',
  ["let _verigex be _%2 and %3 and _%4 and %5 and _%6"],["Ok!"]], 

  [r'(.*)expression contains (part\d*) and (part\d*)(.*)',
  ["let _verigex be _%2 and _%3"],["Ok!"]],

# part2 is 'example' and point and 'org'
  [r'(.*)(part\d*) is (.*) and point and (.*)',
  ["let _%2 be 'example\.org'"],["Ok!"]],
  
# the expression contains part1 and dot and part2
  [r'(.*)expression contains (part\d*) and dot and (part\d*)(.*)',
  ["let _verigex be _%2 and '\.' and _%3"],["Ok!"]],

  [r'(.*)(part\d*) only contains letter (\w) and letter (\w)(.*)',
  ["let _%2 be repeat zeromore ['%3'|'%4']"],["Ok!"]], 

  [r'(.*)(part\d*) only contains letter (\w) and (\w)(.*)',
  ["let _%2 be repeat zeromore '%3' or '%4'"],["Ok!"]], 

  [r'(.*)(part\d*) only contains letter (\w)(.*)',
  ["let _%2 be repeat zeromore '%3'"],["Ok!"]], 

  [r'(.*)(part\d*) contains any letter (.*)',
  ["let _%2 be repeat zeromore '[a-zA-Z]'"],["Ok!"]],

# part1 contains letter or dash
  [r'(.*)(part\d*) contains letter or dash',
  ["let _%2 be repeat onemore letter or '-'"],["Ok!"]],

# part1 contains letter or dash
  [r'(.*)(part\d*) contains letter or point',
  ["let _%2 be repeat onemore letter or '\.'"],["Ok!"]],

# part2 is '@'
  [r'(.*)(part\d*) is any letter',
  ["let _%2 be repeat onemore letter"],["Ok!"]],

  [r'(.*)first (.*) in (part\d*) is (\w) and(.*)last(.*) is (\w)(.*)',
  ["let _%3 be '%4' and '%7'"],["Ok!"]], 

  [r'(.*)(part\d*) contains [\"|\'](.*)[\'|\"] and (.*)(\d*) characters',
  ["let _%2 be '%3' and repeat 6 'x[0-9A-F]{2}'"],["Ok!"]], 

  [r'(.*)(part\d*) is(.*) [\"|\'](.*)[\'|\"](.*)',
  ["let _%2 be '%4'"],["Ok!"]],

# part1 can be a sequence of anything
  [r'(.*)(part\d*) can be a sequence of anything',
  ["let _%2 be repeat zeromore '.'"],["Ok!"]],

# part2 is '@'
  [r'(.*)(part\d*) is \'(.*)\' (.*)',
  ["let _%2 be '%3'"],["Ok!"]],
]

gReflections = {
  "or":"|",
  "one":"1",
  "two":"2",
  "three":"3",
  "four":"4",
  "five":"5",
  "six":"6",
  "seven":"7",
  "eight":"8",
  "nine":"9",
  "zero":"0",
  "not a":"non ",
  "become":"be",
  "integer" : "int",
  "character" : "char",
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you",
  "east":"0",
  "south":"270",
  "west":"180",
  "north":"90",
  "first":"1",
  "second":"2",
  "third":"3"
}

