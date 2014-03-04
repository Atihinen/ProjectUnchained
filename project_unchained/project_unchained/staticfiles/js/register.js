$(document).ready(function(){
	
	var username_field = $('#id_username');
	var email_field = $("#id_email");
	var company_field = $("#id_name");
	var public_field = $("#id_public");
	
	$("#process_registration").on("submit", function() {
		//Pre check if there are some name errors
		if ($("#process_registration input.ajax").length > 0){
			var content = "<ul>";
			$("#process_registration input.ajax").each(function(){
				content += "<li>"+$(this).prev().text()+" "+$(this).next().attr("data-original-title")+"</li>";
			});
			content += "</ul>";
			window.dialog("Warning", "Errors in form", content);
			return false;
		}
		var req_fields = ['id_username', 'id_password', 'id_email'];
		var check = true;
		var fields_labels = "<ul>";
		var email_reg = /@/;
		$.each(req_fields, function(i){
			var f_id = "#"+req_fields[i];
			if($(f_id).val() == ""){
				check = false;
				$(f_id).addClass("field-error");
				fields_labels += "<li>"+$(f_id).prev().text().split(":")[0]+" is required</li>";
				
			}
		});
		if($('#id_name').val() != ""){
			console.log("True"+ $("#id_name").val());
			var req_fields = ['id_name', 'id__www'];
			$.each(req_fields, function(i){
				var f_id = "#"+req_fields[i];
				console.log(f_id+": "+$(f_id).val());
				if($(f_id).val() == ""){	
					check = false;
					$(f_id).addClass("field-error");
					fields_labels += "<li>"+$(f_id).prev().text().split(":")[0]+" is required</li>";
				}
			});
		}
		if(!email_reg.test(email_field.val())){
			check = false;
			email_field.addClass("field-error");
			fields_labels += "<li>Invalid email</li>";
		}
		fields_labels += "</ul>";
		if(!check){
			window.dialog("Warning", "Errors in form", fields_labels);
		}
		return check;
	});
	
	$(".optional_fields").on("click", function(){
		var wrapper = $(this).next();		
		if (wrapper.hasClass("hidden")) {
			wrapper.slideDown("fast", function() {
				wrapper.removeClass("hidden");
			});
		}
		else {
			wrapper.slideUp("fast", function() {
				wrapper.addClass("hidden");
			});
		}

	});
	
	username_field.on("blur", function(){
		make_ajax_on_blur($(this), "user/username");
	});
	
	email_field.on("blur", function(){
		make_ajax_on_blur($(this), "user/email");
	});
	
	company_field.on("blur", function(){
		make_ajax_on_blur($(this), "company/name");
	});
	
	public_field.parent().append("<div title='Defines if your company is visible for the whole system or only your employees.' class='field-helper ui-icon ui-icon-help'></div>");
	$(".field-helper").tooltip({
		show : {
			effect : "slideDown",
			delay : 250
		},
		hide : {
			effect : "slideUp",
			delay : 250
		}
	}); 

	
});

function create_field_helper(field, message) {
	field.css("width", "95%").css("float", "left");
	field.parent().append("<div title='" + message + "' class='field-helper ui-icon ui-icon-help'></div>");
	$(".field-helper").tooltip({
		show : {
			effect : "slideDown",
			delay : 250
		},
		hide : {
			effect : "slideUp",
			delay : 250
		}
	});
}

function make_ajax_on_blur(field, type) {
	var param = field.val();
	field.removeClass("field-error").removeClass("field-success").removeClass("ajax");
	if ($.trim(param) != "") {
		$.ajax({
			type : "GET",
			contentType : "application/json; charset=utf-8",
			url : "./" + type + "/" + param + "/",
			data : "{}",
			dataType : "json",
			success : function(data) {
				var status = data["status"];
				if (status == 200) {
					field.addClass("field-success");
				} else {
					field.addClass("field-error ajax");
				}
				if (field.parent().children().length != 2) {
					field.parent().children().last().remove();
				}
				create_field_helper(field, data['msg']);

			},
			error : function(result) {
				field.addClass("field-error ajax");
				create_field_helper(field, "Network error, try again later");
			}
		});
	}

}




