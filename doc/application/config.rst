.. _config:

配置
##############################

Application Configuration
*************************

The application's kernel is configured using a set of configuration options
that can be customized for application-specific purposes.
The Zephyr build system takes a configuration option's value from the first
source in which it is specified.

The available sources are (in order):

#. The application's current configuration. (i.e. The :file:`.config` file.)

#. The application's default configuration. (i.e. The :file:`.conf` file.)

#. The board configuration used by the application.
   (i.e. The board's :file:`.defconfig` file.)

#. The kernel's default configuration.
   (i.e. One of the kernel's :file:`Kconfig` files.)

For information on available kernel configuration options, including
inter-dependencies between options, see the :ref:`configuration`.

Default Board Configuration
===========================

An application's :file:`.conf` file defines its default kernel configuration.
The settings in this file override or augment the board configuration settings.

The board configuration settings can be viewed
in :file:`\$ZEPHYR_BASE/boards/ARCHITECTURE/BOARD/BOARD_defconfig`.

.. note::

   When the default board configuration settings are sufficient for your
   application, a :file:`.conf` file is not needed. Skip ahead to
   :ref:`override_kernel_conf`.


#. Navigate to the :file:`app`, and create the :file:`prj.conf` file. Enter:

   .. code-block:: bash

       $ vim prj.conf

   The default name is :file:`prj.conf`. The filename must match the
   ``CONF_FILE`` entry in the application :file:`Makefile`.

#. Edit the file and add the appropriate configuration entries.

   a) Add each configuration entry on a new line.

   b) Begin each entry with ``CONFIG_``.

   c) Ensure that each entry contains no spaces
      (including on either side of the = sign).

   d) Use a # followed by a space to comment a line.

   The example below shows a comment line and a board
   configuration override in the :file:`prj.conf`.

   .. code-block:: c

       # Enable printk for debugging
       CONFIG_PRINTK=y

#. Save and close the file.

.. _override_kernel_conf:

Overriding Default Configuration
================================

Override the default board and kernel configuration to temporarily alter the
application's configuration, perhaps to test the effect of a change.

.. note::

   If you want to permanently alter the configuration you
   should revise the :file:`.conf` file.

Configure the kernel options using a menu-driven interface. While you can add
entries manually, using the configuration menu is a preferred method.


#. Run the :command:`make menuconfig` rule to launch the menu-driven interface.

   a) In a terminal session, navigate to the application directory
      (:file:`~/app`).

   b) Enter the following command:

      .. code-block:: bash

          $ make [BOARD=<type>] menuconfig

      A question-based menu opens that allows you to set individual configuration
      options.

      .. image:: figures/app_kernel_conf_1.png
           :width: 600px
           :align: center
           :alt: Main Configuration Menu

#. Set kernel configuration values using the following
   key commands:

   * Use the arrow keys to navigate within any menu or list.

   * Press :kbd:`Enter` to select a menu item.

   * Type an upper case :kbd:`Y` or :kbd:`N` in the
      square brackets :guilabel:`[ ]` to
      enable or disable a kernel configuration option.

   * Type a numerical value in the round brackets :guilabel:`( )`.

   * Press :kbd:`Tab` to navigate the command menu at the bottom of the display.

     .. note::

       When a non-default entry is selected for options that are non-numerical,
       an asterisk :kbd:`*` appears between the square brackets in the display.
       There is nothing added added the display when you select the option's
       default.

#. For information about any option, select the option and tab to
   :guilabel:`<Help >` and press :kbd:`Enter`.

   Press :kbd:`Enter` to return to the menu.

#. After configuring the kernel options for your application, tab to
   :guilabel:`< Save >` and press :kbd:`Enter`.

   The following dialog opens with the :guilabel:`< Ok >` command selected:

   .. image:: figures/app_kernel_conf_2.png
      :width: 400px
      :align: center
      :height: 100px
      :alt: Save Configuration Dialog


#. Press :kbd:`Enter` to save the kernel configuration options to the default
   file name; alternatively, type a file name and press :kbd:`Enter`.

   Typically, you will save to the default file name unless you are
   experimenting with various configuration scenarios.

   An :file:`outdir` directory is created in the application directory. The
   outdir directory contains symbolic links to files under
   :file:`\$ZEPHYR_BASE`.

   .. note::

      At present, only a :file:`.config` file can be built. If you have saved
      files with different file names and want to build with one of these,
      change the file name to :file:`.config`. To keep your original
      :file:`.config`, rename it to something other than :file:`.config`.

   Kernel configuration files, such as the :file:`.config` file, are saved
   as hidden files in :file:`outdir`. To list all your kernel configuration
   files, enter :command:`ls -a` at the terminal prompt.

   The following dialog opens, displaying the file name the configuration
   was saved to.

   .. image:: figures/app_kernel_conf_3.png
         :width: 400px
         :align: center
         :height: 150px
         :alt: Saved Configuration Name Dialog

#. Press :kbd:`Enter` to return to the options menu.

#. To load any saved kernel configuration file, tab to :guilabel:`< Load >` and
   press :kbd:`Enter`.

   The following dialog opens with the :guilabel:`< Ok >` command selected:

   .. image:: figures/app_kernel_conf_4.png
      :width: 400px
      :align: center
      :height: 175px
      :alt: Configuration File Load Dialog

#. To load the last saved kernel configuration file, press :guilabel:`< Ok >`,
   or to load another saved configuration file, type the file name, then select
   :guilabel:`< Ok >`.

#. Press :kbd:`Enter` to load the file and return to the main menu.

#. To exit the menu configuration, tab to :guilabel:`< Exit >` and press
   :kbd:`Enter`.

   The following confirmation dialog opens with the :guilabel:`< Yes >`
   command selected.

   .. image:: figures/app_kernel_conf_5.png
      :width: 400px
      :align: center
      :height: 100px
      :alt: Exit Dialog

#. Press :kbd:`Enter` to retire the menu display and return to the console
   command line.
