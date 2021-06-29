## ffmpeg API
### 用户提交 视频URL 开始和结束时间戳，返回视频URL。

#### 项目环境： 
    DJANGO，使用微服务框架
#### 安装
    pip install django==3.2.4 
    pip install channels==3.0.3
    pip install channels-redis==3.2.0
    pip install pymysql==1.0.2
    pip install mysqlclient==2.0.3
    环境要求 ffmpeg.exe

    
### 需求分析：
    1.数据库日志功能
    2.token用户验证功能（可在项目中配置）考虑部署问题
    3.主动推送（完成提醒）
    4.错误信息完整性（枚举）
    5.ffmpeg采用多线程，可以回调数据更新。

## 基本架构设计：
        ·ffmpeg
            ·api
                ·commit_api.py
                ·search_api.py
            ·config
                ·api.json
                ·config.py
            ·services
                ·commit_services.py
                ·search_services.py
## 数据库设计：
    ·表
        ·视频生成表 generrateVideo
            id  唯一码
            userid  用户id
            operadate   操作日期
            finished    是否已完成子进程工作
            pushback    是否已主动回传
            url         视频url地址
            iurl        视频剪辑后临时下载地址
        ·用户日志 user_log
            userId  用户id
            opedate 操作日期
            pushback 是否主动回传
            url 视频url
        ·视频文件表 hn_video
            id  唯一码
            md  md5码
            url 视频url
            path    视频存储名称和拓展名
            endtime 终止时间戳
## 配置文件
### config文件夹下api.json
    user_auth 用户验证外部接口API
    auth_message 用户验证的信息
    VIDEODIR 文件存储位置名称
    system_message 系统消息
    [
    {
        "name":"user_auth",
        "data":{
            "host":"localhost:8081/userauth",
            "closed":true
        }
    },
    {
        "name":"auth_message",
        "data":
        { 
            "SUCCESS":{"msg":"成功","state_code":200},
            "AUTHERR":{"msg":"用户验证错误","state_code":401},
            "VIDEOERR":{"msg":"请检查视频URL合法性","state_code":402},
            "TIMEERR":{"msg":"请检查视频时间合法性","state_code":403},
            "UNKNOWNERR":{"msg":"视频转换发生错误","state_code":501},
            "VIDEONOTFOUND":{"msg":"找不到视频","state_code":0}
        }
    },
    {
        "name":"VIDEODIR",
        "data":
        {
            "dir":"Videos"
        }
    },

    {
        "name":"system_message",
        "data":
        { 
            "SUCCESS":{"msg":"成功","state_code":200},
            "ERROR":{"msg":"错误","state_code":401},
            "CONTINUE":{"msg":"成功接收，并继续处理","state_code":100}
        }
    }
]

## API
    ·API: ws://host:端口/commit/
        作用:用户提交剪辑片段视频url地址，视频结果主动回传接口
        格式示例：
            {
                "userId":"11",
                "token":"111",
                "url":"www.video.com",
                "start_timestamp":"00:00:00",
                "end_timestamp":"00:01:00"
            }
        结果参照 auth_message 和 system_message
    ·API: ws://host:端口/sp/
        作用:根据用户查询项目进度
        格式示例：
            {
                "userId":"11",
                "token":"111"
                "url":"www.baidu.com" //如果url为空则显示该用户所有进度
            }
        结果参照 auth_message 和 system_message   

## 测试
    maintest.py 可实现简单的客户端提交需求,一些模块的简单单元测试

## TODO
    ✔基本架构
    ✔基本数据库设计
### · 视频剪辑提交功能API
    ✔完成用户验证API
    ✔完成视频合法性验证
    ✔完成时间合法性验证
    ✔视频剪辑线程管理
    ✔视频完成主动推送功能
### · 视频剪辑进度查询API
    ✔用户查询进度功能
    ✔单个剪辑进度查询功能
    ⚔视频临时文件下载url生成
    ⚔视频下载功能
### · 其他
    ⚔用户日志功能
    ⚔错误日志功能
