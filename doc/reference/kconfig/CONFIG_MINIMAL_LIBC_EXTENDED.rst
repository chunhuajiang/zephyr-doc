:orphan:

.. title:: MINIMAL_LIBC_EXTENDED

.. option:: CONFIG_MINIMAL_LIBC_EXTENDED:
.. _CONFIG_MINIMAL_LIBC_EXTENDED:

This option enables building some optional libc functions that
are not used directly by the kernel but can be used in applications.
The option adds the following functions: strtoul, strtol, atoi,
strncasecmp.
Warning: Use the above functions only for testing, if you need to
use any of the functions in an application you probably should be
linking against a full lib c implementation instead.




:Symbol:           MINIMAL_LIBC_EXTENDED
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "y"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Build additional libc functions [EXPERIMENTAL]" if MINIMAL_LIBC (value: "y")
:Default values:

 *  n (value: "n")
 *   Condition: MINIMAL_LIBC (value: "y")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 NETWORKING && NET_UIP && ER_COAP_LINK_FORMAT_FILTERING (value: "n")
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:142