document.addEventListener("DOMContentLoaded", function () {
    var downloadButtons = document.querySelectorAll('[id^="btnDownload"]');

    downloadButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var fileId = button.id.replace('btnDownload', '');
            var account= document.getElementById("accountName");
            const accountName = account.textContent;
            if (isUserAuthenticated()) {
                const downloadCommand = {
                    "id": fileId,
                    "accountName": accountName,
                };

                fetch("/download", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(downloadCommand),
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error(`HTTP error! Status: ${response.status}`);
                        }

                        const fileName = response.headers.get('File-Name');
                        return response.blob().then(blob => ({ fileName, blob }));
                    })
                    .then(({ fileName, blob }) => {
                        const url = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.style.display = 'none';
                        a.href = url;
                        a.download = fileName;
                        document.body.appendChild(a);
                        a.click();
                        window.URL.revokeObjectURL(url);
                    })
                    .catch(error => {
                        console.error("Error downloading file:", error);
                        lert(`Error: ${error.message}`);
                    });

            } else {
                alert("You have to be authenticated to download files!")


            }
            location.reload();
        });
    });
})
