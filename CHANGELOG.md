# Change log for the fparser package #

Original code by Pearu Peterson.

Modifications by (in alphabetical order):

* P. Elson, UK Met Office
* R. W. Ford, Science & Technology Facilities Council, UK
* M. Hambley, UK Met Office
* J. Henrichs, Australia Bureau of Meteorology
* I. Kavcic, UK Met Office
* A. R. Porter, Science & Technology Facilities Council, UK
* B. Reuter, ECMWF, UK
* J. Tiira, University of Helsinki, Finland
* P. Vitt, University of Siegen, Germany
* A. Voysey, UK Met Office

20/01/2021 PR #289 for #288. Bug fix for matching expressions containing
           real literals with signed exponents. This bug was introduced
           by #285.

20/01/2021 PR #286 for #284. Adds checking for datatype of *_Expr classes.

18/01/2021 PR #287 for #280. Fixes overly-deep recursion when reading
           multi-line comments.

11/01/2021 PR #285 for #283. Removes Structure_Constructor_2 class to fix
           problem with Expr matching.

11/01/2021 PR #237 for #236. Fix for slow parsing and printing of code.

23/12/2020 PR #278 for #277. Added github actions CI file, badges and documentation.

18/12/2020 PR #275 for #274. Adds an example script that uses fparser2 to
           generate Makefile dependency rules for a set of Fortran source
           files.

30/11/2020 PR #272 for #271. Bug fix to module_in_file() to ensure that the
           encoding is always set to UTF-8 when reading a file.

25/10/2020 PR #256 for #252. Fixes a bug in the parsing of an array constructor.

03/06/2020 PR #263 for #262. Fixes bug in fparser2 logging a 'critical'
           error when it reaches the end of a file.

03/06/2020 PR #249. Adds support for Fortran2008 CONTIGUOUS and
           CODIMENSION keywords.

## Release 0.0.11 (15/05/2020) ##

09/04/2020 PR #254. Fix for >1 character pre-processor macro identifiers.

24/03/2020 PR #239. Add support for CPP directives in fparser2.

07/03/2020 PR #250 for #248. Identify CPP directives in the reader.

14/02/2020 PR #246 for #245. Fixes some deprecation warnings about '\'
           characters in strings.

13/02/2020 PR #238 for #213. Re-orders the rules that are matched for
           Designators so that e.g. a(:) matches as a section-subscript-list
           rather than a substring-range.

13/02/2020 PR #240. Improves code conformance to pylint and pycodestyle.

06/02/2020 PR #241. Fixes a bug in the number of arguments specified for
           the IBITS intrinsic.

25/01/2020 PR #235 for #172. Fixes bug in absolute pattern matching that
           meant that matches with following content were not being
           rejected as they should.

10/01/2020 PR #230 for #102 and #105. Add parent and children properties
           to nodes. Also add get_root() method and update get_child and
           walk methods.

08/01/2020 PR #234 for #228. Remove the blank space at the end of unnamed
           "END DO" statements.

07/01/2020 PR #233 for #161. Improve the reader handling of multi-statement
           source lines. Especially those containing labels or construct
           names.

06/01/2020 PR #227 for #226. Added support for utf characters in
           Fortran block structures when using Python 2.

03/01/2020 PR #206 for #144. Bug fixes to the parsing of IMPORT
           statements.

20/11/2019 PR #224 for #223. Improvements to the fparser2 script. Errors
           now output to stderr, command-line setting of Fortran flavour
           honoured and no longer aborts if a syntax error is found.

## Release 0.0.10 (18/11/2019) ##

18/11/2019 PR #220 for #219. Fixes bug in the parsing of prefix
           specifications containing white space.

## Release 0.0.9 (04/11/2019) ##

04/11/2019 PR #208 for #207. Adds support for utf characters in Fortran
           strings when using Python 2.

06/10/2019 PR #212. Change setup.py to make fparser2 automatically
           available on the command line when installing.

15/07/2019 PR #203 for #170. Allows List objects to contain a single
           object meaning that the Parse Tree now has a more consistent
           structure.

11/07/2019 PR #210 for #209. Corrects the maximum number of arguments
           for the CMPLX instrinsic.

03/07/2019 PR #200 for #171. Disable Statement Function support
           in fparser2.

02/07/2019 PR #205 for #204. Corrects the minimum number of arguments
           for the SELECTED_REAL_KIND intrinsic.

