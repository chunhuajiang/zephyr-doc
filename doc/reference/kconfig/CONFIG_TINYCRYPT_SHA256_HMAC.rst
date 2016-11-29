:orphan:

.. title:: TINYCRYPT_SHA256_HMAC

.. option:: CONFIG_TINYCRYPT_SHA256_HMAC:
.. _CONFIG_TINYCRYPT_SHA256_HMAC:

This option enables support for HMAC using SHA-256
message authentication code.



:Symbol:           TINYCRYPT_SHA256_HMAC
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "HMAC (via SHA256) message auth support" if TINYCRYPT_SHA256 (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: TINYCRYPT_SHA256 (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/tinycrypt/Kconfig:44