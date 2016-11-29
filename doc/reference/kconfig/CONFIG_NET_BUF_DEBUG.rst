:orphan:

.. title:: NET_BUF_DEBUG

.. option:: CONFIG_NET_BUF_DEBUG:
.. _CONFIG_NET_BUF_DEBUG:

Enable debug logs and checks for the generic network buffers.



:Symbol:           NET_BUF_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Network buffer debugging" if NET_BUF (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NET_BUF (value: "n")
:Selects:

 *  :option:`CONFIG_STDOUT_CONSOLE` if NET_BUF (value: "n")
 *  :option:`CONFIG_SYS_LOG` if NET_BUF (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../net/Kconfig:30