from sys import argv

script, user_name = argv

prompt = "*"

print "Hello %s. Do not be afraid. I am the %s script." %(user_name, script)
print "Who is your favourite DC Comics character?"
dc = raw_input(prompt)
print "Understood. Can you analyse this statement?"
print "This statement is false."
ans = raw_input(prompt)
print "Nihilism or existentialism?"
phil = raw_input(prompt)

print """
All right. So you are named %s.
%s is your favourite DC Comics character.
You said %r about analysing paradoxes.
And you believe in %s, which means
you're an inexperienced douche.
""" %(user_name, dc, ans, phil)