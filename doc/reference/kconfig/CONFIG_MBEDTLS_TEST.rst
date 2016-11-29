:orphan:

.. title:: MBEDTLS_TEST

.. option:: CONFIG_MBEDTLS_TEST:
.. _CONFIG_MBEDTLS_TEST:

Enable self test function for the crypto algorithms



:Symbol:           MBEDTLS_TEST
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Compile internal self test functions" if MBEDTLS_BUILTIN (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: MBEDTLS_BUILTIN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/mbedtls/Kconfig:41