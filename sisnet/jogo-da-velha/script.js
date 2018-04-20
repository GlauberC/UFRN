var jogada = 0;
function fazerJogada(jogada){
    $( "td" ).click(function() {
    if($(this).attr("class") != "usado"){  
      $(this).attr("class","usado");      
      if(jogada%2==0){
         $(this).css("background-image","url('images/circle.png')");
      }else{
        $(this).css("background-image","url('images/cross.png')");
      }
      jogada++;
    }
    });
  }

$(document).ready(function() {
    fazerJogada(jogada);

});