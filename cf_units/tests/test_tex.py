# (C) British Crown Copyright 2019, Met Office
#
# This file is part of cf-units.
#
# cf-units is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cf-units is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cf-units.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import six

from cf_units.tex import tex


if six.PY2:
    pytest.skip('skipping latex in Python2')


def test_basic():
    u = 'kg kg-1'
    assert tex(u) == r'{kg}\cdot{{kg}^{-1}}'


def test_identifier_micro():
    u = 'microW m-2'
    assert tex(u) == r'{{\mu}W}\cdot{{m}^{-2}}'


def test_raise():
    u = 'm^2'
    assert tex(u) == r'{m}^{2}'


def test_multiply():
    u = 'foo bar'
    assert tex(u) == r'{foo}\cdot{bar}'


def test_divide():
    u = 'foo per bar'
    assert tex(u) == r'\frac{foo}{bar}'


def test_shift():
    u = 'foo @ 50'
    assert tex(u) == r'{foo} @ {50}'


def test_complex():
    u = 'microW^2 / (5^-2)π per sec @ 42'
    expected = r'{\frac{{\frac{{{\mu}W}^{2}}{{5}^{-2}}}\cdot{π}}{sec}} @ {42}'
    assert tex(u) == expected
