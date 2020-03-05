const antlr4 = require('antlr4');
const ECMAScriptLexer = require('./ECMAScriptLexer.js');
const ECMAScriptParser = require('./ECMAScriptParser.js');

const input = `console.log(tree.toStringTree(parser.ruleNames));`;

const chars = new antlr4.InputStream(input);
const lexer = new ECMAScriptLexer.ECMAScriptLexer(chars);

lexer.strictMode = false; // do not use js strictMode

const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new ECMAScriptParser.ECMAScriptParser(tokens);
const tree = parser.program();
console.log(tree)
//console.log(parser.ruleNames);
console.log(JSON.stringify(tree.toStringTree(parser.ruleNames)));

