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


.. _Ns.Dns.Record.create:

添加Ns[Dns]记录
--------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.create
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * sub_domain 子域名 如test
    * record_type  记录类型[A/CNAME/MX/]等
    * record_line 线路，可通过线路接口获取
    * value 记录值,例如1.1.1.1
    * mx
    * ttl 最小600
响应代码：
    * 共通返回
    * 2412 域名不能为空
    * 1009 域名不属于此用户
    * 2402 请将记录填写完整
    * 2403 主机记录格式不正确
    * 2027 主机记录不能以.结尾
    * 2421 IP不能是局域网Ip
    * 2405 记录值[ip格式不正确]
    * 2019 此子域名已存在,如需修改记录点编辑
    * 2406 CNAME记录值必须是以.结尾的域名
    * 2019 此子域名已存在,如需修改记录点编辑
    * 2407 mx记录值必须是以.结尾的域名,mx优先级必须是1-20的整数
    * 2408 txt记录值不正确
    * 2405 记录值[ip格式不正确]
    * 2019 此子域名已存在,如需修改记录点编辑
    * 3015 url长度超出限制
    * 2424 记录值格式错误，必须为域名或URL
    * 2028 只能使用默认线路
    * 2019 此子域名已存在,如需修改记录点编辑
    * 2409 ttl必须是1-604800之间
    * 2410 记录重复
    * 2411 记录必须有默认线路，否则解析可能出现问题
    * 2425 同线路A记录和CNAME记录不能同时存在
    * 2426 同线路CNAME和MX记录不能同时存在
    * 2903 请先关闭子域名保护


示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.create -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "status": {
                "code": 1,
                "message": "操作成功",
                "create_at": "2016-02-22 11:43:43"
            },
            "record": {
                "record_id": "79740",
                "domain_id": 8986,
                "sub_domain": "test",
                "sub_domain_edit": "test",
                "record_type": "A",
                "record_line": "默认",
                "line": "any",
                "value": "1.1.1.11",
                "value_edit": "1.1.1.11",
                "mx": 0,
                "ttl": 600,
                "status": 1,
                "hold": 0,
                "remark": ""
            }
        }

.. _Ns.Dns.Record.list:

Ns[Dns]记录列表
--------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.list
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * catedisplay 搜索分类，ALL[全部记录]/A[A记录]/AT_WWW[@和www记录]/CNAME[cname记录]/QYJL[启用记录]/JYJL[暂停记录]/BZJL[备注记录]
    * offset    默认0
    * length 默认10
    * query 搜索值，例如@

响应代码：
    * 共通返回
    * 2422 分类显示type错误
    * 2416 每次最多获取xx条数据
    * 2412 域名不能为空
    * 1009 域名不属于此用户
    * 2417 记录开始的偏移offset无效,最大xx


示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.list -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "status": {
                "code": 1,
                "message": "操作成功",
                "create_at": "2016-02-24 11:54:33"
            },
            "info": {
                "record_total": "4"
            },
            "records": [
                {
                    "id": "59715",
                    "domain_id": "8986",
                    "name": "@",
                    "type": "MX",
                    "view": "any",
                    "value": "mxbiz1.qq.com.",
                    "mx": "5",
                    "ttl": "600",
                    "updatetime": "2016-01-14 18:10:47",
                    "hold": "0",
                    "status": "1",
                    "order": "59715",
                    "record_status": "0",
                    "balance_group_id": "1910",
                    "balance_status": "0",
                    "rmid": null,
                    "rmremark": null,
                    "rmstatus": null,
                    "view_text": "默认",
                    "type_text": "MX"
                },
                {
                    "id": "59714",
                    "domain_id": "8986",
                    "name": "@",
                    "type": "MX",
                    "view": "any",
                    "value": "mxbiz2.qq.com.",
                    "mx": "10",
                    "ttl": "600",
                    "updatetime": "2016-01-14 18:10:47",
                    "hold": "0",
                    "status": "1",
                    "order": "59714",
                    "record_status": "0",
                    "balance_group_id": "1910",
                    "balance_status": "0",
                    "rmid": null,
                    "rmremark": null,
                    "rmstatus": null,
                    "view_text": "默认",
                    "type_text": "MX"
                },
                {
                    "id": "59713",
                    "domain_id": "8986",
                    "name": "@",
                    "type": "A",
                    "view": "any",
                    "value": "113.231.25.215",
                    "mx": "0",
                    "ttl": "600",
                    "updatetime": "2016-02-24 11:43:41",
                    "hold": "0",
                    "status": "1",
                    "order": "59713",
                    "record_status": "0",
                    "balance_group_id": "1910",
                    "balance_status": "0",
                    "rmid": null,
                    "rmremark": null,
                    "rmstatus": null,
                    "view_text": "默认",
                    "type_text": "A"
                },
                {
                    "id": "59712",
                    "domain_id": "8986",
                    "name": "@",
                    "type": "A",
                    "view": "any",
                    "value": "123.226.116.226",
                    "mx": "0",
                    "ttl": "600",
                    "updatetime": "2016-02-24 11:43:42",
                    "hold": "0",
                    "status": "1",
                    "order": "59712",
                    "record_status": "0",
                    "balance_group_id": "1910",
                    "balance_status": "0",
                    "rmid": null,
                    "rmremark": null,
                    "rmstatus": null,
                    "view_text": "默认",
                    "type_text": "A"
                }
            ]
        }


