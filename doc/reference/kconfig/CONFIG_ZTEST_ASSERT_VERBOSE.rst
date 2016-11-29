:orphan:

.. title:: ZTEST_ASSERT_VERBOSE

.. option:: CONFIG_ZTEST_ASSERT_VERBOSE:
.. _CONFIG_ZTEST_ASSERT_VERBOSE:

Set verbosity level for assertions.
Assertion verbosity levels:
0 Write only file and line for failed assertions
1 Write file, line number, function and reason for failed assertions
2 Log also successful assertions



:Symbol:           ZTEST_ASSERT_VERBOSE
:Type:             int
:Value:            ""
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Assertion verbosity level" if ZTEST (value: "n")
:Default values:

 *  1 (value: "n")
 *   Condition: ZTEST (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../tests/ztest/Kconfig:37