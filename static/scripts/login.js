
function createCookie(name, value, days) {
	var expires;
	if (days) {
		var date = new Date();
		date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
		expires = "; expires=" + date.toGMTString();
	}else {
		expires = "";
	}
	document.cookie = name + "=" + value + expires + "; path=/";
}

function getCookie(c_name) {
	if (document.cookie.length > 0) {
		c_start = document.cookie.indexOf(c_name + "=");
		if (c_start != -1) {
			c_start = c_start + c_name.length + 1;
			c_end = document.cookie.indexOf(";", c_start);
			if (c_end == -1) {
				c_end = document.cookie.length;
			}
			return unescape(document.cookie.substring(c_start, c_end));
		}
	}
	return "";
}


function attemptLogin() {
    var username = $('input[name=username]').val();
    var password = $('input[name=password]').val();
	
    let credentials = { 'username': username, 'password': password };


    $.ajax({
        url: '/attempt-login',
        contentType: "application/json;charset=utf-8",
        data: JSON.stringify({credentials}),
	dataType: "json",
	type: 'POST',
        success: function (response) {
            message = response["message"];
	    if (message === "Success"){
	    	ticket = response["ticket"];
		createCookie("ticket", ticket, 2);
		window.location.replace("/")
	    } else{
	    	alert("Wrong username or password");
	    }
        },
	error: function (response){
	    alert("An error occured");
	},
	async:false
    });
}




function verifyTicket(){
	cookie = getCookie("ticket");
	let verify = {'ticket' : parseInt(cookie, 10)}

	$.ajax({
		url: '/verify-ticket',
		contentType: "application/json;charset=utf-8",
		data: JSON.stringify({verify}),
		dataType: "json",
		type: 'POST',
		success: function (response){
			message = response["message"];
			if (message === "Success"){
				
			} else {
				document.getElementById("edit").remove();
			}
		},
		error: function (response){
			alert("An error occured");
		},
		async:false
	});

}
