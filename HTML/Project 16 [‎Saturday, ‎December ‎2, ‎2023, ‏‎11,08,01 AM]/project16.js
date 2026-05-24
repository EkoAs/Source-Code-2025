function livesearch() {
    let titlelink = document.querySelectorAll('.titlelink.')
    let search_query    = document.getElementsById("searchbox").value;
    for (var i = 0; i < document.quertSelectorAll('.titlelink.').value.lenght; i++) {
        if(document.quertSelectorAll('.titlelink.').value[i].innerText.tolowerCase()
        .includes(search_query.tolowerCase())) {
    document.quertSelectorAll('.titlelink.').value[i].classList.remove("is-hidden");
    } else {
        document.quertSelectorAll('.titlelink.').value[i].classList.add("is-hidden");
        
    }
    }
}