:orphan:

.. title:: TINYDTLS_DEBUG

.. option:: CONFIG_TINYDTLS_DEBUG:
.. _CONFIG_TINYDTLS_DEBUG:

Enable tinyDTLS debugging support.



:Symbol:           TINYDTLS_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable tinyDTLS debugging support." if TINYDTLS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: TINYDTLS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 NETWORKING && NET_UIP (value: "n")
:Locations:
 * ../net/ip/Kconfig:502