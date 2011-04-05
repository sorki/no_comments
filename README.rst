no_comments
===========

Easy way to strip comments from various file types.

Description:
------------

Comment stripping utility. Handles both inline comments and block comments.
Strips C/C++ comments by default (both inline and block).

Usage:
------
 - `cat source_code_file | no_comments > out`

Features:
---------
 - strip only inline comments / block comments
 - configurable delimiters
 - strip only comments at the beggining of the line
 - preserve empty lines which contained comments before

Installation:
-------------
 - `easy_install no_comments` or  `pip install no_comments`
 - run `no_comments --help`


Notes:
-------
This utility is DUMB - as it's not language specific it doesn't understand the syntax (It
will remove comments in strings, ignore nested comments or so).
