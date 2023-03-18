# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dec.
    def visitDec(self, ctx:MT22Parser.DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declist.
    def visitDeclist(self, ctx:MT22Parser.DeclistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardec.
    def visitVardec(self, ctx:MT22Parser.VardecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fundec.
    def visitFundec(self, ctx:MT22Parser.FundecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytype.
    def visitArraytype(self, ctx:MT22Parser.ArraytypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimensions.
    def visitDimensions(self, ctx:MT22Parser.DimensionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fourautotype.
    def visitFourautotype(self, ctx:MT22Parser.FourautotypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#variables.
    def visitVariables(self, ctx:MT22Parser.VariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#abc.
    def visitAbc(self, ctx:MT22Parser.AbcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifierlist.
    def visitIdentifierlist(self, ctx:MT22Parser.IdentifierlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameterlist.
    def visitParameterlist(self, ctx:MT22Parser.ParameterlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#re_type.
    def visitRe_type(self, ctx:MT22Parser.Re_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func.
    def visitFunc(self, ctx:MT22Parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp9.
    def visitExp9(self, ctx:MT22Parser.Exp9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expresslist.
    def visitExpresslist(self, ctx:MT22Parser.ExpresslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element.
    def visitElement(self, ctx:MT22Parser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_op.
    def visitIndex_op(self, ctx:MT22Parser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall.
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ass_state.
    def visitAss_state(self, ctx:MT22Parser.Ass_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_state.
    def visitIf_state(self, ctx:MT22Parser.If_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_state.
    def visitFor_state(self, ctx:MT22Parser.For_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_state.
    def visitWhile_state(self, ctx:MT22Parser.While_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhile.
    def visitDowhile(self, ctx:MT22Parser.DowhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_state.
    def visitBreak_state(self, ctx:MT22Parser.Break_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_state.
    def visitContinue_state(self, ctx:MT22Parser.Continue_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#re_state.
    def visitRe_state(self, ctx:MT22Parser.Re_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_element.
    def visitBlock_element(self, ctx:MT22Parser.Block_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_.
    def visitBlock_(self, ctx:MT22Parser.Block_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_state.
    def visitBlock_state(self, ctx:MT22Parser.Block_stateContext):
        return self.visitChildren(ctx)



del MT22Parser