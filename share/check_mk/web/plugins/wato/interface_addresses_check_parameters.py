#!/usr/bin/python
#
# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 3.  This test is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.
# This configures the queue size/consumers limits in WATO.
#
group = "Applications, Processes & Services"

# def register_check_parameters(subgroup, checkgroup, title, valuespec, itemspec, matchtype, has_inventory=True, register_static_check=True):
#
register_check_parameters(
    group,
    "interface_addresses",
    _("Network interface addresses"),
    Dictionary(
        elements = [
            ("requiredIPv4Addresses",
                  TextAscii(title=_("List of required IPv4 Addresses, separated by comma"), 
                            help="Critical if interface is missing one or more of these addresses"),
            ),
        ]
    ),
    TextAscii( title=_("Network interface address"),
    help=_("Addresses of network interface")),
    "first",
)
