gPats = [

# Not
  [r'(.*) does not (contain|have|contains|has) (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE NOT "%5"'], ["Okay, %1 does not contain '%5'!"]],

  [r'(.*) (contain|contains|have|has) only (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%5"'], ["Okay, %1 only contains '%5'!"]],

  [r'(.*) only (contain|contains|have|has) (.*) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%5"'], ["Okay, %1 only contains '%5'!"]],

  [r'(.*) (use|using|has|contains|have|contain) words ending in (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD END "%4"'], ["Okay, %1 uses words ending in '%4'!"]],

  [r'(.*) (contain|contains|have|has) only lowercase (characters|letters|letter|character|alphabet|alphabets)(.*)',
  ['LET _%1 BE REPEAT SEVERAL LOWCASE'], ["Okay, %1 contains only lowercase letters!"]],

  [r'(.*) (use|using|has|contains|have|contain) the word (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD "%4"'], ["Okay, %1 is word '%4'!"]],

  [r'(.*) (use|using|has|contains|have|contain) word (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE WORD "%4"'], ["Okay, %1 is word '%4'!"]],

  [r'(.*) (use|using|has|contains|have|contain) words that (use|using|has|contains|have|contain) (\d*) (vowels|vowel)(.*)',
  ['LET _%1 BE WORD HAS %4 ONE OF "aeiou"'],["Okay, %1 is word has %4 vowels!"]],

  [r'(.*) (use|using|has|contains|have|contain) words (use|using|has|contains|have|contain) (\d*) (vowels|vowel)(.*)',
  ['LET _%1 BE WORD HAS %4 ONE OF "aeiou"'],["Okay, %1 is word has %4 vowels!"]],

  [r'(.*) (use|using|has|contains|have|contain) (\"|\')(.*)(\"|\')(.*)',
  ['LET _%1 BE "%3"'],["Okay, %1 has %3"]]

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