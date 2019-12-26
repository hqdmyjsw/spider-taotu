## 高质量套图爬虫


#### 大致说一下流程，爬虫先获得一个栏目网址，随后通过层层解析，得到每一个图集的的名称 、标签、和所有图片的地址并存到sqlite3数据库中，文件下载时默认命名为 图片链接的md5值。

#### 抓取和下载的过程均为多线程，可以通过调整延时来调整速度。

#### 附：
#### 1.  13MB的套图信息数据库
#### 2.	简单的多线程现在图片演示程序

### 0.照片展示

#### 这里图片下载略乱，但是可以通过简单的修改下载程序，将一套图下载在一个文件夹内。
![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/11.png)
![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/12.jpg)
![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/13.jpg)
![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/14.jpg)

###  1.字段展示
![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/1.png)

###  2.测试展示

![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/urls.png)
###  3.爬取过程展示

![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/insertdb.png)

###  4.爬取过程展示

![1](https://raw.githubusercontent.com/LookCos/spider-taotu/master/imgs/GIF.gif)
