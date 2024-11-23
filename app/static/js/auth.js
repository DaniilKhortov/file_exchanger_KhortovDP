
function isUserAuthenticated() {
    return document.cookie.includes('authenticated=true');
}

function getUserName() {
    const match = document.cookie.match(/username=([^;]+)/);
    return match ? decodeURIComponent(match[1]) : null;
}

function updateUserUI() {
    const noAccountBlock = document.getElementById('no-account');
    const accountBlock = document.getElementById('account');
    const accountName = document.getElementById('accountName');

    if (isUserAuthenticated()) {
        noAccountBlock.classList.add("hidden");

        accountBlock.classList.remove("hidden");
        accountName.textContent = getUserName();
        accountBlock.style.display = 'flex';
    } else {
        noAccountBlock.classList.remove("hidden");
        accountBlock.classList.add("hidden");
        noAccountBlock.style.display = 'flex';
    }
}

document.addEventListener('DOMContentLoaded', updateUserUI);
