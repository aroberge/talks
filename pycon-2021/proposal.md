# Errors should never pass silently

The Zen of Python suggests that *errors should never pass silently*,
but standard tracebacks are perhaps more akin to noise than music.
Depending on your point of view,
tracebacks might contain all the relevant information,
too much information, or not enough information.
Occasionally, they might even be slightly misleading.

Various projects attempt to transform the traceback noise into
different genres of music. In this talk we review many such projects,
and explore ways in which standard tracebacks can be improved upon
and made more useful for your own particular needs.



# Introduction - 3 minutes

* Introduction
* Anatomy of a traceback
* Two different categories: runtime exceptions and syntax errors

# Part 1: Improving on runtime exceptions - 15 minutes

* Highlighting information
  * Changing the format
  * Editing the text
  * Using colors
    * Color imperfect
* Interactive use vs logging
* Adding information
  * Security considerations
* Removing information

# Part 2: Improving on syntax errors - 5 minutes

* Slow and steady improvements by Pypy and CPython
  * This includes some nice improvements added in CPython 3.10.a5
* The challenge of parsing the unparsable
* An ounce of prevention: using linters
* Going beyond linters

# Looking for an "ideal" solution - 7 minutes

* Adaptable based on user experience
  * Differences between beginners and advanced users
* Configurable
  * Presentation: format and color
  * Context (for example: logging vs repl)
  * Amount of information
* Providing additional clues as to the exact cause of an exception
  * Raymond Hettinger's "hint" idea, and beyond
* I18n support

The following are some of the modules/projects that would likely be mentioned.

[1] https://docs.python.org/3/library/cgitb.html

[2] https://github.com/albertz/py_better_exchook/

[3] https://github.com/Infinidat/infi.traceback

[4] https://github.com/Qix-/better-exceptions 

[5] https://github.com/cknd/stackprinter

[6] https://github.com/onelivesleft/PrettyErrors/ 

[7] https://github.com/skorokithakis/tbvaccine 

[8] https://github.com/willmcgugan/rich

[9] xmode for Ipython: https://ipython.readthedocs.io/en/stable/interactive/magics.html

[10] https://github.com/alexmojaki/executing

[11] https://github.com/alexmojaki/stack_data

[12] https://github.com/aroberge/friendly-traceback

[13] https://thonny.org/


# Additional notes

Since 2004, I have been programming in Python as my main hobby, with a
focus on creating tools to make it easier for beginners to learn Python.
These include [Rur-ple](https://sourceforge.net/projects/rur-ple/) and its successor [Reeborg's World](https://reeborg.html), as well as [Crunchy](https://code.google.com/archive/p/crunchy/).

While working on these projects, I have been thinking about how one could improved on standard tracebacks. For example, in 2010 I suggested providing a [translation for tracebacks](https://mail.python.org/pipermail/python-ideas/2010-May/007211.html).

More recently, I have been working on a project specifically aimed at improving
tracebacks: **Friendly-traceback** [code](https://github.com/aroberge/friendly-traceback) and [documentation](https://aroberge.github.io/friendly-traceback-docs/docs/html/index.html).  Friendly-traceback has been awarded a "virtual" [grant for Python in Education by the PSF](http://pyfound.blogspot.com/2019/09/grants-awarded-for-python-in-education.html).
In working on Friendly-traceback, I have looked at various other
traceback enhancers, in an attempt to identify the best ideas to
incorporate in my own project.

I have given a few talks about Python, but none in the recent past.
These talks include the following:

   * A gentle introduction to Python's way, EuroPython 2005.  This was an invited
     talk. I have a copy of the slides in an archive; however, the main part of the presentation was done interactively using Rur-ple.

   * Crunchy, at Pycon 2007. No slides are available as the entire presentation was
     done using Crunchy interactively.
     On his blog, [Bruce Eckel wrote](https://www.artima.com/weblogs/viewpost.jsp?thread=196792)

     > Crunchy (formerly crunchy frog) is a very impressive way to create interactive tutorials that work inside a browser.

   * _Learning and Teaching Python Programming: The Crunchy Way_, Pycon

     2009. Again, no slides available, but I mentioned the abstract in [this blog post](https://aroberge.blogspot.com/2008/12/seeing-double-at-pycon-2009.html) as well as the abstract for the talk mentioned immediately below.

   * _Plugins and Monkeypatching: increasing flexibility, dealing with inflexibility_ A talk on plugins at Pycon 2009, based on a [6-part blog series](https://aroberge.blogspot.com/2008/12/plugins-part-6-setuptools-based.html). No slides available, but this talk was referenced in the book Pro Python System Administration as [mentioned here](https://aroberge.blogspot.com/2011/01/book-review-pro-python-system.html)
