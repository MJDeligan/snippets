# open this python file in append mode and append a print statement
# the first time this is run it won't print anything
# the nth this is run it will print the text n-1 times
with open(__file__, "a") as f:
    f.write('\n    print("This won\'t print the first time you run this.")')
