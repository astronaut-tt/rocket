# # AssetDetection

AssetDetection是一款资源探测工具，可用于发现目标站点的文件、目录、中间件等信息，亦能够进行fuzz测试，并支持剔除指定状态码（如302、404）的结果，以及对请求成功的页面进行截图

截图功能采用的浏览器内核是PhantomJS（下载地址：https://npm.taobao.org/mirrors/phantomjs）

配合fuzzdb（下载地址：https://github.com/fuzzdb-project/fuzzdb），效果更佳 : )

备注：此工具仅用于学习，切勿用于其它用途


## 使用方法

- **资源探测**

```
python AssetDetection.py -w http://testphp.vulnweb.com/FUZZ -t 5 -f dicts.txt
```

此命令为列举出所有 http://testphp.vulnweb.com/ 与dicts.txt组合的url地址，并提示状态码和字符数

返回示例：

```
状态码           字符数            网址
200              275             http://testphp.vulnweb.com/.idea/modules.xml
404              16              http://testphp.vulnweb.com/test1.php
404              16              http://testphp.vulnweb.com/phpinfo.php
404              16              http://testphp.vulnweb.com/test2.php
404              16              http://testphp.vulnweb.com/test.php
200              4958            http://testphp.vulnweb.com/index.php
404              16              http://testphp.vulnweb.com/__index.php
200              224             http://testphp.vulnweb.com/crossdomain.xml
200              5523            http://testphp.vulnweb.com/login.php
...已省略
```

- **fuzz测试**

```
python AssetDetection.py -w http://testphp.vulnweb.com/listproducts.php?cat=FUZZ -t 5 -f dicts.txt
```

根据返回的字符数，筛选有效payload

- **剔除指定状态码**

```
python asset.py -w http://testphp.vulnweb.com/FUZZ -t 5 -f dicts.txt -c 404
```

排除404页面

返回示例：

```
状态码           字符数          网址
200              275             http://testphp.vulnweb.com/.idea/modules.xml
200              4958            http://testphp.vulnweb.com/index.php
200              5523            http://testphp.vulnweb.com/login.php
200              224             http://testphp.vulnweb.com/crossdomain.xml
...已省略
```

- **注意**

为避免截图时报错，建议将selenium版本降级

- **截图**

200 <= 响应状态码 < 300时开启截图功能

原网页（http://testphp.vulnweb.com/index.php）:

![image.png](https://xzfile.aliyuncs.com/media/upload/picture/20210814164621-1943fc1c-fcdc-1.png)

截图:

![image.png](https://xzfile.aliyuncs.com/media/upload/picture/20210814164621-1943fc1c-fcdc-1.png)
