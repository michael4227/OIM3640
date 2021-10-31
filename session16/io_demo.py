# fout = open('data/output.txt', 'w')

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you call him a man?\n"
# fout.write(line2)

# fout.close()

# Context Manager, we don't need to close the file mannually
# So this is recommended
# with open('data/output.txt', 'w') as fout:
#     line1 = "How many roads must a man walk down\n"
#     fout.write(line1)

#     line2 = "Before you call him a man?\n"
#     fout.write(line2)

# error handling
try:
    f = open('data/output3.txt', 'r')
except:
    print("Something bad happened. No worries. We can still move on!")

print('Hello, world!')