const main = document.querySelector('main');

let htmlString = "";

for (let i = 0; i < 10; i++) {
    htmlString += '<th>${i}</th>';
}

main.innerHTML = htmlString;