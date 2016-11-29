:orphan:

.. title:: ZTEST_MOCKING

.. option:: CONFIG_ZTEST_MOCKING:
.. _CONFIG_ZTEST_MOCKING:

Enable mocking support for Ztest. This allows the test to set
return values and expected parameters to functions.



:Symbol:           ZTEST_MOCKING
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Mocking support functions" if ZTEST (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: ZTEST (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../tests/ztest/Kconfig:48