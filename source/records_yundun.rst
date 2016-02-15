记录相关
========

.. _Cname.Record.add:

添加cname记录
--------------------
接口地址：
    * http://api.yundun.cn/V1/Cname.Record.add
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * name 子域名 如www.baidu.com,只需要填www
    * value  源ip  数组 [{"view":"any", "ip":"1.1.1.1"},{"view":"any", "ip":"2.2.2.2"}]
响应代码：
    * 共通返回
    * 1001 域名不能为空
	* 2002 主机记录格式不正确
	* 2003 源IP格式不正确
	* 2005 记录必须有默认线路
    * 2011 主机记录必须
    * 2019 此子域名已存在,如需修改记录点编辑
	* 2022 源ip不能为空
	* 2421 IP不能是局域网Ip
	* 2023 记录重复
	

示例::

    curl -X POST http://api.yundun.cn/V1/Cname.Record.add -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
    
返回参考：

    * JSON::

	{
		"status": {
			"code": 1,
			"message": "操作成功",
			"create_at": "2015-10-20 18:06:36"
		},
		"record": {
			"subdomain": "bb.91ri.org",
			"cname": "d2ba95f6.91ri.org.cname.jsd.cc."
		}
	}

.. _Cname.Record.list:

CNAME记录列表
------------------------
接口地址：
    * http://api.yundun.cn/V1/Cname.Record.list
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id 域名id 必选
响应代码：
    * 共通返回
    * 2001 域名不存在

注意事项：
    * 

示例::

     curl -X POST http://api.yundun.cn/V1/Cname.Record.list -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
    
返回参考：

    * JSON::

		{
			"status": {
				"code": 1,
				"message": "操作成功",
				"create_at": "2015-10-20 18:12:19"
			},
			"records": [
				{
					"subdomain": "aa.cname2015091702.com",
					"cname": "76d984fe.cname2015091702.com.cname.jsd.cc.",
					"protected": false,
					"view_balance": [],
					"view_balance_format": "",
					"useloadbalance": false,
					"href": "http://aa.cname2015091702.com",
					"records": [
						{
							"id": "40581",
							"domain": "aa.cname2015091702.com",
							"balance_group_id": "1760",
							"balance_status": "0",
							"view": "any",
							"host": "2.2.2.2",
							"cname": "76d984fe.cname2015091702.com.cname.jsd.cc.",
							"record_status": "0",
							"parent_id": "40506",
							"view_text": "默认"
						},
						{
							"id": "40580",
							"domain": "aa.cname2015091702.com",
							"balance_group_id": "1760",
							"balance_status": "0",
							"view": "any",
							"host": "1.1.1.1",
							"cname": "76d984fe.cname2015091702.com.cname.jsd.cc.",
							"record_status": "0",
							"parent_id": "40506",
							"view_text": "默认"
						}
					],
					"moreRecords": null,
					"hasMoreRecords": false
				},
			],
			"domain_info": {
				"domain": "cname2015091702.com",
				"domain_id": "40506",
				"level": "1"
			}
		}

.. _Cname.Record.modify:

修改CNAME记录
-------------------------
接口地址：
    *  http://api.yundun.cn/V1/Cname.Record.modify
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain 域名，必选
    * record 
响应代码：
    * 共通返回
    * 1029 子域名不能为空
    * 2026 子域名不属于此用户
    * 2002 主机记录格式不正确
    * 2024 请将线路源ip填写完整
    * 2022 源ip不能为空
    * 2003 源IP格式不正确
    * 2421 IP不能是局域网Ip
    * 2023 记录重复
    * 2005 记录必须有默认线路	

示例::

    curl -X POST http://api.yundun.cn/V1/Cname.Record.modify -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
   
返回参考：

    * JSON::

	{
		"status": {
			"code": 1,
			"message": "操作成功",
			"create_at": "2015-10-20 18:18:24"
		},
		"record": [
			{
				"subdomain": "aa.cname2015091702.com",
				"any": "1.1.1.1",
				"record_id": "40584"
			},
			{
				"subdomain": "aa.cname2015091702.com",
				"any": "2.2.2.2",
				"record_id": "40585"
			}
		]
	}

.. _Cname.Record.remove:

删除CNAME记录
--------------------------
接口地址：
    *  http://api.yundun.cn/V1/Cname.Record.remove
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain 域名，必选
	* subdomain 子域名 例如www.yundun.cn
响应代码：
    * 共通返回
    

示例::

    curl -X POST http://api.yundun.cn/V1/Cname.Record.remove -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
    
返回参考：

    * JSON::

        {
            "status": {
                "code":"1",
                "message":"操作成功",
                "created_at":"2013-05-30 15:39:05"
            }
        }

