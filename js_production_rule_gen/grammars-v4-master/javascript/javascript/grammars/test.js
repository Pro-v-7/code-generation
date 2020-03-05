const fs = require('fs')
ast=fs.readFileSync('1.json', 'utf8');

var antlr4 = require('antlr4');
var MyGrammarLexer = require('./JavaScriptLexer').JavaScriptLexer;
var MyGrammarParser = require('./JavaScriptParser').JavaScriptParser;
var MyGrammarListener = require('./JavaScriptParserListener').JavaScriptParserListener;

var input = "var a=1;"
var chars = new antlr4.InputStream(input);
var lexer = new MyGrammarLexer(chars);
var tokens  = new antlr4.CommonTokenStream(lexer);
var parser = new MyGrammarParser(tokens);
//console.log(chars);
// console.log(CircularJSON.stringify(tokens)) 

parser.buildParseTrees = true;
//const tree = parser.expressionSequence();//console.log(tree)

console.log(JSON.parse(ast).toStringTree(parser.ruleNames));
