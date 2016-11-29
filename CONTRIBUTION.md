# 贡献流程
在 github 上

- 【步骤1】点击仓库右上角的 Fork 图标将仓库 fork 到你自己的账户下

在客户端

- 【步骤2】将你 fork 的仓库 clone 到本地
- 【步骤3】新建一个分支(假设分支名为`new`)，并切换到该分支
- 【步骤4】在你的`new`分支上修改文章，然后分别执行 git add、git commit 将改动提交到本地库，并记住此次提交的 commit id(假设此次提交生成的commit id 为 `9057042`)
- 【步骤5】切换回`v1.6.0`分支，先将你本地仓库的`v1.6.0`分支与我的仓库同步，依次执行：
  - `git remote add tidyjiang8 https://github.com/tidyjiang8/zephyr-doc.git`(这个步骤只需要执行一次，今后再修改文章时不用执行了)
  - `git remote update`
  - `git merge tidyjiang8`
- 【步骤6】将你在你的新分支上修改的东西合并到 v1.6.0 分支
  - 执行 `git cherry-pick <commit-id>`, 即 `git cherry-pick 9057042`
  
  > 合并`new`分支改动时，我们用`git cherry-pick`命令，而不是`git merge`命令，这样的好处是当你的`new`分支有多次提交时，你可以指定只合并某一次的提交
- 【步骤7】将你的本地 v1.6.0 分支 push 到你的远程仓库：`git push origin v1.6.0`

在 github 上

- 【步骤8】进入你的仓库,在仓库下面有个 pull request 链接，点击该链接，然后填写一些说明后提交 PR

在客户端
- 【步骤9】如果你又想修改新文章，先执行【步骤5】将你本地`v1.6.0`与我的仓库同步
- 【步骤10】切换到你的`new`分支，将本地`v1.6.0`分支的内容合并到`new`分支：`git merge v1.6.0`，然后跳转到【步骤4】依次执行

> 当你提交 PR 后，会触在服务器 http://iot-fans.xyz 上设置的编译规则。服务器会尝试拉取你提交的内容，尝试将其编译为 html 文件。如果编译有问题，请先修改你翻译的部分，然后依次执行 `git add xxx`、`git commit --amend`、`git push original v1.6.0 -f`重新提交；如果编译没有问题，我会合并你的 PR，此时会再次触发服务器的设置，并将你提交的内容自动部署到网站上 http://iot-fans.xyz/zephyr/doc/v1.6.0 上面。

# 关于文章格式
- 文档使用的是以 .rst 作为后缀的 reStructuredText 格式。你不需要学习它的语法，只需要在原始的英文文档中将对应的英文替换为中文就可以了，但是请不要破坏文档原有的格式标记。
- 请采用意译，不要采用直译，但是尽量保持与原文一致。
