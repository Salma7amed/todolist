$(document).ready(function() {

	$('form#create_task').submit(function(e){
		e.preventDefault();
		if ($.trim($("#task_title").val())) {
			create_task();
		}
	});

	$(document).on('change', 'input[type="checkbox"].task-item', function() {
		var task_li = $(this).parent();
		var id = task_li.data("taskid");
		var status = $(this).prop("checked");
		done_task(id, status);
	});
});

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    }
});

function create_task(){
	$.ajax({
		url : "/task/create/",
		type : "POST",
		data : { title : $('#task_title').val() },
		success : function(response){
			$('#task_title').val('');
			var task_li = '<li id="task_'+response.id+'" class="list-group-item" data-taskid="'+response.id+'">';
			task_li += '<input class="task-item" type="checkbox">'+ '<span class="task-title">' + response.title + '</span>' + '</li>';
			$('#todo_list').append(task_li);
			$("#empty_todolist_info").hide()
		},
		error : function(xhr,errmsg,err) {
			$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
				" <a href='#' class='close'>&times;</a></div>");
		}
	})

}

function done_task(clicked_task, status){
	$.ajax({
	    url : "/task/resolve/",
	    type : "POST",
	    data : { 
	    		id : clicked_task,
	    		done :  status,
	    	}, 
	    success : function(response) {
	    	var task_li =  $("#task_" + response.id);
	    	var task_checkbox = $("#task_" + response.id + " .task-item");
	        if (response.done) {
	        	task_checkbox.prop("checked", true);
	        	task_li.addClass("list-group-item-info");
        		$("#done_list").append(task_li);
        		$("#empty_completed_list_info").hide()
	        } else {
	        	task_checkbox.prop("checked", false);
	        	task_li.removeClass("list-group-item-info");
	        	$("#todo_list").append(task_li);
	        	$("#empty_todolist_info").hide()
	        }
	    }
	});
}

