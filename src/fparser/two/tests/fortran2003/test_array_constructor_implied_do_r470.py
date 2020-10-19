# Copyright (c) 2020 Science and Technology Facilities Council.
#
# All rights reserved.
#
# Modifications made as part of the fparser project are distributed
# under the following license:
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
Test Fortran 2003 rule R470: this file tests the support for the
various forms of implicit loop within an array constructor.

TODO #255 and #257 - these tests need expanding.

Further tests are required here to fully cover the rule.

'''

import pytest
from fparser.common.readfortran import FortranStringReader
from fparser.two import Fortran2003


@pytest.mark.xfail(reason="#255 - Structure_Constructor_2 ends up matching "
                   "key=var pattern.")
@pytest.mark.usefixtures("f2003_create")
def test_implicit_loop_constructor_no_parentheses():
    ''' Test that the parser does not match an implicit loop if the
    surrounding parentheses are missing (R470). '''
    fcode = "(/ival, ival=1, nval, istep/)"
    reader = FortranStringReader(fcode)
    ast = Fortran2003.Array_Constructor(reader)
    assert ast is None


@pytest.mark.xfail(reason="#257 Constraint C497 is not checked.")
@pytest.mark.usefixtures("f2003_create")
def test_nested_implied_do():
    ''' Test C497 - the ac-do-variable of a nested implicit do shall not
    appear as the ac-do-variable of the containing implicit do. '''
    reader = FortranStringReader(
        "(/(JBODY,JBODY=1,SUM((/(JBODY,JBODY=1,4)/)))/)")
    ast = Fortran2003.Array_Constructor(reader)
    assert ast is None
