const tabla = document.getElementById('tabla');


function divFlotante(){
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
}
divFlotante()
window.onresize = divFlotante;

tabla.addEventListener('mouseover',(e)=>{
    console.log(document.getElementById('trFlecha'))
    document.getElementById('tbody').setAttribute('class',"")
    document.getElementById('tr-flecha').setAttribute('class','d-none')
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})

tabla.addEventListener('mouseout',(e)=>{
    
   
    console.log(document.getElementById('trFlecha'))
    document.getElementById('tbody').setAttribute('class',"d-none")
    document.getElementById('tr-flecha').setAttribute('class','')
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})
/*
tabla.addEventListener('mouseover',(e)=>{
    let tds=document.querySelectorAll('.td-none')
    for (let i = 0; i < tds.length; i++) {
        const td = tds[i];
        td.setAttribute('style','display:inline')
        
    }
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})

tabla.addEventListener('mouseout',(e)=>{
    let tds=document.querySelectorAll('.td-none')
    for (let i = 0; i < tds.length; i++) {
        const td = tds[i];
        td.setAttribute('style','display:none')
        
    }
    tabla.style=`margin-left:${document.querySelector('body').clientWidth - tabla.clientWidth}px`
})
*/