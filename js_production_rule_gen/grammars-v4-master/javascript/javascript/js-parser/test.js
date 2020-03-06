const antlr4 = require('antlr4');
const JavaScriptLexer = require('./JavaScriptLexer.js');
const JavaScriptParser = require('./JavaScriptParser.js');

const input = `var a;`;

const chars = new antlr4.InputStream(input);
const lexer = new JavaScriptLexer.JavaScriptLexer(chars);

lexer.strictMode = false; // do not use js strictMode

const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new JavaScriptParser.JavaScriptParser(tokens);
const tree = parser.program();
console.log(tree)
//console.log(parser.ruleNames);
console.log(JSON.stringify(tree.toStringTree(parser.ruleNames)));

