function uid() {
    return (performance.now().toString(36) + Math.random().toString(36)).replace(/\./g, "");
}

$(document).ready(function () {
    const user = localStorage.getItem('userID');
    if (user === null || user.length == 0) {
        localStorage.setItem('userID', uid());
    }

    const send_btn = document.querySelector('button#send-btn');
    $('button#send-btn').click(function () {
        $("span#before").css("display", "none");
        $("span#after").css("display", "block");
        const input_data = $('input#default-search').val();
        fetch("short-url/", {
            body: JSON.stringify({
                user_id: localStorage.getItem('userID'), link: input_data
            }), method: "POST",

        })
            .then((res) => res.json())
            .then((data) => {
                $("span#before").css("display", "block");
                $("span#after").css("display", "none");
                if (data["status"] === "ok") {
                    var copyText = data["shorted"];
                    navigator.clipboard.writeText(copyText).then(() => {
                        alert("Copied to clipboard");
                    });
                } else {
                    console.log(data["message"]);
                    alert(data["message"]);
                }

            })

    })

})