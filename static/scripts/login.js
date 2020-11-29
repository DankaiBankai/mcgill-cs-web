// Function to change color of background of article when hovered
function attemptLogin() {
    var username = $('input[name=username]').val();
    var password = $('input[name=password]').val();
    $.ajax({
        type: "POST",
        url: "/attempt-login",
        datatype: "json",
        data: { 'username': username, 'password': password },
        success: function (response) {
            alert("success")
        }
    });
}
