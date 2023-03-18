grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: declist EOF ;
dec: vardec|fundec;
declist: dec| dec declist;
vardec: variables SEMI;
fundec: func;
//parser
arraytype: 'array' LB  (dimensions)? RB 'of' fourautotype;
dimensions: INTEGER| INTEGER COMMA dimensions;
arraylit: LC (expresslist|) RC;
fourautotype: 'integer' | 'float' | 'string' | 'boolean'| arraytype;
//voidtype
//autotype
//variables
variables: identifierlist ':' (fourautotype|'auto') | abc;// fix 
abc:		IDEN ':' (fourautotype|'auto') EQUAL expression | IDEN COMMA abc COMMA expression ;
//arr_: identifierlist ':' arraytype;//array
//arr_: IDEN ':' fourautotype EQUAL expression | IDEN COMMA abc COMMA expression ;//array
identifierlist: IDEN | IDEN COMMA identifierlist;
parameter: 'inherit'? 'out'? IDEN COLON fourautotype;
parameterlist: parameter|parameter COMMA parameterlist;
//function
re_type: fourautotype| 'void'|'auto';
func: IDEN COLON 'function' re_type LA (parameterlist|) RA ('inherit' IDEN)? (block_state) ;

expression : exp2 '::' exp2 | exp2;
exp2 : exp3 ('=='|'!='|'<' | '<=' | '>' | '>=') exp3 | exp3;
exp3 : exp3 ('&&'|'||') exp4 | exp4;
exp4 : exp4 ('+' | '-') exp5 | exp5;
exp5 : exp5 ('*'  | '/'|'%') exp6 | exp6;
exp6 : '!' exp6 | exp7 ;
exp7 : '-' exp7 | exp8 ;
exp8 : IDEN '[' expresslist ']' | exp9;
exp9 : element| (LA expression RA);
expresslist: expression | expression COMMA expresslist;
element: STRINGLIT | FLOAT | INTEGER | BOOLEAN|IDEN|arraylit|funcall;
//index_op
index_op: IDEN LB expresslist RB;
//funcall
funcall: IDEN LA (expresslist|) RA;
//statement
statement: ass_state| if_state|for_state|while_state|dowhile|break_state|continue_state|re_state|block_state|(funcall SEMI);
lhs: IDEN | index_op;//indexof
ass_state: lhs EQUAL expression SEMI;
if_state: 'if' LA (expression) RA (statement|block_state)
			('else' (statement|block_state))? ;
for_state: 'for' LA (IDEN|index_op) EQUAL INTEGER COMMA expression COMMA expression RA (statement|block_state);
while_state: 'while' LA expression RA (statement|block_state);
dowhile: 'do' (block_state)
		'while' LA expression RA SEMI;
break_state: 'break' SEMI;
continue_state: 'continue' SEMI;
re_state: 'return' (element|expression|) SEMI;
block_element: vardec| statement;
block_: block_element| block_element block_;
block_state: LC 
				(block_|)
			RC;
// lexer
// comment
COMMENT: (COM1 | COM2) -> skip;
fragment COM1: '/*' .*? '*/';
fragment COM2:'//' (~[\r\n])*;
//key word
// KEYWORD:'auto' | 'break' | 'boolean' | 'do' | 'else'
// 		| 'float' | 'for' | 'function' | 'if'
// 		| 'integer' | 'return' | 'string' | 'while'
// 		| 'void' | 'out' | 'continue' | 'of' | 'inherit' | 'array';
//bool
BOOLEAN: 'true'|'false';
//int---done
INTEGER:  '0'
			| [1-9] [0-9]*('_'* [0-9]+)*{self.text=self.text.replace("_","")};
//float---done
FLOAT: (INTPART DECPART | INTPART DECPART? EXPPART ) {self.text=self.text.replace("_","")};

fragment INTPART : '0'
			| [1-9] [0-9]*('_'* [0-9]+)*;
fragment DECPART : '.' [0-9]*;
fragment EXPPART : [eE] ('+'|'-')? [0-9]+;
//identifiers - done
IDEN: (([A-Za-z] | '_') ([A-Za-z] | '_'|[0-9])*);
//fragment KEYW: ['true', 'false'];

//seperator
LA: '(';
RA: ')';
LB: '[';
RB: ']';
LC: '{';
RC: '}';
//DOT: '.';
SEMI: ';';
COMMA: ',';
EQUAL: '=';
COLON: ':';
//String---done
STRINGLIT : '"' STR_CHAR* '"' {self.text=self.text[1:-1]};
//array// chua xong-----------------------------exx-press


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = [ '\n', '\r', '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;
// possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		// if y[-1] in possible:
		// 	raise UncloseString(y[1:-1])
		// else:
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;
//fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
fragment STR_CHAR: ~["\\\n\r] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
// fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;

// fragment ESC_SEQ: '\\' [btnfr"'\\] ;
// fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;
ERROR_CHAR: . {raise ErrorToken(self.text)};