:orphan:

.. title:: SYS_LOG_SHOW_TAGS

.. option:: CONFIG_SYS_LOG_SHOW_TAGS:
.. _CONFIG_SYS_LOG_SHOW_TAGS:

Prefixes all log lines with an identifier to the log level submitted in
the C code.



:Symbol:           SYS_LOG_SHOW_TAGS
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Prepend level tags to logs" if SYS_LOG (value: "n")
:Default values:

 *  y (value: "y")
 *   Condition: SYS_LOG (value: "n")
:Selects:
 (no selects)
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../misc/Kconfig:275