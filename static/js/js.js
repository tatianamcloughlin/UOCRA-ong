
//logos=['Albañileria','Computacion','Ayudante de Topografo','Electricista','Diseño Asistido','Sanitarista','Soldador' ]

/* hacer ciclo for */
/*
const aside = document.getElementById('aside');
const logoal = document.getElementById('Albañileria');
const logoa2 = document.getElementById('Computacion');
const logoa3 = document.getElementById('Ayudante de Topografo');
const logoa4 = document.getElementById('Electricista');
const logoa5 = document.getElementById('Diseño Asistido');
const logoa6 = document.getElementById('Sanitarista');
const logoa7 = document.getElementById('Soldador');
*/



function divFlotante(){
    aside.style=`margin-left:${document.querySelector('body').clientWidth - aside.clientWidth}px`
    
}

divFlotante()
window.onresize = divFlotante;
    



/*
tabla.addEventListener('mouseover',(e)=>{
    console.log(document.getElementById('tr-Flecha'))
    document.getElementsByClassName('td-none').setAttribute('class',"")
    document.getElementById('tr-flecha').setAttribute('class','d-none')
    aside.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})

tabla.addEventListener('mouseout',(e)=>{
    
   
    console.log(document.getElementById('trFlecha'))
    document.getElementById('desc').setAttribute('class',"d-none")
    document.getElementById('tr-flecha').setAttribute('class','')
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`})

    /*

tabla.addEventListener('mouseover',(e)=>{
    let tds=document.querySelectorAll('.td-none')
    for (let i = 0; i < tds.length; i++) {
        const td = tds[i];
        td.setAttribute('style','display:inline')
        
    }
    aside.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})

tabla.addEventListener('mouseout',(e)=>{
    let tds=document.querySelectorAll('.td-none')
    for (let i = 0; i < tds.length; i++) {
        const td = tds[i];
        td.setAttribute('style','display:none')
        
    }
     aside.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})
*/
/*
$(function(){
        $.scrollUp();
      });

CKEDITOR.config.width = 2500; //ancho (px,%,em)
*/
url = window.location.pathname;
if(url == "/"){
        document.querySelector('body').style="background: #012f50bf;"
        document.querySelector('header').style="display:none"
        document.querySelector('footer').style="display:none"
}


