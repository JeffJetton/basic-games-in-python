# Vintage BASIC Games in Python

This is an in-progress collection of simple, text-based Python games, ported from David H. Ahl's two hugely popular collections of type-in BASIC program listings:
* BASIC Computer Games (1973)
* More BASIC Computer Games (1979)

These books influenced an entire generation of budding programmers back in the day, myself included. It is hoped that beginning Python programmers will derive the same benefits from playing, exploring, and (most importantly) *modifying* these games as we did with the original BASIC versions.

You won't find fancy graphics or arcade action here. These games are truly "old school" and run as they would've originally: Right on on the command line (or in a Python IDE) using written output and typed-in input. This can actually be helpful in a way, since it lets the reader/programmer focus on the basics of the game programming itself, without having to also learn about and deal with graphic libraries, etc. (It's also a fun glimpse into the pre-graphics days of computer gaming.)

### Porting Notes
* The opening comments of each game are taken nearly verbatim from the original descriptions in the books. Some bits that pertained to specific areas of code have been moved to comments near that section of code.
* The games themselves have been kept as close to the original play experience as possible:
   * The text prompts and displays are pretty much exactly as they appeared in the books
   * This includes spacing and spelling (and spelling mistakes)
   * The books included example printouts of test runs of each game. In cases where the output shown was different from what the given code would've produced (a not uncommon occurrence!), editorial choices have been made.
   * While the code in the books used just uppercase (many computers of that era lacked the capability to display lowercase), these ports use upper and lower. A library is provided that allows you to override this.
* Program logic has also been kept fairly close to the originals, for better or for worse:
   *
   * Since Python is a [structured language](https://en.wikipedia.org/wiki/Structured_programming) (in contrast to vintage BASIC's older, [unstructured paradigm](https://en.wikipedia.org/wiki/Non-structured_programming)), all the GOTOs have been replaced with while loops and if/else/then blocks.
   * Functions have been broken out primarily to avoid code duplication only. They have not been broken out merely to group program logic into more-understandable chunks. (If we had to suffer through dense lines of code, so do you! :-) )
   * Apart from tuples (taking the place of BASIC arrays), Python data structures have been used sparingly.
   * Variable names have been changed from single letters to descriptive names. I'm not a monster.
   * Logical errors have been faithfully replicated! Discovering and fixing them is part of the fun, after all.
* As a learning exercise, suggestions for modifications are found in the comments at the end of each code file. These are part of this project and did not appear in the original books.

Share and enjoy!

> **Note:** There is [another project on github](https://github.com/chaosotter/python-101-games) that's doing something similar, although with a few differences in porting philosophy. It looks really cool though, so you might want to check it out too!
