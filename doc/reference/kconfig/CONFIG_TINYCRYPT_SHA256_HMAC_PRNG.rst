:orphan:

.. title:: TINYCRYPT_SHA256_HMAC_PRNG

.. option:: CONFIG_TINYCRYPT_SHA256_HMAC_PRNG:
.. _CONFIG_TINYCRYPT_SHA256_HMAC_PRNG:

This option enables support for pseudo-random number
generator.



:Symbol:           TINYCRYPT_SHA256_HMAC_PRNG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PRNG (via HMAC-SHA256) support" if TINYCRYPT_SHA256_HMAC (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: TINYCRYPT_SHA256_HMAC (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/tinycrypt/Kconfig:53