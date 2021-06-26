## ffmpeg API
### 用户提交 视频URL 开始和结束时间戳，返回视频URL。

#### 项目环境： 
    DJANGO，使用微服务框架

### 需求分析：
    1.数据库日志功能
    2.token用户验证功能（可在项目中配置）考虑部署问题
    3.主动推送（完成提醒）
    4.错误信息完整性（枚举）
    5.ffmpeg采用多线程，可以回调数据更新。

## 架构设计：
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

