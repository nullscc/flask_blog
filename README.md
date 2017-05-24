使用flask开发的个人博客，代码原型为[flasky](https://github.com/miguelgrinberg/flasky)目前已在本人个人博客使用：[nulls.cc](http://nulls.cc/)

## 特性
* 前端参照静态博客[hexo](https://hexo.io/)主题：[jacman](https://github.com/wuchong/jacman)修改
* 由于后续可能会定制一些功能，所以不是静态博客
* 数据库使用mysql
* 使用markdown编写，并基于[md-toc.js](https://github.com/yijian166/md-toc.js)修改并生成文章目录
* 使用[highlightjs](https://highlightjs.org/)进行代码高亮
* 有简单的后台，可管理标签、编辑markdown文档等
* 图标暂时使用[awesome-font](http://www.bootcss.com/p/font-awesome/)，后续可能会使用阿里云的[iconfont](http://www.iconfont.cn/)
* 使用[gunicorn](http://gunicorn.org/)作为生产环境