# Given two dictionaries, merge them into a new dictionary, excluding any keys that start with an underscore.

dictionary1={"k":158, "d":40, "m":80, "_k":200}
dictionary2={"g":158, "l":40, "_m":80, "n":200}
dictionary2.update(dictionary1)

new_dic={x: y for x,y in dictionary2.items() if x[0]!="_"}
print(new_dic)