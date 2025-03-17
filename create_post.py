#!/usr/bin/env python3
import os
from datetime import datetime
import sys

def create_post_template(title):
    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 生成文件名（使用当前日期和标题）
    # 确保文件创建在_posts目录下
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)
    filename = os.path.join(posts_dir, f"{datetime.now().strftime('%Y-%m-%d')}-{title}.md")
    
    # 创建文件内容
    content = f"""---
layout: post
title:  {title}
date:   {current_time} +0800
categories: daily
---

----------------
原创文章如转载，请注明出处""aicracker.com"
"""
    
    # 写入文件
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"已创建文件: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python create_post.py '文章标题'")
        sys.exit(1)
    
    title = sys.argv[1]
    create_post_template(title) 