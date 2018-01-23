$(document).ready(function(){
$.ajax({
url:"/api/v1.0/getCategory",
data:{
type:"list",
token:"test"
},
type:'get',
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


//请求加载成功返回
//加载成功
function onSuccessFunction(data){


var json =eval(data)

$.each(json,function(index){
//便利jsonArray.
item = json[index]

author = item.author
name = item.name
icon = item.icon
member_since = item.member_since
summary = item.summary
url = item.url

var col= $("<div></div>")
col.addClass("col-md-4")

var card = $("<div></div>")
card.addClass("card")
card.addClass("mb-4")
card.addClass("box-shadow")
col.append(card)

// img
var img = $("<img></img>")
img.addClass("ard-img-top")
img.attr("data-src","/static/js/holder.js/100px225?theme=thumb&bg=55595c&fg=eceeef&text=Thumbnail")
//img.attr("src",icon)
card.append(img)

var card_body = $("<div></div>")
card_body.addClass("card-img-top")
card_body.addClass("card-body")
card.append(card_body)


var card_title = $("<h3></h3>")
card_title.addClass("text-primary")
card_title.html(name)
card_body.append(card_title)


var card_text = $("<p></p>")
card_text.addClass("card-text")
card_text.html(summary)
card_body.append(card_text)

var card_content = $("<dic></div>")
card_content.addClass("d-flex")
card_content.addClass("justify-content-between")
card_content.addClass("align-items-center")

card_body.append(card_content)

var btn_group = $("<div></div>")
btn_group.addClass("btn-group")

var button_1 =$("<button></button>")
button_1.addClass("btn")
button_1.addClass("btn-sm ")
button_1.addClass("btn-outline-secondary")
button_1.html("查看")

button_1.click(function(){
openUrl(url)

})
btn_group.append(button_1)

card_content.append(btn_group)
var times = $("<small></small>")
times.addClass("text-muted")
times.html(member_since)
card_content.append(times)

//添加底层div
$(".row.content").append(col)



})

}


function onFailedFunction(){
//加载失败返回


}


//跳转页面
function openUrl(url){
   $(window).attr('location',url)
}