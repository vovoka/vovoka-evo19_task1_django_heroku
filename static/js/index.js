
let shortenUrl = () => {
    let url = document.querySelector('#link').value;
    return fetch('/create_link', {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
            "Content-Type": "application/json; charset=utf-8",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        redirect: "follow",
        referrer: "no-referrer",
        body: JSON.stringify({url : url})
    }).then(function(val) {
        console.log(val);
        return val.json();
    }).then(function(data) {
        let display = document.querySelector('#g_link');
        display.href = data.data;
        display.innerHTML = data.data;
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
