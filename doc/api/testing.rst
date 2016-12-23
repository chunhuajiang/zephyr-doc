.. _testing:

Zephyr 测试框架
########################

Ztest 提供了一个简单的测试框架，用于在开发时进行测试。它提供了基本的断言宏以及一个通用的测试结构体。

该框架可以以两种方式进行使用，既可以作为集成测试的通用框架，也可以用作指定模块的单元测试。

快速开始 - 集成框架
*********************************

一个简单的工作基石位于 `samples/testing/integration` 。您只需要拷贝文件到 `tests/` 中并根据自己的需要进行编辑。sanitycheck 脚本会自动编译并运行该测试。如果您需要测 `foo` 的 `bar` 组件，您应当将例程文件夹拷贝至 test/foo/bar。然后，您就可以使用 `./scripts/sanitycheck -s tests/foo/bar/test` 进行测试。

例程包含下面的文件：

Makefile

.. literalinclude:: ../../samples/testing/integration/Makefile
   :language: Make
   :linenos:

testcase.ini

.. literalinclude:: ../../samples/testing/integration/testcase.ini
   :language: ini
   :linenos:

prj.conf

.. literalinclude:: ../../samples/testing/integration/prj.conf
   :language: text
   :linenos:

src/Makefile

.. literalinclude:: ../../samples/testing/integration/src/Makefile
   :language: Make
   :linenos:

src/main.c

.. literalinclude:: ../../samples/testing/integration/src/main.c
   :language: c
   :linenos:

.. contents::
   :depth: 1
   :local:
   :backlinks: top

快速开始 - 单元测试
**************************

Ztest 可以用于单元测试。这意味着您测试某个单一的功能时不必包含整个 Zephyr OS 工程，您只需要专注于某个指定模块的效果。这样会加速测试，因为只有该模块会被编译，且被测试函数会被直接调用。

由于没有包含依赖的基本内核数据结构体，您必须在测试时提供函数桩。Ztest 为 mocking 函数提供了一些有用的帮助，请参考后面的介绍。

在单元测试中，mock 对象可用于仿真真实的复杂对象的行为，还可以通过判断某个对象是否有交互作用而判断测试是否成功。如果有需要，还可以断言交互的顺序。

`samples/testing/unit` 文件夹中包含了测试 Zephyr 的 net-buf 的 API 的例程。

Makefile

.. literalinclude:: ../../samples/testing/unit/Makefile
   :language: Make
   :linenos:

testcase.ini

.. literalinclude:: ../../samples/testing/unit/testcase.ini
   :language: ini
   :linenos:

main.c

.. literalinclude:: ../../samples/testing/unit/main.c
   :language: c
   :linenos:

API 参考
*************

运行
-------------

.. doxygengroup:: ztest_test
   :project: Zephyr
   :content-only:

断言
----------

如果相关的断言失败，这些宏将立即失败。当断言失败后，它会打印当前文件、行数和函数，以及失败的原因和可选消息。如果配置选项 `CONFIG_ZTEST_ASSERT_VERBOSE=0` ，断言时只会打印文件和行数，从而可以减小测试镜像的尺寸。


`assert_equal(buf->ref, 2, "Invalid refcount")` 测试失败时的输出是这样的：

.. code-block:: none

    Assertion failed at main.c:62: test_get_single_buffer: Invalid refcount (buf->ref not equal to 2)
    Aborted at unit test function

.. doxygengroup:: ztest_assert
   :project: Zephyr
   :content-only:

Mocking
-------

这些功能允许对回调函数和相关函数进行抽象化，并在测试中进行控制。您可以修改测试的配置文件中的选项 `CONFIG_ZTEST_MOCKING=y` 来使能 mocking 框架。并发返回值和期待的参数的数量由  `ZTEST_PARAMETER_COUNT` 进行限制。

下面是一个例程，它希望函数 `expect_two_parameters` 的 `a=2` 和 `b=3`，然后 `returns_int` 返回 `5`：

.. literalinclude:: mocking.c
   :language: c
   :linenos:

.. doxygengroup:: ztest_mock
   :project: Zephyr
   :content-only:
