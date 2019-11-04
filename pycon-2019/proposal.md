# Proposed title

Hooked on Python

## Summary

Import hooks exist in Python to enable programmers to modify
how Python deals with source code, how it reads it and
executes it. Exception hooks make it possible to change the feedback
provided to users when something goes wrong. Combining both types
of hooks makes it possible to extend Python in unusual ways and make it
more easily usable by a different groups of programmers.

## Python level

Intermediate.

While working with import hooks can be considered to be an advanced level topic,
the presentation will be made so that intermediate level
programmers should be able to completely understand all the ideas presented.

## Requested time

This talk as described below is intended for a 30 minutes time slot.

The examples provided will be brief and narrowly focused on the issue
described. Links will be provided for those interested in more detailed
examples.  Admittedly, the propose outline follows a rather restricted
timeline. If a 45 minute time slot was available and thought
to be more appropriate, longer examples
could easily be used, giving a more comprehensive overview of the
potential of using import hooks and exception hooks either separately
or together.

## Description and motivation for this topic

Many programmers know that you can create your own syntax with languages from
the Lisp family. In fact, one of these,
namely [Racket](https://racket-lang.org/) is designed to facilitate the creation of new languages.

In the same way, the vast majority of programmers
believe that you cannot do this with Python ... even though you can, using
an import hook.

In the third edition of the _Python Cookbook_, David Beazley and Brian K. Jones wrote on page 420:

> _...it should be emphasized that Python's module, package and import
> mechanism is one of the most complicated parts fo the entire language --
> often poorly understood by even the most seasoned Python programmers
> unless they've devoted effort to peeling back the covers._

Near the end of the discussion (on page 428), they add

> _Assuming that your head hasn't completely exploded at this point, ...
> Last, but not least, spending some time sleeping with
> [PEP 302](https://www.python.org/dev/peps/pep-0302/) and the
> documentation for `importlib` under your pillow may be advisable._

And, as [Steve d'Aprano wrote in May 2015](https://mail.python.org/pipermail/python-ideas/2015-May/033633.html):

> I think that the majority of Python programmers have no idea that you can even write an import hook at all, let alone how to do it.

While writing code to take full advantage of import hooks can be tricky,
the idea itself can be fairly simply explained and illustrated.

Importing and using non standard Python code means that new
types of exceptions are going to arise.
Providing feedback to users when an exception is raised is a crucial
component of Python. If a modified version of Python is to be used,
it is important that this feedback aspect be taken into consideration.
With the main example used,
it makes sense to discuss how to deal with such exceptions using
exception hooks. If you wish, within the context of this talk,
import hooks and exception hooks
can be seen as two sides of the same coin - even though they are
almost always presented separately.

The examples I will give are based on using import hooks to perform
some sort of code transformation, prior to code execution.
While code transformations have been the subject of talks
given at recent Pycon (see note 4 below), as far as I can tell there has
been no talks on import hooks themselves nor on exception hook since at
least 2015.  As these are essential components of executing
Python code, I believe that it would be highly appropriate to
include a talk on these topics.

Finally, from my own experience,
I found out that integrating two different programs
(or libraries) that provides support for string translations
into various human languages is better done in a slightly different
way than that presented on most if not all tutorials on
supporting i18n in Python.
This lead me to include a tiny part on this aspect as it
is a topic that arise naturally in this context
and is easy to understand.

## Outline

### Introduction [6 min]

* Who am I?
* Setting the stage
  * Describe [Scratch](https://scratch.mit.edu/)
    * Note: this is done as a motivation for AvantPy
  * Introduce AvantPy
    * Describe AvantPy
    * Quick demo (more likely: a few screenshots)
  * When sometething goes wrong: introducing Friendly-traceback
    * Quick demo (more likely: a few screenshots)
  * Brief description of [Hy](http://docs.hylang.org/en/stable/),
    a dialect of Lisp embedded in Python
    * This is another, more serious example of using import hooks
* Setting the stage:
  Using import hooks, modify Python so that it can read and process
  non standard Python constructs. Using exception hooks, enable Python to
  provide more useful information when an exception is raised. Do both of
  these in a way that localized versions, using different human languages,
  can be supported.

### Import hooks [11 min]

* What happens when a module gets imported?
* Creating an import hook
  * Using it to modify the AST
    * Links to examples
  * Using it to modify the bytecode
    * Links to examples
  * Using it to modify the source
    * Simple example
    * AvantPy as a more detailed example
      * Dealing with syntax errors

### Exception hooks [5 min]

* The basic idea
* The type of information available
  * Give various examples here
* Avoiding conflicts
  * Testing frameworks and except hooks
  * Global vs local
  * Give example with Pytest
* Making an extensible API

### Translations and integration [3 min]

* Quick review of standard gettext method for providing translations
* Problem with having `_()` as a globally defined function
  * Conflict with standard REPL
  * Conflict between libraries
  * Solution: locally defined `_()`

### Conclusion [1 min]

### Questions and answers [4 min]

## Notes

1. This talk is going to be based on the following existing code
   and documentation, all of which is open source:
   * Friendly-traceback code
   * Friendly-traceback documentation
   * AvantPy code
   * AvantPy documentation
   * Experimental code and documentation
   * Hy documentation

2. I have discussed examples using import hooks in the following
   blog posts

3. In my career, I have given many talks in my own field (Physics),
   taught over 40 different classes, and given a few talks on my
   favourite hobby: programming using Python. The latter include
   the following:
   * EuroPython
   * Crunchy
   * Other
   * Plugins

4. The list of talks dealing with code transformations includ [Playing with Python Bytecode](https://us.pycon.org/2016/schedule/presentation/1829/),
   [Syntax Trees and Python - Automated Code Transformations
](https://us.pycon.org/2019/schedule/presentation/205/),
   and [The AST and Me](https://us.pycon.org/2018/schedule/presentation/107/)

Check the following:

[How to JIT: Writing a Python JIT from scratch in pure Python](https://us.pycon.org/2019/schedule/presentation/169/)


