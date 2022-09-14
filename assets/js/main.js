function uid() {
    return (performance.now().toString(36) + Math.random().toString(36)).replace(/\./g, "");
}

function getCookie(name) {
    if (!document.cookie) {
        return null;
    }

    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}

const csrfToken = getCookie('CSRF-TOKEN');
const headers = new Headers({
    'Content-Type': 'x-www-form-urlencoded',
    'X-CSRF-TOKEN': csrfToken
});

$(document).ready(function () {
    const user = localStorage.getItem('userID');
    if (user === null || user.length == 0) {
        localStorage.setItem('userID', uid());
    } else {
        console.log(localStorage.getItem('userID'));

    }

    const send_btn = document.querySelector('button#send-btn');
    $('button#send-btn').click(function () {
        $("span#before").css("display", "none");
        $("span#after").css("display", "block");
        console.log('clicked');
        const input_data = $('input#default-search').val();
        console.log(input_data);
        console.log(input_data.type);
        console.log();

        fetch("short-url", {
            // headers,
            // credentials: 'include',
            body: JSON.stringify({
                msg: "salom",

            }), method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                $("span#before").css("display", "block");
                $("span#after").css("display", "none");
                console.log(data);

            })

    })

})