logos=['Albañileria','Computacion','Ayudante de Topografo','Electricista','Diseño Asistido','Sanitarista','Soldador' ]

/* hacer ciclo for */

const aside = document.getElementById('aside');
const logoal = document.getElementById('Albañileria');
const logoa2 = document.getElementById('Computacion');
const logoa3 = document.getElementById('Ayudante de Topografo');
const logoa4 = document.getElementById('Electricista');
const logoa5 = document.getElementById('Diseño Asistido');
const logoa6 = document.getElementById('Sanitarista');
const logoa7 = document.getElementById('Soldador');




function divFlotante(){
    aside.style=`margin-left:${document.querySelector('body').clientWidth - aside.clientWidth}px`
}

divFlotante()
window.onresize = divFlotante;
try {
        logoal.addEventListener('mouseover',(e)=>{
                document.getElementById('1').setAttribute('class',"")})
            
            logoal.addEventListener('mouseout',(e)=>{
                document.getElementById('1').setAttribute('class',"d-none")})
            
            logoa2.addEventListener('mouseover',(e)=>{
                    document.getElementById('2').setAttribute('class',"")})
                
            logoa2.addEventListener('mouseout',(e)=>{
                    document.getElementById('2').setAttribute('class',"d-none")})
            
            logoa3.addEventListener('mouseover',(e)=>{
                    document.getElementById('3').setAttribute('class',"")})
                
            logoa3.addEventListener('mouseout',(e)=>{
                    document.getElementById('3').setAttribute('class',"d-none")})
            
            logoa4.addEventListener('mouseover',(e)=>{
                    document.getElementById('4').setAttribute('class',"")})
                
            logoa4.addEventListener('mouseout',(e)=>{
                    document.getElementById('4').setAttribute('class',"d-none")})
            
            logoa5.addEventListener('mouseover',(e)=>{
                    document.getElementById('5').setAttribute('class',"")})
                
            logoa5.addEventListener('mouseout',(e)=>{
                    document.getElementById('5').setAttribute('class',"d-none")})
            
            logoa6.addEventListener('mouseover',(e)=>{
                    document.getElementById('6').setAttribute('class',"")})
                
            logoa6.addEventListener('mouseout',(e)=>{
                    document.getElementById('6').setAttribute('class',"d-none")})
            
            logoa7.addEventListener('mouseover',(e)=>{
                    document.getElementById('7').setAttribute('class',"")})
                
            logoa7.addEventListener('mouseout',(e)=>{
                    document.getElementById('7').setAttribute('class',"d-none")}) 
} catch (error) {
        console.log(error)        
}


    



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
console.log(url)
if(url == "/"){
        document.querySelector('body').style="background: #012f50bf;"
        document.querySelector('header').style="display:none"
        document.querySelector('footer').style="display:none"
}