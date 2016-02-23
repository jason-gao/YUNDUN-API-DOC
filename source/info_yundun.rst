.. _api-info:

API说明
=======

.. _specification:

API开发规范
------------    

1. 关于滥用：
    以下这些，但并不限于以下这些行为都被视为滥用：
        * 短时间内大量添加、删除、修改、刷新域名或者记录，或者设置记录状态。
        * 其它没有提到的，但会给系统带来压力的请求行为。

2. 关于封禁：
    由于滥用API将会导致账号在API中封禁，但并不影响在官方网站上的使用，封禁一定的时间后会自动解除，一般需要一个小时后才会解封，所以请小心操作，不要拿API进行大量测试。

3. 接口交互方式:
    数据交互方式：通过HTTP协议进行数据交互，即通过HTTP的POST请求响应方式，接口调用方通过发送带参数的请求URL，被调用方接收请求参数并执行业务，结束后将执行结果以纯文本形式返回给调用方。

4. 请求方法：
    只支持POST方法请求数据，用其它方法会提示相关错误。

5. 关于编码：
    请求URL字符编码：UTF-8，相应操作结果字符编码：UTF-8。

6. 技术支持：
    * 帮助中心：http://www.yundun.cn/help/
    * 公司电话：400-999-7070

.. _API_CALL:

API调用
------------
1. 先到yundun官网注册用户，申请app_id,app_secret
2. yundun提供sdk，供用户调用


.. _common_parameters:

公共参数
---------
所有的接口都需要传递这2个参数。
    * app_id 分配的调用接口身份id，必选
    * sign 根据app_id和调用参数生成的签名，必选
    * user_id 用户id，仅代理接口需要，需要操作的用户

.. _common_response:

共通返回
---------
这些返回在所有的接口都有可能返回，它们是所有接口共通的，在此统一说明，下面的接口将不再列出。
    * '-1'  => '只允许 POST 方法',
    * '-2'  => 'app_id不能为空',
    * '-3'  => 'API 使用超出限制',
    * '-4'  => '参数错误',
    * '-5'  => 'api帐号验证不通过',
    * '-6'  => 'api帐号已被暂停',
    * '-7'  => '登录失败次数过多，账号被暂时封禁',
    * '-10' => '非法操作',
    * '-11' => '请检查必填参数',
    * '0'   => '操作失败',
    * '1'   => '操作成功',
    * '602' => 'Signed request has an invalid signature.',
    * '604' => 'Signed request did not pass CSRF validation.',
    * '605' => 'Signed request is using the wrong algorithm.',
    * '606' => 'Malformed signed request.',
    * '607' => 'Signed request has malformed encoded signature data.',
    * '608' => 'Signed request contains malformed base64 encoding.', 
    * '8005' => 'app_id not exist',
    * '8007' => 'sign not exist',
    * '8008' => 'app已禁用'
