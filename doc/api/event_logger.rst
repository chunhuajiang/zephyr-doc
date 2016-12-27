.. _event_logger:

事件日志 API
##################

.. contents::
   :depth: 1
   :local:
   :backlinks: top

事件日志器
************

事件日志器是一个对象，它可以记录重要事件的发生，以便随后被抽取并检查。

.. doxygengroup:: event_logger
   :project: Zephyr
   :content-only:

内核事件日志器
*******************

内核事件日志器记录了内核中重要事件的发生，以便随后被抽取并检查。（参考 :ref:`kernel_event_logger_v2` ）

.. doxygengroup:: kernel_event_logger
   :project: Zephyr
   :content-only:
