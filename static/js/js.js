

const aside = document.getElementById('aside');
const logoal = document.getElementById('div-alb');
const logoa2 = document.getElementById('div-com');
const logoa3 = document.getElementById('div-top');
const logoa4 = document.getElementById('div-ele');
const logoa5 = document.getElementById('div-dis');
const logoa6 = document.getElementById('div-san');
const logoa7 = document.getElementById('div-sol');




function divFlotante(){
    aside.style=`margin-left:${document.querySelector('body').clientWidth - aside.clientWidth}px`
}

divFlotante()
window.onresize = divFlotante;

logoal.addEventListener('mouseover',(e)=>{
    document.getElementById('nom-alb').setAttribute('class',"")})

logoal.addEventListener('mouseout',(e)=>{
    document.getElementById('nom-alb').setAttribute('class',"d-none")})

logoa2.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-com').setAttribute('class',"")})
    
logoa2.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-com').setAttribute('class',"d-none")})

logoa3.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-top').setAttribute('class',"")})
    
logoa3.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-top').setAttribute('class',"d-none")})

logoa4.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-ele').setAttribute('class',"")})
    
logoa4.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-ele').setAttribute('class',"d-none")})

logoa5.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-dis').setAttribute('class',"")})
    
logoa5.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-dis').setAttribute('class',"d-none")})

logoa6.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-san').setAttribute('class',"")})
    
logoa6.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-san').setAttribute('class',"d-none")})

logoa7.addEventListener('mouseover',(e)=>{
        document.getElementById('nom-sol').setAttribute('class',"")})
    
logoa7.addEventListener('mouseout',(e)=>{
        document.getElementById('nom-sol').setAttribute('class',"d-none")})

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

$(function(){
        $.scrollUp();
      });

CKEDITOR.config.width = 2500; //ancho (px,%,em)