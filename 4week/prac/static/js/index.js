$(document).ready(function(){
    load();
});


function load() {
    $.ajax({
        url: '/test/get/data?username=sparta@password=1234',
        type: 'GET',
        data: {},
        success: function(response){
            console.log(response);
        }
    })    
}


function postData(){
    $.ajax({
        url: '/test/post/data',
        type: 'POST',
        data: {
            username: 'sparta',
            password: 1235
        },
        success: function(response){
            console.log(response);
        }
    })
}