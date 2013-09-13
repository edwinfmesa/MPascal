import ply.lex as lex

# class MPascalLexer:
# LIST OF TOCKEN NAMES
reserved ={
    'float':'FLOAT',
    'if':'IF',
    'then':'THEN',
    'else':'ELSE',
    'int':'INT',
    'do':'DO',
    'begin':'BEGIN',
    'print':'PRINT',
    'write':'WRITE',
    'read':'READ',
    'break':'BREAK',
    'return':'RETURN',
    'and':'AND',
    'or':'OR',
    'not':'NOT',
    'fun':'FUN',
    'skip':'SKIP',
    'while':'WHILE',
    'end':'END',
    }

tokens =[
    "LPARENT",
    "RESERVED",
#    "RPARENT",
#    "LBRACKET",
#    "RBRACKET",
#    "COLON",
#    "SEMICOLON",
#    "COMA",
#    "PLUS",
#    "MINUS",
#    "MULTIPLICATION",
#    "DIVISION",
#    "LT", # LESS THAN
#    "GT", # GREATER THAN
#    "EQUALS",
#    "LTE", # LESS THAN OR EQUAL TO
#    "GTE", # GREATER THAN OR EQUAL TO
#    "NE", # NOT EQUAL TO
#    "ASSIGN",
#    "ID",
#    "INTNUMBER",
#    "FLOATNUMBER",    
#    "STRING",
#    "QUOTESCAPE", # USED ON STRING
#    "NLSCAPE", # NEWLINE SCAPE
#    "BSSCAPE", # BACKSLASH SCAPE
#    "COMMENT"
    ]+ list(reserved.values())

# REGULAR EXPRESSION RULES

# simple tockens
#
t_LPARENT = '\('

# A regular expression rule with some action code
def t_RESERVED(t):                 ##RECORDAR CORREGIR ESTE, SI LONG>20 RECORTAR
    r'(_){0,1}[A-Z a-z]{1}[A-Z a-z 0-9 _]{1,18}'
    t.type = reserved.get(t.value, 'RESERVED')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Caracter no permitido '%s'" % t.value[0]," Linea numero: " %t.lexer.lineno)
    t.lexer.skip(1)
    
data = "if ("
    
lexico = lex.lex()
lexico.input(data)

while True:
    tokenizer = lexico.token()
    if not tokenizer: break
    print tokenizer