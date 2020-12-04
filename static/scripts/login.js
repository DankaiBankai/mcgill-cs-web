
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
