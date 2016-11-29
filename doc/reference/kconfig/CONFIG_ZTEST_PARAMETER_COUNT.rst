:orphan:

.. title:: ZTEST_PARAMETER_COUNT

.. option:: CONFIG_ZTEST_PARAMETER_COUNT:
.. _CONFIG_ZTEST_PARAMETER_COUNT:

Maximum amount of concurrent return values / expected parameters.


:Symbol:           ZTEST_PARAMETER_COUNT
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Count of parameters or return values reserved" if ZTEST_MOCKING (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: ZTEST_MOCKING (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../tests/ztest/Kconfig:56