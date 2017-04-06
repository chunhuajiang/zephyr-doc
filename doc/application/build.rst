.. _build:

编译
######################

Build an Application
********************

The Zephyr build system compiles and links all components of an application
into a single application image that can be run on simulated hardware or real
hardware.


#. Navigate to the application directory :file:`~/app`.

#. Enter the following command to build the application's :file:`zephyr.elf`
   image using the configuration settings for the board type specified
   in the application's :file:`Makefile`.

   .. code-block:: console

       $ make

   If desired, you can build the application using the configuration settings
   specified in an alternate :file:`.conf` file using the :code:`CONF_FILE`
   parameter. These settings will override the settings in the application's
   :file:`.config` file or its default :file:`.conf` file. For example:

   .. code-block:: console

       $ make CONF_FILE=prj.alternate.conf

   If desired, you can build the application for a different board type than the
   one specified in the application's :file:`Makefile` using the :code:`BOARD`
   parameter. For example:

   .. code-block:: console

       $ make BOARD=arduino_101

   Both the :code:`CONF_FILE` and :code:`BOARD` parameters can be specified
   when building the application.

Rebuilding an Application
*************************

Application development is usually fastest when changes are continually tested.
Frequently rebuilding your application makes debugging less painful
as the application becomes more complex. It's usually a good idea to
rebuild and test after any major changes to the application's source files,
Makefiles, or configuration settings.

.. important::

    The Zephyr build system rebuilds only the parts of the application image
    potentially affected by the changes. Consequently, rebuilding an application
    is often significantly faster than building it the first time.

Sometimes the build system doesn't rebuild the application correctly
because it fails to recompile one or more necessary files. You can force
the build system to rebuild the entire application from scratch with the
following procedure:


#. Navigate to the application directory :file:`~/app`.

#. Enter the following command to delete the application's generated files
   for the specified board type, except for the :file:`.config` file that
   contains the application's current configuration information.

   .. code-block:: console

       $ make [BOARD=<type>] clean

   Alternatively, enter the following command to delete *all* generated files
   for *all* board types, including the :file:`.config` files that contain
   the application's current configuration information for those board types.

   .. code-block:: console

       $ make pristine

#. Rebuild the application normally following the steps specified
   in `Build an Application`_ above.