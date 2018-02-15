<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<meta name="keywords" content="jquery">
<meta name="description" content="">
<title>voting function</title>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript">
$(function(){
	$("p a").click(function(){
		var love = $(this);
		var id = love.attr("rel");
		love.fadeOut(300);
		$.ajax({
			type:"POST",
			url:"love.php",
			data:"id="+id,
			cache:false,
			success:function(data){
				love.html(data);
				love.fadeIn(300);
			}
		});
		return false;
	});
});
</script>
<style type="text/css">
@charset "utf-8";
/* CSS Document */
html,body,div,span,h1,h2,h3,h4,h5,h6,p,pre,a,code,em,img,small,strong,sub,sup,u,i,center,dl,dt,dd,ol,ul,li,fieldset,form,label{margin:0;padding:0;border:0;outline:0;font-size:100%;vertical-align:baseline;background:transparent}
a{color:#007bc4/*#424242*/; text-decoration:none;}
a:hover{text-decoration:underline}
ol,ul{list-style:none}
body{height:100%; font:12px/18px "Microsoft Yahei", Tahoma, Helvetica, Arial, Verdana, "\5b8b\4f53", sans-serif;}
img{border:none}

.clear{clear:both}
.list{width:760px; margin:20px auto}
.list li{float:left; width:360px; height:280px; margin:10px; position:relative}
.list li p{position:absolute; top:0; left:0; width:220px; height:24px; line-height:24px; background:#fff; opacity:.8;filter:alpha(opacity=80);}
.list li p a{padding-left:30px; height:24px; background:url(images/heart.png) no-repeat 4px -1px;color:#000; font-weight:bold; font-size:14px}
.list li p a:hover{background-position:4px -25px;text-decoration:none}
</style>
</head>

<body>

<div id="main">
     <ul class="list">
     <?php
	 include_once("connect.php");
	 $sql = mysql_query("select * from pic");
	 while($row=mysql_fetch_array($sql)){
		 $pic_id = $row['id'];
		 $pic_name = $row['pic_name'];
		 $pic_url = $row['pic_url'];
		 $love = $row['love'];
	 ?>
     	<li><img src="/images/<?php echo $pic_url;?>" alt="<?php echo $pic_name;?>"><p><a href="#" title="good" class="img_on" rel="<?php echo $pic_id;?>"><?php echo $love;?></a></p></li>
        <?php }?>
     </ul>
     <div class="clear"></div>
   
</div>
</body>
</html>