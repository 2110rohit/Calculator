
// Retrieve the result from session storage
const result = sessionStorage.getItem('loveResult');
if (result !== null) {
    document.getElementById('readOnlyField').textContent = result + "%";
}
