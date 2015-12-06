# my_stats = {"name":"katherine","age":"23","height":"5'8"}
# #print "%s is %s years old with a height of %s." % (my_stats["name"],my_stats["age"],my_stats["height"]) 
# del my_stats["age"]
# print my_stats

#vocabulary_words = {"string":"a statement in quotes","int":"a whole number","float":"a number with a decimal","boolean":"a value that is true or false"}

# name = "katherine"
# for c in name:
#     print {c:name.count(c)}

# random_string = raw_input("type a random string: ")
# for c in random_string:
#     print {c:random_string.count(c)}
   
text_file = open("one_fish_two_fish.txt")
my_file = text_file.readlines()

for word in my_file:
    print {word:my_file.count(word)}

text_file.close()