function showHeadline() {
    $.get("{% url 'berita:json'%}", function(data){

        for (var i = 0; i < 1; i++) {
            var news_title = document.getElementById("first-headline"); 
            var news_body = document.getElementById("newsbody1"); 
            var news_image = document.getElementById("headline1-bg"); 
            var id_berita = data[i].pk
            
            news_image.style.backgroundImage = "url(" + data[i].fields.news_image + ")";    
            
            news_title.innerHTML = data[i].fields.news_title; 
            news_title.setAttribute("href", "news_page/".concat(id_berita));
            news_body.innerHTML = data[i].fields.news_body; 
             
        }

        for (var j = 1; j < 2; j++) {
            var news_title = document.getElementById("second-headline"); 
            var news_body = document.getElementById("newsbody2"); 
            var news_image = document.getElementById("headline2-bg"); 
            var id_berita = data[i].pk
            news_title.setAttribute("href", "news_page/".concat(id_berita));

            news_image.style.backgroundImage = "url(" + data[j].fields.news_image + ")";    
            

            news_title.innerHTML = data[j].fields.news_title; 
            news_body.innerHTML = data[j].fields.news_body; 
        }

        for (var k = 2; k < 3; k++) {
            var news_title = document.getElementById("third-headline"); 
            var news_body = document.getElementById("newsbody3"); 
            var news_image = document.getElementById("headline3-bg"); 
            var id_berita = data[k].pk
            news_title.setAttribute("href", "news_page/".concat(id_berita));
            
            news_image.style.backgroundImage = "url(" + data[k].fields.news_image + ")";    
        
            news_title.innerHTML = data[k].fields.news_title; 
            

            news_body.innerHTML = data[k].fields.news_body; 
        }
    })
}

function showNewsCard() {
    $.get("{% url 'berita:json'%}",function(data){
        
            var newsCard = document.getElementById("card-news"); 
            newsCard.innerHTML = ""
            let htmlstring = ``
            let href = "news_page/"

            
            for (var i = 3; i < data.length -5; i++) {
            var id_berita = data[i].pk
            
            htmlstring += 
            
            `
                <div class="card h-100 rounded-0 " id="news-card">
                    <img class="card-img-top rounded-0" src="${data[i].fields.news_image}" alt="news image">
                    <div class="card-body" >
                        <a class="card-title" id="newsCardTitle" href=${href.concat(id_berita)}>${data[i].fields.news_title}</a>
                        <p class="card-text" id="card-news-body">${data[i].fields.news_body}</p>
                    </div>
                </div>
            `
            
            }

            newsCard.innerHTML = htmlstring
            let str = document.getElementById("card-news-body").innerHTML; 
            let res = str.replace(/\\n/g, '<br> <br>');
            document.getElementById("card-news-body").innerHTML = res;
    })
}



function showSideNews(){
    $.get("{% url 'berita:json'%}", function(data){
        var sideNews = document.getElementById("side-news"); 
        sideNews.innerHTML = ""
        let htmlstring = ``
        let href = "news_page/"

        for (var i = data.length - 5; i < data.length; i++) {
            var id_berita = data[i].pk
            
            htmlstring += 
            
            `
                <div class='container2' >
                    <div id="side-news">
                        <a  href=${href.concat(id_berita)}>${data[i].fields.news_title}</a>
                        <div id="published-date">'${data[i].fields.news_published}</div>
                    </div>
                </div>
                
            `
            }
            sideNews.innerHTML = htmlstring
    })
}



