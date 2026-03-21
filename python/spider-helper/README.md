# spider-helper

```
import sh # 导入
get = sh.get_url('https://example.net/') # 爬虫
```
1. `get[0]`   xpath
> `get[0]('your xpath')`
2. `get[1]`   html原文
3. `get[2]`   请求到的链接
> 可以检测重定向或制作短链接还原
