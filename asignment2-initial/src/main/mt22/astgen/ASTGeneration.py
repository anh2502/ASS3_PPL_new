from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
class ASTGeneration(MT22Visitor):
    #program: declist EOF ;
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.declist()))
    #dec: vardec|fundec;
    def visitDec(self, ctx: MT22Parser.DecContext):
            if ctx.vardec():
                return self.visit(ctx.vardec())
            return self.visit(ctx.fundec())
    # declist: dec| dec declist;
    def visitDeclist(self, ctx: MT22Parser.DeclistContext):
        temp = self.visit(ctx.dec())
        if ctx.getChildCount()==1:
            return temp if isinstance(temp,list) else [temp]
        if isinstance(temp,list):
            return self.visit(ctx.dec()) + self.visit(ctx.declist())
        return [self.visit(ctx.dec())] + self.visit(ctx.declist())
    # vardec: variables SEMI;
    def visitVardec(self, ctx: MT22Parser.VardecContext):
        return self.visit(ctx.variables())
    # fundec: func;
    def visitFundec(self, ctx: MT22Parser.FundecContext):
        return self.visit(ctx.func())
    #arraytype: 'array' LB  (dimensions)? RB 'of' fourautotype;
    def visitArrayType(self, ctx: MT22Parser.ArraytypeContext):
        typ = self.visit(ctx.fourautotype())
        dimen = self.visit(ctx.dimensions())
        return ArrayType(dimen, typ)
    # dimensions: INTEGER| INTEGER COMMA dimensions;
    def visitDimensions(self, ctx: MT22Parser.DimensionsContext):
        if ctx.getChildCount()==1:
            return [IntegerLit(int(ctx.INTEGER(0).getText()))]
        return [IntegerLit(int(ctx.INTEGER(0).getText()))] + self.visit(ctx.dimensions())
    #arraylit: LC (expresslist|) RC;
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        if ctx.getChildCount==2:
            return ArrayLit([])
        return ArrayLit(self.visit(ctx.expresslist()))
    # fourautotype: 'integer' | 'float' | 'string' | 'boolean'| arraytype;
    def visitFourautotype(self, ctx: MT22Parser.FourautotypeContext):
        if ctx.arraytype():
            return self.visit(ctx.arraytype())
        temp = ctx.getChild(0).getText()
        if temp=='integer':
            return IntegerType()
        elif temp=='float':
            return FloatType()
        elif temp=='string':
            return StringType()
        elif temp=='boolean':
            return BooleanType()
    # variables: identifierlist ':' (fourautotype|'auto') | abc;// fix 
    def visitVariables(self, ctx: MT22Parser.VariablesContext):
        if ctx.abc():
            abc=self.visit(ctx.abc())
            idenlist=abc[0]
            typ=abc[1][-1]
            exp=abc[2]
            exp=reversed(exp)
            return list(map(lambda x,y: VarDecl(x,typ,y), idenlist, exp))
        idenlist=self.visit(ctx.identifierlist())
        typ = None
        if ctx.fourautotype():
            typ = self.visit(ctx.fourautotype())
        else: typ=AutoType()
        return list(map(lambda x : VarDecl(x, typ), idenlist))
    # abc:		IDEN ':' (fourautotype|'auto') EQUAL expression | IDEN COMMA abc COMMA expression ;
    def visitAbc(self, ctx: MT22Parser.AbcContext):
        # if ctx.fourautotype():
        #     typ = self.visit(ctx.fourautotype())
        #     print('1****1')
        # else: typ=AutoType()
        #typ=None
        if ctx.abc():
            temp = self.visit(ctx.abc())
            return ([ctx.IDEN()] + temp[0],[]+temp[1],[self.visit(ctx.expression())] + temp[2]) 
        else:
            if ctx.fourautotype():
                typ = self.visit(ctx.fourautotype())
            else: typ=AutoType()
            return ([ctx.IDEN()] , [typ] ,[self.visit(ctx.expression())] ) 
    # def get(self, ctx: MT22Parser.AbcContext):
    #     if ctx.abc():
    #         return [ctx.IDEN().getText()] + self.visit(ctx.getstr())
    #     return [ctx.IDEN().getText()]
    # identifierlist: IDEN | IDEN COMMA identifierlist;
    def visitIdentifierlist(self, ctx: MT22Parser.IdentifierlistContext):
        if ctx.getChildCount()==1:
            return [(ctx.IDEN().getText())]
        else:
            return [(ctx.IDEN().getText())] + self.visit(ctx.identifierlist())
    # parameter: 'inherit'? 'out'? IDEN COLON fourautotype;
    def visitParameter(self, ctx: MT22Parser.ParameterContext):
        temp=ctx.getChild(0).getText()
        out=False
        inher=False
        if temp=='inherit':
            inher=True
            temp2=ctx.getChild(1).getText()
            if temp2=='out':
                out=True
        if temp=='out':
            out=True
        iden=ctx.IDEN().getText()
        typ=self.visit(ctx.fourautotype())
        return ParamDecl(iden, typ,out,inher)
    # parameterlist: parameter|parameter COMMA parameterlist;
    def visitParameterlist(self, ctx: MT22Parser.ParameterlistContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())] + self.visit(ctx.parameterlist())
    # re_type: fourautotype| 'void'|'auto';
    def visitRe_type(self, ctx: MT22Parser.Re_typeContext):
        if ctx.fourautotype():
            return self.visit(ctx.fourautotype())
        else:
            temp=ctx.getChild(0).getText()
        if temp=='void':
            return VoidType()
        elif temp=='auto':
            return AutoType()
    # func: IDEN COLON 'function' re_type LA (parameterlist|) RA ('inherit' IDEN)? (block_state) ;
    def visitFunc(self, ctx: MT22Parser.FuncContext):
        name=ctx.IDEN(0).getText()
        typ=self.visit(ctx.re_type())
        if ctx.parameterlist():
            param=self.visit(ctx.parameterlist())
        else: 
            param=[]
        block=self.visit(ctx.block_state())
        if len(ctx.IDEN())==2:
            name2=ctx.IDEN(1).getText()
            return FuncDecl(name,typ,param,name2,block)
        return FuncDecl(name,typ,param,None,block)    
    # expression : exp2 '::' exp2 | exp2;
    def visitExpression(self, ctx: MT22Parser.ExpressionContext):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp2(0))
        else:
            left=self.visit(ctx.getChild(0))
            right=self.visit(ctx.getChild(2))
            return BinExpr('::',left,right)
    #exp2 : exp3 ('=='|'!='|'<' | '<=' | '>' | '>=') exp3 | exp3;
    def visitExp2(self, ctx: MT22Parser.Exp2Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp3(0))
        else:
            op=ctx.getChild(1).getText()
            left=self.visit(ctx.getChild(0))
            right=self.visit(ctx.getChild(2))
            return BinExpr(op,left,right)
    #exp3 : exp3 ('&&'|'||') exp4 | exp4;
    def visitExp3(self, ctx: MT22Parser.Exp3Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp4())
        else:
            op=ctx.getChild(1).getText()
            left=self.visit(ctx.getChild(0))
            right=self.visit(ctx.getChild(2))
            return BinExpr(op,left,right)
    # exp4 : exp4 ('+' | '-') exp5 | exp5;
    def visitExp4(self, ctx: MT22Parser.Exp4Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp5())
        else:
            op=ctx.getChild(1).getText()
            left=self.visit(ctx.getChild(0))
            right=self.visit(ctx.getChild(2))
            return BinExpr(op,left,right)
    # exp5 : exp5 ('*'  | '/'|'%') exp6 | exp6;
    def visitExp5(self, ctx: MT22Parser.Exp5Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp6())
        else:
            op=ctx.getChild(1).getText()
            left=self.visit(ctx.getChild(0))
            right=self.visit(ctx.getChild(2))
            return BinExpr(op,left,right)
    # exp6 : '!' exp6 | exp7 ;
    def visitExp6(self, ctx: MT22Parser.Exp6Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp7())
        else:
            op=ctx.getChild(0).getText()
            val=self.visit(ctx.getChild(1))
            return UnExpr(op,val)
    # exp7 : '-' exp7 | exp8 ;
    def visitExp7(self, ctx: MT22Parser.Exp7Context):
        if ctx.getChildCount()==1:
            return self.visit(ctx.exp8())
        else:
            op=ctx.getChild(0).getText()
            val=self.visit(ctx.getChild(1))
            return UnExpr(op,val)
    # exp8 : IDEN '[' expresslist ']' | exp9;
    def visitExp8(self, ctx: MT22Parser.Exp8Context):
        if ctx.IDEN():
            name=ctx.IDEN()
            cell= self.visit(ctx.expresslist())
            return ArrayCell(name, cell)
        else:
            return self.visit(ctx.exp9())
    # exp9 : element| (LA expression RA);
    def visitExp9(self, ctx: MT22Parser.Exp9Context):
        if ctx.element():
            return self.visit(ctx.element())
        else:
            return self.visit(ctx.expression())
    # expresslist: expression | expression COMMA expresslist;
    def visitExpresslist(self, ctx: MT22Parser.ExpresslistContext):
        if ctx.getChildCount()==1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.expresslist())
    # element: STRINGLIT | FLOAT | INTEGER | BOOLEAN|IDEN|arraylit|funcall;
    def visitElement(self, ctx: MT22Parser.ElementContext):
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.FLOAT():
            return FloatLit(float(ctx.FLOAT().getText()))
        elif ctx.INTEGER():
            return IntegerLit(ctx.INTEGER().getText())
        elif ctx.BOOLEAN():
            return BooleanLit(ctx.BOOLEAN().getText())
        elif ctx.IDEN():
            return Id(ctx.IDEN().getText())
        elif ctx.arraylit():
            return self.visit(ctx.arraylit())
        elif ctx.funcall():
            return self.visit(ctx.funcall())
    ################################
    # index_op: IDEN LB expresslist RB;
    def visitIndex_op(self, ctx: MT22Parser.Index_opContext):
        name=ctx.IDEN().getText()
        cell=self.visit(ctx.expesslist())
        return ArrayCell(name, cell)
    # //funcall
    # funcall: IDEN LA (expresslist|) RA;
    def visitFuncall(self, ctx: MT22Parser.FuncallContext):
        name=ctx.IDEN().getText()
        if ctx.getChildCount==3:
            return FuncCall(name, [])
        cell=self.visit(ctx.expresslist())
        return FuncCall(name, cell)
    # //statement
    # statement: ass_state| if_state|for_state|while_state|dowhile|break_state|continue_state|re_state|block_state|(funcall SEMI);
    def visitStatement(self, ctx: MT22Parser.StatementContext):
        if ctx.ass_state():
            return self.visit(ctx.ass_state())
        elif ctx.if_state():
            return self.visit(ctx.if_state())
        elif ctx.for_state():
            return self.visit(ctx.for_state())
        elif ctx.while_state():
            return self.visit(ctx.while_state())
        elif ctx.dowhile():
            return self.visit(ctx.dowhile())
        elif ctx.break_state():
            return self.visit(ctx.break_state())
        elif ctx.continue_state():
            return self.visit(ctx.re_state())
        elif ctx.block_state():
            return self.visit(ctx.block_state())
        elif ctx.funcall():
            temp= self.visit(ctx.funcall())
            name=temp.name
            arg=temp.args
            return CallStmt(name,arg)
    # lhs: IDEN | index_op;//indexof
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        if ctx.IDEN():
            return Id(ctx.IDEN().getText())    
        return self.visit(ctx.index_op())
    # ass_state: lhs EQUAL expression SEMI;
    def visitAss_state(self, ctx: MT22Parser.Ass_stateContext):
        lhs=self.visit(ctx.lhs())
        rhs=self.visit(ctx.expression())
        return AssignStmt(lhs,rhs)
    # if_state: 'if' LA (expression) RA (statement|block_state)
    #             ('else' (statement|block_state))? ;
    def visitIf_state(self, ctx: MT22Parser.If_stateContext):
        con=self.visit(ctx.expression())
        tstmt=self.visit(ctx.getChild(4))
        if ctx.getChildCount()==5:
            return IfStmt(con,tstmt)
        fstmt=self.visit(ctx.getChild(6))
        return IfStmt(con,tstmt,fstmt)
    # for_state: 'for' LA (IDEN|index_op) EQUAL INTEGER COMMA expression COMMA expression RA (statement|block_state);
    def visitFor_state(self, ctx: MT22Parser.For_stateContext):
        if ctx.IDEN():
            lhs=Id(ctx.IDEN().getText())  
        elif ctx.index_op():
            lhs=self.visit(ctx.index_op)
        rhs=ctx.INTEGER()
        assign=AssignStmt(lhs,rhs)
        cond=self.visit(ctx.getChild(6))
        upd=self.visit(ctx.getChild(8))
        stmt=self.visit(ctx.getChild(10))
        return ForStmt(assign,cond,upd,stmt)
    # while_state: 'while' LA expression RA (statement|block_state);
    def visitWhile_state(self, ctx: MT22Parser.While_stateContext):
        cond=self.visit(ctx.expression())
        stmt=self.visit(ctx.getChild(4))
        return WhileStmt(cond,stmt)
    # dowhile: 'do' (block_state)
    #         'while' LA expression RA SEMI;
    def visitDowhile(self, ctx: MT22Parser.DowhileContext):
        cond=self.visit(ctx.expression())
        stmt=self.visit(ctx.block_state())
        return DoWhileStmt(cond,stmt)
    # break_state: 'break' SEMI;
    def visitBreak_state(self, ctx: MT22Parser.Break_stateContext):
        return BreakStmt()
    # continue_state: 'continue' SEMI;
    def visitContinue_state(self, ctx: MT22Parser.Continue_stateContext):
        return ContinueStmt()
    # re_state: 'return' (element|expression|) SEMI;
    def visitRe_state(self, ctx: MT22Parser.Re_stateContext):
        if ctx.getChildCount()==2:
            return ReturnStmt()
        exp=self.visit(ctx.getChild(1))
        return ReturnStmt(exp)
    # block_element: vardec| statement;
    def visitBlock_element(self, ctx: MT22Parser.Block_elementContext):
        if(ctx.vardec()):
            return self.visit(ctx.vardec())
        return [self.visit(ctx.statement())]
    # block_: block_element| block_element block_;
    def visitBlock_(self, ctx: MT22Parser.Block_Context):
        if ctx.block_():
            return self.visit(ctx.block_element())+ self.visit(ctx.block_())
        return self.visit(ctx.block_element())
    # block_state: LC 
    #                 (block_|)
    #             RC;
    def visitBlock_state(self, ctx: MT22Parser.Block_stateContext):
        if ctx.block_():
            return BlockStmt(self.visit(ctx.block_()))
        return BlockStmt([])