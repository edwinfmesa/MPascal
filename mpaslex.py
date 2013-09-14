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
#    '\"':"QUOTESCAPE", # USED ON STRING
#    '\n':"NLSCAPE", # NEWLINE SCAPE
#    '\\':"BSSCAPE", # BACKSLASH SCAPE
    }

tokens =[
    "ID",
    "LPARENT",
    "RPARENT",
    "LBRACKET",
    "RBRACKET",
    "COLON",
    "SEMICOLON",
    "COMA",
    "PLUS",
    "MINUS",
    "MULTIPLICATION",
    "DIVISION",
    "LT", # LESS THAN
    "GT", # GREATER THAN
    "EQUAL",
    "LTE", # LESS THAN OR EQUAL TO
    "GTE", # GREATER THAN OR EQUAL TO
    "NE", # NOT EQUAL TO
    "ASSIGN",
    "DOT",
    "INTNUMBER",
    "FLOATNUMBER",    
    "STRING",
    "COMMENT",
    
    ]+ list(reserved.values())

# REGULAR EXPRESSION RULES

# simple tockens

t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r':'
t_SEMICOLON = r';'
t_COMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_LT = r'<'
t_GT = r'>'
t_EQUAL = r'='
t_LTE = r'<='
t_GTE = r'>='
t_NE = r'!='
t_ASSIGN = r':='
t_DOT = r'\.'

# Complex tockens
def t_COMMENT(t):
    r'/[*](.|\n)*?[*]/'
    return t

def t_ID(t):                 ##RECORDAR CORREGIR ESTE, SI LONG>20 RECORTAR
    r'((_)|([A-Za-z]))(\w)*'
    s = str(t.value)[:21]
    t.type = reserved.get(s.lower(), 'ID')
    return t

def t_STRING(t):
    r'\"([^\\^\n] |(\\.))*\"'
    return t

def t_FLOATNUMBER(t):
    r'(((-)?(\d+\.\d+)([e|E][+-]?\d+)?)|(\d+[e|E][+-]?\d+))'
    t.value = float(t.value)
    return t

def t_error_IDNUMBER(t):
   r' \d+[A-Za-z_](.*)'
   print "Error: the identifier cannot begin with numbers: ", t.value," Line:", t.lineno
   t.lexer.skip(1)

def t_INTNUMBER(t):
    r'((-)?[0-9]+)'
    t.value = int(t.value)
    return t


    
    
#t_QUOTESCAPE = r''
#t_NLSCAPE = r''
#t_BSSCAPE = r''

def t_error_COMENTARIOC(t):
    r'/\*(.|\n)*'
    print ("Invalid comment: ", t.value[0:7])
    print ("Line: ", t.lineno)
    t.lexer.skip(1)

def t_error_STRING(t):
    r'\".*'
    print ("Error: with string: ", t.value, " Line: ", t.lineno)
    t.lexer.skip(1)
    
## Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Invalid character '%s'" % t.value[0]," Linea numero: " %t.lexer.lineno)
    t.lexer.skip(1)
    
import msvcrt as m
def wait():
    m.getch()
        
for i in range(1, 13):
    f = open('test/test'+str(i)+'.txt','r')    #Load test file.
    s = f.read()                #Read the text of the file
    print "\n\n --------------------CODE TEST # "+str(i)+"------------------------\n\n",s
    lexico = lex.lex()
    lexico.input(s)
    print "\n\n --------------------RETURN------------------------\n\n"
    try:
        while True:
            tokenizer = lexico.token()
            if not tokenizer: break
            print tokenizer
    except:
        print "Unknown ERROR"
    f.close()
    print("\n Please press any key... ")
    wait()
    


