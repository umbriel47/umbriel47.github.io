---
layout: post
title: "tensorflow相关小问题"
date: 2022-04-08 13:21:50 +0800
lang: zh
ref: tensorflow-gotchas
tags: [notes]
redirect_from:
  - "/daily/2022/04/08/tensorflow相关小问题.html"
---

1.  AttributeError: module 'tensorflow._api.v2.io.gfile' has no attribute 'get_filesystem' #47139 
2.  Projector tab is blank in Tensorboard (no checkpoint was found) error in tensorboard

#### AttributeError: module 'tensorflow._api.v2.io.gfile' has no attribute 'get_filesystem' #47139 
解决方案：参考[pytorch issue #47139][pytorch]

import tensorflow as tf
import tensorboard as tb
tf.io.gfile = tb.compat.tensorflow_stub.io.gfile

[pytorch]: https://github.com/pytorch/pytorch/issues/47139

#### Projector tab is blank in Tensorboard (no checkpoint was found) error in tensorboard

Solution: Restart the tensorboard, because the projector loading is not dynamic. It will only show the embeddings writed in logdir before tensorboard cli starts.
