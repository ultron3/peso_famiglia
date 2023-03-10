console.log("SCRIPT OK")


console.log('Ciao MovitAi ti da il benvenuto, ecco i tuoi risultati, seguici su i nostri social, stampa il file attraverso il QRcode');







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
        //document.querySelector("#qr-img .error").innerHTML = "error"; 
        document.querySelector("#img").src = "https://api.qrserver.com/v1/create-qr-code/?data=HelloWorld&amp;size=100x100" + Qrtext;
    }

}


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
  
  // Close the dropdown menu if the user clicks outside of it
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }



  const switchElement = document.getElementById('switch');

  switchElement.addEventListener('change', (event) => {
    if (event.target.checked) {
      console.log('Lo switch è stato attivato!');
      // Esegui azione quando lo switch è stato attivato
    } else {
      console.log('Lo switch è stato disattivato!');
      // Esegui azione quando lo switch è stato disattivato
    }
  });
  


