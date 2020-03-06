# coding=utf-8
import sys
#print(sys.path)
sys.path.append('/home/admin1/Documents/tranX-master/')
import ast
from asdl.lang.py3.py3_transition_system import *
from asdl.hypothesis import *
import astor
from ast2json import ast2json
import json
from pprint import pprint

if __name__ == '__main__':
    # read in the grammar specification of Python 2.7, defined in ASDL
    asdl_text = open('/home/admin1/Documents/tranX-master/asdl/lang/py3/py3_asdl.simplified.txt').read()
    
    grammar = ASDLGrammar.from_text(asdl_text)

    py_code = """df=pandas.read('file.csv', nrows=100,header=False)"""

    # get the (domain-specific) python AST of the example Python code snippet
    py_ast = ast.parse(py_code)
    #print()
    #print (json.dumps(ast2json(py_ast), indent=1))
    #sys.exit()
    # convert the python AST into general-purpose ASDL AST used by tranX
    #pprint(grammar.__dict__)
    asdl_ast = python_ast_to_asdl_ast(py_ast.body[0], grammar)
    
    print("pyAst")
    #pprint(py_ast.body[0].__dict__)
    #print(py_ast.__dict__)
    #sys.exit()
    print('String representation of the ASDL AST: \n%s' % asdl_ast.to_string())
    print('Size of the AST: %d' % asdl_ast.size)

    # we can also convert the ASDL AST back into Python AST
    py_ast_reconstructed = asdl_ast_to_python_ast(asdl_ast, grammar)

    # initialize the Python transition parser
    #pprint(grammar.__dict__)
    #sys.exit()
    parser = Python3TransitionSystem(grammar)
    #pprint([x.__dict__ for x in list(parser.__dict__['grammar'].__dict__['type2id'].keys())])

    # get the sequence of gold-standard actions to construct the ASDL AST
    actions = parser.get_actions(asdl_ast)

    # a hypothesis is an (partial) ASDL AST generated using a sequence of tree-construction actions
    hypothesis = Hypothesis()
    for t, action in enumerate(actions, 1):
        # the type of the action should belong to one of the valid continuing types
        # of the transition system
        assert action.__class__ in parser.get_valid_continuation_types(hypothesis)

        # if it's an ApplyRule action, the production rule should belong to the
        # set of rules with the same LHS type as the current rule
        if isinstance(action, ApplyRuleAction) and hypothesis.frontier_node:
            assert action.production in grammar[hypothesis.frontier_field.type]

        p_t = hypothesis.frontier_node.created_time if hypothesis.frontier_node else -1
        print('t=%d, p_t=%d, Action=%s' % (t, p_t, action))
        hypothesis.apply_action(action)

    # get the surface code snippets from the original Python AST,
    # the reconstructed AST and the AST generated using actions
    # they should be the same
    src1 = astor.to_source(py_ast).strip()
    src2 = astor.to_source(py_ast_reconstructed).strip()
    src3 = astor.to_source(asdl_ast_to_python_ast(hypothesis.tree, grammar)).strip()
    print(src1,src2,src3)
    assert src1 == src2 == src3 == "pandas.read('file.csv', nrows=100, header=False)"
