function isUserAuthenticated() {
    return document.cookie.includes('authenticated=true');
}

document.addEventListener("DOMContentLoaded", function () {

    var showButtons = document.querySelectorAll('[id^="btnShow"]');

    showButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var fileId = button.id.replace('btnShow', '');  
            var iconShow = document.getElementById('iconShow' + fileId);
            var iconHide = document.getElementById('iconHide' + fileId);
            var element = document.getElementById('element' + fileId);

            iconShow.classList.add('hidden');
            iconHide.classList.remove('hidden');
            element.classList.add('list-element-unactive');

            const newData = {
                "id": fileId,
                "display": false,
            }

            fetch("/updateRecordStatus", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json", 
                },
                body: JSON.stringify(newData),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json(); 
                })
                .then(result => {
                    console.log("Server response:", result);
                })
                .catch(error => {
                    console.error("Error sending JSON to server:", error);
                });
        });
    });

    var hideButtons = document.querySelectorAll('[id^="btnHide"]');

    hideButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var fileId = button.id.replace('btnHide', '');  
            var iconShow = document.getElementById('iconShow' + fileId);
            var iconHide = document.getElementById('iconHide' + fileId);
            var element = document.getElementById('element' + fileId);

            iconShow.classList.remove('hidden');
            iconHide.classList.add('hidden');
            element.classList.remove('list-element-unactive');
            const newData = {
                "id": fileId,
                "display": true,
            }

            fetch("/updateRecordStatus", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json", 
                },
                body: JSON.stringify(newData), 
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(result => {
                    console.log("Server response:", result);
                })
                .catch(error => {
                    console.error("Error sending JSON to server:", error);
                });

        });
    });

    var deleteButtons = document.querySelectorAll('[id^="btnTrash"]');

    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var fileId = button.id.replace('btnTrash', '');

            const deleteData = {
                "id": fileId,
            }

            fetch("/delete", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(deleteData),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(result => {
                    console.log("Server response:", result);

                    if (result.status === 'success') {

                        var fileElement = document.getElementById('file' + fileId);
                        if (fileElement) {
                            fileElement.remove(); 
                        }
                    }
                    location.reload();
                })
                .catch(error => {
                    console.error("Error sending JSON to server:", error);
                });
        });
    });

});


function change_period(period) {
    var fileSect = document.getElementById("fileSect");
    var logSect = document.getElementById("logSect");
    var activitySect = document.getElementById("activitySect");
    var selector = document.getElementById("selector");
    var fileList = document.getElementById("fileList");
    var logList = document.getElementById("logList");
    var activityList = document.getElementById("activityList");
    if (period === "fileSect") {
        selector.style.left = 0;
        selector.style.width = fileSect.clientWidth + "px";
        selector.style.backgroundColor = "#CE0E2D";
        selector.innerHTML = "FILES";

        activityList.classList.add("hidden");
        logList.classList.add("hidden");
        fileList.classList.remove("hidden");

    } else if (period === "logSect") {
        selector.style.left = fileSect.clientWidth + "px";
        selector.style.width = logSect.clientWidth + "px";
        selector.innerHTML = "LOGS";
        selector.style.backgroundColor = "#911d30";

        logList.classList.remove("hidden");
        fileList.classList.add("hidden");
        activityList.classList.add("hidden");
    } else {
        selector.style.left = fileSect.clientWidth + logSect.clientWidth + 1 + "px";
        selector.style.width = activitySect.clientWidth + "px";
        selector.innerHTML = "ACTIVITY";
        selector.style.backgroundColor = "#701d2b";
        logList.classList.add("hidden");
        fileList.classList.add("hidden");
        activityList.classList.remove("hidden");
    }
}