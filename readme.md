# 视频拼接

传入几个视频和需要给拼接后的视频添加的BGM音乐，就可以直接帮你把所有视频按顺序合成一个视频，并配上指定的BGM音乐。

**支持的功能列表：**
1. 视频拼接
2. 添加转场
    1. 1.0不支持转场
    2. 2.0支持选择固定的一个转场`待开发`
    3. 3.0支持在每个衔接处指定不同的转场`待开发`
3. 添加统一音频
    1. 需要去掉原有视频的音频


> 💡 每个视频的分辨率和码率必须一样

请求JSON：

```jsx
{
    "Action": "SpliceVideo",
    "Data": {
        "Input": {
            "URLs": [
                "xxxx",
                "xxxx"
            ],
            "Audio": "xxx.mp3",
            "Transitions": "None",
            "CallbackURL": "https://xxxx/release/callback"
        },
        "Output": {
            "Vod": {
                "Region": "ap-beijing",
                "SubAppId": 101
            }
        }
    }
}
```

字段解释

| 字段 | 类型 | 解释 |
| --- | --- | --- |
| URLs | list | 要拼接的视频的顺序列表 |
| Audio | string | 拼接后的视频会使用的统一音频 |
| Transitions | enum | 转场的类型选择，目前仅支持： |
| CallbackURL | string | 回调URL |
| SubAppId | int | 要上传的VOD的subappid |
| Region | string | 要上传的VOD的地域 |

成功回调JSON：

```jsx
{
    "Result": "Success",
    "Data": {
        "OutputUrl": "xxxxx"
    },
    "RequestId": "xxxxxx"
}
```

失败回调JSON：

```jsx
{
    "Result": "Failure",
    "ErrorCode": "InternalError",
    "ErrorMessage": "internal error: xxxx",
    "RequestId": "xxxx"
}
```