:orphan:

.. title:: TINYCRYPT_CTR_PRNG

.. option:: CONFIG_TINYCRYPT_CTR_PRNG:
.. _CONFIG_TINYCRYPT_CTR_PRNG:

This option enables support for the pseudo-random number
generator in counter mode.



:Symbol:           TINYCRYPT_CTR_PRNG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "PRNG in counter mode" if TINYCRYPT (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: TINYCRYPT (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../ext/lib/crypto/tinycrypt/Kconfig:26