26/06/2019 PR #199 for #189. Adds an Intrinsic_Function_Reference node
           to represent Fortran Intrinsics with the parse tree.

15/06/2019 PR #195. Travis change to make it raise errors with failing
	   unicode tests.

14/06/2019 PR #181. Added an xfailing test to demonstrate an error in
	   EndStmtBase.

14/06/2019 PR #196. Fix for unicode input errors in Python.

14/06/2019 PR #194. Fix for unicode input errors in Python 3.6.

05/04/2019 PR #192. END statements which use class EndStmtBase now output
	   the same tokens as the input e.g. names are not added if they
	   don't exist in the input.

29/03/2019 Issue #167 and PR #182. Fix to Fortran2003 rule 701 where large
           codes were causing recurse-depth errors in Python.

26/03/2019 Issue #136 and PR #183. Adds the ability to enforce the ordering
	   of matches in the blockbase class and uses this functionality
	   to fix potential errors in Fortran2003 rule 1101.

20/03/2019 Issue #132 and PR #184. Fixes for reading source files containing
 	   utf8 characters under Python 2.

08/03/2019 Issue #165 and PR #185. Fixes Python-3 specific code in the
           read.py script and adds some documentation.

28/02/2019 Issue #139 and PR #176. Makes the handling of include files more
           robust and adds a representation for them in the parse tree if
           they cannot be resolved.

28/02/2019 Issue #146 and PR #160. Adds support for Hollerith string
  	   constants in Format specifiers.

15/02/2019 Issue #138 and PR #173. Adds support for un-resolved include
           statements such that they are included in the generated parse
           tree (rather than being thrown away).

13/02/2019 PR #163. fparser1 bug fix for complex expressions in
           loop bounds.

17/01/2019 PR #137 for #125. Fixes an error in dealing with the case
           when the names of a program and end program do not match.

17/01/2019 PR #159. Adds support for the Cray pointer extension.

09/01/2019 PR #156 for #142. Bug fixes for the Binary and Unary
           Operator types.

08/01/2019 PR #154 for #142. Bug fixes for the Fortran 2003 forall
           statement (r759).

08/01/2019 PR #152 for #142. Bug fixes for the Fortran 2003 forall header
           rule (r754).

07/01/2019 PR #158 for #157. Adds support for a Defined Operator (r311 and
           r312).

07/01/2019 PR #141 for issue #129. Adds extension to support the use of 'x'
           without a preceeding integer in format strings.

20/12/2018 PR #149 for issue #147. Bug fix that corrects the name of one
	   of the subclasses (Associate_Construct) of Executable_Construct.

20/12/2018 PR #151 for issue #150 (and part of PR #142). Removes the
	   triggering of Coveralls from Travis (because it often incorrectly
	   reports that coverage has decreased).

## Release 0.0.8 (03/12/2018) ##

28/11/2018 PR #131 for issue #106. Bug fixes for Procedure_Binding and
           Char_Literal_Constant classes.

28/11/2018 PR #133 for issue #130. Bug fix for handing of derived-type
           statements.

28/11/2018 PR #134 for issue #119. Bug fix for parsing files that contain
           nothing or just white space.

23/11/2018 PR #122 for issue #118. Bug fix for reporting invalid
           Fortran when parsing `use module_name, only:` in fparser2.

21/11/2018 PR #127 for #126. Adds get_child function to help AST traversal.

19/11/2018 PR #124 for #112. Bug fix - spaces within names are now
           rejected by fparser2.

15/11/2018 PR #123 for #117, Fixes a bug that caused fparser to crash
           for code where a PROGRAM statement was missing an associated
           name.

14/11/2018 PR #121 for #120. Fixes bug in BlockBase such that name
           matches are no longer case sensitive. Improves error
           handling.

08/10/2018 PR #111 - bug fix for #110. Adds support for `kind(my_var)`
           inside a kind expression for a variable declaration.

03/09/2018 PR #100 for issue #99. Adds new SyntaxError to fparser2 and
           fixes bug so that errors are reported correctly for multiple
           program units in a single source file.

08/08/2018 PR #96, for issue #95. Removes dependency on nose and
           tidy test_fortran2003.py for pylint.

01/08/2018 PR #94 for issue #92. Re-structures fparser2 and introduces
           a parser factory. This creates a parser for a specified
           Fortran dialect (currently 2003 or 2008). Intoduces support
           for Fortran2008 submodules.

