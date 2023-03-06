console.log("SCRIPT OK")

let docTitle = document.title;
window.addEventListener("blur", () => {
    document.title = "torna qui;(";
});

window.addEventListener("focus", () => {
    return
});

function generateQR() {
    document.querySelector("#qr-image").style.display = "block";
    let Qrtext = document.querySelector("#text").value;
    if (Qrtext.trim().length==0){

        document.querySelector("#qr-image .error").innerHTML = "enter text";
        document.querySelector("#img").style.display = "none";
    } else {
        document.querySelector("#img").style.display = "block";
       // document.querySelector("#qr-img .error").innerHTML = "error";
        document.querySelector("#img").src = "https://api.qrserver.com/v1/create-qr-code/?data=HelloWorld&amp;size=100x100" + Qrtext;
    }

}
