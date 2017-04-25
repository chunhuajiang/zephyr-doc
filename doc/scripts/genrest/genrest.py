# Prints a tree of all items in the configuration
# vim: tabstop=4 shiftwidth=4 expandtab

import kconfiglib
import sys

# Integers representing symbol types
UNKNOWN, BOOL, TRISTATE, STRING, HEX, INT = range(6)

# Strings to use for types
TYPENAME = {UNKNOWN: "unknown", BOOL: "bool", TRISTATE: "tristate",
            STRING: "string", HEX: "hex", INT: "int"}

done = []

def print_with_indent(s, indent):
    print((" " * indent) + s)

def print_items(items, outdir, indent):
    for item in items:
        if item.is_symbol() or item.is_choice():
            text = item.get_help()
        elif item.is_menu():
            text = item.get_title()
        else:
            # Comment
            text = item.get_text()
        if item.is_symbol():
            #print_with_indent("config {0}".format(item.get_name()), indent)

            var = "CONFIG_%s" %item.get_name()
            if not var in done:
                done.append(var)
                f.write("   * - :option:`%s`\n" %var)
                if len(item.get_prompts()) > 0:
                    p = item.get_prompts()[0]
                else:
                    p = ""
                f.write("     - %s\n" %p)
                config = open("%s/%s.rst" % (outdir, var), "w")
                config.write(":orphan:\n\n")
                config.write(".. title:: %s\n\n"
                    %item.get_name())
                config.write(".. option:: CONFIG_%s:\n" %item.get_name())
                config.write(".. _CONFIG_%s:\n" %item.get_name())
                if text:
                    config.write("\n%s\n\n" %text)
                else:
                    config.write("\nThe configuration item %s:\n\n" %var)
                config.write(item.rest())

                config.close()
        elif item.is_menu():
            #print_with_indent('menu "{0}"'.format(item.get_title()), indent)
            print_items(item.get_items(), outdir, indent + 2)
        elif item.is_choice():
            #print_with_indent('choice', indent)
            print_items(item.get_items(), outdir, indent + 2)
        elif item.is_comment():
            pass
            #print_with_indent('comment "{0}"'.format(item.get_text()), indent)


f = open("%s/index.rst" % (sys.argv[2]), "w")
f.write(""".. _configuration:

配置选项参考指南
#####################################

简介
************

Kconfig 文件描述了编译系统所支持的配置符号、逻辑组织和结构（将符号以菜单和子菜单的方式组合起来）、不同配置符号间关系。

Kconfig 文件遍布于整个编写目录中，它们以其通用特性和被添加到配置菜单的新符号组织在一起。

配置选项信息由 :program:`Kconfig` 抽取而来，且由脚本文件 :file:`~/doc/scripts/genrest/genrest.py` 产生。

所支持的选项
*****************

""")
f.write(".. list-table:: Configuration Options\n\n")
conf = kconfiglib.Config(sys.argv[1])
print_items(conf.get_top_level_items(), sys.argv[2],  0)
f.close()
