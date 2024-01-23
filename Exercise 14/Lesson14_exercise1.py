# 1.Write a function in python to read the content from a text file "example.txt" line by line and display the same on screen.


with open("jein.txt", mode="w+", encoding="utf-8") as jein:
# with open("jein.txt", mode="a+", encoding="utf-8") as jein: այս դեպքում կավելանա, առաջինում՝ չէ

#jein=open("jein.txt", mode="a", encoding="utf-8")
    
    jein.write('''
Jane Eyre is divided into 38 chapters. It was originally published in three volumes in the 19th century, consisting of chapters 1 to 15, 16 to 27, and 28 to 38.

The second edition was dedicated to William Makepeace Thackeray.

The novel is a first-person narrative from the perspective of the title character. Its setting is somewhere in the north of England, late in the reign of George III (1760–1820).[a] It has five distinct stages: Jane's childhood at Gateshead Hall, where she is emotionally and physically abused by her aunt and cousins; her education at Lowood School, where she gains friends and role models but suffers privations and oppression; her time as governess at Thornfield Hall, where she falls in love with her mysterious employer, Edward Fairfax Rochester; her time in the Moor House, during which her earnest but cold clergyman cousin, St John Rivers, proposes to her; and ultimately her reunion with, and marriage to, her beloved Rochester. Throughout these sections it provides perspectives on a number of important social issues and ideas, many of which are critical of the status quo.

The five stages of Jane's life:

           ''')
    jein.readlines()

# jein.close()

print(jein)