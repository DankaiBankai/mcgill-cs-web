// Function to change color of background of article when hovered
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
            alert(response)
        },
	async:false
    });
}
