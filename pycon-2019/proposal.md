# Title: _Hooked on Python_

## Summary

Import hooks exist in Python to enable programmers to modify how Python deals with source code, such as where it reads if from, how it reads it and executes it. Exception hooks make it possible to change the feedback provided to users when something goes wrong. Combining both types of hooks makes it possible to extend Python in unusual ways that can benefit a wider and more diverse audience.

## Python level

Intermediate.

While working with import hooks can be considered to be an advanced level topic, the presentation will be made so that intermediate level programmers should be able to completely understand all the concepts presented.

## Requested time

This talk as outlined below is intended for a 30 minutes time slot. I would prefer a 45 minute time slot but have written this proposal on the assumption that this would not be possible.

The examples provided will be brief and narrowly focused on the issue described. Links will be provided for those interested in more detailed examples. If a 45 minute time slot was available, slightly longer examples could easily be used, giving a more comprehensive overview of the potential of using import hooks and exception hooks either separately or together. In the outline below, I have indicated a few places where additional information could be provided if a 45 minutes time slot was available. In a shorter talk, they would be mentioned in passing as "food for thought" for the listeners.

## Description and motivation for this topic

Many programmers know that you can create your own syntax with languages from  the Lisp family. In fact, one of these, namely [Racket](https://racket-lang.org/), has been explicitly designed to facilitate the creation of new languages. In the same way, the vast majority of programmers believe that you cannot do this with Python ... even though you can, using an import hook.

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

While writing code to take full advantage of import hooks from scratch can be tricky (see note 0 below), the idea itself can be fairly simply explained and illustrated.

Importing and using non standard Python code means that new types of exceptions are going to arise. Providing feedback to users when an exception is raised is a crucial component of Python. If a modified version of Python is to be used, it is important that this feedback aspect be taken into consideration. With the main example used, it makes sense to discuss how to deal with such situations using exception hooks. If you wish, within the context of this talk, import hooks and exception hooks can be seen as two complementary topics - even though they are always presented separately.

The examples I will give are based on using import hooks to perform some sort of code transformation, prior to code execution. All the examples given will be based on existing code and documentation (see note 1 below), many of which I have described previously in blog posts (see note 2 below) from a different perspective.

While code transformations have been the subject of talks given at recent Pycon (see note 4 below), as far as I can tell there has been no talks on import hooks themselves nor on exception hooks since at least 2015 when David Beazley included them in a 3 hour long tutorial (see note 5 below).  As these are essential components of executing Python code, I believe that it would be highly appropriate to include a talk on these topics.

Finally, when working on these projects, I found out that integrating two different programs (or libraries) that separately provide support for string translations into various human languages is better done in a slightly different way than that presented on most if not all tutorials on supporting i18n in Python. If a 45 minute time slot were available, I would include a tiny part on this aspect as it is a topic that arise naturally in this context and is quick and easy to describe and understand, and could be of benefit to designers of libraries that support translation and localization.

## Outline

### Introduction [5 min]

* Who am I?
* Goal of the presentation:
  Using import hooks, learn how to modify Python so that it can read and process
  non standard Python constructs. Using exception hooks, enable Python to
  provide more useful information when an exception is raised. Do both of
  these in such a way that localized versions, using different human languages,
  can be supported.
* Setting the stage
  * Describe [Scratch](https://scratch.mit.edu/) (see note 6 below)
  * Introduce AvantPy
    * Quick demo (more likely: a few screenshots)
  * Possible brief description/mention of [Hy](http://docs.hylang.org/en/stable/),
    a dialect of Lisp embedded in Python (see note 7 below)

### Import hooks [13/30 min or 20/45 min]

* What happens when a module gets imported?
  * Describe the various steps, from locating a text file intended as
    a source of code to its execution by cPython.
* Creating an import hook
  * Steps required
    * Create a MetaPathFinder
      * Potentially only deal with files that meet certain criteria
    * Make it available via `sys.meta_path()`
    * Create a custom Loader
      * Possibly specify how code is modified prior to its execution
  * Using it
    * Find files to be imported which meet our criteria
    * Our custom Loader is called; what can we do with it?
      * Using it to modify the AST
        * Given the time restriction, no actual example will be explained
          in this presentation but links to explicit examples and to previous Pycon talks on the topic of modifying the AST will be included in the slides.
      * Using it to modify the bytecode
        * Given the time restriction, no actual example will be explained
          in this presentation but links to explicit examples and to previous Pycon talks on the topic of modifying the bytecode will be included in the slides.
      * Using it to modify the textual source
        * A simple example will be given first
        * AvantPy as a slightly more detailed example
          * Dealing with errors in the original text file
            * Preserving space structure of original document for feedback.
          * (If more time were available, more details could be provided here.)

### Exception hooks [7/30 min or 12/45 min]

* When something goes wrong: introducing Friendly-traceback
  * Quick demo (more likely: a few screenshots)
* The basic idea of exception hooks
* Beyond the standard tracebacks.
  * In addition to the cgitb module in Python's standard library,
    many open source projects are designed to improve upon the
    standard Python tracebacks. Links to such projects will
    be provided and Friendly-traceback will be used as the
    main source of most examples.
  * Special case: REPL(s) and exception hooks (likely not covered for lack of time.)
* Testing frameworks and custom exception hooks
  * Avoiding conflicts (example with Pytest likely not covered for lack of time.)
* Making an extensible API: enabling an exception hook to
  work correctly on its own or when used in conjunction with
  an import hook that modifies Python's syntax.
  * Barebone example: AvantPy error or Python error?

### Translations and integration [0/30 min or 2/45 min]

* Quick review of standard gettext method for providing translations
* Problem with having `_()` as a globally defined function
  * Conflict with standard REPL and/or between libraries defining
    their own version of `_()`.
  * Solution: locally defined `_()`

### Conclusion [1 min]

### Questions and answers [4/30 min or 5/45 min]

## Notes

0. While I was able to figure out how to write an import hook on my
   own using the deprecated `imp` module from the standard library,
   I had to resort to asking a [question on StackOverflow](https://stackoverflow.com/q/43571737/558799)
   in order to understand how to use `importlib` to achieve the same goal.
   This was before I dove further into the code and watch additional talks,
   such as those listed below.

1. This talk is going to be based on the following existing code
   and documentation, all of which is open source:
   
   * **Friendly-traceback** code and documentation. Friendly-traceback
     has been awarded a "virtual" [grant for Python in Education by the PSF](http://pyfound.blogspot.com/2019/09/grants-awarded-for-python-in-education.html)
   * **AvantPy** code and documentation
   * **Experimental** code and documentation

   This [short, silent video](https://www.youtube.com/watch?v=t5wMjJlsudM) demonstrates
   how **Friendly-traceback** and **AvantPy** can be used together with a
   modified version of Python's IDLE.

2. I have discussed examples using import hooks in the following
   blog posts, most of which use a module I called **experimental**
   referenced in note 1 above.

   * Links to blog posts to be added

3. Experience as a speaker: in my career,
   I have given many talks in my own field (Physics),
   taught over 40 different classes, and given a few talks on my
   favourite hobby: programming using Python. The latter include
   the following:
   
   * EuroPython - add links/more details to all these.
   * Crunchy
   * Other
   * Plugins

4. The list of talks dealing with code transformations includes [Playing with Python Bytecode](https://us.pycon.org/2016/schedule/presentation/1829/),
   [Syntax Trees and Python - Automated Code Transformations](https://us.pycon.org/2019/schedule/presentation/205/),
   and [The AST and Me](https://us.pycon.org/2018/schedule/presentation/107/).
   A good overview of all the steps involved in the code execution, is given
   by [From Source to Code: How CPython's Compiler Works - Pycon Canada 2013](https://www.youtube.com/watch?v=R31NRWgoIWM) by Brett Cannon.

5. List of talks dealing with the import system includesa 3 hour long tutorial
   [Modules and Packages: Live and Let Die! - PyCon 2015](https://www.youtube.com/watch?v=0oTh1CXRaQ0) by David Beazley,
   [How import works - Pycon US 2013](https://www.youtube.com/watch?v=AqnxyRuenAg&list=PL4S0lvhXvdhIV2C28Ia_DeIeloBrsQBOW&index=3) by Brett Cannon.
   Another talk presented at Pycon PL in 2018 is [from * import python](https://www.youtube.com/watch?v=FuYpDBfcaD4) by Łukasz Taczuk.

6. **Scratch** is a very widely used project, possibly known by more people
   than Python itself. Scratch is mentioned as a motivation
   for using AvantPy as the main example for this talk.

7. **Hy** is another project that uses import hooks, one that has many
   more users than **AvantPy**. **Hy**'s code is a lot more complex than
   that of **AvantPy** and is harder to understand and describe as a basic
   example of import hooks. See [Getting Hy on Python: How to implement a Lisp front-end to Python - PyCon 2014](https://www.youtube.com/watch?v=AmMaN1AokTI)
   by Paul Tagliamonte.