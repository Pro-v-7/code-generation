   var antlr4 = require('antlr4');
   var JavaScriptBaseLexer = require('./JavaScriptBaseLexer').JavaScriptBaseLexer;
   var JavaScriptBaseParser = require('./JavaScriptBaseParser').JavaScriptBaseParser;
   var JavaScriptBaseListener = require('./JavaScriptBaseParserListener').JavaScriptBaseParserListener;

   var input = "var a=9"
   var chars = new antlr4.InputStream(input);
   var lexer = new JavaScriptBaseLexer(chars);
   var tokens  = new antlr4.CommonTokenStream(lexer);
   var parser = new JavaScriptBaseParser(tokens);
   console.log(parser)
   parser.buildParseTrees = true;
   var tree = parser.JavaScriptBaseStartRule();
