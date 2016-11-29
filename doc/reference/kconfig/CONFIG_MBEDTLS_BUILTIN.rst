:orphan:

.. title:: MBEDTLS_BUILTIN

.. option:: CONFIG_MBEDTLS_BUILTIN:
.. _CONFIG_MBEDTLS_BUILTIN:

Link with local mbedTLS sources instead of external library.



:Symbol:           MBEDTLS_BUILTIN
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Enable mbedTLS integrated sources" if MBEDTLS (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: MBEDTLS (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/mbedtls/Kconfig:27