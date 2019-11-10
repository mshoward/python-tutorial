"""
This will be the entry point for our program.
Purpose:  Our program will output 'Hello, World!' when ran
How to run this program:  Python programs are run through the interpreter
                          To run our program, we'll execute the following line,
                          'python tutorial.py', on the command line.
"""

"""
Three double quotes indicate the beginning of a multi line string in python.
A string is series of characters.  A character is a piece of data that has to do
with language.  As an example, this is a string.  In python, these multi line
strings are frequently used as documentation comments to explain the code, both
to yourself and to others.
"""

# this line is commented. The first non-whitespace character in a line is a '#'.
# whitespace are things like spaces, or the character(s) that indicate a new
# line.

# this is the main function that will be called with the program is run
def main():
    """
    def is short for 'define' or 'definition' - I'm not sure which.  
    It's what's called a keyword in the programming language, which just means
    it has special meaning.  In this case, it's saying to the interpreter "hey,
    this is a function definition, its name is the next word, what it does is in
    the indented block below me".
    
    A function definition consists of the following syntax.
    
    def function_name(parameter_one, another_parameter):
        # function body
    
    You'll see a lot of people whine and complain about how picky python is
    about indentation, but if edit files in a code editor that renders
    whitespace as little dots, and you use consistent indentation,
    you shouldn't have any issues.  I use 4 spaces as an indentation level
    and just try to format things neatly, not really worrying about how much
    vertical space it takes up.  I try to keep lines less than 80 characters
    long, no more than like 85 or so.
    """
    
    """
    In python, there are a number of built in functions - these do no have to be
    imported, they are already / always accessible.  The one we're using here is
    the print function.  print() takes any number of variables, and outputs them
    to its output stream.  Its default output stream is standard out.

    An output stream is something you can write to.  I don't know why it's
    called a stream.  You put things in it, it has an internal buffer that holds
    the things, and it either flushes (writes everything in the buffer to the
    output and resets the buffer) automatically, or you manually call the flush.
    idk I guess it flushes stuff down the stream.
    
    Standard out is the standard output stream handed to programs when they're
    run.  Every program has a standard out.  It's usually rendered to your 
    screen, sometimes it's passed to another program as 'standard input'.  
    Standard input / standard in is the same thing but for input.  You read 
    from it.
    """
    print('Hello, World!')  # pass the 'Hello, World!' string to print to be 
                            # printed to standard out
    
    """
    functions return things.  Always.  That's what they do.  They take an input,
    in this function's case, nothing, and return an output.
    In mathy terms, they map input to output.
    
    In python, functions always return something, even if you don't specify 
    anything.  If you don't specify anything, they return the special value, 
    None.  None signifies some semi-tangible 'nothing', an absence of data,
    the abyss in which the zalgo waits and watches.  It is a void, a complete
    absence of anything - it is None.  So, I return other things, because then,
    I can check it and I know what happened.
    
    In this case we're returning 0, an int, or integer.  Integers are numbers.
    Numbers are things you can do math on.  You can do math on other things as 
    well, but the further from numbers you go, the closer the Zalgo watches. As 
    a rule, we try not to draw the attention of the Zalgo.  Doing math on things
    that aren't meant for math is a good way to unleash the Zalgo if you're not
    paying close attention, and we try not to do that.
    """
    return 0

"""
This is an if statement. If statements consist of the following syntax:

if some_condition:
    # stuff that's executed if the condition evaluates to True.

Python has quite a few weird rules for conditionals and what it deems to be 
True or not.  We'll explore those more later.  For now, I'll explain each of
the things in the condition and explore it more later.

  __name__ is a special built-in variable name that refers to the name of the 
current program being run.  Think of variables as buckets that hold data 
instead of water, and the buckets have names.
  '__main__' refers to the special naming scheme
that python does - the program being invoked is called __main__, I guess because
it's the main point of entry for the program.  As in, the whole thing starts 
executing there.  So it gets named __main__.
  == is the equality comparison, read out loud as 'equal to' usually.  It's 
(essentially) checking if both things are the same.  For strings, it means 
making sure the characters are the same for each string.

Comparisons return True, or they return False.  Usually.  And the cases
where things aren't True or False are usually treated like "probably false",
so it's not something you typically have to worry about.  This comparison is
pretty safe.

Like functions, and every other occasion where you're grouping code blocks 
together, you indent things one level (4 spaces, 1 tab, don't use tabs) to
indicate the code that executes if the condition evaluates to true.
"""
if __name__ == '__main__':
    main()  # this is called 'calling' the function.  It means execute it.
    # outcome objective function goes on this line

"""
This has been a Hello, World! program explained.
Outcome objectives:  
  1) Modify this file to add a function that gets called after main(), that 
    prints "Goodbye, World!".
  2) Submit a Pull Request from the 'feature-hello-world' branch to the 'dev' 
    branch with the added code.
Bonus objectives:
  1) None this time.
"""
