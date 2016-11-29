:orphan:

.. title:: TINYCRYPT_AES_CBC

.. option:: CONFIG_TINYCRYPT_AES_CBC:
.. _CONFIG_TINYCRYPT_AES_CBC:

This option enables support for AES-128 block cipher mode.



:Symbol:           TINYCRYPT_AES_CBC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "AES-128 block cipher" if TINYCRYPT_AES (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: TINYCRYPT_AES (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/tinycrypt/Kconfig:88