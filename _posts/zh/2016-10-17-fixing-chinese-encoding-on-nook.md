---
layout: post
title: "如何解决nook中的中文问号乱码问题"
date: 2016-10-17 22:50:33
lang: zh
ref: fixing-chinese-encoding-on-nook
tags: [tech]
redirect_from:
  - "/科学技术/2016/10/17/如何解决nook中的中文问号乱码问题.html"
---
以下内容参考于网上的解决方案，供大家参考与自己备案（估计已经没有谁用这么老的电子书了）。

1. 首先在calibre里面选择转换
2. 在样式和外观里面有一项样式，其中有 Extra CSS 的输入框，在其中输入以下样式代码：

```
@font-face {
font-family: “DroidFont”, serif, sans-serif;
font-weight: normal;
font-style: normal;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: “DroidFont”, serif, sans-serif;
font-weight: bold;
font-style: normal;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: “DroidFont”, serif, sans-serif;
font-weight: normal;
font-style: italic;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
@font-face {
font-family: “DroidFont”, serif, sans-serif;
font-weight: bold;
font-style: italic;
src: url(res:///system/fonts/DroidSansFallback.ttf);
}
body { font-family: “DroidFont”, serif;}
```
究其原因，还是中文字体支持的问题。所以如网上其他方案，将epub转为.zip文件，然后修改其中的css样式文件，应该也是可以的。这里就偷个懒，直接用calibre的bulk convert处理了。
