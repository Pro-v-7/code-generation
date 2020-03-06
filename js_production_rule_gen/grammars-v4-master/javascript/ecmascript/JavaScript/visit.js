var antlr4 = require('antlr4');
var MyGrammarLexer = require('./ECMAScriptLexer.js').ECMAScriptLexer;
var MyGrammarParser = require('./ECMAScriptParser').ECMAScriptParser;
var MyGrammarListener = require('./ECMAScriptListener').ECMAScriptListener;


var input = "field = 123 AND items in (1,2,3)"
var chars = new antlr4.InputStream(input);
var lexer = new MyGrammarLexer(chars);
var tokens = new antlr4.CommonTokenStream(lexer);
var parser = new MyGrammarParser(tokens);
parser.buildParseTrees = true;
var tree = parser.program();

class Visitor {
  visitChildren(ctx) {
    if (!ctx) {
      return;
    }

    if (ctx.children) {
      return ctx.children.map(child => {
        if (child.children && child.children.length != 0) {
          return child.accept(this);
        } else {
          return child.getText();
        }
      });
    }
  }
}

console.log(JSON.stringify(tree.accept(new Visitor())));

