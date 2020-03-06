const antlr4 = require('antlr4');
const ECMAScriptLexer = require('./ECMAScriptLexer.js');
const ECMAScriptParser = require('./ECMAScriptParser.js');
const fs = require('fs');

//const input = `var first = numbers.find(myFunction);`;
const input = `var first = numbers.find(myFunction);`;

const chars = new antlr4.InputStream(input);
const lexer = new ECMAScriptLexer.ECMAScriptLexer(chars);

lexer.strictMode = false; // do not use js strictMode

const tokens = new antlr4.CommonTokenStream(lexer);
const parser = new ECMAScriptParser.ECMAScriptParser(tokens);
const tree = parser.program();
//console.log(tree['children'][0]['children'][0]['children'][0]['children'][0]['children'][0]['parenttx']['children'])
//fs.writeFile('Output.txt', tree) 
//console.log((parser.ruleNames))
//console.log(parser.getTokenStream().tokens[0])
//console.log(tree.toString(parser.ruleNames))
//console.log(parser['_buildParseTrees']);
//console.log(Object.getOwnPropertyNames(parser))
//console.log(JSON.parse(tree.toStringTree()))
//console.log(tree.findAllNodes())
rules=JSON.stringify(tree.toStringTree(parser.ruleNames))
console.log(JSON.stringify(tree.toStringTree(parser.ruleNames),undefined, 4));
var rx2 = /\(([^)]+)\)/
console.log(rules.match(rx2))