.. _Ns.Dns.Record.modify:

Ns[Dns]修改记录
--------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.modify
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * record_id 记录id
    * sub_domain 子域名 如test
    * record_type  记录类型[A/CNAME/MX/]等
    * record_line 线路，可通过线路接口获取
    * value 记录值,例如1.1.1.1
    * mx 0
    * ttl 最小600

响应代码：
    * 共通返回
    * 2412 域名不能为空
    * 2413 record_id不能为空
    * 1009 域名不属于此用户
    * 2009 记录不属于此域名
    * 2402 请将记录填写完整
    * 2403 主机记录格式不正确
    * 2027 主机记录不能以.结尾
    * 2421 IP不能是局域网Ip
    * 2405 记录值[ip格式不正确]
    * 2019 此子域名已存在,如需修改记录点编辑
    * 2406 CNAME记录值必须是以.结尾的域名
    * 2407 mx记录值必须是以.结尾的域名,mx优先级必须是1-20的整数
    * 2408 txt记录值不正确
    * 3015 url长度最多%d
    * 2424 记录值格式错误，必须为域名或URL
    * 2028 只能使用默认线路
    * 2409 ttl必须是1-604800之间
    * 2410 记录重复
    * 2411 记录必须有默认线路，否则解析可能出现问题
    * 2425 同线路A记录和CNAME记录不能同时存在
    * 2426 同线路CNAME和MX记录不能同时存在



示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.modify -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "status": {
                "code": 1,
                "message": "操作成功",
                "create_at": "2016-02-25 17:57:40"
            },
            "record": {
                "record_id": "59713",
                "domain_id": 8986,
                "sub_domain": "@",
                "sub_domain_edit": "@",
                "record_type": "A",
                "record_line": "默认",
                "line": "any",
                "value": "113.231.25.217",
                "value_edit": "113.231.25.217",
                "mx": 0,
                "ttl": 600,
                "status": "1",
                "hold": "0",
                "remark": ""
            }
        }


.. _Ns.Dns.Record.remove:

Ns[Dns]删除记录
--------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.remove
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * record_id 记录id

响应代码：
    * 共通返回
    * 2412 域名不能为空
    * 2413 record_id不能为空
    * 1009 域名不属于此用户
    * 2009 记录不属于此域名




示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.remove -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

       {
            "data": "删除成功",
            "info": "删除成功",
            "status": 1
       }


.. _Ns.Dns.Record.status:

Ns[Dns]启用/暂停记录
--------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.status
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * record_id 记录id
    * status 1启用，0暂停

响应代码：
    * 共通返回
    * 2412 域名不能为空
    * 2413 record_id不能为空
    * 1009 域名不属于此用户
    * 2009 记录不属于此域名




示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.status -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "data": {
                "domain_id": "8986",
                "record_id": "59711",
                "sub_domain": "*",
                "sub_domain_edit": "*",
                "record_type": "A",
                "record_line": "默认",
                "line": "any",
                "value": "113.231.25.215",
                "value_edit": "113.231.25.215",
                "mx": "0",
                "ttl": "600",
                "status": 0,
                "hold": "0",
                "remark": ""
            },
            "info": "暂停成功",
            "status": 1
        }

.. _Ns.Dns.Record.saverecordremark:

Ns[Dns]更新记录备注
---------------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.saverecordremark
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * record_id 记录id
    * remark 备注内容，备注不存在->添加备注，存在->更新备注，remark为空时表示清空备注

响应代码：
    * 2412 域名不能为空
    * 2413 record_id不能为空
    * 1009 域名不属于此用户
    * 2009 记录不属于此域名
    * 2423 备注字符长度只能在1-200之间




示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.saverecordremark -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "data": {
                "domain_id": "8986",
                "record_id": "59711",
                "sub_domain": "*",
                "sub_domain_edit": "*",
                "record_type": "A",
                "record_line": "默认",
                "line": "any",
                "value": "113.231.25.212",
                "value_edit": "113.231.25.212",
                "mx": "0",
                "ttl": "600",
                "status": "0",
                "hold": "0",
                "remark": "2016-03-15 13:21:26"
            },
            "info": "更新备注成功",
            "status": 1
        }


.. _Ns.Dns.Record.getrecordremark:

Ns[Dns]获取记录备注
---------------------------
接口地址：
    * http://api.yundun.cn/V1/Ns.Dns.Record.getrecordremark
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain_id  域名id 必选
    * record_id 记录id

响应代码：
    * 2412 域名不能为空
    * 2413 record_id不能为空
    * 1009 域名不属于此用户
    * 2009 记录不属于此域名




示例::

    curl -X POST http://api.yundun.cn/V1/Ns.Dns.Record.getrecordremark -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::

        {
            "status": {
                "code": 1,
                "message": "操作成功",
                "create_at": "2016-03-15 13:49:24"
            },
            "data": {
                "remark": "2016-03-15 13:49:22",
                "domain_id": 8986,
                "record_id": 59711
            }
        }

