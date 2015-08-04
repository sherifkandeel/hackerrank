import re

def search(sen, s):
    if not sen: return "INVALID"
    for i in (sen.groups()):
        if i and len(i) == len(s):
            return "VALID"
    return "INVALID"

exp = "((CPP)|(JAVASCRIPT)|(OBJECTIVEC)|(JAVA)|(PYTHON)|(PERL)|(PHP)|(RUBY)|(CSHARP)|(HASKELL)|(CLOJURE)|(BASH)|(SCALA)|(ERLANG)|(CLISP)|(LUA)|(BRAINFUCK)|(OCAML)|(PASCAL)|(SBCL)|(DART)|(GROOVY)|(GO)|(C)|(D)|(R))"
n = int(raw_input())
for i in range(n):
    s = raw_input().split(' ')[1]
    sen = re.match(exp, s)
    print search(sen,s)
