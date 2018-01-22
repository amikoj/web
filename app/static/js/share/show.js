$(document).ready(function(){
$.ajax({
url:"getlist",
data:{
token:"test",
number:10

},
type:'post',
cache:false,
dataType:'json',
beforeSend:loadFunction,
success:onSuccessFunction,
error:onFailedFunction
})

})



/**
 *请求加载函数
**/
function loadFunction(){





}


function onSuccessFunction(data){
//请求加载成功返回

//加载成功

var json =eval(data)

$.each(json,function(index){
//便利jsonArray.




})

}


function onFailedFunction(){
//加载失败返回


}