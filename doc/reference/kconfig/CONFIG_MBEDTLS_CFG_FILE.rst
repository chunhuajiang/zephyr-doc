:orphan:

.. title:: MBEDTLS_CFG_FILE

.. option:: CONFIG_MBEDTLS_CFG_FILE:
.. _CONFIG_MBEDTLS_CFG_FILE:

Enable custom mbed TLS configuration



:Symbol:           MBEDTLS_CFG_FILE
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "mbed TLS configuration file" if MBEDTLS_BUILTIN (value: "n")
:Default values:

 *  "config-threadnet.h"
 *   Condition: MBEDTLS_BUILTIN (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/mbedtls/Kconfig:34