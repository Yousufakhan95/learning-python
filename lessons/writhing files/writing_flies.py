

# the "a" means append
# the "w" means write the w is going erase what ever you have in and writ the new this
employee_file = open("writing_filles_test.txt", "w")
# this is going to add toby in to the doucment but rember you can add the same thing over and over again
# and it is going put this where you left off so you need to leave off at the next line over
# the back slash n is for a new line so you dont have add a new line evey time  you append
employee_file.write("\nToby - human resources")
employee_file.write("\nKelly - customer service")

employee_file.close()

# here we just created a new file called hello123.txt
hello = open("hello123.txt", "w")
# in this file it will open it
hello.write("hello testing")
hello.close()

# if your creating like a web site you will use this function alot
# because you can use differnt languages
# if you want to use another language just put index.language name
new = open("index.html", "w")
new.write("<p>This is HTML</p>")
new.close()

