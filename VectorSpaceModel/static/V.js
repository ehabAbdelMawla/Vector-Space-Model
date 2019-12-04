window.onload = function() {

    var Tit = document.querySelector('h1');
    var newVal = ""
    newVal += `<span><img src="../static/Planet-512.png"></span>`
    for (i = 0; i < Tit.innerText.length; i++) {

        if (Tit.innerText[i] !== " ")
            newVal += `<span>${Tit.innerText[i]}</span>`
        else newVal += " "
    }
    newVal += `<span><img src="../static/Planet-512.png"></span>`
    Tit.innerHTML = ""
    Tit.innerHTML = newVal;

    var spans = document.querySelectorAll("h1 span");
    i = 1
    spans.forEach(function(s) {
        s.style.animationDelay = i / 7.5 + "s"
        i += 1
    })

    var searchIcon = document.getElementById("SIcon");
    searchIcon.addEventListener('click', function() {
        document.querySelector("input[value='search']").click();
        // console.log()

    });





    var myscores = document.querySelectorAll(".Score");
    console.log(myscores)
    myscores.forEach(function(score) {
        // console.log(score.offsetWidth)
        score.style.height = score.style.width + 'px';
        // console.log(score.offsetHeight)
    });
    var auth = document.querySelectorAll(".ver2");
    console.log(auth)
    auth.forEach(function(doc) {
        // console.log(score.offsetWidth)
        doc.style.height = 150 + 'px';
        doc.style.width = 150 + 'px';
        // console.log(score.offsetHeight)
    });




};