print("Lets practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs")


poem = """
\t The lovely world
with logic so firmly planted
cannot discern(rozeznac) \n the needs of love
not comprehend passion from intuition
and requires and explanation
\n\t where there is none
"""

print("-----------")
print(poem)
print("-----------")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)  #another way to format string

print("With a starting point f: {}".format(start_point))
print(f"We 'd have {beans} beans, {jars} jars, and {crates} creates")

start_point = start_point/10

print("We can also do that this way")
formula = secret_formula(start_point)
print("We 'd have {} beans, {} jars, and {} creates".format(beans, jars, crates))


