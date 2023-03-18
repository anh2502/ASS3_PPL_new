# Generated from c:\Users\nguye\Downloads\asignment2-initial\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01df\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\5$\u0117\n$\3$\3$\3%\3%\3%\3%\7")
        buf.write("%\u011f\n%\f%\16%\u0122\13%\3%\3%\3%\3&\3&\3&\3&\7&\u012b")
        buf.write("\n&\f&\16&\u012e\13&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u0139\n\'\3(\3(\3(\7(\u013e\n(\f(\16(\u0141\13")
        buf.write("(\3(\7(\u0144\n(\f(\16(\u0147\13(\3(\6(\u014a\n(\r(\16")
        buf.write("(\u014b\7(\u014e\n(\f(\16(\u0151\13(\3(\5(\u0154\n(\3")
        buf.write(")\3)\3)\3)\3)\5)\u015b\n)\3)\3)\5)\u015f\n)\3)\3)\3*\3")
        buf.write("*\3*\7*\u0166\n*\f*\16*\u0169\13*\3*\7*\u016c\n*\f*\16")
        buf.write("*\u016f\13*\3*\6*\u0172\n*\r*\16*\u0173\7*\u0176\n*\f")
        buf.write("*\16*\u0179\13*\5*\u017b\n*\3+\3+\7+\u017f\n+\f+\16+\u0182")
        buf.write("\13+\3,\3,\5,\u0186\n,\3,\6,\u0189\n,\r,\16,\u018a\3-")
        buf.write("\5-\u018e\n-\3-\7-\u0191\n-\f-\16-\u0194\13-\3.\3.\3/")
        buf.write("\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\78\u01ac\n8\f8\16")
        buf.write("8\u01af\138\38\38\38\39\69\u01b5\n9\r9\169\u01b6\39\3")
        buf.write("9\3:\3:\7:\u01bd\n:\f:\16:\u01c0\13:\3:\5:\u01c3\n:\3")
        buf.write(":\3:\3;\3;\7;\u01c9\n;\f;\16;\u01cc\13;\3;\3;\3;\3<\3")
        buf.write("<\5<\u01d3\n<\3=\3=\3=\3>\3>\3>\5>\u01db\n>\3?\3?\3?\3")
        buf.write("\u0120\2@\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I\2K\2M&O\'Q(S\2U\2W\2Y)[*]+_,a-c.e/g\60i\61k\62m\63")
        buf.write("o\64q\65s\66u\67w\2y\2{\2}8\3\2\16\4\2\f\f\17\17\3\2\63")
        buf.write(";\3\2\62;\4\2GGgg\4\2--//\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\6\2\f\f\17\17$$")
        buf.write("^^\n\2$$))^^ddhhppttvv\3\2^^\2\u01f0\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2")
        buf.write("\2\2\2E\3\2\2\2\2G\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2}\3\2\2\2\3\177\3\2\2\2\5\u0085\3\2\2\2\7")
        buf.write("\u0088\3\2\2\2\t\u0090\3\2\2\2\13\u0096\3\2\2\2\r\u009d")
        buf.write("\3\2\2\2\17\u00a5\3\2\2\2\21\u00aa\3\2\2\2\23\u00b2\3")
        buf.write("\2\2\2\25\u00b6\3\2\2\2\27\u00bb\3\2\2\2\31\u00c4\3\2")
        buf.write("\2\2\33\u00c7\3\2\2\2\35\u00ca\3\2\2\2\37\u00cd\3\2\2")
        buf.write("\2!\u00cf\3\2\2\2#\u00d2\3\2\2\2%\u00d4\3\2\2\2\'\u00d7")
        buf.write("\3\2\2\2)\u00da\3\2\2\2+\u00dd\3\2\2\2-\u00df\3\2\2\2")
        buf.write("/\u00e1\3\2\2\2\61\u00e3\3\2\2\2\63\u00e5\3\2\2\2\65\u00e7")
        buf.write("\3\2\2\2\67\u00e9\3\2\2\29\u00ec\3\2\2\2;\u00f1\3\2\2")
        buf.write("\2=\u00f5\3\2\2\2?\u00fb\3\2\2\2A\u00fe\3\2\2\2C\u0104")
        buf.write("\3\2\2\2E\u010d\3\2\2\2G\u0116\3\2\2\2I\u011a\3\2\2\2")
        buf.write("K\u0126\3\2\2\2M\u0138\3\2\2\2O\u0153\3\2\2\2Q\u015e\3")
        buf.write("\2\2\2S\u017a\3\2\2\2U\u017c\3\2\2\2W\u0183\3\2\2\2Y\u018d")
        buf.write("\3\2\2\2[\u0195\3\2\2\2]\u0197\3\2\2\2_\u0199\3\2\2\2")
        buf.write("a\u019b\3\2\2\2c\u019d\3\2\2\2e\u019f\3\2\2\2g\u01a1\3")
        buf.write("\2\2\2i\u01a3\3\2\2\2k\u01a5\3\2\2\2m\u01a7\3\2\2\2o\u01a9")
        buf.write("\3\2\2\2q\u01b4\3\2\2\2s\u01ba\3\2\2\2u\u01c6\3\2\2\2")
        buf.write("w\u01d2\3\2\2\2y\u01d4\3\2\2\2{\u01da\3\2\2\2}\u01dc\3")
        buf.write("\2\2\2\177\u0080\7c\2\2\u0080\u0081\7t\2\2\u0081\u0082")
        buf.write("\7t\2\2\u0082\u0083\7c\2\2\u0083\u0084\7{\2\2\u0084\4")
        buf.write("\3\2\2\2\u0085\u0086\7q\2\2\u0086\u0087\7h\2\2\u0087\6")
        buf.write("\3\2\2\2\u0088\u0089\7k\2\2\u0089\u008a\7p\2\2\u008a\u008b")
        buf.write("\7v\2\2\u008b\u008c\7g\2\2\u008c\u008d\7i\2\2\u008d\u008e")
        buf.write("\7g\2\2\u008e\u008f\7t\2\2\u008f\b\3\2\2\2\u0090\u0091")
        buf.write("\7h\2\2\u0091\u0092\7n\2\2\u0092\u0093\7q\2\2\u0093\u0094")
        buf.write("\7c\2\2\u0094\u0095\7v\2\2\u0095\n\3\2\2\2\u0096\u0097")
        buf.write("\7u\2\2\u0097\u0098\7v\2\2\u0098\u0099\7t\2\2\u0099\u009a")
        buf.write("\7k\2\2\u009a\u009b\7p\2\2\u009b\u009c\7i\2\2\u009c\f")
        buf.write("\3\2\2\2\u009d\u009e\7d\2\2\u009e\u009f\7q\2\2\u009f\u00a0")
        buf.write("\7q\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3")
        buf.write("\7c\2\2\u00a3\u00a4\7p\2\2\u00a4\16\3\2\2\2\u00a5\u00a6")
        buf.write("\7c\2\2\u00a6\u00a7\7w\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\20\3\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7p\2\2\u00ac\u00ad\7j\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af")
        buf.write("\7t\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7v\2\2\u00b1\22")
        buf.write("\3\2\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\24\3\2\2\2\u00b6\u00b7\7x\2\2\u00b7\u00b8")
        buf.write("\7q\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba\7f\2\2\u00ba\26")
        buf.write("\3\2\2\2\u00bb\u00bc\7h\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7k\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7p\2\2\u00c3\30")
        buf.write("\3\2\2\2\u00c4\u00c5\7<\2\2\u00c5\u00c6\7<\2\2\u00c6\32")
        buf.write("\3\2\2\2\u00c7\u00c8\7?\2\2\u00c8\u00c9\7?\2\2\u00c9\34")
        buf.write("\3\2\2\2\u00ca\u00cb\7#\2\2\u00cb\u00cc\7?\2\2\u00cc\36")
        buf.write("\3\2\2\2\u00cd\u00ce\7>\2\2\u00ce \3\2\2\2\u00cf\u00d0")
        buf.write("\7>\2\2\u00d0\u00d1\7?\2\2\u00d1\"\3\2\2\2\u00d2\u00d3")
        buf.write("\7@\2\2\u00d3$\3\2\2\2\u00d4\u00d5\7@\2\2\u00d5\u00d6")
        buf.write("\7?\2\2\u00d6&\3\2\2\2\u00d7\u00d8\7(\2\2\u00d8\u00d9")
        buf.write("\7(\2\2\u00d9(\3\2\2\2\u00da\u00db\7~\2\2\u00db\u00dc")
        buf.write("\7~\2\2\u00dc*\3\2\2\2\u00dd\u00de\7-\2\2\u00de,\3\2\2")
        buf.write("\2\u00df\u00e0\7/\2\2\u00e0.\3\2\2\2\u00e1\u00e2\7,\2")
        buf.write("\2\u00e2\60\3\2\2\2\u00e3\u00e4\7\61\2\2\u00e4\62\3\2")
        buf.write("\2\2\u00e5\u00e6\7\'\2\2\u00e6\64\3\2\2\2\u00e7\u00e8")
        buf.write("\7#\2\2\u00e8\66\3\2\2\2\u00e9\u00ea\7k\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb8\3\2\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0\7g\2\2\u00f0:\3")
        buf.write("\2\2\2\u00f1\u00f2\7h\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4<\3\2\2\2\u00f5\u00f6\7y\2\2\u00f6\u00f7")
        buf.write("\7j\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9\7n\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa>\3\2\2\2\u00fb\u00fc\7f\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd@\3\2\2\2\u00fe\u00ff\7d\2\2\u00ff\u0100")
        buf.write("\7t\2\2\u0100\u0101\7g\2\2\u0101\u0102\7c\2\2\u0102\u0103")
        buf.write("\7m\2\2\u0103B\3\2\2\2\u0104\u0105\7e\2\2\u0105\u0106")
        buf.write("\7q\2\2\u0106\u0107\7p\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7k\2\2\u0109\u010a\7p\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7g\2\2\u010cD\3\2\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7v\2\2\u0110\u0111\7w\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7p\2\2\u0113F\3\2\2\2\u0114\u0117")
        buf.write("\5I%\2\u0115\u0117\5K&\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u0119\b$\2\2\u0119")
        buf.write("H\3\2\2\2\u011a\u011b\7\61\2\2\u011b\u011c\7,\2\2\u011c")
        buf.write("\u0120\3\2\2\2\u011d\u011f\13\2\2\2\u011e\u011d\3\2\2")
        buf.write("\2\u011f\u0122\3\2\2\2\u0120\u0121\3\2\2\2\u0120\u011e")
        buf.write("\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3\2\2\2\u0123")
        buf.write("\u0124\7,\2\2\u0124\u0125\7\61\2\2\u0125J\3\2\2\2\u0126")
        buf.write("\u0127\7\61\2\2\u0127\u0128\7\61\2\2\u0128\u012c\3\2\2")
        buf.write("\2\u0129\u012b\n\2\2\2\u012a\u0129\3\2\2\2\u012b\u012e")
        buf.write("\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("L\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0130\7v\2\2\u0130")
        buf.write("\u0131\7t\2\2\u0131\u0132\7w\2\2\u0132\u0139\7g\2\2\u0133")
        buf.write("\u0134\7h\2\2\u0134\u0135\7c\2\2\u0135\u0136\7n\2\2\u0136")
        buf.write("\u0137\7u\2\2\u0137\u0139\7g\2\2\u0138\u012f\3\2\2\2\u0138")
        buf.write("\u0133\3\2\2\2\u0139N\3\2\2\2\u013a\u0154\7\62\2\2\u013b")
        buf.write("\u013f\t\3\2\2\u013c\u013e\t\4\2\2\u013d\u013c\3\2\2\2")
        buf.write("\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u0140\u014f\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0144")
        buf.write("\7a\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0149\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0148\u014a\t\4\2\2\u0149\u0148\3")
        buf.write("\2\2\2\u014a\u014b\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c")
        buf.write("\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u0145\3\2\2\2\u014e")
        buf.write("\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2")
        buf.write("\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2\u0152\u0154\b")
        buf.write("(\3\2\u0153\u013a\3\2\2\2\u0153\u013b\3\2\2\2\u0154P\3")
        buf.write("\2\2\2\u0155\u0156\5S*\2\u0156\u0157\5U+\2\u0157\u015f")
        buf.write("\3\2\2\2\u0158\u015a\5S*\2\u0159\u015b\5U+\2\u015a\u0159")
        buf.write("\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c\3\2\2\2\u015c")
        buf.write("\u015d\5W,\2\u015d\u015f\3\2\2\2\u015e\u0155\3\2\2\2\u015e")
        buf.write("\u0158\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0161\b)\4\2")
        buf.write("\u0161R\3\2\2\2\u0162\u017b\7\62\2\2\u0163\u0167\t\3\2")
        buf.write("\2\u0164\u0166\t\4\2\2\u0165\u0164\3\2\2\2\u0166\u0169")
        buf.write("\3\2\2\2\u0167\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168")
        buf.write("\u0177\3\2\2\2\u0169\u0167\3\2\2\2\u016a\u016c\7a\2\2")
        buf.write("\u016b\u016a\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e\u0171\3\2\2\2\u016f\u016d")
        buf.write("\3\2\2\2\u0170\u0172\t\4\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("\u0173\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2")
        buf.write("\u0174\u0176\3\2\2\2\u0175\u016d\3\2\2\2\u0176\u0179\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178\3\2\2\2\u0178\u017b")
        buf.write("\3\2\2\2\u0179\u0177\3\2\2\2\u017a\u0162\3\2\2\2\u017a")
        buf.write("\u0163\3\2\2\2\u017bT\3\2\2\2\u017c\u0180\7\60\2\2\u017d")
        buf.write("\u017f\t\4\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2")
        buf.write("\u0180\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181V\3\2\2")
        buf.write("\2\u0182\u0180\3\2\2\2\u0183\u0185\t\5\2\2\u0184\u0186")
        buf.write("\t\6\2\2\u0185\u0184\3\2\2\2\u0185\u0186\3\2\2\2\u0186")
        buf.write("\u0188\3\2\2\2\u0187\u0189\t\4\2\2\u0188\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018a\u0188\3\2\2\2\u018a\u018b\3")
        buf.write("\2\2\2\u018bX\3\2\2\2\u018c\u018e\t\7\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0192\3\2\2\2\u018f\u0191\t\b\2\2\u0190")
        buf.write("\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0192\u0193\3\2\2\2\u0193Z\3\2\2\2\u0194\u0192\3\2\2")
        buf.write("\2\u0195\u0196\7*\2\2\u0196\\\3\2\2\2\u0197\u0198\7+\2")
        buf.write("\2\u0198^\3\2\2\2\u0199\u019a\7]\2\2\u019a`\3\2\2\2\u019b")
        buf.write("\u019c\7_\2\2\u019cb\3\2\2\2\u019d\u019e\7}\2\2\u019e")
        buf.write("d\3\2\2\2\u019f\u01a0\7\177\2\2\u01a0f\3\2\2\2\u01a1\u01a2")
        buf.write("\7=\2\2\u01a2h\3\2\2\2\u01a3\u01a4\7.\2\2\u01a4j\3\2\2")
        buf.write("\2\u01a5\u01a6\7?\2\2\u01a6l\3\2\2\2\u01a7\u01a8\7<\2")
        buf.write("\2\u01a8n\3\2\2\2\u01a9\u01ad\7$\2\2\u01aa\u01ac\5w<\2")
        buf.write("\u01ab\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01b0\u01b1\7$\2\2\u01b1\u01b2\b8\5\2\u01b2p")
        buf.write("\3\2\2\2\u01b3\u01b5\t\t\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01b9\b9\2\2\u01b9r\3\2\2\2")
        buf.write("\u01ba\u01be\7$\2\2\u01bb\u01bd\5w<\2\u01bc\u01bb\3\2")
        buf.write("\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf")
        buf.write("\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1")
        buf.write("\u01c3\t\n\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c5\b:\6\2\u01c5t\3\2\2\2\u01c6\u01ca\7$\2\2")
        buf.write("\u01c7\u01c9\5w<\2\u01c8\u01c7\3\2\2\2\u01c9\u01cc\3\2")
        buf.write("\2\2\u01ca\u01c8\3\2\2\2\u01ca\u01cb\3\2\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cd\u01ce\5{>\2\u01ce\u01cf")
        buf.write("\b;\7\2\u01cfv\3\2\2\2\u01d0\u01d3\n\13\2\2\u01d1\u01d3")
        buf.write("\5y=\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3x")
        buf.write("\3\2\2\2\u01d4\u01d5\7^\2\2\u01d5\u01d6\t\f\2\2\u01d6")
        buf.write("z\3\2\2\2\u01d7\u01d8\7^\2\2\u01d8\u01db\n\f\2\2\u01d9")
        buf.write("\u01db\n\r\2\2\u01da\u01d7\3\2\2\2\u01da\u01d9\3\2\2\2")
        buf.write("\u01db|\3\2\2\2\u01dc\u01dd\13\2\2\2\u01dd\u01de\b?\b")
        buf.write("\2\u01de~\3\2\2\2 \2\u0116\u0120\u012c\u0138\u013f\u0145")
        buf.write("\u014b\u014f\u0153\u015a\u015e\u0167\u016d\u0173\u0177")
        buf.write("\u017a\u0180\u0185\u018a\u018d\u0190\u0192\u01ad\u01b6")
        buf.write("\u01be\u01c2\u01ca\u01d2\u01da\t\b\2\2\3(\2\3)\3\38\4")
        buf.write("\3:\5\3;\6\3?\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    COMMENT = 35
    BOOLEAN = 36
    INTEGER = 37
    FLOAT = 38
    IDEN = 39
    LA = 40
    RA = 41
    LB = 42
    RB = 43
    LC = 44
    RC = 45
    SEMI = 46
    COMMA = 47
    EQUAL = 48
    COLON = 49
    STRINGLIT = 50
    WS = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'array'", "'of'", "'integer'", "'float'", "'string'", "'boolean'", 
            "'auto'", "'inherit'", "'out'", "'void'", "'function'", "'::'", 
            "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'if'", "'else'", 
            "'for'", "'while'", "'do'", "'break'", "'continue'", "'return'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", "'='", 
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "BOOLEAN", "INTEGER", "FLOAT", "IDEN", "LA", "RA", 
            "LB", "RB", "LC", "RC", "SEMI", "COMMA", "EQUAL", "COLON", "STRINGLIT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "COMMENT", "COM1", "COM2", "BOOLEAN", 
                  "INTEGER", "FLOAT", "INTPART", "DECPART", "EXPPART", "IDEN", 
                  "LA", "RA", "LB", "RB", "LC", "RC", "SEMI", "COMMA", "EQUAL", 
                  "COLON", "STRINGLIT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[38] = self.INTEGER_action 
            actions[39] = self.FLOAT_action 
            actions[54] = self.STRINGLIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[61] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTEGER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text=self.text.replace("_","")
     

    def FLOAT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text=self.text.replace("_","")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text=self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		y = str(self.text)
            		possible = [ '\n', '\r', '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


