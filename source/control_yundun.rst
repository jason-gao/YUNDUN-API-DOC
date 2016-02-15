控制台相关
=======================

.. _Domain.DashBoard.nodeinfo:

获取域名节点
-----------------------
接口地址：
    *  http://api.yundun.cn/V1/Domain.DashBoard.nodeinfo
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * id, 控制台id [域名返回的control_id] 必选
响应代码：
    * 共通返回

示例::

    curl -X POST http://api.yundun.cn/V1/Domain.DashBoard.nodeinfo -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
    
返回参考：

    * JSON::

	{
		"status": {
			"code": 1,
			"message": "操作成功",
			"create_at": "2015-10-20 18:52:49"
		},
		"data": {
			"node": [
				{
					"isInfo": 1,
					"line": "默认",
					"ip": "115.231.25.150",
					"enabled": 1,
					"isFireWallIp": 0,
					"isYundunIp": 0,
					"location": "长沙"
				},
				{
					"isInfo": 1,
					"line": "默认",
					"ip": "115.231.25.212",
					"enabled": 1,
					"isFireWallIp": 0,
					"isYundunIp": 0,
					"location": "monitor"
				},
				{
					"isInfo": 1,
					"line": "宁夏联通",
					"ip": "115.231.25.214",
					"enabled": 1,
					"isFireWallIp": 0,
					"isYundunIp": 0,
					"location": "monitor"
				},
				{
					"isInfo": 1,
					"line": "默认",
					"ip": "115.29.28.191",
					"enabled": 1,
					"isFireWallIp": 0,
					"isYundunIp": 0,
					"location": "张总"
				},
				{
					"isInfo": 1,
					"line": "默认",
					"ip": "61.153.111.34",
					"enabled": 1,
					"isFireWallIp": 1,
					"isYundunIp": 0,
					"location": "test"
				},
				{
					"isInfo": 0,
					"line": "华北电信",
					"ip": "61.153.111.34",
					"enabled": 1,
					"isFireWallIp": 1,
					"isYundunIp": 0,
					"location": "test"
				}
			]
		}
	}
	