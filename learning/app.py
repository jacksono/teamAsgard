
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive todo list command application.
Usage:
    app.py add_skill <skill>
    app.py view_skills
    app.py mark_learnt <skill>
    app.py view_skills_learnt
    app.py view_skills_unlearnt
    app.py view_progress
    app.py (-i | --interactive)
    app.py (-h | --help | --version)

"""
import os
import sys
import cmd
from docopt import docopt, DocoptExit
from functions import LearningMap
function = LearningMap()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def start():
    os.system("clear")
    intro = 'Welcome to my interactive program!'
    prompt = 'learning_map>>>'
    print(__doc__)



class ToDo(cmd.Cmd):
    intro = 'Welcome to my interactive program!'
    prompt = 'todo>>>'

    @docopt_cmd
    def do_add_skill(self, arg):
        """Usage: add_skill <skill>"""
        pass
        function.add_skill()

    @docopt_cmd
    def do_view_skills(self, arg):
        """Usage: view_skills"""
        pass
        function.view_skills()

    @docopt_cmd
    def do_mark_learnt(self, arg):
        """Usage: mark_learnt <skill>"""
        pass
        function.mark_learnt()

    @docopt_cmd
    def do_view_skills_learnt(self, arg):
        """Usage: view_skills_learnt"""
        pass
        function.view_skills_learnt()

    @docopt_cmd
    def do_view_skills_unlearnt(self, arg):
        """Usage: view_skills_unlearnt"""
        pass
        function.view_skills_unlearnt()

    @docopt_cmd
    def do_view_progress(self, arg):
        """Usage: view_progress"""
        pass
        function.view_progress()









    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!', "cyan")
        exit()

opt = docopt(__doc__, sys.argv[1:])

if __name__ == "__main__":
    try:
        start()
        ToDo().cmdloop()
    except KeyboardInterrupt:
        os.system("clear")
        print('Application Exiting')