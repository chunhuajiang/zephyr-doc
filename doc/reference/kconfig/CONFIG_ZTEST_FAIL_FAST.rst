:orphan:

.. title:: ZTEST_FAIL_FAST

.. option:: CONFIG_ZTEST_FAIL_FAST:
.. _CONFIG_ZTEST_FAIL_FAST:

Stop and abort on first failing test. Do not continue with other
tests that might be in the queue.



:Symbol:           ZTEST_FAIL_FAST
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Abort on first failing test" if ZTEST (value: "n")
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
 * ../tests/ztest/Kconfig:29