

/* hacer ciclo for */

const aside = document.getElementById('aside');




function divFlotante(){
    aside.style=`margin-left:${document.querySelector('body').clientWidth - aside.clientWidth}px`
}

divFlotante()
window.onresize = divFlotante;
      aside.addEventListener('mouseover',(e)=>{
        if(e.target.getAttribute('name')=='imagenBarra'){
                
                if(e.target.parentNode.parentNode.children[0].getAttribute('class')=='d-none'){
                        e.target.parentNode.parentNode.children[0].setAttribute('class','')
                }

        }
        
      })

      aside.addEventListener('mouseout',(e)=>{
        if(e.target.getAttribute('name')=='imagenBarra'){
                
                if(e.target.parentNode.parentNode.children[0].getAttribute('class')==''){
                        e.target.parentNode.parentNode.children[0].setAttribute('class','d-none')
                }

        }
        
      })
      



url = window.location.pathname;

if(url == "/"){
        document.querySelector('body').style="background: #012f50bf;"
        document.querySelector('header').style="display:none"
        document.querySelector('footer').style="display:none"
}