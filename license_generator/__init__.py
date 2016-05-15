#
#    license-generator
#    Copyright (C) 2016  Walter Dolce <walterdolce@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__author__ = 'Walter Dolce'
__author_email__ = 'walterdolce@gmail.com'
__copyright_short__ = 'Copyright (C) 2016  {author} {author_email}'.format(
    author=__author__,
    author_email=__author_email__
)
__license_short__ = 'License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>'
__version__ = '0.2.0'
__version_info__ = """license-generator {version}
{copyright}
{license_short}
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.""".format(
    copyright=__copyright_short__,
    license_short=__license_short__,
    version=__version__
)
