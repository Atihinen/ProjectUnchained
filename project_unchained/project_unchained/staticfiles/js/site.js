var enable_login = $("#login_partial_enable");
var login_partial = $("#login_partial_form");
var login_enable_iID;
$(document).ready(function() {
	enable_login = $("#login_partial_enable");
	login_partial = $("#login_partial_form");
	$(".alert").alert();
	
	enable_login.on("click", function(){
		show_login_form();
		login_enable_iID = setInterval(hide_login_form, 15000);
	});
	
}); 


function dialog(splitText, title, content){
	var SplitText = splitText;
	var $dialog = $('<div></div>')
	    .html(SplitText )
	    .dialog({
	        height: 500,
	        width: 600,
	        title: title});
	
	$dialog.dialog('open');
	
	$dialog.html(content);
}

function show_login_form(){
	enable_login.fadeOut(function(){
		login_partial.removeClass("hidden").fadeIn();
	});
}

function hide_login_form(){
	login_partial.fadeOut(function(){
		login_partial.addClass("hidden");
		enable_login.fadeIn();
	});
	clearInterval(login_enable_iID);
}