09/07/2018 PR #90 for issue #89. Make fparser2 pycodestyle conformant.

09/07/2018 PR #88 for issue #81. Bug fix for undefined variable in fparser
           class 'HasImplicitStmt'.

07/07/2018 PR #71 for issue #68. Adds support for keeping input comments
           in the Fortran output for parser 2.

27/06/2018 PR #85 for issue #82. Adds support for the full list of possible
           procedure attributes (POINTER and PROTECTED were missing).

19/06/2018 PR #86 and issue #83. Adds support for the full list of possible
           procedure specifications (MODULE and IMPURE were missing).

## Release 0.0.7 (23/04/2018) ##

20/04/2018 PR #78 and issue #74. Allow the use of the fparser cache to
	   be controlled and disable its use by default.

19/04/2018 PR #70. Re-organise module structure in order to split
	   versions 1 and 2 of the parser.

23/03/2018 PR #75. Allow FortranFileReader to accept either a filename
           or a file handle. Many pylint/pep8 improvements.

20/03/2018 PR #77 and issue #76. Fix bug in ALLOCATE statement when
	   using names of derived types as type specifiers.

05/03/2018 PR #73. Improvements to SourceInfo so that it can take either
	   a filename or a file handle.

26/02/2018 PR #72 and issue #69. Fixes for bugs found when using fparser2
	   to parse and then re-generate LFRic code.

15/01/2018 PR #67. Move old testing code from source files into test
	   framework.

12/01/2018 PR #66 and issue #64. Fix bug where = in a string was being
           treated like an assignment, causing parse errors in some
           format statements

08/01/2018 PR #65 and issue #59. fparser no longer presumes to set-up
           logging - this is left to the master application.

## Release 0.0.6 (04/12/2017) ##

04/12/2017 PRs #61 and #62. Remove the dependence on numpy.

24/11/2017 PR #60. Add fparser2 support for the 'deferred' attribute on a
           procedure declaration.

24/11/2017 PR #54. Add support for array initialisation using square
	   brackets in fparser1, e.g. 'integer :: a(2) = [x, y]'

09/11/2017 Issue #40 and PR #56 bug fix for missing comma when
           generating "USE, intrinsic :: ..."

21/10/2017 issue #36 and PR #47 generate correct open statement in
           fparser2 when the 'UNIT' keyword is not provided

20/10/2017 PR #49 pep8, pylint and nose->pytest changes for test_parse.py

20/10/2017 issue #43 and PR #48 add support for Python 3.

19/10/2017 issue #45 and PR #46 - bug fix for optional '::'
           between MODULE PROCEDURE and <procedure name>

13/10/2017 issue #41 and PR #42 - removed __init__.py files from
           directories that do not contain package code

28/09/2017 issue #35 pr #39 add support for the 'opened' option
	   in the inquire statement in fparser2.

06/09/2017 issue #34 pr #37 Fix a format statement parsing
	   bug in fparser2

## Release 0.0.5 (20/06/2017) ##

20/06/2017 issue #30 pr #31 Extend fparser1 to support
 	   Fortran2003 procedure declarations

## Release 0.0.4 ##

11/05/2017 pypi configuration was incorrect so 0.0.3 was
           released on github but not on pypi. 0.0.4 has the
           same functionality as 0.0.3 but is available on
           both pypi and github.

## Release 0.0.3 ##

11/05/2017 #27 Fix a bug in fparser1 to support (Fortran2003)
           class declarations e.g. CLASS(my_class) :: var

## Release 0.0.2 ##

22/03/2017 #11 Configure Travis to automatically release to
           pypi when a tag is created. Create release 0.0.2.

03/03/2017 #5 Extend fparser1 to support calls to type-bound
           procedures when accessed via array elements.

24/02/2017 #4 Extend fparser1 to support the (Fortran2003)
           SELECT TYPE block.

09/02/2017 #2 Create initial documentation, mostly based on
	   Pearu's previous work.

07/02/2017 #10 Merge in fixes to Fortran2003 parser originally
  	   done as part of Habakkuk development.

## Release 0.0.1 ##

31/01/2017 #6 Create first release and upload to pypi.

31/01/2017 #7 Apply regex bug-fix to 'entry' parsing so that
	   all tests pass.

16/01/2017 #1 Initial import of parser code extracted from
	   the f2py project.
