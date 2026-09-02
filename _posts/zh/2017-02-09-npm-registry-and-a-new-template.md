---
layout: post
title: "npm源及换新模版"
date: 2017-02-09 00:08:45
lang: zh
ref: npm-registry-and-a-new-template
tags: [tech]
redirect_from:
  - "/科学技术/2017/02/09/npm源及换新模版.html"
---

### npm源的问题 ###

今天更换hexo主题，在安装`hexo-renderer-sass`的时候遇到了无法从github获取数据的问题。据说是因为在国内的原因，经过尝试，通过设定registry到taobao，同时使用cnpm可以解决[npm国内源问题](http://www.jianshu.com/p/0deb70e6f395)。

1. 用淘宝源替换

临时替换：
`npm --registry https://registry.npm.taobao.org install [expected package]`

持久替换：
`npm config set registry https://registry.npm.taobao.org`
`npm config get registry`

2. 安装cnpm

`npm install -g cnpm --registry=https://registry.npm.taobao.org`

3. 使用cnpm安装相应包

`cnpm i [package]`

终于不用再等待了...

### 新的主题 ###
一直找一款简洁主题，方便添加评论，标签，分类和外部链接。昨天终于找到了——[Maupassant(修改版)](https://www.haomwei.com/technology/maupassant-hexo.html)。同时还添加了[多说评论](duoshuo.com)和Google Analytics。

另：如需更改hexo new [title]生成的文件的front-matter内容，可以直接修改/`scaffolds/post.md`的内容。
