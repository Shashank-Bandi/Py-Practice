import textwrap
s= '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.'''
print(s)

s_dedent = textwrap.dedent(s)
print(s_dedent)
s_wrapped = textwrap.fill(s_dedent,width=70)
print(s_wrapped)
s_final = textwrap.indent(s_wrapped,'>')
print(s_final)
