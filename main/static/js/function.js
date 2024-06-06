$(document).ready(function(){
  
$('#searchNews').on('click',function(){
   
       value=$('#news').val();
       mdata={"news":value}
       $.ajax({
        url:'/news_filter',
        data:mdata,
        method:'GET',
        success:function(resp){
           console.log(resp.data);
           $("#news_filter").html(resp.data)
        }
       })
});

$('#videosearch').on('click',function(){
   
   value=$('#video').val();
   mdata={"video":value}
   $.ajax({
    url:'/video_filter',
    data:mdata,
    method:'GET',
    success:function(resp){
       console.log(resp.data);
       $("#video_filter").html(resp.data)
    }
   })
});

$('#searchbooks').on('click',function(){
   
   value=$('#books').val();
   mdata={"books":value}
   $.ajax({
    url:'/books_filter',
    data:mdata,
    method:'GET',
    success:function(resp){
       console.log(resp.data);
       $("#book_filter").html(resp.data)
    }
   })
});

})