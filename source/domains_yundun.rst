域名相关
========

.. _Domain.add:

添加新域名
-----------
接口地址：
    * http://api.yundun.cn/V1/Domain.add
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain 域名, 没有 www, 如 yundun.com
    * type 类型{cname|ns}，接入方式，可选参数，默认ns
响应代码：
    * 共通返回
    * 1001 域名为空
    * 1002 域名格式不正确
    * 1003 域名后缀不被支持
    * 1004 该域名为系统保护域名，不能被添加！
    * 1005 该域名(CNAME)已存在！
    * 1006 该域名(NS)已存在！
    * 1008 域名类型只能是cname|ns
    * 1011 域名在黑名单中
    * 1054 域名(别名)已存在
    * 1055 域名长度不能超过64个字符
    * 8534 企业用户必须提交资料审核通过才可以添加域名
	
示例::

    curl -X POST http://api.yundun.cn/V1/Domain.add  -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

    * JSON::
		
		{
			"status": {
				"code": 1,
				"message": "操作成功",
				"create_at": "2015-10-20 17:22:31"
			},
			"data": {
				"domain_id": "40573",
				"type": "cname",
				"domain": "cname2015102002.com",
				"dashboard_id": "21852"
			}
		}

.. _Domain.list:

获取域名列表
-------------
接口地址：
    * http://api.yundun.cn/V1/Domain.list
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
	* p 当前页 默认1
	* pagesize 每页显示多少 默认10
	* domain_type {cname|ns} 获取cname域名还是ns域名，不传获取所有域名
	
响应代码：
    * 共通返回

示例::
    
    curl -X POST http://api.yundun.cn/V1/Domain.list -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'

返回参考：

   * JSON::

       {
			"status": {
				"code": 1,
				"message": "操作成功",
				"create_at": "2015-10-20 17:26:51"
			},
			"domains": [
				{
					"id": "40573",
					"addtime": "2015-10-20 17:23:07",
					"domain": "cname2015102002.com",
					"expiry_time": "2015-11-19 00:00:00",
					"level_id": "0",
					"useyundun": "0",
					"domain_status": "11",
					"domain_type": "cname",
					"control_id": "21852",
					"level_name": null,
					"group_id": null,
					"dns_or_web": null,
					"zzkd_status": false,
					"zzkd_expiry_time": null,
					"zzkd_product_id": null,
					"gfdns_status": false,
					"gfdns_expiry_time": null,
					"gfdns_product_id": null,
					"dlssl_status": false,
					"dlssl_expiry_time": null,
					"dlssl_product_id": null,
					"status_name": "向导第二步",
					"is_expiry": false,
					"expiry_time_format": "2015-11-19",
					"control_url": "/cname/step2/record_list/40573",
					"control_text": "继续向导",
					"zzkd_is_expiry": true,
					"zzkd_buy": false,
					"zzkd_name": "增值抗D,100G套餐",
					"zzkd_expiry_time_format": "1970-01-01",
					"gfdns_is_expiry": true,
					"gfdns_buy": false,
					"gfdns_name": "高防DNS增值,100G+100万QPS",
					"gfdns_expiry_time_format": "1970-01-01",
					"dlssl_is_expiry": true,
					"dlssl_buy": false,
					"dlssl_name": "独立SSL",
					"dlssl_expiry_time_format": "1970-01-01"
				} 
			],
			"total": "1"
		}

.. _Domain.remove:

删除域名
---------
接口地址：
    * http://api.yundun.cn/V1/Domain.remove
HTTP请求方式：
    * POST
请求参数：
    * 公共参数
    * domain，域名
    * domain_type {cname|ns}
响应代码：
    * 共通返回

示例::

    curl -X POST http://api.yundun.cn/V1/Domain.remove -d 'app_id=b0de1etPkjqJfjvWmDOW&sign=xxx'
    
返回参考：

    * JSON::
        
	{
		"status": {
			"code": 1,
			"message": "操作成功",
			"create_at": "2015-10-20 17:34:30"
		}
	}


