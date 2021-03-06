#Token Definitions for Ada Language - http://en.wikibooks.org/wiki/Ada_Programming/Lexical_elements#Numbers

from reserved_Tokens import *

error_list = []

# List of token names.   This is always required
tokens = [
    'IDENTIFIER',
    'INTEGER',
    'BASE_INTEGER',
    'FLOAT',
    'BASE_FLOAT',
    'ARROW',
    'DOTDOT',
    'STARSTAR',
    'ASSIGNMENT',
    'NOTEQUAL',
    'GREATEREQ',
    'LESSEQ',
    'LESSLESS',
    'MOREMORE',
    'LESSMORE',
    'STRING',
    'CHAR',
    'TICK' #Special Token
] + list(reserved.values())

#Regular Expressions for Compound Delimiters
t_ARROW = r'=>'
t_DOTDOT = r'\.\.'
t_STARSTAR = r'\*\*'
t_ASSIGNMENT = r':='
t_NOTEQUAL = r'/='
t_GREATEREQ = r'>='
t_LESSEQ = r'<='
t_LESSLESS = r'<<'
t_MOREMORE = r'>>'
t_LESSMORE = r'<>'

#Regular expression rules for simple tokens - reference taken from http://en.wikibooks.org/wiki/Ada_Programming/Lexical_elements#Numbers

#we are assuming that ADA is a reserved word in programs. Most of the general libraries are like ada.text_IO and so on.

#Regular Expression Rules for identifiers
def t_IDENTIFIER(t):
    r'[A-Za-z](_?[A-Za-z0-9])*'
    t.type=reserved.get(t.value.lower(),'IDENTIFIER') #giving reserved words a higher priority
    return t

def t_CHAR(t):
    r'\'.\''  #Because in python dot matches any character except newline
    return t

def t_STRING(t):
    r'\"((\"\")|[^"])*\"' #Strings start and end with " only 
    return t

def t_TICK(t):
    r'\''
    return t

def t_FLOAT(t):
    r'(([0-9](_?[0-9]+)*(\.[0-9](_?[0-9]+)*)?)[eE]\-[0-9](_?[0-9]+)*)|([0-9](_?[0-9]+)*\.[0-9](_?[0-9]+)*)([eE][\+]?[0-9](_?[0-9]+)*)?'
#single character literals used as Operators or Delimiters
    t.value = float(t.value.replace("_",""))
    return t

#Integers in some other base
#We are not considering floating point numbers in some other base

def t_BASE_FLOAT(t):
    r'(0*[0-9]|1[0-6])\#((([0-9A-F](_?[0-9A-F]+)*(\.[0-9A-F](_?[0-9A-F]+)*)?)\#[eE]\-[0-9](_?[0-9]+)*)|([0-9A-F](_?[0-9A-F]+)*\.[0-9A-F](_?[0-9A-F]+)*)\#([eE][\+]?[0-9](_?[0-9]+)*)?)'
    #Exponents are in decimal base only. 
    t.value = t.value.replace("_", "")
    return t 

def t_BASE_INTEGER(t):
    r'(0*[2-9]|1[0-6])\#[0-9A-F](_?[0-9A-F]+)*\#([Ee](\+)?[0-9A-F](_?[0-9A-F]+)*)?'
    t.value = t.value.replace("_", "")
    return t 



def t_INTEGER(t):
    r'[0-9](_?[0-9]+)*([Ee](\+)?[0-9](_?[0-9]+)*)?'
    t.value = int(float(t.value.replace("_","")))
    return t

literals = "&()*+,-./:;<=>" # ' is removed from standard ada literals to allow characters to be interpretted


#The below definitions are not to be added to Tokens list.
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #Returns nothing

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_comment(t):
    r'--.*'
    #Returns nothing... Ignores the comment

# Error handling rule
def t_error(t):
    error_list.append("Line:" + str( t.lineno) + " illegal character '%s' found"% t.value[0])
    t.lexer.skip(1)

