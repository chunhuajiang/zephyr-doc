:orphan:

.. title:: NET_BUF_SIMPLE_DEBUG

.. option:: CONFIG_NET_BUF_SIMPLE_DEBUG:
.. _CONFIG_NET_BUF_SIMPLE_DEBUG:

Enable extra debug logs and checks for the generic network buffers.



:Symbol:           NET_BUF_SIMPLE_DEBUG
:Type:             bool
:Value:            "n"
:User value:       (no user value)
:Visibility:       "n"
:Is choice item:   false
:Is defined:       true
:Is from env.:     false
:Is special:       false
:Prompts:

 *  "Network buffer memory debugging" if NET_BUF_DEBUG (value: "n")
:Default values:

 *  n (value: "n")
 *   Condition: NET_BUF_DEBUG (value: "n")
:Selects:

 *  :option:`CONFIG_STDOUT_CONSOLE` if NET_BUF_DEBUG (value: "n")
 *  :option:`CONFIG_SYS_LOG` if NET_BUF_DEBUG (value: "n")
:Reverse (select-related) dependencies:
 (no reverse dependencies)
:Additional dependencies from enclosing menus and ifs:
 (no additional dependencies)
:Locations:
 * ../net/Kconfig:39