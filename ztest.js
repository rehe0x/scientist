
// var url = 'https://limit.yysports.com/limitelotterybeijing/activity/registitems';
// // var url1 = 'https://wx.yysports.com/limitelottery/regist/checkssologin?code=${code}&redirecturl=form.html?activityId=${this.activityId}'
// const headerss = {
//    'Accept': '*/*',
//    'Accept-Encoding': 'gzip, deflate, br',
//    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
//    'Connection': 'keep-alive',
//    'Host': 'limit.yysports.com',
//    'Referer': 'https://limit.yysports.com/limitelotterybeijing/registresult.html?activityId=0',
//    'Sec-Fetch-Dest': 'empty',
//    'Sec-Fetch-Mode': 'cors',
//    'Sec-Fetch-Site': 'same-origin',
//    'X-Requested-With': 'XMLHttpRequest',
//    'Cookie':'acw_sc__v3=5fbf7738cbccb07728183923170c5df85d89516b11',
//   //  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36',
//    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJsaW1pdGVkX2VkaXRpb25fbG90dGVyeSIsImlhdCI6MTYwNjM3MjQxMCwianRpIjoiMzg1MjI5MDgiLCJzdWIiOiIxODU4MzE1ODAwNyIsImxpbWl0ZWRVc2VyIjp0cnVlfQ.bVUHSBMpkGKmjjh4iYPCPNlUK3ccOm6UNsqCh00ff4E'
//   }


// var request = require('request')


// request({
//   url: url,  // 请求的URL
//   method: 'GET', 
//   // proxy: 'http://113.194.29.40:9999',
//   headers: headerss
// }, function (error, response, body) {
//     console.log(response) // 输出网页内容
// });


var url = 'https://sso-prod.yysports.com/api/member/pousheng/account/login'
var data = {
  'username' : '18583158007',
  'password': new Buffer('xiehong123').toString('base64'),
  'client_id': 'matrix',
  'redirect_uri': 'https://wx.yysports.com/limitelotterybeijing/registresult.html?activityId=0',
  'response_type': 'code',
  'state': 'fd87828dd5ce44fd9fa530e177fafb02'
}

const headerss = {
   'Accept': '*/*',
   'Accept-Encoding': 'gzip, deflate, br',
   'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
   'Connection': 'keep-alive',
   'Host': 'sso-prod.yysports.com',
   'Origin': 'https://sso-prod.yysports.com',
   'Sec-Fetch-Dest': 'empty',
   'Sec-Fetch-Mode': 'cors',
   'Sec-Fetch-Site': 'same-origin',
   'X-Requested-With': 'XMLHttpRequest',
   'Cookie':'acw_sc__v3=5fbf7738cbccb07728183923170c5df85d89516b11',
  }


var request = require('request')


request({
  url: url,  // 请求的URL
  method: 'POST', 
  data : data,
  proxy: 'http://113.194.29.40:9999',
  headers: headerss
}, function (error, response, body) {
    console.log(response) // 输出网页内容
});