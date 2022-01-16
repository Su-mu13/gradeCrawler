# 教务系统爬虫
下图的教务系统未添加验证码，这很不安全。
![image](https://user-images.githubusercontent.com/60730620/149653680-b3789b62-dc7d-439b-8621-3fbf65d798ff.png)
这个脚本是针对这样的教务系统而设计的爬虫，一般情况下新入学的学生用户名与密码都是设定好的，大多学生无法意识到弱密码的危险，就不会修改密码，如果已知大多数学生的一些基本信息，即可使用该爬虫脚本爬取每个人的教务信息，上面的脚本以爬取成绩页面为例，使用前需要准备好用户名字典和密码字典。
运行结果如下：
![image](https://user-images.githubusercontent.com/60730620/149654178-df69d1d4-b87a-4020-8889-cfe34a9507fb.png)
错误日志记录密码错误的信息
![image](https://user-images.githubusercontent.com/60730620/149654206-40a21574-9842-4bac-8079-fb9babd8cff8.png)
结果以html文件格式存储，也可以自行修改脚本，获取字段，分类存储到数据库
![image](https://user-images.githubusercontent.com/60730620/149654267-374ed191-130a-405b-9060-8c8b0283cc48.png)

