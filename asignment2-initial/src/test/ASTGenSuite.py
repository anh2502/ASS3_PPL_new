import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
#     def test_short_vardecl(self):
#         input = """x: integer;"""
#         expect = str(Program([VarDecl("x", IntegerType())]))
#         self.assertTrue(TestAST.test(input, expect, 300))

#     def test_full_vardecl(self):
#         input = """x, y, z: integer = 1, 2, 3;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 301))

#     def test_vardecls(self):
#         input = """x, y, z: integer = 1, 2, 3;
#         a, b: float;"""
#         expect = """Program([
# 	VarDecl(x, IntegerType, IntegerLit(1))
# 	VarDecl(y, IntegerType, IntegerLit(2))
# 	VarDecl(z, IntegerType, IntegerLit(3))
# 	VarDecl(a, FloatType)
# 	VarDecl(b, FloatType)
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 302))

#     def test_simple_program(self):
#         """Simple program"""
#         input = """main: function void () {
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 303))

#     def test_more_complex_program(self):
#         """More complex program"""
#         input = """main: function void () {
#             printInteger(4);
#         }"""
#         expect = """Program([
# 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 304))
#     def test305(self):
#         """More complex program"""
#         input = """
# foo: function void (inherit a: integer, inherit out b: float) inherit bar {}

# main: function void () {
#      printInteger(4);
# }"""
#         expect = """Program([
# \tFuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
# \tFuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
# ])"""
#         self.assertTrue(TestAST.test(input, expect, 305))

    def test_whilestmt_2(self):
        input = """main: function void (){
                    while(x<9){
                        a = a + 1;
                        _ = !x || (y == 0) && (z > 12.5E-6);
                    }
                }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(x), IntegerLit(9)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), AssignStmt(Id(_), BinExpr(&&, BinExpr(||, UnExpr(!, Id(x)), BinExpr(==, Id(y), IntegerLit(0))), BinExpr(>, Id(z), FloatLit(1.25e-05))))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))

