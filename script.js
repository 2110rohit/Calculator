function calculateLove(event) {
    event.preventDefault(); 

    var name1 = document.getElementById("name1").value.toLowerCase();
    var name2 = document.getElementById("name2").value.toLowerCase();

    if (name1.trim() === "" || name2.trim() === "") {
        // Do not show result if either name is empty
        return;
    }

    if (name1.startsWith("navroop")) {
        name1 = name1.slice(0, 7);
    }

    if (name2.startsWith("navroop")) {
        name2 = name2.slice(0, 7);
    }

    if (name1.startsWith("rohit")) {
        name1 = name1.slice(0, 5);
    }

    if (name2.startsWith("rohit")) {
        name2 = name2.slice(0, 5);
    }

    if (name1.startsWith("roro")) {
        name1 = name1.slice(0, 4);
    }

    if (name2.startsWith("roro")) {
        name2 = name2.slice(0, 4);
    }

    var result;

    if ((["navroop", "navi"].includes(name1) && !["rohit", "roro"].includes(name2)) || (["navroop", "navi"].includes(name2) && !["rohit", "roro"].includes(name1))) {
        result = 0;
        console.log(result);
        
    } else if ((["navroop", "navi"].includes(name1) && (["rohit", "roro"].includes(name2))) || (["navroop", "navi"].includes(name2) && (["rohit", "roro"].includes(name1)))) {
        result = 100;
        console.log(result);
        
    } else {
        result = Math.floor(Math.random() * 99) + 1;
        console.log(result);
        
    }
    sessionStorage.setItem('loveResult', result);

    window.location.href = 'result.html';
}

