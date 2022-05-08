function $gotoSPA_Page() {
    const input = document.getElementById(
        'seller-id'
    );
    const container = document.getElementById(
        'details'
    );
    const id = input.value;
    var url = `/chapter-8/sellertoken/${id}/`;

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Token c98fc8fc73d9ad69e92ede8efa4ef724f34d620f',
            'User': 'test'
        }
    }).then(async(response) => {
        return await response.text();
    }).then(async(data) => {
        container.innerHTML = await data;
    }); 
}
