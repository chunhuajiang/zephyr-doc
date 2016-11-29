:orphan:

.. title:: MBEDTLS_INSTALL_PATH

.. option:: CONFIG_MBEDTLS_INSTALL_PATH:
.. _CONFIG_MBEDTLS_INSTALL_PATH:

This option holds the path where the mbedTLS libraries and headers are
installed. Make sure this option is properly set when MBEDTLS_LIBRARY
is enabled otherwise the build will fail.


:Symbol:           MBEDTLS_INSTALL_PATH
:Type:             string
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "mbedTLS install path" if MBEDTLS_LIBRARY (value: "n")
:Default values:
 (no default values)
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/mbedtls/Kconfig:55